#!/usr/bin/python3

# Include the system and graphical user interface modules
import pyfirmata
import sys
from PySide.QtGui import *
import RPi.GPIO as GPIO
import threading
import time

pin = 11
relayPin = 36
pinState = False

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.IN)
GPIO.setup(relayPin, GPIO.OUT)

intPinState=0
exitFlag = 0
board=pyfirmata.Arduino('/dev/ttyACM0')
pin13=board.get_pin('d:13:o')

class MyWindow(QWidget):
	
	def __init__(self):
		super(MyWindow,self).__init__()
		# name the widget
		self.setWindowTitle('Window Events')
		# create a label (a bit of text)
		self.label = QLabel('Read Me', self)
		# create a button widget, position it and
		# connect a function when it is clicked
		button = QPushButton('Push Me', self)
		button.clicked.connect(self.buttonClicked)
		# create a vertically orientated layout box
		# for the other widgets
		layout = QVBoxLayout(self)
		layout.addWidget(button)
		layout.addWidget(self.label)

		# track the mouse
		self.setMouseTracking(True)
		
	def buttonClicked(self):
		""" Update the text when the button is clicked """
		global intPinState
		self.label.setText("Clicked")
		pin13.write(intPinState)
		if intPinState == 0:
			intPinState = 1
		else:
			intPinState = 0

	def mouseMoveEvent(self, event):
		"""
		Update the text when the (tracked) mouse moves over MyWindow
		"""
		self.label.setText(str(event.x()) + "," + str(event.y()))
		
class myThread (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
   def run(self):
      print ("Starting " + self.name)
      ledControl(self.name, self.counter, 5)
      print ("Exiting " + self.name)

		
def ledControl(threadName, delay, counter):
	while True:
		input_value = GPIO.input(pin)
		if input_value == False:
			
			while input_value == False:
				input_value = GPIO.input(pin)
				GPIO.output(relayPin,True)
		else:GPIO.output(relayPin,False)
                        

# Create two threads as follows
try:
	# Create new threads
	thread1 = myThread(1, "Thread-1", 1)
except:
   print("Error: unable to start thread")

# Start new Threads
thread1.start()
# start an application and create a widget for the window,
# giving it a name
application = QApplication(sys.argv)
# construct a widget called MyWindow
widget = MyWindow()

# show the widget
widget.show()
# start the application so it can do things
# with the widgets we've created
application.exec_()
GPIO.cleanup()



