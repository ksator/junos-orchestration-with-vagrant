### About vagrant for junos: 

https://ittechnologist.wordpress.com/2015/09/09/use-vagrant-with-juniper-junos-vms-on-windows/
https://keepingitclassless.net/2015/03/go-go-gadget-networking-lab/  
https://www.dravetech.com/blog/2016/01/08/vagrant-for-network-engineers.html  
https://github.com/Juniper/vqfx10k-vagrant

### Junos vagrant boxes:  

- vsrx: https://atlas.hashicorp.com/boxes/search?utf8=%E2%9C%93&sort=&provider=&q=juniper   
- vqfx: http://www.juniper.net/us/en/dm/free-vqfx-trial/

### Vagrant presentation: 

https://github.com/ksator/vagrant-with-junos/blob/master/Vagrant.pdf

### What to find in this repository: 

There are 4 ready to use examples into this repository. There are 4 directories, each one has its own Vagranfile:   

- The directory **3_vsrx_vagrant_non_provisionning**:
    - it has vagrant details for 3 vsrx (ffp) connected together in a triangle topology.  
    - it uses a Virtualbox provider.   

- The directory **3vsrx**: 
    - it has vagrant details for a 3 vsrx (ffp) connected together in a triangle topology.  
    - it uses a vagrant provisionner (ansible).  
    - it uses a Virtualbox provider.  

- The directory **3vsrx-v2**: 
    - it has vagrant details for a 3 vsrx (ffp) connected together in a triangle topology.  
    - it use a Virtualbox provider.  
    - it uses a vagrant provisionner (ansible). This one is more advanced and interresting: ansible uses a jinja2 template to build bgp
    details for each device and then push the rendered configuration on the devices.  
    - it has also some automation content (python and ansible) you can use against the topology.  

- The directory **ubuntu_junos**:  
    - It has vagrant details for a vsrx (ffp) and an ubuntu box (14.04).  
    - It uses a Virtualbox provider.  
    - The server is provisonned (pyez, ansible, and some automation content as well). so you can use the ubuntu vagrant box to test some
    automation content against a junos vagrant box. so no need to install programs (ansible pyez ...) on your laptop.  

###  Network topology: 

The topology for all examples: https://github.com/ksator/vagrant-junos/blob/master/topology.pdf

### How to use this repository:

- Deal with the requirements:   
    - Install vagrant  
    - Install virtual box  
    - Install vagrant plugin for junos (https://github.com/JNPRAutomate/vagrant-junos)  
    - Some of these examples requires Ansible to provision automatically the Vagrant boxes.  
    
- Clone the repository: 
```
git clone https://github.com/ksator/vagrant-with-junos.git
```
- Move to the local copy:  
```
cd vagrant-with-junos
```
- Move to the directory you want to use, and then run the command "vagrant up" to create the topology:  
```
cd xxxx
vagrant up
```

### Demo 

#### example with the directory 3vsrx-v2

you first need to install Vagrant, Virtual box, and the required Vagrant plugins.  

##### Clone the repo, and move to the directory 3vsrx-v2:

```
ksator@ubuntu:~$ git clone https://github.com/ksator/vagrant-with-junos.git
ksator@ubuntu:~$ cd vagrant-with-junos/
ksator@ubuntu:~/vagrant-with-junos$ cd 3vsrx-v2
```
##### Check the installed plugins: 
```
ksator@ubuntu:~/vagrant-with-junos/3vsrx-v2$ vagrant plugin list 
vagrant-host (0.0.1)
vagrant-host-shell (0.0.4)
vagrant-junos (0.2.1)
vagrant-share (1.1.5, system)
```
##### Deploy the topology described into the Vagrantfile: 
```
ksator@ubuntu:~/vagrant-with-junos/3vsrx-v2$ vagrant up
Bringing machine 'vsrx01' up with 'virtualbox' provider...
Bringing machine 'vsrx02' up with 'virtualbox' provider...
Bringing machine 'vsrx03' up with 'virtualbox' provider...
==> vsrx01: Importing base box 'juniper/ffp-12.1X47-D15.4-packetmode'...
==> vsrx01: Matching MAC address for NAT networking...
==> vsrx01: Checking if box 'juniper/ffp-12.1X47-D15.4-packetmode' is up to date...
==> vsrx01: Setting the name of the VM: 3vsrx-v2_vsrx01_1488993393736_67595
==> vsrx01: Clearing any previously set network interfaces...
==> vsrx01: Preparing network interfaces based on configuration...
    vsrx01: Adapter 1: nat
    vsrx01: Adapter 2: intnet
    vsrx01: Adapter 3: intnet
==> vsrx01: Forwarding ports...
    vsrx01: 22 (guest) => 2221 (host) (adapter 1)
==> vsrx01: Running 'pre-boot' VM customizations...
==> vsrx01: Booting VM...
==> vsrx01: Waiting for machine to boot. This may take a few minutes...
    vsrx01: SSH address: 127.0.0.1:2221
    vsrx01: SSH username: root
    vsrx01: SSH auth method: private key
    vsrx01: 
    vsrx01: Vagrant insecure key detected. Vagrant will automatically replace
    vsrx01: this with a newly generated keypair for better security.
    vsrx01: 
    vsrx01: Inserting generated public key within guest...
    vsrx01: Removing insecure key from the guest if it's present...
    vsrx01: Key inserted! Disconnecting and reconnecting using new SSH key...
==> vsrx01: Machine booted and ready!
==> vsrx01: Checking for guest additions in VM...
    vsrx01: No guest additions were detected on the base box for this VM! Guest
    vsrx01: additions are required for forwarded ports, shared folders, host only
    vsrx01: networking, and more. If SSH fails on this machine, please install
    vsrx01: the guest additions and repackage the box to continue.
    vsrx01: 
    vsrx01: This is not an error message; everything may continue to work properly,
    vsrx01: in which case you may ignore this message.
==> vsrx01: Setting hostname...
==> vsrx01: Configuring and enabling network interfaces...
==> vsrx01: Running provisioner: ansible...
    vsrx01: Running ansible-playbook...

PLAY [Build and deploy configuration] ******************************************

TASK [Build configuration] *****************************************************
changed: [vsrx01]

TASK [Deploy config to device ... please wait] *********************************
changed: [vsrx01]

PLAY RECAP *********************************************************************
vsrx01                     : ok=2    changed=2    unreachable=0    failed=0   

==> vsrx02: Importing base box 'juniper/ffp-12.1X47-D15.4-packetmode'...
==> vsrx02: Matching MAC address for NAT networking...
==> vsrx02: Checking if box 'juniper/ffp-12.1X47-D15.4-packetmode' is up to date...
==> vsrx02: Setting the name of the VM: 3vsrx-v2_vsrx02_1488993554448_49074
==> vsrx02: Clearing any previously set network interfaces...
==> vsrx02: Preparing network interfaces based on configuration...
    vsrx02: Adapter 1: nat
    vsrx02: Adapter 2: intnet
    vsrx02: Adapter 3: intnet
==> vsrx02: Forwarding ports...
    vsrx02: 22 (guest) => 2222 (host) (adapter 1)
==> vsrx02: Running 'pre-boot' VM customizations...
==> vsrx02: Booting VM...
==> vsrx02: Waiting for machine to boot. This may take a few minutes...
    vsrx02: SSH address: 127.0.0.1:2222
    vsrx02: SSH username: root
    vsrx02: SSH auth method: private key
    vsrx02: 
    vsrx02: Vagrant insecure key detected. Vagrant will automatically replace
    vsrx02: this with a newly generated keypair for better security.
    vsrx02: 
    vsrx02: Inserting generated public key within guest...
    vsrx02: Removing insecure key from the guest if it's present...
    vsrx02: Key inserted! Disconnecting and reconnecting using new SSH key...
==> vsrx02: Machine booted and ready!
==> vsrx02: Checking for guest additions in VM...
    vsrx02: No guest additions were detected on the base box for this VM! Guest
    vsrx02: additions are required for forwarded ports, shared folders, host only
    vsrx02: networking, and more. If SSH fails on this machine, please install
    vsrx02: the guest additions and repackage the box to continue.
    vsrx02: 
    vsrx02: This is not an error message; everything may continue to work properly,
    vsrx02: in which case you may ignore this message.
==> vsrx02: Setting hostname...
==> vsrx02: Configuring and enabling network interfaces...
==> vsrx02: Running provisioner: ansible...
    vsrx02: Running ansible-playbook...

PLAY [Build and deploy configuration] ******************************************

TASK [Build configuration] *****************************************************
changed: [vsrx02]

TASK [Deploy config to device ... please wait] *********************************
changed: [vsrx02]

PLAY RECAP *********************************************************************
vsrx02                     : ok=2    changed=2    unreachable=0    failed=0   

==> vsrx03: Importing base box 'juniper/ffp-12.1X47-D15.4-packetmode'...
==> vsrx03: Matching MAC address for NAT networking...
==> vsrx03: Checking if box 'juniper/ffp-12.1X47-D15.4-packetmode' is up to date...
==> vsrx03: Setting the name of the VM: 3vsrx-v2_vsrx03_1488993722018_10236
==> vsrx03: Clearing any previously set network interfaces...
==> vsrx03: Preparing network interfaces based on configuration...
    vsrx03: Adapter 1: nat
    vsrx03: Adapter 2: intnet
    vsrx03: Adapter 3: intnet
==> vsrx03: Forwarding ports...
    vsrx03: 22 (guest) => 2223 (host) (adapter 1)
==> vsrx03: Running 'pre-boot' VM customizations...
==> vsrx03: Booting VM...
==> vsrx03: Waiting for machine to boot. This may take a few minutes...
    vsrx03: SSH address: 127.0.0.1:2223
    vsrx03: SSH username: root
    vsrx03: SSH auth method: private key
    vsrx03: 
    vsrx03: Vagrant insecure key detected. Vagrant will automatically replace
    vsrx03: this with a newly generated keypair for better security.
    vsrx03: 
    vsrx03: Inserting generated public key within guest...
    vsrx03: Removing insecure key from the guest if it's present...
    vsrx03: Key inserted! Disconnecting and reconnecting using new SSH key...
==> vsrx03: Machine booted and ready!
==> vsrx03: Checking for guest additions in VM...
    vsrx03: No guest additions were detected on the base box for this VM! Guest
    vsrx03: additions are required for forwarded ports, shared folders, host only
    vsrx03: networking, and more. If SSH fails on this machine, please install
    vsrx03: the guest additions and repackage the box to continue.
    vsrx03: 
    vsrx03: This is not an error message; everything may continue to work properly,
    vsrx03: in which case you may ignore this message.
==> vsrx03: Setting hostname...
==> vsrx03: Configuring and enabling network interfaces...
==> vsrx03: Running provisioner: ansible...
    vsrx03: Running ansible-playbook...

PLAY [Build and deploy configuration] ******************************************

TASK [Build configuration] *****************************************************
changed: [vsrx03]

TASK [Deploy config to device ... please wait] *********************************
changed: [vsrx03]

PLAY RECAP *********************************************************************
vsrx03                     : ok=2    changed=2    unreachable=0    failed=0   

```

##### Check the states of the virtual machines
```
ksator@ubuntu:~/vagrant-with-junos/3vsrx-v2$ vagrant status 
Current machine states:

vsrx01                    running (virtualbox)
vsrx02                    running (virtualbox)
vsrx03                    running (virtualbox)

This environment represents multiple VMs. The VMs are all listed
above with their current state. For more information about a specific
VM, run `vagrant status NAME`.
```
##### Check the junos configuration files (the jinja2 template is rendered by ansible): 
```
ksator@ubuntu:~/vagrant-with-junos/3vsrx-v2$ more /tmp/vsrx01.conf 
system {
    host-name vsrx01;
    services {
        ssh {
            root-login allow;
        }
        netconf {
            ssh;
        }
    }
}
interfaces {
    ge-0/0/1 {
        unit 0 {
            description "to vsrx02";
            family inet {
                address 192.168.0.0/31;
            }
        }
    }
    ge-0/0/2 {
        unit 0 {
            description "to vsrx03";
            family inet {
                address 192.168.0.2/31;
            }
        }
    }
}
protocols {
    lldp {
        interface all;
    }
    bgp {
        group underlay {
            import bgp-in;
            export bgp-out;
            type external;
            local-as 104;
            multipath multiple-as;
            neighbor 192.168.0.1 {
                peer-as 109;
            }
            neighbor 192.168.0.3 {
                peer-as 110;
            }
        }
    }
}

routing-options {
    router-id 10.20.1.1;
    forwarding-table {
        export bgp-ecmp;
    }
}

policy-options {
    policy-statement bgp-ecmp {
        then {
            load-balance per-packet;
        }
    }
    policy-statement bgp-in {
        then accept;
    }
    policy-statement bgp-out {
        then accept;
    }
}
```
##### Check the devices configuration (they are provisonned by ansible): 
```
ksator@ubuntu:~/vagrant-with-junos/3vsrx-v2$ vagrant ssh vsrx01
--- JUNOS 12.1X47-D15.4 built 2014-11-12 02:13:59 UTC
root@vsrx01% cli

root@vsrx01> show system commit          
0   2017-03-08 17:19:06 UTC by root via netconf
    configured by ansible

root@vsrx01> show configuration | compare rollback 1 
[edit interfaces ge-0/0/1 unit 0]
+    description "to vsrx02";
[edit interfaces ge-0/0/1 unit 0 family inet]
+       address 192.168.0.0/31;
[edit interfaces ge-0/0/2 unit 0]
+    description "to vsrx03";
[edit interfaces ge-0/0/2 unit 0 family inet]
+       address 192.168.0.2/31;
[edit]
+  routing-options {
+      router-id 10.20.1.1;
+      forwarding-table {
+          export bgp-ecmp;
+      }
+  }
+  protocols {
+      bgp {
+          group underlay {
+              type external;
+              import bgp-in;
+              export bgp-out;
+              local-as 104;
+              multipath multiple-as;
+              neighbor 192.168.0.1 {
+                  peer-as 109;
+              }
+              neighbor 192.168.0.3 {
+                  peer-as 110;
+              }
+          }                            
+      }
+      lldp {
+          interface all;
+      }
+  }
+  policy-options {
+      policy-statement bgp-ecmp {
+          then {
+              load-balance per-packet;
+          }
+      }
+      policy-statement bgp-in {
+          then accept;
+      }
+      policy-statement bgp-out {
+          then accept;
+      }
+  }
```
##### Check the devices op states of the devices: 
```
root@vsrx01> show lldp neighbors 
Local Interface    Parent Interface    Chassis Id          Port info          System Name
ge-0/0/1.0         -                   4c:96:14:10:01:00   to vsrx01          vsrx02              
ge-0/0/2.0         -                   4c:96:14:10:01:00   to vsrx01          vsrx03              


root@vsrx01> show bgp neighbor   
Peer: 192.168.0.1+179 AS 109   Local: 192.168.0.0+51314 AS 104  
  Type: External    State: Established    Flags: <Sync>
  Last State: OpenConfirm   Last Event: RecvKeepAlive
  Last Error: Cease
  Export: [ bgp-out ] Import: [ bgp-in ]
  Options: <Preference PeerAS Multipath LocalAS Refresh>
  Options: <MultipathAs>
  Holdtime: 90 Preference: 170 Local AS: 104 Local System AS: 0
  Number of flaps: 2
  Last flap event: Stop
  Error: 'Cease' Sent: 2 Recv: 0
  Peer ID: 10.20.1.2       Local ID: 10.20.1.1         Active Holdtime: 90
  Keepalive Interval: 30         Peer index: 0   
  BFD: disabled, down
  Local Interface: ge-0/0/1.0                       
  NLRI for restart configured on peer: inet-unicast
  NLRI advertised by peer: inet-unicast
  NLRI for this session: inet-unicast
  Peer supports Refresh capability (2)
  Stale routes from peer are kept for: 300
  Peer does not support Restarter functionality
  NLRI that restart is negotiated for: inet-unicast
  NLRI of received end-of-rib markers: inet-unicast
  NLRI of all end-of-rib markers sent: inet-unicast
  Peer supports 4 byte AS extension (peer-as 109)
  Peer does not support Addpath
  Table inet.0 Bit: 10000
    RIB State: BGP restart is complete
    Send state: in sync
    Active prefixes:              1     
    Received prefixes:            4
    Accepted prefixes:            4
    Suppressed due to damping:    0
    Advertised prefixes:          4
  Last traffic (seconds): Received 21   Sent 22   Checked 12  
  Input messages:  Total 24     Updates 6       Refreshes 0     Octets 624
  Output messages: Total 31     Updates 8       Refreshes 0     Octets 908
  Output Queue[0]: 0

Peer: 192.168.0.3+55454 AS 110 Local: 192.168.0.2+179 AS 104  
  Type: External    State: Established    Flags: <Sync>
  Last State: OpenConfirm   Last Event: RecvKeepAlive
  Last Error: Cease
  Export: [ bgp-out ] Import: [ bgp-in ]
  Options: <Preference PeerAS Multipath LocalAS Refresh>
  Options: <MultipathAs>
  Holdtime: 90 Preference: 170 Local AS: 104 Local System AS: 0
  Number of flaps: 3
  Last flap event: RecvNotify
  Error: 'Cease' Sent: 1 Recv: 1
  Peer ID: 10.20.1.3       Local ID: 10.20.1.1         Active Holdtime: 90
  Keepalive Interval: 30         Peer index: 1   
  BFD: disabled, down
  Local Interface: ge-0/0/2.0                       
  NLRI for restart configured on peer: inet-unicast
  NLRI advertised by peer: inet-unicast
  NLRI for this session: inet-unicast
  Peer supports Refresh capability (2)
  Stale routes from peer are kept for: 300
  Peer does not support Restarter functionality
  NLRI that restart is negotiated for: inet-unicast
  NLRI of received end-of-rib markers: inet-unicast
  NLRI of all end-of-rib markers sent: inet-unicast
  Peer supports 4 byte AS extension (peer-as 110)
  Peer does not support Addpath
  Table inet.0 Bit: 10000
    RIB State: BGP restart is complete
    Send state: in sync
    Active prefixes:              1
    Received prefixes:            4
    Accepted prefixes:            4
    Suppressed due to damping:    0
    Advertised prefixes:          5
  Last traffic (seconds): Received 5    Sent 3    Checked 87  
  Input messages:  Total 9      Updates 4       Refreshes 0     Octets 302
  Output messages: Total 7      Updates 2       Refreshes 0     Octets 268
  Output Queue[0]: 0

root@vsrx01> exit 

root@vsrx01% exit
logout
Connection to 127.0.0.1 closed.
```
##### execute automation content against the topology:  
```
ksator@ubuntu:~/vagrant-with-junos/3vsrx-v2$ python programatic_access/python/print_facts_vagrant.py
the device vsrx01 is a FIREFLY-PERIMETER running 12.1X47-D15.4
the device vsrx02 is a FIREFLY-PERIMETER running 12.1X47-D15.4
the device vsrx03 is a FIREFLY-PERIMETER running 12.1X47-D15.4
```

```
ksator@ubuntu:~/vagrant-with-junos/3vsrx-v2$ ansible-playbook programatic_access/ansible/get_facts.p.yml -i .vagrant/provisioners/ansible/inventory/vagrant_ansible_inventory

PLAY [Get Facts] ***************************************************************

TASK [Retrieve information from devices running Junos] *************************
ok: [vsrx03]
ok: [vsrx02]
ok: [vsrx01]

TASK [Print some facts] ********************************************************
ok: [vsrx01] => {
    "msg": "device vsrx01 runs version 12.1X47-D15.4"
}
ok: [vsrx03] => {
    "msg": "device vsrx03 runs version 12.1X47-D15.4"
}
ok: [vsrx02] => {
    "msg": "device vsrx02 runs version 12.1X47-D15.4"
}

PLAY RECAP *********************************************************************
vsrx01                     : ok=2    changed=0    unreachable=0    failed=0   
vsrx02                     : ok=2    changed=0    unreachable=0    failed=0   
vsrx03                     : ok=2    changed=0    unreachable=0    failed=0   
```
##### destroy the VMs: 
```
ksator@ubuntu:~/vagrant-with-junos/3vsrx-v2$ vagrant destroy 
    vsrx03: Are you sure you want to destroy the 'vsrx03' VM? [y/N] y
==> vsrx03: Forcing shutdown of VM...
==> vsrx03: Destroying VM and associated drives...
    vsrx02: Are you sure you want to destroy the 'vsrx02' VM? [y/N] y
==> vsrx02: Forcing shutdown of VM...
==> vsrx02: Destroying VM and associated drives...
    vsrx01: Are you sure you want to destroy the 'vsrx01' VM? [y/N] y
==> vsrx01: Forcing shutdown of VM...
==> vsrx01: Destroying VM and associated drives...

ksator@ubuntu:~/vagrant-with-junos/3vsrx-v2$ vagrant status 
Current machine states:

vsrx01                    not created (virtualbox)
vsrx02                    not created (virtualbox)
vsrx03                    not created (virtualbox)

This environment represents multiple VMs. The VMs are all listed
above with their current state. For more information about a specific
VM, run `vagrant status NAME`.

```
