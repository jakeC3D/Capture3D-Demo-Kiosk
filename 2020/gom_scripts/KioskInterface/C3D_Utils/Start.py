# -*- coding: utf-8 -*-

import gom
import os 
try:
	from Base.Misc import Globals
	from Base.Measuring import Measure
	from Base.Communication import Communicate
except: 
	from KioskInterface.Base.Misc import Globals
	from KioskInterface.Base.Measuring import Measure
	from KioskInterface.Base.Communication import Communicate

from .StartHelper import StartHelper
from RivianScripts.RivianSettings import config 
from .Dialogs import Dialogs, Handlers
class Start: 
	
	def __init__(self, start_obj): 
		'''
			Params: 
				start_obj : Instance of the StartUpV8 class 
		'''
		self.start_up = start_obj 
		self.start_helper = StartHelper(self.start_up) 
	
	def open_template(self, startup = False, multipart = None): 
		"""Handler to decide what type of open_template is needed 
		This method will grow with future expansion and configurations 
		"""
		return self.open_template_rfid_ds(startup, multipart) 
	
	def open_template_rfid_ds(self, startup = False, multipart = None): 
		#DS and RFID 
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
		opened_template = {'template_name':None, 'config_level':None}
		gom.script.sys.close_project ()
		try:
			cfg_level = [Globals.SETTINGS.TemplateConfigLevel]
			if cfg_level[0] == 'both':
				cfg_level = ['shared', 'user']
			# called directly after dialog show or for multipart
			if startup:
				self.start_up.dialog.buttonTemplateChoose.text = 'Choose Template'
				return None, None
		except Exception as err:
			self.start_up.log.error("Open template 2019 " + f'{err}') 
		try:
				# show the template dialog
			if Globals.SETTINGS.ShowTemplateDialog:
				filter = self.start_up.Template_filter  # first get the filter before deactivating the dialog
				self.start_up.dialog.enabled = False
				print(Globals.DRC_EXTENSION)
				if Globals.DRC_EXTENSION is not None and Globals.DRC_EXTENSION.PrimarySideActive():
					# open script later
					#--------- PATCH STARTS HERE ------
					
					filter = self.start_helper.get_ds_filter() #Distance Sesnor
					print('Double Robot') 
					opened_template = gom.interactive.sys.get_visible_project_templates ( 
						config_levels = cfg_level,
						filters = filter )
					opened_template['DRC_Ext_DelayedLoading']=True
				else:
					filter = self.start_helper.get_ds_filter() #Distance Sesnor 
					if not filter:
						filter = self.start_helper.get_rfid_filter()
						print('Kiosk') 
					opened_template = gom.interactive.sys.get_visible_project_templates ( 
						config_levels = cfg_level,
						template_name = Globals.SETTINGS.TemplateName,
						filters = filter )
					template = gom.script.sys.create_project_from_template (
						config_level=opened_template['config_level'], 
						template_name=opened_template['template_name'])
				self.start_helper.pic_data = opened_template['preview_image']
			# dont show the template dialog
			else:
				template = gom.script.sys.create_project_from_template ( 
					config_level = Globals.SETTINGS.TemplateConfigLevel,
					template_name = Globals.SETTINGS.TemplateName )
				opened_template['template_name'] = Globals.SETTINGS.TemplateName
				opened_template['config_level'] = Globals.SETTINGS.TemplateConfigLevel
		except Globals.EXIT_EXCEPTIONS:
			raise
		except gom.BreakError:
			pass
		except Exception as error:
			self.start_up.log.exception( str( error ) )
		finally:
			self.start_up.dialog.enabled = True

		res = self.start_up._after_template_opened( opened_template, multipart )
		self.start_up.log.info( 'opened template "{}"'.format( Globals.SETTINGS.CurrentTemplate ) )
		return res

	def verify_selection(self): 
		verify_dialog = Handlers().check_handler() 
		verify_dialog.image1.data = self.start_helper.pic_data
		verify_dialog.project.text = gom.app.project.name 
		res = gom.script.sys.show_user_defined_dialog(dialog = verify_dialog) 
		return res 

	def buttonNext_handler(self): 
		if config.VERIFY:
			res = self.verify_selection
			if not res:
				return False 
		self.set_keywords(self.start_up.dialog) 
		return True
		

	def _generate_kw_desc(self, kw_str): 
		temp = kw_str.split('_') 
		if len(temp) > 1:
			return f'{temp[0][0].upper()+temp[0][1:]} {" ".join(temp[1:])}'
		return f'{temp[0][0].upper()+temp[0][1:]}'

	def set_keywords(self, dialog_obj): 
		for widget in [widget for widget in dialog_obj.widgets if widget.name.startswith('kw_')]: 
			try:
				keyword_name = widget.name.split('kw_')[-1]  # Get the object name to use as keyword name 
				keyword_description = self._generate_kw_desc(keyword_name)

				gom.script.sys.set_project_keywords (
					keywords={keyword_name: widget.value}, 
					keywords_description={keyword_name: keyword_description})

			except Exception as err:
				print('Failed to set keyword:',err) 
				
