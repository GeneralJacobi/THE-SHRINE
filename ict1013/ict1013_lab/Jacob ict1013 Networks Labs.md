
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