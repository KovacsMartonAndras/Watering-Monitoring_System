import smbus
import time
import RPi.GPIO as GPIO
from Relay import *
from Database import *

red = 40
green = 37
blue = 38
Relay_channel = 18

def setup(): 
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(Relay_channel, GPIO.OUT, initial=GPIO.HIGH) 

	GPIO.setup(red, GPIO.OUT, initial=GPIO.LOW)
	GPIO.setup(blue, GPIO.OUT, initial=GPIO.LOW)
	GPIO.setup(green, GPIO.OUT, initial=GPIO.LOW)




def main():
	setup()
	while True:
		moist = readMoist()
		StartMonitoring = True
		while StartMonitoring:
			moist = readMoist()
			if moist >= 0.70 and moist <= 7.5:
				WaterPlants()
				print(moist)
				time.sleep(1)
			else:
				StopWatering()
				StartMonitoring = False	
		print(moist)
		date = time.ctime(time.time())
		print(date)
		#InsertData(date,moist,0)	
		time.sleep(3600) # 0.5 Hour cycle
		
def readMoist():
	#Analog Reader
	address = 0x48
	A0 = 0x40
	bus = smbus.SMBus(1)

	bus.write_byte(address,A0)
	value = bus.read_byte(address)
	return value/255

try:
	main()
except KeyboardInterrupt:
	GPIO.cleanup()
	print("Opsie")