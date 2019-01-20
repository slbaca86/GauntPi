import RPi.GPIO as GPIO
from time import sleep
from subprocess import call
import requests

GPIO.setmode(GPIO.BCM)

ledblue = 7
ledred = 4
ledorange = 27
ledpurple = 17
ledgreen = 22
ledyellow = 23

fswitchpoint = 5
fswitchmid = 13
fswitchpin = 26
fswitchthm = 12
fswitchrng = 6
fswitchmind = 24

leds = [ledblue, ledred, ledorange, ledpurple, ledgreen, ledyellow]
fswitch = [fswitchpoint,fswitchmid, fswitchpin, fswitchthm, fswitchrng, fswitchmind]

for led in leds:
	GPIO.setup(led,GPIO.OUT)

for led in leds[1:5]:
	GPIO.output(led, 0)

GPIO.output(ledblue, 1)
GPIO.output(ledyellow, 1)	
	
for switch in fswitch:
	GPIO.setup(switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def fingerswitch():

	try:
		print("Program Running...")
		while True:
			if GPIO.input(fswitchpoint)==1:
				GPIO.output(ledpurple, 1)
				call(["aplay", "/home/pi/Documents/powerstone.wav"])
				sleep(1)
			if GPIO.input(fswitchthm)==1:
				GPIO.output(ledgreen, 1)
				call(["aplay", "/home/pi/Documents/timestonelong.wav"])
				sleep(1)
			if GPIO.input(fswitchpin)==1:
				GPIO.output(ledorange, 1)
				call(["aplay", "/home/pi/Documents/realitystone2.wav"])
				sleep(1)
			if GPIO.input(fswitchmid)==1:
				GPIO.output(ledblue, 0)
				call(["aplay", "/home/pi/Documents/spacestonefirst.wav"])
				sleep(1)
			if GPIO.input(fswitchrng)==1:
				GPIO.output(ledred, 1)
				call(["aplay", "/home/pi/Documents/realitystone.wav"])
				sleep(1)
			if GPIO.input(fswitchmind)==1:
				GPIO.output(ledyellow, 0)
				call(["aplay", "/home/pi/Documents/spacestonefirst.wav"])
				sleep(1)
				
		
			
	except KeyboardInterrupt:
		pass
		print("Closing program and cleaning up pins")
		return
		
		
	
if __name__=="__main__":
		
	try:
	
		fingerswitch()
	
	except KeyboardInterrupt:
		pass
		print("Closing program and cleaning up pins")
	
	finally:
		GPIO.cleanup()
		

	
