## Topic 1 | Introduction to Computer Networks

Internet = interconnection of computer networks / network of networks
internetworks connection uses data packet-forwarding devices (routers)

3 physical types: 
- End devices
	- Desktop, Laptop, Tablet
	- IP phone, Printer
- Intermediary devices
	- Router (Wireless and Wired)
	- LAN switch
	- Multilayer switch
	- Firewall
- Network Media
	- Wireless Media
	- LAN Media
	- WAN Media

Network Topology Diagram
- Is a logical topo diagram
- ![network topo image](<images/network topo image.png>)

Good practice for use of Router and Switch:  
- Net1 Router <--> Net 2 Router;    OK
- Net1 Switch <--> Net 2 Switch;    OK
- Net1 Router <--> Net1 Switch;    OK
- End Device <--> Net1 Router;    OK
- End Device <--> Net1 Switch;    OK
- Net 1 Router <--> Net2 Switch;    Bad Prac

### Layered Network Architecture

#### Why make layers?
break down complex problem into components i.e. Layers

#### OSI and TCP/IP
![OSI_TCP_IP model](<images/OSI_TCP_IP model.png>)

TCP/IP model is used for actual implementation
OSI is used for reference model, discussion and network literature

- Application Layer
- Transport Layer
	- Process-to-process comms for Application Layer
- Network Layer
	- Host-to-host comms
- Data Link Layer
	- node-to-node comms
- Physical Layer
	- TxRx physical signals i.e. communication Media
- ![/TCP_IP_example](images/TCP_IP_example.png)

Because have TCP/IP layers, can develop network applications without too much understanding of the network, just call API

Each layers rules = protocol
A protocol suite / protocol stack = collection of inter-related protocols for different layers

Standards and protocols made with IEEE; Called Request for Comments (RFC)

#### Network Addresses & Encapsulation

With many processes on host and many host + intermediary devices on net, need address to ID them

| Which Layer |           | Need What to ID            |
| ----------- | --------- | -------------------------- |
| Transport   | TCP / UDP | Port number                |
| Network     | IP        | IP Address                 |
| Data Link   | LAN       | Link Address / MAC Address |

Network addresses from part of respective layers' protocol header
AKA encapsulation
![encapsulation](images/encapsulation.png)


#### Cisco Switch Commands

hostname \[New name] - change switch name
enable - enter enable mode from user mode
disable - back to user mode from enable
configure terminal - enter config mode from enable mode
exit - return to config mode
no ip domain lookup - disable DNS
banner motd #  - create banner message for login
sh ip interface brief - show ip interface w/ layer 1 and layer 2 status
sh nterface status - show interface w/ only interface status
sh file systems - show file systems recognized by OS
dir \[drive] - like linux ls, list files on drive
copy \[Input] \[output] - copy input file at filepath \[input] to output file at filepath \[output]
show flash - display files stored in nvram
delete \[filepath] - delete file at \[filepath], can be in flash mem or NVRAM, must define filepath
erase \[file] - erase filysystem / all available files on a file system
reload - reload OS, will ask if you want to save configs, if say  no, can reset configs

note:  
Startup config stores initial config used anytime the switch reload OS - stored in NVRAM
Running config stores currently used config, changes dynamically when use config cmds - stored in RAM

Help cmds

| cmd                 | description                                                                                                                  |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| ?                   | Help for all cmds available in this mode                                                                                     |
| help                | text describing how to use help command                                                                                      |
| command param?      | help describing all first param options for this cmd                                                                         |
| command parm \<Tab> | Tab mid word - CLI spells rest of param or does nothing<br>if does nothing, got >1 param with similar name or dun have param |
| command param1 ?    | CLI list all next param + brief explanation                                                                                  |

| Keyboard cmd         | outcome                                                                                                                                     |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| Up arrow / Ctrl+p    | displays most recently used cmd, pressing again will display next most recent cmd, until history buffer exhausted<br>(P stand for previous) |
| Down arrow / ctrl+n  | Display more recently used cmd, move forward in history buffer<br>(N for next)                                                              |
| left arrow / ctrl+b  | move cursor back w/o deleting cmd<br>(B for back)                                                                                           |
| right arrow / ctrl-f | move cursor forward w/o deleting<br>(F for forward)                                                                                         |
| backspace            | delete char, move cursor back                                                                                                               |
| Ctrl+A               | move  cursor to first char                                                                                                                  |
| Ctrl+E               | move cursor to last char                                                                                                                    |
| Ctrl+R               | redisplay cmd line with all chars                                                                                                           |
| Ctrl+D               | delete single char                                                                                                                          |
| Ctrl+Shift+6         | Interrupt current cmd                                                                                                                       |


| Line Status / layer 1 status | Protocol Status / layer 2 status | Interface Status | Typical root cause                                                                                                                                                                                 |
| ---------------------------- | -------------------------------- | ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Administratively Down        | Down                             | disabled         | interface config-ed with `shutdown` command                                                                                                                                                        |
| Down                         | Down                             | notconnect       | - No cable<br>- Bad cable<br>- wrong cable pinouts<br>- speed mismatch between devices<br>- device on other end is off<br>- device on other end is `shutdown`<br>- device on other end is disabled |
| Up                           | Down                             | notconnect       | interface up/down state not expected on LAN switch physical interfaces                                                                                                                             |
| Down                         | Down (err-disabled)              | err-disabled     | port security disabled the interface                                                                                                                                                               |
| Up                           | Up                               | connected        | interface OK                                                                                                                                                                                       |



- Routing Concepts
- Switching Concepts


## Topic 2 | Data Link Layer I : LAN, Ethernet and Switching Concepts


## Topic 3 | Network Layer I : Internet Protocol and IPv4 Addressing


## Topic 4 | Data Link Layer II / Network Layer II : Network Design I, VLAN and Inter-VLAN Routing


## Topic 5 | Data Link Layer III / Network Layer III : Routing Concepts and ARP


## Topic 6 | Data Link Layer IV / Network Layer IV : Network Design II, EtherChannel, STP and HSRP


## Topic 7 | Network Layer V : Static Routing and Dynamic Routing Protocols


## Topic 8 | Network Layer VI : ICMP and NAT


## Topic 9 | Transport Layer : UDP and TCP


## Topic 10 | Application Layer : DHCP and DNS

