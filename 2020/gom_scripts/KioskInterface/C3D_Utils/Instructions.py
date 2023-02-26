# -*- coding: utf-8 -*-

import gom
import os
import re

instructions_folder = os.path.join(gom.app.public_directory, 'instructions') 
if not os.path.exists(instructions_folder): 
	os.makedirs(instructions_folder) 

class Instructions: 
	
	def __init__(self): 
		self.DIALOG=gom.script.sys.create_user_defined_dialog (content='<dialog>' \
' <title>Dialog Title</title>' \
' <style></style>' \
' <control id="Empty"/>' \
' <position>automatic</position>' \
' <embedding>embedded_in_kiosk</embedding>' \
' <sizemode>fixed</sizemode>' \
' <size height="1163" width="1186"/>' \
' <content rows="4" columns="2">' \
'  <widget columnspan="2" row="0" rowspan="1" type="image" column="0">' \
'   <name>image</name>' \
'   <tooltip></tooltip>' \
'   <use_system_image>false</use_system_image>' \
'   <system_image>system_message_information</system_image>' \
'   <data><![CDATA[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]]></data>' \
'   <file_name>C:/Kiosk/Toyota/Important Files/Images/123-123.png</file_name>' \
'   <keep_original_size>false</keep_original_size>' \
'   <keep_aspect>false</keep_aspect>' \
'   <width>1050</width>' \
'   <height>750</height>' \
'  </widget>' \
'  <widget columnspan="2" row="1" rowspan="1" type="label" column="0">' \
'   <name>label</name>' \
'   <tooltip></tooltip>' \
'   <text>Description field</text>' \
'   <word_wrap>false</word_wrap>' \
'  </widget>' \
'  <widget columnspan="1" row="2" rowspan="1" type="button::pushbutton" column="0">' \
'   <name>prev</name>' \
'   <tooltip></tooltip>' \
'   <text>Previous</text>' \
'   <type>push</type>' \
'   <icon_type>system</icon_type>' \
'   <icon_size>icon</icon_size>' \
'   <icon_system_type>arrow_left</icon_system_type>' \
'   <icon_system_size>default</icon_system_size>' \
'  </widget>' \
'  <widget columnspan="1" row="2" rowspan="1" type="button::pushbutton" column="1">' \
'   <name>next</name>' \
'   <tooltip></tooltip>' \
'   <text>Next</text>' \
'   <type>push</type>' \
'   <icon_type>system</icon_type>' \
'   <icon_size>icon</icon_size>' \
'   <icon_system_type>arrow_right</icon_system_type>' \
'   <icon_system_size>default</icon_system_size>' \
'  </widget>' \
'  <widget columnspan="2" row="3" rowspan="1" type="button::pushbutton" column="0">' \
'   <name>cancel</name>' \
'   <tooltip></tooltip>' \
'   <text>Cancel</text>' \
'   <type>push</type>' \
'   <icon_type>system</icon_type>' \
'   <icon_size>icon</icon_size>' \
'   <icon_system_type>cancel</icon_system_type>' \
'   <icon_system_size>default</icon_system_size>' \
'  </widget>' \
' </content>' \
'</dialog>')
		self.DIALOG.handler = self.dialog_event_handler
		self.folder_contents = ''  
		self.current_page = 1 
	
	def execute_instructions(self):
	#This function will gather all of the instructions with pictures and display them
		contents = self.find_instructions_folder() #find_instrucitons_folder will check if there is an instructions folder, if not return false, if return contents of folder 
		print('Log 102:',contents) 
		if not contents: 
			return True
		if not self.show_instructions(contents): 
			return False 
		return True
	
	def find_instructions_folder(self):
		for file in os.listdir(instructions_folder): 
			
			temp_path = os.path.join(instructions_folder,file)
#			print(temp_path) 
			if os.path.isdir(temp_path) and gom.app.project.user_part in temp_path: 
				print('instrcutions folder:',temp_path) 
				contents = self.iterate_through_folder(temp_path) 
				return contents
		return False 
	
	def iterate_through_folder(self,path):
		image_dict = {}
		for file in os.listdir(path): 
			if file.upper().endswith('.PNG') or file.upper().endswith('.JPG'): 
				num = int(re.findall(r'[\d]+',file)[0]) 
				image_dict[num] = os.path.join(path,file) 
			elif file.endswith('.txt'): 
				instructions = os.path.join(path,file) 
		print('image dictionary:',image_dict) 
		return (image_dict, instructions) 
	
	def show_instructions(self, contents):
		self.folder_contents = contents
		self.contents = self.folder_contents[0]
		self.instruc = self.read_instructions(self.folder_contents)
		result = self.execute()
		if not result: 
			return False 
		return True
	
	def execute(self): 
		RESULT=gom.script.sys.show_user_defined_dialog (dialog=self.DIALOG)
		print('result from instructions:',RESULT)
		return RESULT
	
	def dialog_event_handler (self,widget):
		if widget == self.DIALOG.next and self.DIALOG.next.text == 'Next': 
			self.current_page += 1
		elif widget == self.DIALOG.prev: 
			self.current_page -= 1 
		elif widget == self.DIALOG.cancel: 
			gom.script.sys.close_user_defined_dialog (dialog = self.DIALOG, result = False) 
		elif widget == self.DIALOG.next and self.DIALOG.next.text == 'Ok': 
			gom.script.sys.close_user_defined_dialog(dialog = self.DIALOG, result = True) 
		print('current page:',self.current_page) 
		print('Length of instructions:',len(self.contents))
#		print(self.contents) 
		self.DIALOG.label.text = self.instruc[self.current_page] 
		file = os.open( self.contents[self.current_page], os.O_RDONLY | os.O_BINARY )
		bytes = os.read( file, os.fstat( file ).st_size )
		os.close( file ) 
		self.DIALOG.image.data = bytes
		if self.current_page == len(self.contents): 
			self.DIALOG.next.icon_system_type = 'ok' 
			self.DIALOG.next.text = 'Ok' 
		else:
			self.DIALOG.next.icon_system_type = 'arrow_right' 
			self.DIALOG.next.text = 'Next' 
		if self.current_page == 1: 
			self.DIALOG.prev.enabled = False 
		else:
			self.DIALOG.prev.enabled = True 
	
	def read_instructions(self,contents): 
		instruc = {}
		with open(contents[1],'r') as my_file: 
			count = 1
			lines = my_file.readlines() 
			for line in lines:
				if line == '':
					continue 
				instruc[count] = line 
				count += 1
		print('read_instructions method:',instruc)
		return instruc
