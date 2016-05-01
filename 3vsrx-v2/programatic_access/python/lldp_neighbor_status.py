from jnpr.junos import Device
from jnpr.junos.op.lldp import LLDPNeighborTable

port_list=["2221", "2222", "2223"]

for item in port_list:
 dev=Device(host="127.0.0.1", user="root", password="Juniper", port=item)
 dev.open()
 lldp_neighbors=LLDPNeighborTable(dev)
 lldp_neighbors.get()
 print "\nstatus of LLDP neighbors of " + dev.facts["hostname"]+ ":"
 for xxx in lldp_neighbors:
  print "interface " + xxx.local_int + " has this neighbor: " + xxx.remote_sysname
 dev.close()

