import RPi.GPIO as GPIO
from time import sleep
Relay_channel = 18

def setup(): 
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(Relay_channel, GPIO.OUT,initial=GPIO.HIGH) 

def WaterPlants():
	GPIO.output(Relay_channel,0)	

def StopWatering():
	GPIO.output(Relay_channel,1)

def destroy():
 	GPIO.output(Relay_channel, GPIO.LOW)
 	GPIO.cleanup()


