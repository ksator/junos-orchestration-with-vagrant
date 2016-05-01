#-----------------------------------------------------------------------------------------------------------------------
# DESCRIPTION:
# Connect to a series of devices and print facts related to each device to both the console and an inventory text file.
#
# CONTACT:   bvilletard@juniper.net; cbinckly@juniper.net; ksator@juniper.net; pgeenens@juniper.net; tgrimonet@juniper.net
#
# CREATED:  2015-11-11
#
# VERSION: 1
#
# USAGE: print_facts.py
# -----------------------------------------------------------------------------------------------------------------------
 
from jnpr.junos import Device
port_list=["2221", "2222", "2223"]
for item in port_list:
 dev=Device(host="127.0.0.1", user="root", password="Juniper", port=item)
 dev.open()
 print ("the device "+ dev.facts["hostname"]+ " is a " + dev.facts['model'] + " running " + dev.facts["version"])
 dev.close()



