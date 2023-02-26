# -*- coding: utf-8 -*-

import gom

class Dialogs: 
	CHECK=gom.script.sys.create_user_defined_dialog (content='<dialog>' \
' <title>Message</title>' \
' <style></style>' \
' <control id="Empty"/>' \
' <position>center</position>' \
' <embedding>always_toplevel</embedding>' \
' <sizemode>automatic</sizemode>' \
' <size width="547" height="559"/>' \
' <content columns="5" rows="5">' \
'  <widget type="image" column="0" rowspan="1" columnspan="1" row="0">' \
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
'  <widget type="display::text" column="1" rowspan="1" columnspan="2" row="0">' \
'   <name>text</name>' \
'   <tooltip></tooltip>' \
'   <text>&lt;!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">' \
'&lt;html>&lt;head>&lt;meta name="qrichtext" content="1" />&lt;style type="text/css">' \
'p, li { white-space: pre-wrap; }' \
'&lt;/style>&lt;/head>&lt;body style="    ">' \
'&lt;p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">&lt;span style=" font-size:12pt; font-weight:600;">Are you sure you want to run the project listed below? &lt;/span>&lt;/p>' \
'&lt;p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:600;">&lt;br />&lt;/p>' \
'&lt;p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:600;">&lt;br />&lt;/p>&lt;/body>&lt;/html></text>' \
'   <wordwrap>false</wordwrap>' \
'  </widget>' \
'  <widget type="spacer::horizontal" column="3" rowspan="5" columnspan="1" row="0">' \
'   <name>spacer_1</name>' \
'   <tooltip></tooltip>' \
'   <minimum_size>0</minimum_size>' \
'   <maximum_size>-1</maximum_size>' \
'  </widget>' \
'  <widget type="spacer::horizontal" column="4" rowspan="5" columnspan="1" row="0">' \
'   <name>spacer</name>' \
'   <tooltip></tooltip>' \
'   <minimum_size>0</minimum_size>' \
'   <maximum_size>-1</maximum_size>' \
'  </widget>' \
'  <widget type="image" column="0" rowspan="1" columnspan="3" row="1">' \
'   <name>image1</name>' \
'   <tooltip></tooltip>' \
'   <use_system_image>false</use_system_image>' \
'   <system_image>system_message_warning</system_image>' \
'   <data><![CDATA[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]]></data>' \
'   <file_name>C:/Ford MAP/Capture.PNG</file_name>' \
'   <keep_original_size>false</keep_original_size>' \
'   <keep_aspect>true</keep_aspect>' \
'   <width>470</width>' \
'   <height>321</height>' \
'  </widget>' \
'  <widget type="label" column="0" rowspan="1" columnspan="1" row="2">' \
'   <name>label</name>' \
'   <tooltip></tooltip>' \
'   <text>Project: </text>' \
'   <word_wrap>false</word_wrap>' \
'  </widget>' \
'  <widget type="label" column="1" rowspan="1" columnspan="2" row="2">' \
'   <name>project</name>' \
'   <tooltip></tooltip>' \
'   <text>Description field</text>' \
'   <word_wrap>false</word_wrap>' \
'  </widget>' \
'  <widget type="separator" column="0" rowspan="1" columnspan="3" row="3">' \
'   <name>separator</name>' \
'   <tooltip></tooltip>' \
'   <title></title>' \
'  </widget>' \
'  <widget type="button::pushbutton" column="0" rowspan="1" columnspan="2" row="4">' \
'   <name>yes</name>' \
'   <tooltip></tooltip>' \
'   <text>Yes</text>' \
'   <type>push</type>' \
'   <icon_type>system</icon_type>' \
'   <icon_size>icon</icon_size>' \
'   <icon_system_type>ok</icon_system_type>' \
'   <icon_system_size>default</icon_system_size>' \
'  </widget>' \
'  <widget type="button::pushbutton" column="2" rowspan="1" columnspan="1" row="4">' \
'   <name>no</name>' \
'   <tooltip></tooltip>' \
'   <text>No</text>' \
'   <type>push</type>' \
'   <icon_type>system</icon_type>' \
'   <icon_size>icon</icon_size>' \
'   <icon_system_type>cancel</icon_system_type>' \
'   <icon_system_size>default</icon_system_size>' \
'  </widget>' \
' </content>' \
'</dialog>')

class Handlers: 
	
	def __init__(self): 
		pass 
	
	def check_handler(self): 
		return_dialog = Dialogs.CHECK 
		return_dialog.handler = self._check_handler 
		return return_dialog
	
	def _check_handler(self,widget): 
		if widget == CHECK.yes: 
			gom.script.sys.close_user_defined_dialog(dialog = Dialogs.CHECK, result = True) 
		elif widget == CHECK.no: 
			gom.script.sys.close_user_defined_dialog(dialog = Dialogs.CHECK, result = False) 
			
