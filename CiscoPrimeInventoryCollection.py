#This script collects device info from Cisco Prime Inventory Manager and returns data in seperate files.
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

#requests.packages.urllib3.disable_warnings()
USER="XXXXX"
PASSWORD="XXXXX"

IOS_ROUTERS = open('/home/ogruca/pythonscripts/prime/IOS_ROUTERS','w')
IOS_XE_ROUTERS = open('/home/ogruca/pythonscripts/prime/IOS_XE_ROUTERS','w')
CATALYST = open('/home/ogruca/pythonscripts/prime/CATALYST','w')
NEXUS = open('/home/ogruca/pythonscripts/prime/NEXUS','w')
BASE="https://%s:%s@IP-OF-CISCO-PRIME//webacs/api/v2/" %(USER,PASSWORD)

class NoDeviceFound(Exception):
    pass
def all_devices():
    print ("Getting all IOS Routers")
    print (format("IP address"))
    result0 = requests.get(BASE + "data/Devices.json?.full=true&.maxResults=1000&productFamily=contains(Routers)&softwareType=contains(IOS)", verify=False)
    result0.raise_for_status()

    for device in result0.json()['queryResponse']['entity']:
        print (device['devicesDTO']['ipAddress'])
        IOS_ROUTERS.write(device['devicesDTO']['ipAddress'] + '\n')

    print ("Getting all IOS-XE Routers")
    print (format("IP address"))
    result1 = requests.get(BASE + "data/Devices.json?.full=true&.maxResults=1000&productFamily=contains(Routers)&softwareType=contains(IOS-XE)", verify=False)
    result1.raise_for_status()

    for device in result1.json()['queryResponse']['entity']:
        print (device['devicesDTO']['ipAddress'])
        IOS_XE_ROUTERS.write(device['devicesDTO']['ipAddress'] + '\n')

    print ("Getting all Catalyst Switches")
    print (format("IP address"))
    result2 = requests.get(BASE + "data/Devices.json?.full=true&.maxResults=1000&productFamily=contains(Hubs)&deviceType=contains(Catalyst)", verify=False)
    result2.raise_for_status()

    for device in result2.json()['queryResponse']['entity']:
        print (device['devicesDTO']['ipAddress'])
        CATALYST.write(device['devicesDTO']['ipAddress'] + '\n')


    print ("Getting all Nexus Switches")
    print (format("IP address"))
    result3 = requests.get(BASE + "data/Devices.json?.full=true&.maxResults=1000&productFamily=contains(Hubs)&deviceType=contains(Nexus)", verify=False)
    result3.raise_for_status()

    for device in result3.json()['queryResponse']['entity']:
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
