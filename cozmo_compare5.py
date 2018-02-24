# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 14:12:01 2018

@author: William Egbert
Python 3.6

"""

import cozmo

text1 = "my battery is low"
defD = 0.5
defP = 0.0
ui = input("What do you want Cozmo to say? ")
uspd = input("Duration scalar: Enter an integer between 0 and 10 ")
inpit = input("Voice pitch: Enter a number between 0 and 1 ")
if ui != "": 
	text1 = ui

if uspd != "": 
	defD = float(uspd)/10.0
	
if inpit != "":
	defP = float(inpit)


def cozmo_program(robot: cozmo.robot.Robot):
    
   
    robot.say_text(
            "Pitch at user specification: "+ str(defP) + text1, use_cozmo_voice=False, duration_scalar = defD, voice_pitch=defP).wait_for_completed()
    robot.say_text(
            "Pitch at half: " + text1, use_cozmo_voice=False, duration_scalar=defD, voice_pitch=defP-(defP/2)).wait_for_completed()
    robot.say_text(
            "Pitch at negative half:" + text1, use_cozmo_voice=False, duration_scalar=defD, voice_pitch=-(defP-defP/2)).wait_for_completed()
    robot.say_text(
            "Pitch at negative full:" + text1, use_cozmo_voice=False, duration_scalar=defD, voice_pitch=(-defP)).wait_for_completed()
    robot.say_text(
            "Pitch at default: " + text1, use_cozmo_voice=False, duration_scalar=defD , voice_pitch=(0.0)).wait_for_completed()



cozmo.run_program(cozmo_program)
