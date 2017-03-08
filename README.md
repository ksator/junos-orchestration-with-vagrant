# vagrant-junos

Some links about Vagrant and Junos:  
https://ittechnologist.wordpress.com/2015/09/09/use-vagrant-with-juniper-junos-vms-on-windows/
https://keepingitclassless.net/2015/03/go-go-gadget-networking-lab/  
https://www.dravetech.com/blog/2016/01/08/vagrant-for-network-engineers.html  
https://github.com/Juniper/vqfx10k-vagrant  

There are 4 examples into this repository: 

- **3_vsrx_vagrant_non_provisionning** has vagrant details for a topo with 3 vsrx (ffp) connected together. 

- **3vsrx** has vagrant details for a topo with 3 vsrx (ffp) connected together + ansible provisionner (basic).

- **3vsrx-v2** has vagrant details for a topology with 3 vsrx (ffp) connected together + ansible provisionner. This one is more advanced and interresting: ansible uses a jinja2 template to build bgp details for each device and then push the conf

- **ubuntu_junos** has vagrant details for a vsrx (ffp) and an ubuntu box (14.04). The server is provisonned (pyez, ansible, and some automation content as well). so you can use the ubuntu vagrant box to test some automation content against a junos vagrant box.  so no need to install programs (ansible pyez ...) on your laptop.  

The topology for all examples: https://github.com/ksator/vagrant-junos/blob/master/topology.pdf

Usage:
- Requirements: vagrant and virtual box. junos plugin for vagrant (https://github.com/JNPRAutomate/vagrant-junos)
- clone the repo
```
git clone https://github.com/ksator/vagrant-with-junos.git
```
- move to the local copy
```
cd vagrant-with-junos
```
- move to the directory you want to use, and run the below command:
```
vagrant up
```

Example with the directory 3vsrx-v2: 
```
cd 3vsrx-v2/
vagrant up
vagrant status
ansible-playbook programatic_access/ansible/get_facts.p.yml -i .vagrant/provisioners/ansible/inventory/vagrant_ansible_inventory 
python programatic_access/python/print_facts_vagrant.py
```
```
vagrant ssh vsrx02
```

