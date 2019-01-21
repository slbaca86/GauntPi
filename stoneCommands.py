#! /home/Gauntlet/.virtualenvs/Gauntlet-xis9mkqt/bin/python
import requests
from pexpect import *
from subprocess import Popen, call
import time



def lightswitch():
	return

def togglelight():

	requests.get('https://maker.ifttt.com/trigger/pclight/with/key/{ifttkey}')
	return

def bubbletoggle():
	return


def lockopen():
	return


def lockclose():

	return


def moondrop():#function for releasing little fake moon

	return


def formOfElecclip():

	return child


def ironmanstartup():
	requests.get(("http://{}:5000").format(gauntsat1))
	return


def ironmanclip():

	return child, child2


def sendcommand(engagedstones):

	if engagedstones["Power"] and sum(engagedstones.values()) == 1:
		print("Power only")

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
