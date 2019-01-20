import requests
from subprocess import call
import time

def sendcommand(engagedstones):

	if engagedstones["Power"] and sum(engagedstones.values()) == 1:
		print("Power only")
		powertoggle()
	if engagedstones["Soul"] and sum(engagedstones.values()) == 1:
		print("Soul only")
		bubbletoggle()
	if engagedstones["Time"] and sum(engagedstones.values()) == 1:
		print("Time only")
	if engagedstones["Space"]and sum(engagedstones.values()) == 1:
		print("Space only")
	if engagedstones["Mind"] and sum(engagedstones.values()) == 1:
		print("Mind only")
	if engagedstones["Reality"] and sum(engagedstones.values()) == 1:
		print("Reality only")
	if engagedstones["Soul"] and engagedstones["Power"]:
		powertoggle()
		time.sleep(1)
		bubbletoggle()

	return

def powersound():

	print("playing power sound")
	call(["aplay", "/home/Gauntlet/GauntEnv/powerstone.wav"])
	return

def realitysound():

	print("playing reality sound")
	call(["aplay", "/home/Gauntlet/GauntEnv/realitystone.wav"])
	return

def timesound():
	call(["aplay", "/home/Gauntlet/GauntEnv/timestonelong.wav"])
	return

def spacesound():
	call(["aplay", "/home/Gauntlet/GauntEnv/spacestonefirst.wav"])
	return

def mindsound():
	call(["aplay", "/home/Gauntlet/GauntEnv/powerstone.wav"])
	return

def soulsound():
	call(["aplay", "/home/Gauntlet/GauntEnv/realitystone2.wav"])
	return
