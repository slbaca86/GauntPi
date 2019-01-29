<<<<<<< HEAD
#! /home/Gauntlet/.virtualenvs/Gauntlet-xis9mkqt/bin/python
import requests
from pexpect import *
from subprocess import Popen, call
import time
import json

with open('deviceDict.txt') as devices:
	deviceDict = json.load(devices)


def getIftttkey():
    return deviceDict["keys"][0]["key"]


def getDeviceURL(deviceName):
    for dict in deviceDict["devices"]:
            if dict["Name"] == deviceName:
                return dict["URL"]


def deviceRequest(deviceName, urlFetch, keyFetch):
    for dict in deviceDict["devices"]:
            if dict["Name"] == deviceName:
                if "ifttt" in dict["URL"]:
                    requests.get(("{}{}").format(urlFetch(deviceName), keyFetch()))
                else:
                    requests.get(("{}").format(urlFetch(deviceName)))
                    return

def selectDevice(engagedstones):

	devices = []

	if engagedstones["Power"] and sum(engagedstones.values()) == 1:
		print("Power only")
		devices.append("Allights")
	if engagedstones["Soul"] and sum(engagedstones.values()) == 1:
		print("Soul only")
		devices.append("FPON")
	if engagedstones["Time"] and sum(engagedstones.values()) == 1:
		print("Time only")
	if engagedstones["Space"]and sum(engagedstones.values()) == 1:
		print("Space only")
		devices.append("FDUL")
	if engagedstones["Mind"] and sum(engagedstones.values()) == 1:
		print("Mind only")
		devices.append("familylight")
	if engagedstones["Reality"] and sum(engagedstones.values()) == 1:
		print("Reality only")
		devices.append("FPON")
	if engagedstones["Soul"] and engagedstones["Power"]:
		pass
	if engagedstones["Power"] and engagedstones["Time"]:
		devices.append("PClightOn")
	if engagedstones["Soul"] and engagedstones["Space"]:
		pass
	if engagedstones["Soul"] and engagedstones["Mind"]:
		pass
	if engagedstones["Soul"] and engagedstones["Time"]:
	 	pass
	if engagedstones["Soul"] and engagedstones["Space"]:
		pass
	if engagedstones["Time"] and engagedstones["Mind"]:
		devices.append("familylightoff")
		pass
	if engagedstones["Reality"] and engagedstones["Space"]:
		pass
	if engagedstones["Reality"] and engagedstones["Soul"]:
		pass
	if engagedstones["Power"] and engagedstones["Time"]:
		pass

	return devices

def sendCommand(reqFunc, getUrlfunc, keyFunc, devList):
    for device in devList:
        reqFunc(device, getUrlfunc, keyFunc)
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
=======
#! /home/Gauntlet/.virtualenvs/Gauntlet-xis9mkqt/bin/python
import requests
from pexpect import *
from subprocess import Popen, call
import time
import json

with open('deviceDict.txt') as devices:
	deviceDict = json.load(devices)


def getIftttkey():
    return deviceDict["keys"][0]["key"]


def getDeviceURL(deviceName):
    for dict in deviceDict["devices"]:
            if dict["Name"] == deviceName:
                return dict["URL"]


def deviceRequest(deviceName, urlFetch, keyFetch):
    for dict in deviceDict["devices"]:
            if dict["Name"] == deviceName:
                if "ifttt" in dict["URL"]:
                    requests.get(("{}{}").format(urlFetch(deviceName), keyFetch()))
                else:
                    requests.get(("{}").format(urlFetch(deviceName)))
                    return

def selectDevice(engagedstones):

	devices = []

	if engagedstones["Power"] and sum(engagedstones.values()) == 1:
		print("Power only")
		devices.append("Allights")
	if engagedstones["Soul"] and sum(engagedstones.values()) == 1:
		print("Soul only")
		devices.append("FPON")
	if engagedstones["Time"] and sum(engagedstones.values()) == 1:
		print("Time only")
	if engagedstones["Space"]and sum(engagedstones.values()) == 1:
		print("Space only")
		devices.append("FDUL")
	if engagedstones["Mind"] and sum(engagedstones.values()) == 1:
		print("Mind only")
		devices.append("familylight")
	if engagedstones["Reality"] and sum(engagedstones.values()) == 1:
		print("Reality only")
		devices.append("FPON")
	if engagedstones["Soul"] and engagedstones["Power"]:
		pass
	if engagedstones["Power"] and engagedstones["Time"]:
		devices.append("PClightOn")
	if engagedstones["Soul"] and engagedstones["Space"]:
		pass
	if engagedstones["Soul"] and engagedstones["Mind"]:
		pass
	if engagedstones["Soul"] and engagedstones["Time"]:
	 	pass
	if engagedstones["Soul"] and engagedstones["Space"]:
		pass
	if engagedstones["Time"] and engagedstones["Mind"]:
		devices.append("familylightoff")
		pass
	if engagedstones["Reality"] and engagedstones["Space"]:
		pass
	if engagedstones["Reality"] and engagedstones["Soul"]:
		pass
	if engagedstones["Power"] and engagedstones["Time"]:
		pass

	return devices

def sendCommand(reqFunc, getUrlfunc, keyFunc, devList):
    for device in devList:
        reqFunc(device, getUrlfunc, keyFunc)
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
>>>>>>> bb5d13141812bab07d2c10679a0f9437a7603f04
