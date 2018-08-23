#!/usr/bin/env python
from __future__ import print_function
import requests
import json
from argparse import ArgumentParser

#requests.packages.urllib3.disable_warnings()
USER="s34866"
PASSWORD="home4589"
BASE="https://%s:%s@10.139.43.60//webacs/api/v2/" %(USER,PASSWORD)

class NoDeviceFound(Exception):
    pass
def all_devices():
    print ("Getting all devices")
    print ("{0:6s} {1:10s}".format("ID", "IP address"))
    result = requests.get(BASE + "data/Devices.json?.full=true&.maxResults=1000&productFamily=contains(Routers)", verify=False)
    result.raise_for_status()
    for device in result.json()['queryResponse']['entity']:
        print (device['devicesDTO']['ipAddress'])
        #print (device['devicesDTO']['productFamily'], device['devicesDTO']['ipAddress'])
        # if device['devicesDTO']['productFamily'] == 'Routers':
        #     print device['devicesDTO']['ipAddress'])

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
