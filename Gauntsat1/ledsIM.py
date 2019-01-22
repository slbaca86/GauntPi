
import RPi.GPIO as GPIO
import time
from datetime import datetime

GPIO.setmode(GPIO.BCM)
head = 6
chest = 5
hand =23

leds = [chest, head, hand]

for led in leds:
	GPIO.setup(led, GPIO.OUT)

#Intialization
GPIO.output(chest,1)
GPIO.output(head,1)
GPIO.output(hand,1)

ledspwm = []

for pwm in leds:
	ledspwm.append(GPIO.PWM(pwm, 100))
	
#for pwm in ledspwm:
#	pwm.start(0)

	
print()

def flickon(slptm):
	
	for pwm in ledspwm[0:2]:
		pwm.start(0)

	for dc in range(1,100,1):
		ledspwm[0].ChangeDutyCycle(100-dc)
		ledspwm[1].ChangeDutyCycle(100-dc)
		time.sleep(slptm)
	
	#GPIO.cleanup()
	return
	
	
	

def flickerstartup():
	
	
	flickon(.005)
	time.sleep(.15)
	flickon(.0005)
	time.sleep(.005)
	flickon(.001)
	time.sleep(.005)
	flickon(.005)
	time.sleep(.1)
	flickon(.0005)
	time.sleep(.005)
	flickon(.001)
	time.sleep(.1)
	flickon(.05)
	return
	
		
	
		
		
	
def repulsor():
	
	ledspwm[2].start(1)
	time.sleep(2)
	for dc in range(2,100,5):
				ledspwm[2].ChangeDutyCycle(100-dc)
				time.sleep(0.02)
	for dc in range(100, 2,-5):
				ledspwm[2].ChangeDutyCycle(100-dc)
				time.sleep(0.02)
	GPIO.cleanup()
	return
	
def fadeinout():

	for pwm in ledspwm:
		pwm.start(0)
	
	try:
		while 1:
			for dc in range(0,50,1):
				for i in ledspwm:
					i.ChangeDutyCycle(dc)
					time.sleep(0.01)
			for dc in range(50,100,5):
				for i in ledspwm:
					i.ChangeDutyCycle(dc)
					time.sleep(0.001)
			for dc in range(100, 0,-5):
				for i in ledspwm:
					i.ChangeDutyCycle(dc)
					time.sleep(0.01)
	except KeyboardInterrupt:
		GPIO.cleanup()
		print("Cleaning up pins")
		return
		
flickerstartup()
try:
	while 1:
	
		ledspwm[0].ChangeDutyCycle(0)
		ledspwm[1].ChangeDutyCycle(0)
		
except KeyboardInterrupt:
	pass
			
#fadeinout()
repulsor()

GPIO.cleanup()

