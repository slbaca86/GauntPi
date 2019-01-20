import RPi.GPIO as GPIO
from time import sleep

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





GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.output(23, 1)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)




try:
	print("Program Running...")
	while True:
		if GPIO.input(fswitchpoint)==1:
			#print("pointpurpleswitched")
			GPIO.output(ledpurple, not GPIO.input(ledpurple))
		#else:
			#print("not switched2")
			#GPIO.output(ledpurple,not GPIO.input(ledpurple))
		if GPIO.input(fswitchthm)==0:
			#print("switched1")
			GPIO.output(ledgreen,0)
		else:
			#print("not switched2")
			GPIO.output(ledgreen,1)
		if GPIO.input(fswitchpin)==0:
			GPIO.output(ledorange,0)
		else:
			#print("not switched2")
			GPIO.output(ledorange,1)
		if GPIO.input(fswitchmid)==0:
			#print("switched1")
			GPIO.output(ledblue,1)
		else:
			#print("not switched2")
			GPIO.output(ledblue,0)
		if GPIO.input(fswitchrng)==0:
			#print("switched1")
			GPIO.output(ledred,0)
		else:
			#print("not switched2")
			GPIO.output(ledred,1)
		sleep(0.1)
		
		
		
except KeyboardInterrupt:
	pass
	print("Closing program and cleaning up pins")
	
finally:	
	GPIO.cleanup()
	

	
