import logging
import sys
import time

from Adafruit_BNO055 import BNO055


import RPi.GPIO as GPIO

#!/home/Gauntlet/.virtualenvs/GauntEnv-xis9mkqT/bin/python

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
	
GPIO.output(23, 1)
GPIO.output(7, 1)

#
#for pwm in pwmleds:
#	if pwm == pwmleds[0] or pwm == pwmleds[5]:
#		pwm.start(100)	
#	else: pwm.start(0)


# Create and configure the BNO sensor connection.  Make sure only ONE of the
# below 'bno = ...' lines is uncommented:
# Raspberry Pi configuration with serial UART and RST connected to GPIO 18:
bno = BNO055.BNO055(serial_port='/dev/ttyS0', rst=24)
# BeagleBone Black configuration with default I2C connection (SCL=P9_19, SDA=P9_20),
# and RST connected to pin P9_12:
#bno = BNO055.BNO055(rst='P9_12')


# Enable verbose debug logging if -v is passed as a parameter.
if len(sys.argv) == 2 and sys.argv[1].lower() == '-v':
    logging.basicConfig(level=logging.DEBUG)

# Initialize the BNO055 and stop if something went wrong.
if not bno.begin():
    raise RuntimeError('Failed to initialize BNO055! Is the sensor connected?')

# Print system status and self test result.
status, self_test, error = bno.get_system_status()
print('System status: {0}'.format(status))
print('Self test result (0x0F is normal): 0x{0:02X}'.format(self_test))
# Print out an error if system status is in error mode.
if status == 0x01:
    print('System error: {0}'.format(error))
    print('See datasheet section 4.3.59 for the meaning.')

# Print BNO055 software revision and other diagnostic data.
sw, bl, accel, mag, gyro = bno.get_revision()
print('Software version:   {0}'.format(sw))
print('Bootloader version: {0}'.format(bl))
print('Accelerometer ID:   0x{0:02X}'.format(accel))
print('Magnetometer ID:    0x{0:02X}'.format(mag))
print('Gyroscope ID:       0x{0:02X}\n'.format(gyro))



print('Reading BNO055 data, press Ctrl-C to quit...')
while True:
    # Read the Euler angles for heading, roll, pitch (all in degrees).
    heading, roll, pitch = bno.read_euler()
    # Read the calibration status, 0=uncalibrated and 3=fully calibrated.
    sys, gyro, accel, mag = bno.get_calibration_status()
    # Print everything out.
    print('Heading={0:0.2F} Roll={1:0.2F} Pitch={2:0.2F}\tSys_cal={3} Gyro_cal={4} Accel_cal={5} Mag_cal={6}'.format(
          heading, roll, pitch, sys, gyro, accel, mag))
    # Other values you can optionally read:
    if heading >= 0 and heading <=30:
    	GPIO.output(ledorange,1)
    else:
    	GPIO.output(ledorange,0)
    	
    if heading >= 30 and heading <=60:
    	GPIO.output(ledred,1)
    else:
    	GPIO.output(ledred,0)
    	
    if heading >= 60 and heading <=90:
    	GPIO.output(ledblue,0)
    else:
    	GPIO.output(ledblue,1)
    	
    if heading >= 90 and heading <=120:
    	GPIO.output(ledpurple,1)
    else:
    	GPIO.output(ledpurple,0)
    	
    if heading >= 120 and heading <=180:
    	GPIO.output(ledgreen,1)
    else:
    	GPIO.output(ledgreen,0)
  
    time.sleep(1)
    

GPIO.cleanup()
