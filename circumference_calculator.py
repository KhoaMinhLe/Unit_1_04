# Created by: Khoa Le
# Created on September 25 2017
# Created for ICS3U
# This program is the "Circumference Calculator".

import ui

def calculate_touch_up_inside(sender):
	#Constant
	PI = 3.14
	#Input
	radius = int(view['raidus_textfield'].text)
	#Process
	circumference = 2 * PI * radius
	#Output
	view['answer_label'].text = str(circumference)

view = ui.load_view()
view.present('sheet')
