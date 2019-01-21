import time
import RPi.GPIO as GPIO


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

pwmleds =[]

for led in leds:
	GPIO.setup(led,GPIO.OUT)

for led in leds:
	pwmleds.append(GPIO.PWM(led,100))

for pwm in pwmleds:
	if pwm == pwmleds[0] or pwm == pwmleds[5]:
		pwm.start(100)	
	else: pwm.start(0)
	
leds = [ledblue, ledred, ledorange, ledpurple, ledgreen, ledyellow]


for i in pwmleds:
	if i == pwmleds[0] or i == pwmleds[5]:
		i.ChangeDutyCycle(0)
	else: i.ChangeDutyCycle(100)
	time.sleep(1)
	
	

try:
	while 1:
		for dc in range(20,100,10):
			for i in pwmleds[1:5]:
				i.ChangeDutyCycle(dc)
			pwmleds[0].ChangeDutyCycle(100-dc)
			pwmleds[5].ChangeDutyCycle(100-dc)
			time.sleep(0.15)
		for dc in range(100, 20,-10):
			for i in pwmleds[1:5]:
				i.ChangeDutyCycle(dc)
			pwmleds[0].ChangeDutyCycle(100-dc)
			pwmleds[5].ChangeDutyCycle(100-dc)
			time.sleep(0.15)
except KeyboardInterrupt:
	pass


GPIO.output(23, 1)
GPIO.output(7, 1)
GPIO.cleanup()
