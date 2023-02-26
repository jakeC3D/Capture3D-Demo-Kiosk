# -*- coding: utf-8 -*-

import gom
import re 
try:
	from Base.Misc import Globals
	from Base.Measuring import Measure
	from Base.Communication import Communicate
except: 
	from KioskInterface.Base.Misc import Globals
	from KioskInterface.Base.Measuring import Measure
	from KioskInterface.Base.Communication import Communicate

from RivianScripts.RivianSettings import config 
from Tools import RFID, ModbusTCP, EditRFIDConfig 
RFID_PATH = EditRFIDConfig.RFID_PATH
if config.USERFID:
	rfid = RFID.RFID_System(config.RFID_IP, int(config.PORT))
class StartHelper: 
	
	def __init__(self, start_up = None): 
		self.rfid_contents = self.read_csv() 
		if isinstance(self.rfid_contents,dict):
			print(self.rfid_contents.keys())
		self.start_up = start_up
		self.pic_data = '' 
		self.curr_tags = []
	
	def read_csv(self): 
		if not config.USERFID: 
			return '' 
		with open(RFID_PATH, 'r') as my_file: 
			lines = my_file.readlines()
		return_dict = {} 
		for line in [line.strip('\n').strip() for line in lines[1:]]: 
			split_line = line.split(',') 
			if not split_line[0] in return_dict.keys(): 
				return_dict[split_line[0]] = [split_line[1:]] 
			else: 
				return_dict[split_line[0]].append(split_line[1:]) 
		return return_dict
	
	def _8360_rfid_filter(self,filter): 
		if not config.USERFID: 
			return ['*']
		return_list = [''] 
		if socket.gethostbyname(socket.gethostname()) == config.PRIMARY: 
			suffix = config.PRIMARY_SUFFIX
		elif socket.gethostbyname(socket.gethostname()) == config.SECONDARY: 
			suffix = config.SECONDARY_SUFFIX
		else: 
			self.start_up.log.debug('Host is not set properly in the Ford_Settings.cfg') 
			return return_list 
		for i in filter: 
			print(f'flag 101:\ni.lower - {i.lower()}\nSuffix - {suffix}')
			if i.lower().strip('*').endswith(suffix): 
				return_list.append(i) 
		return return_list 

	def create_filter(self, value, side): 
		return f'{value} {side}*'

	def modify_filter(self, tags, packaged_tags, suffix): 
		return_list = []
		for tag_id in tags:
			if not tag_id in packaged_tags:
				continue 
			for folder in packaged_tags[tag_id]: 
				folder = folder.strip('*')
				modified_filter = self.create_filter(folder, suffix) 
				return_list.append(modified_filter)
		return return_list 


	def get_6235_filter(self, packaged_tags, tag_antenna_id_dict): 
		"""Modify filter to only include left or right versions of template folders 
		
		Args:
			packaged_tags(dict<str, list>): {<tag_id>:[<folder>]}
			tag_antenna_id_dict(dict<str, list>): {<antenna_id>:[<tag_id>]}
		Returns: 
			return_list(list): List of filters
		""" 
		return_list = [] 
		antenna_1_key = [id for id in tag_antenna_id_dict.keys() if '1' in id][0] 
		antenna_2_key = [id for id in tag_antenna_id_dict.keys() if id != antenna_1_key][0] 
		return_list += self.modify_filter(tag_antenna_id_dict[antenna_1_key], packaged_tags, config.ANTENNA_1_SUFFIX) 
		return_list += self.modify_filter(tag_antenna_id_dict[antenna_2_key], packaged_tags, config.ANTENNA_2_SUFFIX)
		
		return return_list 

	def open_2019_template(self, startup = False, multipart = False): 
		'''
		This is the part of 2019 open_template that we will not be patching 
		create a project from template
		if startup is given directly opens last used template
		'''
		if not startup:
			# if the filter is unique (only one template would match)
			# directly open the project template
			unique_template, unique_cfg = self.start_up.is_template_filter_unique()
			if unique_template is not None and unique_template == Globals.SETTINGS.CurrentTemplate and Globals.SETTINGS.CurrentTemplateCfg == unique_cfg:
				self.start_up.log.debug( 'already open' )
				self.start_up._after_template_opened( opened_template = {'template_name':unique_template, 'config_level': unique_cfg} )
				return None, None
			elif unique_template is not None:
				gom.script.sys.close_project ()
				if Globals.DRC_EXTENSION is not None and Globals.DRC_EXTENSION.PrimarySideActive():
					template = dict()
					template['template_name'] = unique_template
					template['config_level'] = unique_cfg
					template['DRC_Ext_DelayedLoading'] = True
				else:
					template = gom.script.sys.create_project_from_template ( 
						config_level = unique_cfg,
						template_name = unique_template )
					self.start_up.log.debug( 'opened automatically {}'.format( unique_template ) )
					template['template_name'] = unique_template
					template['config_level'] = unique_cfg
				self.start_up._after_template_opened( template )
				return None, None
			elif Globals.SETTINGS.Inline:
				opened_template = {'template_name':None, 'config_level':None}
				self.start_up._after_template_opened( opened_template )
				return None, None
		
		gom.script.sys.close_project ()
		opened_template = {'template_name':None, 'config_level':None}
		try:
			cfg_level = [Globals.SETTINGS.TemplateConfigLevel]
			if cfg_level[0] == 'both':
				cfg_level = ['shared', 'user']
			# called directly after dialog show or for multipart
			if startup:
				template = gom.script.sys.create_project_from_template ( 
					config_level = Globals.SETTINGS.CurrentTemplateCfg,
					template_name = Globals.SETTINGS.CurrentTemplate )
				opened_template['template_name'] = Globals.SETTINGS.CurrentTemplate
				opened_template['config_level'] = Globals.SETTINGS.CurrentTemplateCfg
				return None, None
		except Exception as err:
			self.start_up.log.error("Open template 2019 " + err) 
		return opened_template, cfg_level 
	
	def open_2018_template(self, startup = False): 
		'''
		create a project from template
		if startup is given directly opens last used template
		'''
		if not startup:
			# if the filter is unique (only one template would match)
			# directly open the project template
			unique_template = self.start_up.is_template_filter_unique()
			if unique_template is not None and unique_template == Globals.SETTINGS.CurrentTemplate:
				self.start_up.log.debug( 'already open' )
				self.start_up._after_template_opened( opened_template = {'template_name':unique_template} )
				return
			elif unique_template is not None:
				gom.script.sys.close_project ()
				template = gom.script.sys.create_project_from_template ( 
					config_level = Globals.SETTINGS.TemplateConfigLevel,
					template_name = unique_template )
				self.start_up.log.debug( 'opened automatically {}'.format( unique_template ) )
				template['template_name'] = unique_template
				self.start_up._after_template_opened( template )
				return
			elif Globals.SETTINGS.Inline:
				opened_template = {'template_name':None}
				self.start_up._after_template_opened( opened_template )
				return
		
		gom.script.sys.close_project ()
		opened_template = {'template_name':None}
		return opened_template 

	def find_antennas(self,tag_data):
		tag_dict = {}
		
		split_data = tag_data.split('\\')
		number_of_tags = (len(split_data) - 4)/4
		print('Number of Tags read -',number_of_tags)
		
		del split_data[0:2], split_data[-2:]
		print(split_data)
	
		tag_list = self.identify_tag_data(split_data,number_of_tags)
		
		for tag in range(int(number_of_tags)):
			print(f'-----------Tag Number {tag+1}-----------\n{tag_list[tag]}')
			tag_id = tag_list[tag][0]
			antenna_id = tag_list[tag][1]
			print('tag id -',tag_id)
			print('antenna id -',antenna_id)
			if not antenna_id in tag_dict.keys():
				print('antenna not in dict')
				tag_dict[antenna_id] = [tag_id]
			elif not tag_id in tag_dict[antenna_id]:
				tag_dict[antenna_id].append(tag_id)
		
		print('tag dictionary -',tag_dict)
		return tag_dict

	def identify_tag_data(self,tag_data,tag_amount):
		return_list = []
		for tag in range(1,int(tag_amount)+1):
			temp_list = tag_data[:4]
			return_list.append(temp_list)
			del tag_data[:4]
		return return_list

	def check_that_tags_did_not_change(self): 
		if config.USERFID:
			tags = self.get_tag_info()
			if tags == self.curr_tags: 
				return True 
			else:
				RESULT=gom.script.sys.execute_user_defined_dialog (content='<dialog>' \
				' <title>Message</title>' \
				' <style></style>' \
				' <control id="Close"/>' \
				' <position>automatic</position>' \
				' <embedding>always_toplevel</embedding>' \
				' <sizemode>automatic</sizemode>' \
				' <size height="169" width="255"/>' \
				' <content columns="2" rows="1">' \
				'  <widget row="0" type="image" column="0" rowspan="1" columnspan="1">' \
				'   <name>image</name>' \
				'   <tooltip></tooltip>' \
				'   <use_system_image>true</use_system_image>' \
				'   <system_image>system_message_warning</system_image>' \
				'   <data><![CDATA[AAAAAAAAAA==]]></data>' \
				'   <file_name></file_name>' \
				'   <keep_original_size>true</keep_original_size>' \
				'   <keep_aspect>true</keep_aspect>' \
				'   <width>0</width>' \
				'   <height>0</height>' \
				'  </widget>' \
				'  <widget row="0" type="display::text" column="1" rowspan="1" columnspan="1">' \
				'   <name>text</name>' \
				'   <tooltip></tooltip>' \
				'   <text>&lt;!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">' \
				'&lt;html>&lt;head>&lt;meta name="qrichtext" content="1" />&lt;style type="text/css">' \
				'p, li { white-space: pre-wrap; }' \
				'&lt;/style>&lt;/head>&lt;body style="    ">' \
				'&lt;p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">&lt;span style=" font-size:16pt; font-weight:600;">Tag has changed, please select a valid project! &lt;/span>&lt;/p>&lt;/body>&lt;/html></text>' \
				'   <wordwrap>false</wordwrap>' \
				'  </widget>' \
				' </content>' \
				'</dialog>')
				return False 
		return True 
	
	def clean_response(self, rfid_response):
		split_string = rfid_response.split('\\') 
		return_list = [] 
		for part in split_string:
			if not re.match(r'5[\d\d]',part[-3:]):
				continue
			if len(part) > 20: 
				tag = part[-3:]
				print('tag in clean', tag)
				if not tag in self.rfid_contents.keys(): 
					self.additional_dialogs.show_link_tag(tag)
					self.rfid_contents = self.read_csv()
				if not tag in return_list:
					return_list.append(tag) 
		return return_list
	
	def get_tag_info(self): 
		try:
			tag = r'{}'.format(rfid.read_IO()) 
		except Exception as err:
			print('RFID Error:',err)
			RESULT=gom.script.sys.execute_user_defined_dialog (content='<dialog>' \
			' <title>Message</title>' \
			' <style></style>' \
			' <control id="Close"/>' \
			' <position>center</position>' \
			' <embedding>always_toplevel</embedding>' \
			' <sizemode>automatic</sizemode>' \
			' <size height="169" width="255"/>' \
			' <content columns="2" rows="1">' \
			'  <widget column="0" rowspan="1" columnspan="1" row="0" type="image">' \
			'   <name>image</name>' \
			'   <tooltip></tooltip>' \
			'   <use_system_image>true</use_system_image>' \
			'   <system_image>system_message_warning</system_image>' \
			'   <data><![CDATA[AAAAAAAAAA==]]></data>' \
			'   <file_name></file_name>' \
			'   <keep_original_size>true</keep_original_size>' \
			'   <keep_aspect>true</keep_aspect>' \
			'   <width>0</width>' \
			'   <height>0</height>' \
			'  </widget>' \
			'  <widget column="1" rowspan="1" columnspan="1" row="0" type="display::text">' \
			'   <name>text</name>' \
			'   <tooltip></tooltip>' \
			'   <text>&lt;!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">' \
			'&lt;html>&lt;head>&lt;meta name="qrichtext" content="1" />&lt;style type="text/css">' \
			'p, li { white-space: pre-wrap; }' \
			'&lt;/style>&lt;/head>&lt;body style="    ">' \
			'&lt;p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">&lt;span style=" font-size:18pt; font-weight:600;">RFID Tag Missing! &lt;/span>&lt;/p>&lt;/body>&lt;/html></text>' \
			'   <wordwrap>false</wordwrap>' \
			'  </widget>' \
			' </content>' \
			'</dialog>')
			return False 
		return self.clean_response(tag), tag
	
	def get_ds_actual(self): 
		
		if not Modbus.connect( IP=config.DS_IP ):
			print('Failed to establish socket connection. Check IP settings.')
			RESULT=gom.script.sys.execute_user_defined_dialog (content='<dialog>' \
' <title>Message</title>' \
' <style></style>' \
' <control id="Close"/>' \
' <position>automatic</position>' \
' <embedding>always_toplevel</embedding>' \
' <sizemode>automatic</sizemode>' \
' <size width="576" height="155"/>' \
' <content columns="2" rows="1">' \
'  <widget columnspan="1" row="0" type="image" column="0" rowspan="1">' \
'   <name>image</name>' \
'   <tooltip></tooltip>' \
'   <use_system_image>true</use_system_image>' \
'   <system_image>system_message_warning</system_image>' \
'   <data><![CDATA[AAAAAAAAAA==]]></data>' \
'   <file_name></file_name>' \
'   <keep_original_size>true</keep_original_size>' \
'   <keep_aspect>true</keep_aspect>' \
'   <width>0</width>' \
'   <height>0</height>' \
'  </widget>' \
'  <widget columnspan="1" row="0" type="display::text" column="1" rowspan="1">' \
'   <name>text</name>' \
'   <tooltip></tooltip>' \
'   <text>&lt;!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">' \
'&lt;html>&lt;head>&lt;meta name="qrichtext" content="1" />&lt;style type="text/css">' \
'p, li { white-space: pre-wrap; }' \
'&lt;/style>&lt;/head>&lt;body style="    ">' \
'&lt;p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">&lt;span style=" font-size:16pt; font-weight:600;">Cannot communicate with distance sensor relay! &lt;/span>&lt;/p>&lt;/body>&lt;/html></text>' \
'   <wordwrap>false</wordwrap>' \
'  </widget>' \
' </content>' \
'</dialog>')
			return False 
		coils = Modbus.FC_01( Address=0, CoilsToRead=24 )
		Modbus.exit()
		actual_values = [coils[0],coils[1], coils[2], coils[3]]
		return actual_values
	
	def package_rfid_filter(self,tags): 
		return_list = ['']
		return_dict = {}
		for tag in tags: 
			if not tag in self.rfid_contents.keys(): 
				continue 
			for col in self.rfid_contents[tag]:
				print(col) 
				if col[0].upper() == 'DS_TAG' or not col[0]: 
					continue  
				filter_value = '{}*'.format(col[0])
				return_list.append(filter_value) 
				if not tag in return_dict: 
					return_dict[tag] = [filter_value] 
					continue 
				return_dict[tag].append(filter_value)
		return return_list, return_dict
		
	def get_rfid_filter(self): 
		if config.USERFID: 
			tags, rfid_info = self.get_tag_info()
			if not tags: 
				return False
			self.curr_tags = tags 
			filter_list, filter_dict = self.package_rfid_filter(tags) 
			
			if config.SCANBOX == '6235':  # TODO move this if block to it's own method that will call get_rfid_filter
				tag_linked_with_antenna_id = self.find_antennas(rfid_info)
				return self.get_6235_filter(filter_dict, tag_linked_with_antenna_id) 
			elif config.SCANBOX == '8360': 
				return self._8360_rfid_filter(filter_list)
			
			return res
			
		return ['*'] 
	
	def get_ds_config(self,tags):
		ds_path = '' 
		for tag in tags: 
			if not tag in self.rfid_contents: 
				continue 
			for col in self.rfid_contents[tag]:
				if col[0].upper() == 'DS_TAG': 
					return os.path.join(gom.app.public_directory, col[-1] + '.csv')
		RESULT=gom.script.sys.execute_user_defined_dialog (content='<dialog>' \
				' <title>Message</title>' \
				' <style></style>' \
				' <control id="Close"/>' \
				' <position>automatic</position>' \
				' <embedding>always_toplevel</embedding>' \
				' <sizemode>automatic</sizemode>' \
				' <size height="155" width="556"/>' \
				' <content columns="2" rows="1">' \
				'  <widget type="image" columnspan="1" row="0" column="0" rowspan="1">' \
				'   <name>image</name>' \
				'   <tooltip></tooltip>' \
				'   <use_system_image>true</use_system_image>' \
				'   <system_image>system_message_warning</system_image>' \
				'   <data><![CDATA[AAAAAAAAAA==]]></data>' \
				'   <file_name></file_name>' \
				'   <keep_original_size>true</keep_original_size>' \
				'   <keep_aspect>true</keep_aspect>' \
				'   <width>0</width>' \
				'   <height>0</height>' \
				'  </widget>' \
				'  <widget type="display::text" columnspan="1" row="0" column="1" rowspan="1">' \
				'   <name>text</name>' \
				'   <tooltip></tooltip>' \
				'   <text>&lt;!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">' \
				'&lt;html>&lt;head>&lt;meta name="qrichtext" content="1" />&lt;style type="text/css">' \
				'p, li { white-space: pre-wrap; }' \
				'&lt;/style>&lt;/head>&lt;body style="    ">' \
				'&lt;p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">&lt;span style=" font-size:18pt; font-weight:600;">Cannot find Distance Sensor config file! &lt;/span>&lt;/p>&lt;/body>&lt;/html></text>' \
				'   <wordwrap>false</wordwrap>' \
				'  </widget>' \
				' </content>' \
				'</dialog>')
		
		return False 
	
	def parse_out_na(self, line,actual_values): 
		untouched_folder = line[0]
		return_line = ['1' if i.lower() == 'true' else '0' if i.lower() == 'false' else 'NA' for i in line[1:]] #Translate True to 1, False to 0 and NA to actual value to match format of actual value and to ignore sensors we don't care about
		while True: 
			if not 'NA' in return_line:
				return_line.insert(0,untouched_folder) 
				return return_line
			na_index = return_line.index('NA')
			return_line[na_index] = actual_values[na_index] 
	
	def package_ds_filter(self,path,actual_values):
		''' 
		Parse file and compare with actual values, return folder names for matching configuration 
		'''
		return_filter = ['']
		with open(path, 'r') as file:
			lines = file.readlines()
		split_lines = [item.strip('\n').upper().split(',') for item in lines] #.upper() for possible NA values
		for line in split_lines:
			line = self.parse_out_na(line,actual_values)
			if actual_values == line[1:]:
				return_filter.append('{}*'.format(line[0]))
		return return_filter
	
	def get_ds_filter(self): 
		
		if config.USE_DISTANCE_SENSOR: 
			tags, rfid_info = self.get_tag_info()
			print('tags -',tags)
			if not tags:
				return False
			config_path = self.get_ds_config(tags) 
			if not config_path:
				return False
			actual_values = self.get_ds_actual() 
			print('actual values',actual_values)
			return self.package_ds_filter(config_path, actual_values)
		elif config.USERFID:
			filter_list = []
			filters = self.get_rfid_filter()
			for item in filters:
				if item.strip('*').lower().endswith(config.PRIMARY_SUFFIX) or item.strip('*').lower().endswith(config.SECONDARY_SUFFIX):
					continue
				else:
					filter_list.append(item.strip())
			print('filter list:',filter_list)
			return filter_list
		return ['*']
