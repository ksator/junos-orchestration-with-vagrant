from jnpr.junos import Device
from jnpr.junos.op.bgp import *

port_list=["2221", "2222", "2223"]

for item in port_list:
 dev=Device(host="127.0.0.1", user="root", password="Juniper", port=item)
 dev.open()
 bgp=BGPNeighborTable (dev)
 bgp.get()
 print "\nstatus of BGP neighbors of " + dev.facts["hostname"]+ ":"
 for xxx in bgp:
 	print xxx.type + " BGP neighbor " + xxx.neighbor + " is " + xxx.state + " (flap count is: " + xxx.flap_count +")" 
 dev.close()
