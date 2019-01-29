

#main code for managing gauntlet fingerswitch sensing, LED mechanics, and decision handling
##


import RPi.GPIO as GPIO
import time
from subprocess import call
import requests
from multiprocessing import Process
import stoneCommands

# set pinmode to BCM layout for RPi
GPIO.setmode(GPIO.BCM)

#list of LEDS connected to RPI Google Voice hat
ledblue = 7
ledred = 4
ledorange = 27
ledpurple = 17
ledgreen = 22
ledyellow = 23
#list of pins for Switches located in fingers
fswitchpoint = 5
fswitchmid = 13
fswitchpin = 26
fswitchthm = 12
fswitchrng = 6
fswitchmind = 24

leds = [ledblue, ledred, ledorange, ledpurple, ledgreen, ledyellow]
fswitch = [fswitchpoint,fswitchmid, fswitchpin, fswitchthm, fswitchrng,fswitchmind]
#blank list for holding RPi.GPIO PWM objects
pwmleds =[]

#initialize led pins
for led in leds:
	GPIO.setup(led,GPIO.OUT)

#intiliaze input pins for switches located in fingers -
for switch in fswitch:
	GPIO.setup(switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


activestone ={"Soul":0,"Power":0,"Space":0,"Reality":0, "Mind":0, "Time":0}
activeswitch= {"Index":0,"Thumb":0, "Middle":0, "Ring":0, "Pinky":0}

#due to hardware limitations a mixture of active high and active low pins are
#used in the driving the leds - blue and yellow are set to high to turn them off
def ledsoff():
	for led in leds[1:5]:
		GPIO.output(led,0)
	GPIO.output(ledblue,1)
	GPIO.output(ledyellow,1)

# function that causes selected stones to "breath" or fade in and out
def fadeinout(ledspmw):

	try:
		for i in ledspmw:
			i.start(0)
		while 1:
			for dc in range(20,100,10):
				for i in ledspmw:
					i.ChangeDutyCycle(dc)
				time.sleep(0.15)
			for dc in range(100, 20,-10):
				for i in ledspmw:
					i.ChangeDutyCycle(dc)
				time.sleep(0.15)
	except KeyboardInterrupt:
		return

#function for selecting the active Stone
# once iniatited the algorithm waits for fingerswitch signals within 4 seconds
# after 4 seconds the selected stones are then passed on
def selectstone():

	start = time.time()

   	try:

		print("Select Stones...")
		while time.time() < start + 4 :
			if GPIO.input(fswitchpoint)==1:
				GPIO.output(ledpurple, 1)
				activestone["Power"]=1
				stoneCommands.powersound()
				start = time.time()
				pwmleds.append(GPIO.PWM(ledpurple,100))
			if GPIO.input(fswitchthm)==1:
				GPIO.output(ledgreen, 1)
				activestone["Time"]=1
				stoneCommands.timesound()
				start = time.time()
				pwmleds.append(GPIO.PWM(ledgreen,100))
			if GPIO.input(fswitchpin)==1:
				GPIO.output(ledorange, 1)
				activestone["Soul"]=1
				stoneCommands.soulsound()
				start = time.time()
				pwmleds.append(GPIO.PWM(ledorange,100))
			if GPIO.input(fswitchmid)==1:
				GPIO.output(ledblue, 0)
				activestone["Space"]=1
				stoneCommands.spacesound()
				start = time.time()
				pwmleds.append(GPIO.PWM(ledblue,100))
			if GPIO.input(fswitchrng)==1:
				GPIO.output(ledred, 1)
				activestone["Reality"]=1
				stoneCommands.realitysound()
				start = time.time()
				pwmleds.append(GPIO.PWM(ledred,100))
			if GPIO.input(fswitchmind)==1:
				GPIO.output(ledyellow, 0)
				activestone["Mind"]=1
				stoneCommands.realitysound()
				start = time.time()
				pwmleds.append(GPIO.PWM(ledyellow,100))
			if sum(activestone.values()) == 0:
				start=time.time()


	except KeyboardInterrupt:
		pass
		print("exiting loop")

	finally:
		print ("Stone(s) selected")
		for stone in activestone:
			if activestone[stone] == 1:
				print("{} is active!").format(stone)
		print(pwmleds)
		return activestone, pwmleds

#function to detect a fist being made(i.e all 5 finger switches actuated)
def fist(ledpwms):
	try:
		p = Process(target=fadeinout, args=(ledpwms,))
		p.start()

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
				p.terminate()
				call(["aplay", "./wavfiles/spacestonefirst.wav"])
				print("Stones Engaged")

				return


	except KeyboardInterrupt:
			return
#main function to run when file is executed
if __name__ == "__main__":

	try:

		while True:
			#initialize LEDS
			ledsoff()

			pwmleds = []

			activestone = activestone.fromkeys(activestone, 0)

			activeswitch = activeswitch.fromkeys(activeswitch, 0)

			selectstone()

			fist(pwmleds)

			deviceList = stoneCommands.selectDevice(activestone)

			stoneCommands.sendCommand(stoneCommands.deviceRequest, stoneCommands.getDeviceURL, stoneCommands.getIftttkey, deviceList)

			print(("Stone Status: {}").format(activestone))
			time.sleep(3)


	except KeyboardInterrupt:
			pass
			print("Closing program and cleaning up pins")

	finally:
		GPIO.cleanup()
