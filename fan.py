import time
from pyfirmata import Arduino, util
import serial

arduinoData = serial.Serial('com3',9600) #EDIT WITH YOUR PORT
print

def led_on():
	arduinoData.write('1') # fan is turned on

def led_off():
	arduinoData.write('0') # fan is turned off

print("[Welcome to the Fan CNC] ")
print("Do you want to start the fan? ")
question = raw_input("(Y)es or (N)o: ") # Question to turn it on

if question == 'y' or question == 'Y':
	time.sleep(2)
	led_on() # If answered with y or Y, the fan will turn on
  	print("Fan has started")
	time.sleep(2)
	question2 = raw_input("Would you like to keep running or turn the fan off, y/n?")
	time.sleep(1)
	if question2 == 'y' or question2 == 'Y':
		led_on()
		print("The fan is stably running")
		time.sleep(2)
	elif question2 == 'N' or question2 == 'n':
		led_off()
		time.sleep(2)
elif question == 'n' or question == 'N': # If answered with n or N, the fan will not turn on
	led_off()
  	print("Fan will not start")
else:
  print("That is not an option") # Any other answer that is not yes or no is disregarded and nothing happens
