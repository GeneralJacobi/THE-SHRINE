## Project

Submissions to drop box
- Report including
	- Front page
		- Team num
		- All group members
	- Addressing table containing
		- addressing scheme
		- device connection
		- shld complement logical topo
	- rationale on design
		- Highlight considerations that demonstrate your understanding
	- rationale on implementation 
		- if allocated devices fully utilised and still insufficient,
		- implement design while leaving out a level (given that all requierments per level must be met if implemented)
		- then justify why and which level to be left out based on technical consideration
	- DNS operation
		- refering to wireshark captures on DNS server
		- state exact line numbers of relevant network packets corresponding to the correct sequence of DNS ops to demonstrate understanding
	- Reflection on using / not using AI tools
		- may use ChatGPT or other genAI tools if suitable
		- if using, sample screenshots of queries and ans obtained w/ teams comments on helpfulness
		- if not using, comment why not
- logical top diagram (good-quality pdf file) which shows:
	- network devices + given hostname of our choice
	- Connection links labled w/ exact interface / port num of device
	- VLAN numbers
	- Subnet address blocks
	- Subnet masks
	- IP Addresses assigned to network devices (if applicable)
	- (Exclude IP Addresses assigned to user workstations / end devices)
	- 
	- Note
	- Not recommended to use Cisco packet tracer to make diagram
	- img quality bad
	- Recommended Editors
		- Dia Diagram Editor
		- MS Powerpoint
	- Link for Icons
		- https://www.cisco.com/c/en/us/about/brand-center/network-topology-icons.html
	- 
- config files
	- running-conf of network devices
		- one file per device
		- filename = hostname as oer logical topo
		- do not change file format / combine files
	- DNS config
	- Wireshark capture on DNS server
- in person demo w/ fault injections
	- i.e. the profs fucking with us
	- showcase resiliency and redundancy

Details
- physical building
	- 4 levels
		- Lvl 4:
			- Country manager office
				- 1x country manager
				- 1x Dy country manager
				- 2x secretary
			- HR office
				- 1x HR manager
				- 1x HR executive
			- Large meeting room
				- 28 ports
			- 1x network engineer 
		- Lvl 3
			- Solution Dev Dept
				- 1x Solution Manager
				- 2x Senior Software devs
			- Network Dept
				- 1x Network manager
				- 1x senior network engineer
				- 1x network engineer
			- Server Room
			- 1x HR executive
		- Lvl 2
			- Marketing & Sales Dept
				- 1x Sales manager
				- 1x Dy sales manager
				- 8x sales executives
			- 1x HR exceutive
			- 1x Network engineer
		- Lvl 1
			- Customer Service dept
				- 1x Service Manager
				- 1x Dy Service Manager
				- 10 Service Executives
			- 1x HR executive
			- 1x network Engineer
			- 3x Small meeting room
				- 2 ports each 
	- each staff 1 ethernet port w/ internet access
	- assume all ports have internet access???????
- setup & host outward facing web server
	- purpose:
		- offer cashless payment service
		- off promotions to attract customers to sign up
- setup & host authoritative DNS server
	- purpose:
		- allow public to access web server via domain name
- setup & host Caching DNS server
	- purpose
		- to support users in company to access internet w/o relying on public DNS servers like 8.8.8.8
- Company's internal ip address block : 172.16.1.0/24 
- Variable Length Subnet Mask will be used
- No requirement to cate for future expansion
- Coy is subscribed to 2x ISP (See Appendix A)

Limitations / Implementation Considerations
- Maximum Devices
	- 1x Network rack
	- 2x Router
	- 6x switches
- End devices not required, only some required for demo
	- still require all ports to be setup correctly
- WEBPAGE FOR WEB SERVER OPTIONAL
- Required to come up with hostname in format: \[hostname].sitict.net 
	- used for webserver
- 

Enable HSRP HotSwap router protocol to guard against Sudden disconnecttion of router (Some random y3 ICT tell me)

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

switches learn mac addresses belong to which port ONLY when it recieves a frame
multiple mac addresses can belong to one port
when a mac address is not found from the table, the switch will broadcast to all ports to learn


## Topic 3 | Network Layer I : Internet Protocol and IPv4 Addressing

Network layer provides layer and service
- host-to-host (device to device / hop-to-hop)
- source-to-destination (end device to end device)


| Scalability | able to have world-wide-coverage                                                |
| ----------- | ------------------------------------------------------------------------------- |
| Performance | low overhead; as little unnecessasry delay as possible                          |
| Robustness  | able to continue functioning despite isolated faults scatter throughout networs |
| Cost        | as resource efficient as possible in order to be low cost                       |
Desirable Criteria ^^^


IP networks / datagram networks (same same)
router not meant to connect to users, thats why only few ports

Routers can expand using Pluggable Interface Modules (PIM) or Network Interface Module (NIM) 

Routers connect to each other to create a WAN, "gluing" multiple LAN's

Router will de-encapsulate to determine which link to send to

IP network core functions
- Addressing
	- append IP addr as part of network header to ID src and dest
- Routing
	- determin next link to forward IP packet
- Fragmentation and reassembly
	- if ip packet size \> max transmission unit (MTU) of data link layer of next forward link
		- fragment original packet into smaller fragments \< MTU
		- send out
	- net layer of dest responsible for reassembly back to original packet

| IPv4   | IPv6 |
| ------ | ---- |
| 32 bit |      |
IPv4 not compatible with IPv6
but can run concurrently

### IPv4 header
Size: 20-60 byte

VER - 4 bit
- indicate IP version; IPv4 = 0100
HLEN - 4 bit
- indicate length of IPv4 header in multiples of 4
- 20 byte = 5 x 4 = 0101
Service - 8 bit
- support differentiated service (RFC 2474)
Total Length - 16 bit
- max size = 2^16 = 65536 bytes
Identification - 16 bit
Flags - 3 bit
Fragmentation offset - 13 bit
Time to live - 8 bit
- countdown to prevent packet being circulated forever
- value decrement by 1 for each router
- discard packet at 0
Protocol - 8 bit
- indicate type of data carried
	- ICMP 0x01
	- TCP 0x06
	- UDP 0x11
Header checksum - 16 bit
Source IP
Dest IP
Options
- rarely used
- deprecated (RFC 6814)

### whois cmd to find ip address of URL

| Class | type         | change                     | range                        |
| ----- | ------------ | -------------------------- | ---------------------------- |
| A     | Unicast      | 1st bit 0                  | 0.0.0.0 - 127.255.255.255    |
| B     | Uni          | 1st bit 1. 2nd bit 0       | 128.0.0.0 - 191.255.255.255  |
| C     | Uni          | 1st & 2nd bit 1, 3rd bit 0 | 192.0.0.0 - 223.255.255.255  |
| D     | Multicast    | 1,2,3 bits 1, 4 bit 0      | 224.0..0.0 - 239.255.255.255 |
| E     | Experimental | 1,2,3,4 bits 1             | 240.0.0.0 - 255.255.255.255  |
### Classful addressing
format:
- Network ID / Prefix
- Host ID / number

Classless Inter-domain routing (CIDR)
adopted in 1990
introduce network mask 
written as dotted notation 255.255.255.255 or slash notation /27
original A,B,C class become public addr range
private IP for private networks, require Network Address Translation to connect to outer world


| ip                | reserved for                                                                           | e.g.                                                                                        |
| ----------------- | -------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| 0.0.0.0/8         | indicating network / host                                                              | src addr for DHCP discover msg when host has no IP addr but needs one to send out IP packet |
| 127.0.0.0/8       | loopback addr within host                                                              | commonly used to communicate with self                                                      |
| 169.254.0.0/16    | link-local addr for OS to assign to host when fails to obtain IP addr from DHCP server |                                                                                             |
| 255.255.255.25/32 | limited broadcast addr within subnet                                                   |                                                                                             |
Special address blocks

### Fixed Length Subnet Mask (FLSM)

used to improve security
divide host number into subnet number and host number
network prefix + subnet number = extended network prefix

host id of all 0 is network addr to ID network
host id of all 1 is directed broadcast addr for that sub net

note
limited broadcast addr = send broadcast in same subnet
directed broadcast add = send broadcast to given subnet


### Variable Length Subnet Mask (VLSM)

allow 1 org to have subnets of different total host sizes in the same overall ip addr block

e.g. 
given block 116..113.0.0/16
subnet 1 :
- 166.113.0.0/20
- subnet = \[]
	- 0111 0100. 0111 0001 .  \[0000] 0000 . 0000 0000  -   0111 0100. 0111 0001 .  \[0000] 1111 . 1111 1111
Subnet 2:
- 166.113.0.0/21
	- 0111 0100. 0111 0001 . \[1111 1] 000 . 0000 0000 -  0111 0100. 0111 0001 . \[1111 1] 000 . 0000 0000

## Topic 4 | Data Link Layer II / Network Layer II : Network Design I, VLAN and Inter-VLAN Routing

### Hierarchical network model
recommend use 3 tiers of devices
- Core tier
	- high speed backbone connectivity
- Distribution tier
	- provide switching, routing, network access policy functions to access the network
- Access tier
	- provide network access
	- switches on this layer are access switches

enterprise network can span up to multiple buildings
is modular, scalable
if want to expand, can duplicate same hierarchy in all buildings and connect at core tier

e.g.
![[heirarchical network.png]]

### Core
Typically, core switch/ router installed in server room
typically layer 3 switch / router
### Distribution
Typically, distribution switches are installed in server room
interconnects access switches
typically layer 3 switch

This way, smaller LANs do not need core tier 

### Access
Typically access switches installed in equipment room of each level of building
typically layer 2 switch

### Collapsed Core design
![[collapsed_core.png]]
This design directly connects every distribution switches to every other distribution switch

| Advantage                    | Disadvantage                   |
| ---------------------------- | ------------------------------ |
| one less machine to maintain | need to manage the connections |

### Three Tier
![[three-tier.png]]

| Advantage                                         | Disadvantage                  |
| ------------------------------------------------- | ----------------------------- |
| simplify interconnection of distribution switches | Requires core switch / router |
| save cost on cable-laying                         | device costs money lmao       |
### Layer-3/Multilayer switch
![[multilayer design.png]]
basically, reduce device type, still keep fast switching and routing capabilities
typically used for core and distribution
but can be used for access if you have the \$\$\$

### Virtual LAN
On normal layer 2 switch, all devices on same broadcast domain
with VLAN, can split into multiple network with single switch
cost effective

VLAN technically can be avoided by having more switches and routers, but practically, VLAN very useful e.g. to separate departments in 1 building

VLANs are logical
Each has unique ID num
same vlan on diff switch will link tgt if switches connected
generally most direct method is 1 link to support 1 VLAN

### VLAN access mode
port only need to carry frames belonging to 1 vlan as configured
### VLAN trunk mode
switches that port to mode to carry traffic for multiple vlans

### VLAN frame
![[vlan frame.png]]
VLAN frames can be ID-ed by the tag portion of the frame as part of ethernet header
- Type
	- same as Ethernet Header field
	- fixed hex value 0x8100
- Priority & flag
	- for VoIP
	- out of scope
- VLAN ID
	- 12-bit
	- decimal value range 0-4095

VLAN tag is INSERTED into ethernet frame before sending over trunk
Receiving switch removes tag before sending to dest

### Native Vlan
Designed for backwards compatibility
frames belonging to the native VLAN do not get vlan tags inserted

### Dynamic Trunking protocol
DTP is Cisco proprietary protocol
automates trunk negotiation between ports
introduces 2 more modes
- dynamic auto
	- enable DTP
	- wait passively for DTP trunk negotiation to become trunk or access
- dynamic desirable
	- initiates DTP trunk negotiation to become trunk / access

![[DTP layout.png]]
![[dtp table.png]]

table is for SW1 Gi0/1 and SW2 Gi0/2
if Gi0/1 = trunk (not dynamic) and Gi0/2 = access, will conflict and have unexpected network connectivity issues

### Inter VLAN routing

To enable communication between VLANs, use layer 3
#### Legacy inter-VLAN routing
VLAN, 1 switch, 1 router
- limited ports; some need use for router, some need for switch
![[legacy intervlan routing.png]]
#### Router on a stick
save ports, only need 1 trunk
![[router on a stick.png]]
#### Layer 3 switch routing
1 device, better performance
![[layer 3 switch routinng.png]]


## Topic 5 | Data Link Layer III / Network Layer III : Routing Concepts and ARP


## Topic 6 | Data Link Layer IV / Network Layer IV : Network Design II, EtherChannel, STP and HSRP


## Topic 7 | Network Layer V : Static Routing and Dynamic Routing Protocols


## Topic 8 | Network Layer VI : ICMP and NAT


## Topic 9 | Transport Layer : UDP and TCP


## Topic 10 | Application Layer : DHCP and DNS

