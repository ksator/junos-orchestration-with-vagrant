```
$ vagrant up
```
```
$ vagrant status
```
```
$ vagrant ssh ubuntu
```
```
vagrant@vagrant-ubuntu-trusty-64:~$ python provision/facts.py 
the device vsrx is a FIREFLY-PERIMETER running 12.1X47-D20.7
```
```
vagrant@vagrant-ubuntu-trusty-64:~$ ansible-galaxy list
- Juniper.junos, 1.4.3
```
```
vagrant@vagrant-ubuntu-trusty-64:~$ ls /etc/ansible/roles/Juniper.junos/library/
__init__.py       junos_get_facts       junos_jsnapy    junos_rpc
junos_cli         junos_get_table       junos_ping      junos_shutdown
junos_commit      junos_install_config  junos_pmtud     junos_srx_cluster
junos_get_config  junos_install_os      junos_rollback  junos_zeroize
```

```
vagrant@vagrant-ubuntu-trusty-64:~$ ansible-playbook provision/playbook.yml 

PLAY [Get Facts] ****************************************************************

TASK [Retrieve information from devices running Junos] **************************
ok: [vsrx01]

TASK [Print some facts] *********************************************************
ok: [vsrx01] => {
    "msg": "device vsrx runs version 12.1X47-D20.7"
}

PLAY RECAP **********************************************************************
vsrx01                     : ok=2    changed=0    unreachable=0    failed=0   
```
