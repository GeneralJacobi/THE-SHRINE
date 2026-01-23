
Lab Laptop  
Username: sitstudent  
pw: Student@sit

Steps to power on
1. 2x Red button at back, on both
2. Wait for boot
3. for rack equipment, when asked if want to enter initial configuration dailog; do not enter
4. Use 'Student@s1t' as password for rack equipment
5. When asked to save config, choose option\[0] to go to IDS without saving
6. Once "switch #" appear, ready to go
Dont change the password for the cable locker

2 Firewall
1 server
2 Router
2 Distribution Switch / Layer 3 Switch
4 Layer 2 Switch
## Lab1

### 2.6
Application:  Hypertext Transfer Protocol
Transport:  Transmission Control Protocol, Src Port: 58774, Dst Port: 80, Seq: 1, Ack: 1, Len: 478
Network:  
Data Link:



## Lab2

2.11
What version of Cisco IOS - 17.12.04
What system image filename - Cisco ISO EX
What problem encountered when 'show running-config' - cannot run
Can you use 'enable' can you  'show running-config' - can run

user mode -- enable --> enable mode -- Configure teminal --> config mode
config mode -- end/ctrl+z --> enable mode -- disable --> user mode

config mode -- interface *type/number* --> Interface mode
config mode -- vlan *x* --> vlan mode
config mode -- line console 0 --> Console mode
config mode -- line vty 0 15 --> VTY line mode

Switch 1

| interface | Line status | Protocol status | interface status |
| --------- | ----------- | --------------- | ---------------- |
| G1/0/6    | up          | up              | connected        |
| G1/0/24   | up          | up              | connected        |


Switch 2

| interface | Line status | Protocol status | interface status |
| --------- | ----------- | --------------- | ---------------- |
| G1/0/18   | up          | up              | connected        |
| G1/0/24   | up          | up              | connected        |

OUI portion of MAC address of PC A NIC (first 3 set f hex) - 74-D4-DD
OUI portion of MAC address of PC A NIC (last 3 set f hex) - 81-5C-4B
Vendor - _Quanta Computer Inc_.

OUI portion of MAC address of PC B NIC (first 3 set f hex) - 74-D4-DD
OUI portion of MAC address of PC B NIC (last 3 set f hex) - 81-5C-4A
Vendor - _Quanta Computer Inc_.


base Ethernet MAC address of your switch SW1 - b0:8d:57:73:d6:80

MAC address for port G1/0/6 on your switch SW1 - b0:8d:57:73:d6:86

MAC address for port G1/0/24 on your switch SW1 - b0:8d:57:73:d6:98

base Ethernet MAC address of your switch SW2 - b0:8d:57:73:b6:00

MAC address for port G1/0/18 on your switch SW2 - b0:8d:57:73:b6:12

MAC address for port G1/0/24 on your switch SW2 - b0:8d:57:73:b6:18

deduction: each port address is \[add port number to base ethernet address]

What is the MAC address ffff.ffff.ffff used for?  
What type of MAC address does 0180.c200.0000 belong to? What is it used for?
local mac addresses
belong to switch
are multicast addresses for services
this specific one is Spanning Tree Protocol

List down the dynamically learned MAC addresses and the corresponding ports on SW1.  
- 74d4.dd81.5c4b
- b08d.5773.b618
list down the dynamically learned MAC addresses and corresponding ports on SW2.  


3.7 Are you able to explain how the switches dynamically learned these MAC addresses?
enter the command clear mac address-table dynamic. 

When recieve packers from port, dynamically learn and record down

Immediately, enter the show mac address-table dynamic command again.  
What do you observe?

now info updated after new packets

Highlighted bytes corresponding to Ethernet II:
74 d4 dd 81 5c 4a 74 d4 dd 81 5c 4b 08 00

Highlighted bytes corresponding to Destination:  
74 d4 dd 81 5c 4a

Highlighted bytes corresponding to Source:
74 d4 dd 81 5c 4b

Highlighted bytes corresponding to Type:
08 00

represents that is ping request

need for type field to determine protocol

## Lab 3

Router commands
- show
	- version - display os version
	- running-config - display current running config
	- ip interface brief
- enable - enable mode
- hostname - change hostname
- no ip domain lookup - disable dns


## Lab 4

in enable mode
- show interfaces
	- trunk - show trunking interfaces and allowed vlans
in config mode
- vlan \[ID num] - create new vlan with id \[ID num]
- name \[string] - name current vlan with \[string]; if last cmd was vlan 10, next name will name vlan 10
- no vlan \[ID num] - removes vlan \[ID num] from vlan interface
in interface config for specific port (e.g. g1/0/06 or range g1/0/11-24)
- switchport 
	- mode
		- access - statically disables trunking on the port(s), default mode is dynamic trunk
			- access vlan 10 - changes port(s) to only allow access to vlan 10; using no before this changes access vlan to default vlan (does not require vlan num)
		- trunk - statically changes mode to trunk; default trunking mode is  auto
			- trunk allow vlan - allows trunk to use vlan
- no shut - changes interface status to up
- switchport mode dynamic negotiate - switches port mode to dynamic trunk negotiate (default is auto)
- switchport trunk - allows vlan access to trunk but  like how tho????

note 
- before removing vlan from database, recommended reassign all ports in that vlan
- dynamic trunking protocol allows port to negotiate trunk mode, but it waits for others to initiate



can pc a ping pc b - yes
can pc a ping pc c - no
can pc b ping pc c - no

if no why
because default gateway is 192.168.10.1, so cannnot ping 192.168.20.3
diff subbnet

what is default vlan
vlan 1

what ports assigned to default vlan
g1/0/1-24   g1/1/1-4

can pc a ping pc b after assigning pc a to vlan 10
no lol
diff vlan not allowed to send frames across

which vlan is port 24 associated with after changing vlan
vlan 20 faculty

what is default name of lan 30? - vlan0030

after 'no switchport access vlan' to g1/0/24, which vlan is g1/0/24 assigned to? - defualt vlan

if delete vlan while port associated with it, port will not be associated with ANY vlan

after trunk enable

pc a to pc b - yes
pc a to pc c - no
pc b to pc c - no

Why might you want to manually configure an interface to trunk mode instead of using DTP?
not all equipment uses dtp, dtp is cisco only

Reflection  
1. What is needed to allow hosts on VLAN 10 to communicate to hosts on VLAN 20?  
	- trunk port
2. What are some primary benefits that an organization can receive through effective use of VLANs?
	- sectioning off different groups to improve network performance

legacy routing
a. On R1, issue the show ip route command. What routes are listed on R1?  
192.168.10.0 - 192.168.10.1
192.168.20.0 - 192.168.20.1

b. On both S1 and S2, issue the show interface trunk command. Are both S1  
G1/0/1 and S2 G1/0/1 ports set to trunk?
yes

c. Issue a show vlan brief command on both S1 and S2. Verify that VLANs 10  
and 20 are active and that the proper ports on the switches are in the correct  
VLANs. Why is S1 G1/0/1 and S2 G1/0/1 not listed in any of the active  
VLANs?  
they are trunks not part of vlan

d. Ping from PC-A in VLAN 10 to PC-C in VLAN 20. If inter-VLAN routing is setup  
correctly, the pings between the 192.168.10.0 network and the 192.168.20.0  
should be successful.  
Note: It may be necessary to disable the PC firewall to ping between PCs.  
yes

e. Verify connectivity between devices. You should be able to ping between all  
devices. Troubleshoot if you are not successful.
ok done

Reflection  
- What is an advantage of using legacy inter-VLAN routing?
	- ease of configuration.

router on stick
a. Enter the command to view the routing table in R1. What networks are  
listed?  
192.168.10.0/24 - 192.168.10.1/32
192.168.20.0/24 - 192.168.20.1/32

b. From PC-A, is it possible to ping the default gateway for VLAN 10?  
yes

c. From PC-A, is it possible to ping PC-C?
yes

What is the advantage of trunk-based or router-on-a-stick inter-VLAN routing?
less machines to maintain, all configs on one device


a. Enter show ip route command to view the routing table in S3. What networks  
are listed?  
192.168.10.0/24 - 192.168.10.1/32
192.168.20.0/24 - 192.168.20.1/32

b. From PC-A, is it possible to ping the default gateway for VLAN 10?  
yes

c. From PC-A, is it possible to ping PC-C?
yes