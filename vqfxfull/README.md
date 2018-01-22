This vagrantfile is using a vqfx10k-re and a vqfx10k-pfe

```
root@ubuntu:~/vagrant-with-junos/test# vagrant up
Bringing machine 'vqfx-pfe' up with 'virtualbox' provider...
Bringing machine 'vqfx' up with 'virtualbox' provider...
==> vqfx-pfe: Importing base box 'juniper/vqfx10k-pfe'...
==> vqfx-pfe: Matching MAC address for NAT networking...
==> vqfx-pfe: Checking if box 'juniper/vqfx10k-pfe' is up to date...
==> vqfx-pfe: Setting the name of the VM: test_vqfx-pfe_1516633701496_53622
==> vqfx-pfe: Clearing any previously set network interfaces...
==> vqfx-pfe: Preparing network interfaces based on configuration...
    vqfx-pfe: Adapter 1: nat
    vqfx-pfe: Adapter 2: intnet
==> vqfx-pfe: Forwarding ports...
    vqfx-pfe: 22 (guest) => 2222 (host) (adapter 1)
==> vqfx-pfe: Booting VM...
==> vqfx-pfe: Waiting for machine to boot. This may take a few minutes...
    vqfx-pfe: SSH address: 127.0.0.1:2222
    vqfx-pfe: SSH username: vagrant
    vqfx-pfe: SSH auth method: private key
==> vqfx-pfe: Machine booted and ready!
==> vqfx-pfe: Checking for guest additions in VM...
    vqfx-pfe: No guest additions were detected on the base box for this VM! Guest
    vqfx-pfe: additions are required for forwarded ports, shared folders, host only
    vqfx-pfe: networking, and more. If SSH fails on this machine, please install
    vqfx-pfe: the guest additions and repackage the box to continue.
    vqfx-pfe: 
    vqfx-pfe: This is not an error message; everything may continue to work properly,
    vqfx-pfe: in which case you may ignore this message.
==> vqfx: Importing base box 'juniper/vqfx10k-re'...
==> vqfx: Matching MAC address for NAT networking...
==> vqfx: Checking if box 'juniper/vqfx10k-re' is up to date...
==> vqfx: Setting the name of the VM: test_vqfx_1516633767444_51809
==> vqfx: Fixed port collision for 22 => 2222. Now on port 2200.
==> vqfx: Clearing any previously set network interfaces...
==> vqfx: Preparing network interfaces based on configuration...
    vqfx: Adapter 1: nat
    vqfx: Adapter 2: intnet
    vqfx: Adapter 3: intnet
    vqfx: Adapter 4: intnet
    vqfx: Adapter 5: intnet
    vqfx: Adapter 6: intnet
    vqfx: Adapter 7: intnet
    vqfx: Adapter 8: intnet
==> vqfx: Forwarding ports...
    vqfx: 22 (guest) => 2200 (host) (adapter 1)
==> vqfx: Booting VM...
==> vqfx: Waiting for machine to boot. This may take a few minutes...
    vqfx: SSH address: 127.0.0.1:2200
    vqfx: SSH username: vagrant
    vqfx: SSH auth method: private key
==> vqfx: Machine booted and ready!
==> vqfx: Checking for guest additions in VM...
    vqfx: No guest additions were detected on the base box for this VM! Guest
    vqfx: additions are required for forwarded ports, shared folders, host only
    vqfx: networking, and more. If SSH fails on this machine, please install
    vqfx: the guest additions and repackage the box to continue.
    vqfx: 
    vqfx: This is not an error message; everything may continue to work properly,
    vqfx: in which case you may ignore this message.
==> vqfx: Setting hostname...
```
```
root@ubuntu:~/vagrant-with-junos/test# vagrant status 
Current machine states:

vqfx-pfe                  running (virtualbox)
vqfx                      running (virtualbox)

This environment represents multiple VMs. The VMs are all listed
above with their current state. For more information about a specific
VM, run `vagrant status NAME`.
```
```
root@ubuntu:~/vagrant-with-junos/test# vagrant ssh vqfx
--- JUNOS 15.1X53-D63.9 built 2017-04-01 20:45:26 UTC
{master:0}
vagrant@vqfx-re> show chassis hardware 
Hardware inventory:
Item             Version  Part number  Serial number     Description
Chassis                                32641051726       QFX3500

```
```
{master:0}
vagrant@vqfx-re> show interfaces xe-0/0/* terse 
Interface               Admin Link Proto    Local                 Remote
xe-0/0/0                up    up
xe-0/0/0.0              up    up   inet    
xe-0/0/1                up    up
xe-0/0/1.0              up    up   inet    
xe-0/0/2                up    up
xe-0/0/2.0              up    up   inet    
xe-0/0/3                up    up
xe-0/0/3.0              up    up   inet    
xe-0/0/4                up    up
xe-0/0/4.0              up    up   inet    
xe-0/0/5                up    up
xe-0/0/5.0              up    up   inet    
xe-0/0/6                up    up
xe-0/0/6.0              up    up   inet    
xe-0/0/7                up    up
xe-0/0/7.0              up    up   inet    
xe-0/0/8                up    up
xe-0/0/8.0              up    up   inet    
xe-0/0/9                up    up
xe-0/0/9.0              up    up   inet    
xe-0/0/10               up    up
xe-0/0/10.0             up    up   inet    
xe-0/0/11               up    up
xe-0/0/11.0             up    up   inet    

{master:0}
vagrant@vqfx-re> 

```
```
vagrant destroy -f
==> vqfx: Forcing shutdown of VM...
==> vqfx: Destroying VM and associated drives...
==> vqfx-pfe: Forcing shutdown of VM...
==> vqfx-pfe: Destroying VM and associated drives...
```
