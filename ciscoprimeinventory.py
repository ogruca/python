#!/usr/bin/env python
from __future__ import print_function
import requests
import json
from argparse import ArgumentParser
import paramiko
import threading
import os.path
import subprocess
import smtplib
import time
import sys
import re
import pdb
import shutil
import pdb

# requests.packages.urllib3.disable_warnings()
USER = "xxxx"
PASSWORD = "xxxxx"

ROUTERSIOS = open('/home/ogruca/scripts/pythonscripts/prime/inventory/ROUTERS-IOS', 'w')
ROUTERSIOSXE = open('/home/ogruca/scripts/pythonscripts/prime/inventory/ROUTERS-IOS-XE', 'w')
CATALYSTIOS = open('/home/ogruca/scripts/pythonscripts/prime/inventory/CATALYST-IOS', 'w')
CATALYSTIOSXE = open('/home/ogruca/scripts/pythonscripts/prime/inventory/CATALYST-IOS-XE', 'w')
NEXUS = open('/home/ogruca/scripts/pythonscripts/prime/inventory/NEXUS', 'w')
BASE = "https://%s:%s@10.139.43.60//webacs/api/v2/" %(USER, PASSWORD)


class NoDeviceFound(Exception):
    pass


def all_devices():
#################################### start getting IOS routers ####################################
    print ('~'*79)
    print ("Getting all IOS Routers")
    print ('~'*79)
    result0 = requests.get(BASE + "data/Devices.json?.full=true&.maxResults=1000&productFamily=eq(Routers)&softwareType=eq(IOS)", verify=False)
    result0.raise_for_status()


    for device in result0.json()['queryResponse']['entity']:
        print (device['devicesDTO']['ipAddress'])
        ROUTERSIOS.write(device['devicesDTO']['ipAddress'] + '\n')

####################################start getting IOS-XE Routers ####################################
    print ('~'*79)
    print ("Getting all IOS-XE Routers")
    print ('~'*79)
    result1 = requests.get(BASE + "data/Devices.json?.full=true&.maxResults=1000&productFamily=eq(Routers)&softwareType=eq(IOS-XE)", verify=False)
    result1.raise_for_status()


    for device in result1.json()['queryResponse']['entity']:
        print (device['devicesDTO']['ipAddress'])
        ROUTERSIOSXE.write(device['devicesDTO']['ipAddress'] + '\n')

#################################### start getting IOS switches ####################################
    print ('~'*79)
    print ("Getting all Catalyst IOS Switches")
    print ('~'*79)
    result2 = requests.get(BASE + "data/Devices.json?.full=true&.maxResults=1000&productFamily=eq(\"Switches and Hubs\")&softwareType=eq(IOS)", verify=False)
    result2.raise_for_status()


    for device in result2.json()['queryResponse']['entity']:
        print (device['devicesDTO']['ipAddress'])
        CATALYSTIOS.write(device['devicesDTO']['ipAddress'] + '\n')

#################################### start getting IOS-XE switches ####################################
    print ('~'*79)
    print ("Getting all Catalyst IOS-XE Switches")
    print ('~'*79)
    result3 = requests.get(BASE + "data/Devices.json?.full=true&.maxResults=1000&productFamily=eq(\"Switches and Hubs\")&softwareType=eq(IOS-XE)", verify=False)
    result3.raise_for_status()


    for device in result3.json()['queryResponse']['entity']:
        print (device['devicesDTO']['ipAddress'])
        CATALYSTIOSXE.write(device['devicesDTO']['ipAddress'] + '\n')

#################################### start getting nexus switches ####################################
    print ('~'*79)
    print ("Getting all Nexus Switches")
    print ('~'*79)
    result4 = requests.get(BASE + "data/Devices.json?.full=true&.maxResults=1000&productFamily=eq(\"Switches and Hubs\")&softwareType=eq(NX-OS)", verify=False)
    result4.raise_for_status()


    for device in result4.json()['queryResponse']['entity']:
        print (device['devicesDTO']['ipAddress'])
        NEXUS.write(device['devicesDTO']['ipAddress'] + '\n')


def device_by_id(id):
    print ("Getting a specific device")
    result = requests.get(BASE + "data/Devices/%s.json?.full=true" % id, verify=False)
    result.raise_for_status()
    print (json.dumps(result.json(), indent=2))


def device_by_ip(ip):
    result = requests.get(BASE + "data/Devices.json?.full=true&ipAddress=%s" % ip, verify=False)
    result.raise_for_status()
    if result.json()['queryResponse']['@count'] == "1":
        return result.json()
    else:
        raise NoDeviceFound("No device with ip: %s" %ip)


def device_to_id(devicesearchDTO):
    return devicesearchDTO['queryResponse']['entity'][0]['devicesDTO']['@id']


if __name__ == "__main__":
    parser = ArgumentParser(description='Select options.')
    parser.add_argument('--id', type=str,
                        help="device details by id")
    parser.add_argument('--ip', type=str,
                        help="device details by ip address")
    args = parser.parse_args()

    if args.id:
        device_by_id(args.id)
    elif args.ip:
        print (json.dumps(device_by_ip(args.ip), indent=2))
    else:
        all_devices()
