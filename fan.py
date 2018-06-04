import time
from pyfirmata import Arduino, util
import serial

arduinoData = serial.Serial('com3',9600) #EDIT WITH YOUR PORT
print

def led_on():
	arduinoData.write('1') # fan is turned on

def led_off():
	arduinoData.write('0') # fan is turned off
def main():
	print("[Welcome to the Fan CNC] ")
	print("Do you want to start the fan? ")
	question = raw_input("(Y)es or (N)o: ") # Question to turn it on

	if question == 'y' \
	or question == 'Y':
		led_on() # If answered with y or Y, the fan will turn on
  		print("Fan has started")
		time.sleep(5)
		question2 = raw_input("0 for off, 1 to keep the fan on")
		if question2 == '1':
			led_on()
		elif question2 == '0':
			led_off()

	elif question == 'n' \
	or question == 'N': # If answered with n or N, the fan will not turn on
		led_off()
  		print("Fan will not start")
	else:
  		print("That is not an option") # Any other answer that is not yes or no is disregarded and nothing happens

main()
