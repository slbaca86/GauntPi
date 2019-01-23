#! /home/Gauntlet/.virtualenvs/Gauntlet-xis9mkqt/bin/python
import requests
from pexpect import *
from subprocess import Popen, call
import time
import json

with open('deviceDict.txt') as devices:
	device = json.load(devices)

def lightswitch():
	return

def lightsOff():
	requests.get("{}{}".format(data["devices"][3]["URL"], data["keys"][0]["URL"])
	return

def bubbletoggle():
	return


def lockopen():
	return


def lockclose():

	return


def formOfElecclip():

	return child


def ironmanstartup():
	requests.get(("http://{}:5000").format(gauntsat1))
	return


def ironmanclip():
	return

def sendcommand(engagedstones):

	if engagedstones["Power"] and sum(engagedstones.values()) == 1:
		print("Power only")
		lightsOff()
	if engagedstones["Soul"] and sum(engagedstones.values()) == 1:
		print("Soul only")
	if engagedstones["Time"] and sum(engagedstones.values()) == 1:
		print("Time only")
	if engagedstones["Space"]and sum(engagedstones.values()) == 1:
		print("Space only")
	if engagedstones["Mind"] and sum(engagedstones.values()) == 1:
		print("Mind only")
	if engagedstones["Reality"] and sum(engagedstones.values()) == 1:
		print("Reality only")
	if engagedstones["Soul"] and engagedstones["Power"]:
		pass
	if engagedstones["Soul"] and engagedstones["Space"]:
		pass
	if engagedstones["Soul"] and engagedstones["Mind"]:
		pass
	if engagedstones["Soul"] and engagedstones["Time"]:
	 	pass
	if engagedstones["Soul"] and engagedstones["Space"]:
		pass
	if engagedstones["Time"] and engagedstones["Mind"]:
		pass
	if engagedstones["Reality"] and engagedstones["Space"]:
		pass
	if engagedstones["Reality"] and engagedstones["Soul"]:
		pass
	if engagedstones["Power"] and engagedstones["Time"]:
		pass

	return

def powersound():
	print("playing power sound")
	call(["aplay", "./wavfiles/powerstone.wav"])
	return

def realitysound():
	print("playing reality sound")
	call(["aplay", "./wavfiles/realitystone.wav"])
	return

def timesound():
	print("playing time sound")
	call(["aplay", "./wavfiles/timestonelong.wav"])
	return

def spacesound():
	print("playing space sound")
	call(["aplay", "./wavfiles/spacestonefirst.wav"])
	return

def mindsound():
	print("playing mind sound")
	call(["aplay", "./wavfiles/powerstone.wav"])
	return

def soulsound():
	print("playing soul sound")
	call(["aplay", "./wavfiles/realitystone2.wav"])
	return
