# Import required libraries
import RPi.GPIO as GPIO
import time
import datetime

# -*- coding: utf-8 -*-
######GPIO pin refresh#################################################
def pin_refresh():
   GPIO.setup(17,GPIO.IN,pull_up_down = GPIO.PUD_DOWN)
   GPIO.setup(18,GPIO.IN,pull_up_down = GPIO.PUD_DOWN)
   GPIO.setup(21,GPIO.IN,pull_up_down = GPIO.PUD_DOWN)  
   GPIO.setup(22,GPIO.IN,pull_up_down = GPIO.PUD_DOWN)
   GPIO.setup(23,GPIO.IN,pull_up_down = GPIO.PUD_DOWN)
   GPIO.add_event_detect(23,GPIO.RISING,callback = my_callback1,bouncetime =300)
######event detection removal#########################################
def event_removal():
         GPIO.remove_event_detect(23)        # this is to avoid looping of the callback function

  
######callback functions (GPIO imterrupt service)######################

def my_callback1(channel):
        global s
        s = 1
        os.system('pkill -9 -f "/usr/bin/omxplayer.bin -s"')
        print "wohoooo"
        if ( (GPIO.input(17) == 0) and (GPIO.input(18) == 0) and (GPIO.input(21) == 0) and (GPIO.input(22) == 0) ):
          os.system('pkill -9 -f "/usr/bin/omxplayer.bin -s"')
          current_video = OMXPlayer(video_2)
          video_duration1 = duration(video_2)
          time.sleep(video_duration1 - 0.1450)
        if ( (GPIO.input(17) == 1) and (GPIO.input(18) == 0) and (GPIO.input(21) == 0) and (GPIO.input(22) == 0) ):
          os.system('pkill -9 -f "/usr/bin/omxplayer.bin -s"')
          current_video = OMXPlayer(video_3)
          video_duration1 = duration(video_3)
          time.sleep(video_duration1 - 0.1450)
        if ( (GPIO.input(17) == 0) and (GPIO.input(18) == 1) and (GPIO.input(21) == 0) and (GPIO.input(22) == 0) ):
          os.system('pkill -9 -f "/usr/bin/omxplayer.bin -s"')
          current_video = OMXPlayer(video_4)
          video_duration1 = duration(video_4)
          time.sleep(video_duration1 - 0.1450)
        if ( (GPIO.input(17) == 1) and (GPIO.input(18) == 1) and (GPIO.input(21) == 0) and (GPIO.input(22) == 0) ):
          os.system('pkill -9 -f "/usr/bin/omxplayer.bin -s"')
          current_video = OMXPlayer(video_5)
          video_duration1 = duration(video_5)
          time.sleep(video_duration1 - 0.1450)
        
        s = 0
        event_removal()
         
        
######main function###################################################
def main():
        global s
        while (1):
          while (s == 0):  
            GPIO.cleanup()
            pin_refresh()
            video_duration1 = duration(video_1)
             os.system('pkill -9 -f "/usr/bin/omxplayer.bin -s"')
             current_video = OMXPlayer(video_1)
             time.sleep(video_duration1 - 0.1450)
                                          
          while (s!= 0):                                 
            time.sleep(0.5)
######################################################################

# Tell GPIO library to use GPIO references
GPIO.setmode(GPIO.BCM)GPIO.board(BCD)
main()
