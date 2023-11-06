import pyeapi
import pprint
import os
import sys
import json
import requests
from datetime import datetime
from prettytable import PrettyTable, ALL, FRAME, from_json

#double check you have the .eapi.conf in the correct dir

# list of all leaf swiches
leafs = ['leaf1','leaf2','leaf3','leaf4']
# list of all spine switches
spines = ['spine1','spine2']

# Connect to the Arista switch using eAPI
connection = pyeapi.connect_to('leaf1')

# Send the command to retrieve MLAG status
response = connection.enable('show mlag')

# Print the MLAG status
# print(response)

# Parse the response for MLAG status
mlag_status = response[0]['result']['state']
mlag_sysmac = response[0]['result']['systemId']

# Print the MLAG status
# print(mlag_status)

# Print the MLAG SysMAC
# print(mlag_sysmac)



def write_output(data, funcname):
    """ Write a file to the present working directory """
    today = datetime.now()
    if not os.path.exists('pyeAPI-output'):
        os.mkdir('pyeAPI-output')
    os.makedirs("pyeAPI-output/"+today.strftime("%d-%m-%Y"), exist_ok=True)
    day = "pyeAPI-output/"+today.strftime("%d-%m-%Y")
    with open(os.path.join(day, (today.strftime('%d-%m-%Y_%H%M%S')+funcname+'_output.json')), 'w') as outfile: 
        json.dump(data, outfile)

def append_new_line(file_name, text_to_append):
    """Append given text as a new line at the end of file"""
    tday = datetime.now()
    day = "pyeAPI-output/"+tday.strftime("%d-%m-%Y")
    original = sys.stdout
    # Open the file in append & read mode ('a+')
    with open(os.path.join(day, (tday.strftime('%d-%m-%Y_%H%M')+file_name)), "a+") as file_object:
        # Move read cursor to the start of file.
        file_object.seek(0)
        # If file is not empty then append '\n'
        data = file_object.read(100)
        if len(data) > 0:
            file_object.write("\n")
        # Append text at the end of file
        file_object.write(text_to_append)
    sys.stdout = original

### Get the All the Fabric EVPN Route-type 2's

def get_rt2():
    """ Get Devices """
    pt = PrettyTable()
    pt.field_names = ["Role", "Name", "FabricState","Adst"]
    for leaf in leafs:
        # Connect to the Arista switch using eAPI
        connection = pyeapi.connect_to(leaf)
        # Send the command to retrieve MLAG status
        response = connection.enable('show bgp evpn route-type mac-ip')
        # Parse the response for MLAG status
        bgp_evpnRt2 = response[0]['result']['evpnRoutes']
        # Print the response from switch
        print("\n"+40*'='+' GET ALL RouteType-2 '+leaf+' '+'='*40+"\n")
        for key, value in bgp_evpnRt2.items():
            print (key)
        # print(bgp_evpnRt2)
        # print("\n"+80*'='+'='*40+"\n")

get_rt2()