import pyeapi
import pprint
import os
import sys
import json
import requests
from datetime import datetime
from prettytable import PrettyTable, ALL, FRAME, from_json

pp = pprint.PrettyPrinter()

#double check you have the .eapi.conf in the correct dir

# list of all leaf swiches
leafs = ['leaf1','leaf2','leaf3','leaf4']
# list of all spine switches
spines = ['spine1','spine2']
# list of end host for ping tests
hosts = ['host1','host2']

## Todo , write file to output in local Dir
## Filter the response msg from the pings, only show [-2] second to last index in list
## Use PrettyTable to present info in a nicer format.

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


def ping_l2hosts():
    """ Get Devices """
    pt = PrettyTable()
    pt.field_names = ["Role", "Name", "FabricState","Adst"]
    for host in hosts:
        # Connect to the Arista switch using eAPI
        connection = pyeapi.connect_to(host)
        # Send the command to ping both loopbacks for h1
        ping_hx = connection.enable('ping 10.10.10.1')
        # Parse the response for MLAG status
        ping_response = ping_hx[0]['result']['messages']
        # Print the response from switch
        print("\n"+40*'='+' Ping 10.10.10.1 Host1, from '+host+' '+'='*40+"\n")
        pp.pprint(ping_response)
        # Send the command to ping both loopbacks for h2
        ping_hx = connection.enable('ping 10.10.10.2')
        # Parse the response for MLAG status
        ping_response = ping_hx[0]['result']['messages']
        # Print the response from switch
        print("\n"+40*'='+' Ping 10.10.10.2 Host2, from '+host+' '+'='*40+"\n")
        pp.pprint(ping_response)


ping_l2hosts()

def ping_l3hosts():
    """ Get Devices """
    pt = PrettyTable()
    pt.field_names = ["Role", "Name", "FabricState","Adst"]
    for host in hosts:
        # Connect to the Arista switch using eAPI
        connection = pyeapi.connect_to(host)
        # Send the command to ping both loopbacks for h1
        ping_hx = connection.enable('ping 9.9.9.9')
        # Parse the response for MLAG status
        ping_response = ping_hx[0]['result']['messages']
        # Print the response from switch
        print("\n"+40*'='+' Ping 9.9.9.9 Host1, from '+host+' '+'='*40+"\n")
        pp.pprint(ping_response)
        # Send the command to ping both loopbacks for h2
        ping_hx = connection.enable('ping 8.8.8.8')
        # Parse the response for MLAG status
        ping_response = ping_hx[0]['result']['messages']
        # Print the response from switch
        print("\n"+40*'='+' Ping 8.8.8.8 Host2, from '+host+' '+'='*40+"\n")
        pp.pprint(ping_response)


ping_l3hosts()

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
        # Parse the response 
        bgp_evpnRt2 = response[0]['result']['evpnRoutes']
        # Print the response from switchs
        print("\n"+40*'='+' GET ALL RouteType-2 '+leaf+' '+'='*40+"\n")
        for key, value in bgp_evpnRt2.items():
            print (key)
        # print(bgp_evpnRt2)
        # print("\n"+80*'='+'='*40+"\n")

get_rt2()

def get_rt5():
    """ Get Devices """
    pt = PrettyTable()
    pt.field_names = ["Role", "Name", "FabricState","Adst"]
    for leaf in leafs:
        # Connect to the Arista switch using eAPI
        connection = pyeapi.connect_to(leaf)
        # Send the command to retrieve MLAG status
        response = connection.enable('show bgp evpn route-type ip-prefix ipv4')
        # Parse the response 
        bgp_evpnRt5 = response[0]['result']['evpnRoutes']
        # Print the response from switchs
        print("\n"+40*'='+' GET ALL RouteType-5 '+leaf+' '+'='*40+"\n")
        for key, value in bgp_evpnRt5.items():
            print (key)
        # print(bgp_evpnRt2)
        # print("\n"+80*'='+'='*40+"\n")

get_rt5()


