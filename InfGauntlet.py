import RPi.GPIO as GPIO
import time
from subprocess import call
import requests
from multiprocessing import Process
import stoneCommands
import fingerswitchtoggle

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
pwmleds =[]

for led in leds:
	GPIO.setup(led,GPIO.OUT)

for switch in fswitch:
	GPIO.setup(switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


activestone ={"Soul":0,"Power":0,"Space":0,"Reality":0, "Mind":0, "Time":0}
activeswitch= {"Index":0,"Thumb":0, "Middle":0, "Ring":0, "Pinky":0}

def ledsoff():
	for led in leds[1:5]:
		GPIO.output(led,0)
	GPIO.output(ledblue,1)
	GPIO.output(ledyellow,1)

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
				pwmleds.append(GPIO.PWM(ledpurple,100))
			if GPIO.input(fswitchthm)==1:
				GPIO.output(ledgreen, 1)
				activestone["Time"]=1
				commands.timesound()
				start = time.time()
				pwmleds.append(GPIO.PWM(ledgreen,100))
			if GPIO.input(fswitchpin)==1:
				GPIO.output(ledorange, 1)
				activestone["Soul"]=1
				commands.soulsound()
				start = time.time()
				pwmleds.append(GPIO.PWM(ledorange,100))
			if GPIO.input(fswitchmid)==1:
				GPIO.output(ledblue, 0)
				activestone["Space"]=1
				commands.spacesound()
				start = time.time()
				pwmleds.append(GPIO.PWM(ledblue,100))
			if GPIO.input(fswitchrng)==1:
				GPIO.output(ledred, 1)
				activestone["Reality"]=1
				commands.realitysound()
				start = time.time()
				pwmleds.append(GPIO.PWM(ledred,100))
			if GPIO.input(fswitchmind)==1:
				GPIO.output(ledyellow, 0)
				activestone["Mind"]=1
				commands.realitysound()
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
				call(["aplay", "/home/Gauntlet/GauntEnv/spacestonefirst.wav"])
				print("Stones Engaged")

				return


	except KeyboardInterrupt:
			return

if __name__ == "__main__":

	try:

		while True:
			ledsoff()
			pwmleds = []
			activestone = activestone.fromkeys(activestone, 0)
			activeswitch= activeswitch.fromkeys(activeswitch, 0)
			selectstone()
			fist(pwmleds)
			commands.sendcommand(activestone)
			print(("Stone Status: {}").format(activestone))
			time.sleep(3)


	except KeyboardInterrupt:
			pass
			print("Closing program and cleaning up pins")

	finally:
		GPIO.cleanup()
