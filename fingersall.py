import RPi.GPIO as GPIO
import time
from subprocess import call
import requests
import threading
import commands
import fingerswitchtoggle

# set pinmode to BCM layout for RPi
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
fswitch = [fswitchpoint,fswitchmid, fswitchpin, fswitchthm, fswitchrng,fswitchmind]

for led in leds:
	GPIO.setup(led,GPIO.OUT)
	GPIO.output(led,0)

GPIO.output(ledblue, 1)
GPIO.output(ledyellow, 1)

for switch in fswitch:
	GPIO.setup(switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


activestone ={"Soul":0,"Power":0,"Space":0,"Reality":0, "Mind":0, "Time":0}
activeswitch= {"Index":0,"Thumb":0, "Middle":0, "Ring":0, "Pinky":0}



def selectstone():

	start = time.time()

   	try:

		print("Select Stones...")
		while time.time() < start + 4 :
			if GPIO.input(fswitchpoint)==1:
				GPIO.output(ledpurple, 1)
				activestone["Power"]=1
				commands.powersound()
				start = time.time()
			if GPIO.input(fswitchthm)==1:
				GPIO.output(ledgreen, 1)
				activestone["Time"]=1
				commands.timesound()
				start = time.time()
			if GPIO.input(fswitchpin)==1:
				GPIO.output(ledorange, 1)
				activestone["Soul"]=1
				commands.soulsound()
				start = time.time()
			if GPIO.input(fswitchmid)==1:
				GPIO.output(ledblue, 0)
				activestone["Space"]=1
				commands.spacesound()
				start = time.time()
			if GPIO.input(fswitchrng)==1:
				GPIO.output(ledred, 1)
				activestone["Reality"]=1
				commands.realitysound()
				start = time.time()
			if GPIO.input(fswitchmind)==1:
				GPIO.output(ledyellow, 0)
				activestone["Mind"]=1
				commands.realitysound()
				start = time.time()


	except KeyboardInterrupt:
		pass
		print("exiting loop")

	finally:
		print ("Stone(s) selected")
		for stone in activestone:
			if activestone[stone] == 1:
				print("{} is active!").format(stone)
		return activestone


def fist():
	try:

		print("Ready to Activate")
		while True:
			if GPIO.input(fswitchpoint)==1:
				activeswitch["Index"]=1
			if GPIO.input(fswitchthm)==1:
				activeswitch["Thumb"]=1
			if GPIO.input(fswitchpin)==1:
				activeswitch["Pinky"]=1
			if GPIO.input(fswitchmid)==1:
				activeswitch["Middle"]=1
			if GPIO.input(fswitchrng)==1:
				activeswitch["Ring"]=1
			count = 0
			for switch in activeswitch:
				if activeswitch[switch] == 1:
					count +=1
			if count == 5:
				call(["aplay", "/home/pi/Documents/spacestonefirst.wav"])
				print("Stones Engaged")
				return


	except KeyboardInterrupt:
			return

if __name__ == "__main__":

	try:

		#fingerswitchtoggle.fingerswitch()
		selectstone()
		fist()
		commands.sendcommand(activestone)


		print(("Stone Status: {}").format(activestone))


	except KeyboardInterrupt:
			pass
			print("Closing program and cleaning up pins")

	finally:
		GPIO.cleanup()
