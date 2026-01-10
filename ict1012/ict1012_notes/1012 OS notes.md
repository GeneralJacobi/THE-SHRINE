# OwO Linux quick shit

. is current dir  
.. is one dir higher / previous dir  
~ is HOME dir of user  
/ is root dir of whole system  
/home/sysadmin is a ABSOLUTE PATH  
documents/School/art is a RELATIVE PATH (cus dont start with root /)  
cat food.txt > newfile1.txt;    will write output of cat cmd to newfil1.txt, overwriting content
cat food.txt >> newfile1.txt;    will write output of cat cmd to newfil1.txt, appending content
## commands n shit  

ls - list available dirs
pwd - **P**rint current **W**orking **D**ir
cd - **C**hange **D**ir
su - **S**uper **U**ser  
exit - exit su mode
sudo - **S**uper **U**ser **DO**  
chmod - **Ch**ange **mod**e or access (perms)  
chown - **Ch**ange **own**er  
cat - con**cat**enate, show entire contents of file, shld use on smaller file only
head - display first 10 lines of file
tail - display last 5 lines of file
cp - **copy** file
dd - bit level copy
mv - move file
rm - remove file; is permenant, no trash can
grep - search func for file contents
shutdown - prep device for shutdown
date - show date in format \[weekday month day hour:minute:second UTC year]
ifconfig - **I**nter**f**ace **config**; as in network interface
iwconfig - wireless Interface config; as in wireless network interface
ps - see processes, like task manager
apt-get update - update known list of packages and their versions
apt-cache search  - search known list for package name
apt-get install  - install package
apt-get upgrade  - update all packages and dependencies to latest version given by known list
apt-get remove  - uninstall package, leave config files
apt-get purge  - uninstall package and delete config files
passwd - update password
echo - print argument to terminal, can combine with > redirection to write to files

vi - atas, premier editor, pronounced *vee eye* btw {src: netdevgroup Linux Unmatched ccourse}
nano - tiny editor
vim - as in vi improved

vi pros:
- available on all Linux distros
- has CLI and GUI
- core funcs from 1970 with new features added, old fogies also can use
### Options for commands
| opt                          | what                        | deets                                                                             |
| ---------------------------- | --------------------------- | --------------------------------------------------------------------------------- |
| [ls] -l                      | **L**ong                    | lists **full deets** like rwx of files n shit                                     |
| [ls] -r                      | **R**everse                 | used to reverse the listing of shit                                               |
| [ls] -t                      | **T**imestamp               | sort by timestamp                                                                 |
| [ls] -s                      | **S**ize                    | sort by size                                                                      |
| [su] - / -l / --login        | **L**ogin                   | require login to fully configure new shell settings with settings of the new user |
| [head/tail] -n *someInteger* | **n**umber of lines to show |                                                                                   |
| [rm] -r / -R                 | recursive delete            | used to delete dirs, will delete all files and subdirs inside                     |

### Combined nonsense
|opt|what|deets|
|-|-|-|
|-lr / -rl|reverse & long|combine them chiggas|

### ls output breakdown

| file type | perms for OWNER | perms for GROUP | perms for OTHER | Hard links count | User owner |Group owner| File Size (Bytes) | date time | File name | [optional] link destination|
|-|-|-|-|-|-|-|-|-|-|-|
|d|rwx|r-x|r-x|2|root|root|4096|Apr 11  2014|upstart||
|-|rw-|r-|---|1|syslog|adm|1346|Oct  2  22:17|auth.log||
|l|rwx|rwx|rwx|1|root|root| |Nov  6  2012|/etc/grub.conf|-> ../boot/grub/grub.conf|


**Note**:  
Dirs and larger files ay be shown in Kb since Bytes is damn big  
OR  
Sometimes Dirs file size is in Blocks sincce Block size is size of seriese of data stored in file system  

When Dirs have r and not x perms, non-detailed listing  
When have r and x perms, detailed listing  
Dirs must have x to have w perm  
x perm allows user to chang dir if parent dir have x perm as well

### RWX perms  

|d|r|w|x|r|w|x|r|w|x|
|-|-|-|-|-|-|-|-|-|-|
|File type|-|Owner rwx perms|-|-|Group rwx perms|-|-|Others rwx perms|-|

### File type type shit

|Symbol|File type|Description|
|-|-|-|
|d|directory|File that stores other files|
|-|regular file|Inclds: readable files, img files, binary files, compressed files|
|l|symbolic link|Points to another file, like a Shortcut|
|s|socket|Allows for communicaiton between processes|
|p|pipe|Allows for communicaiton between processes|
|b|block|Used to communicate with hardware|
|c|character file|Used to communicate with hardware|

### chmod  deets

chmod \<SET\> \<ACTION\> \<PERMISSIONS\> \[options] FILE 

SET; set for who

|Symbol|Meaning|
|-|-|
|u|User; owner of file|
|g|Group; group that own file|
|o|Others; others that is not owner or in group|
|a|All; lmao|

ACTION; do what to existing perms

|Symbol|Meaning|
|-|-|
|+|Add this perm, if necessary|
|=|Set to this exact set of perms|
|-|Remove this perm, if necessary|

PERMISSIONS; perms

| Symbol | Meaning |
| ------ | ------- |
| r      | read    |
| w      | write   |
| x      | execute |

### Copy files deets

cp \[OPTIONS] SOURCE DESTINATION

SOURCE is a relative / absolute filepath to a file
DEST is a relative / absolute filepath to a dir,

to copy need:
	exec perms for SRC **DIR**  
	read perms for **actual file**
	write & exec perms for DEST **DIR**

can also copy with:

dd [OPTIONS] OPERAND

| operands | Definition                                                                                                                                     |
| -------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| if       | input filepath                                                                                                                                 |
| of       | output filepath                                                                                                                                |
| bs       | block size; default is byte size, use suffix K,M,G,T for kilo, mega, giga, tera,<br>e.g. bs = 1M<br>if omit & omit count, will copy whole file |
| count    | numer of blocks to read from input file<br>if omit & omit bs, will copy whole file                                                             |

### Move file deets

mv \[OPTIONS] SOURCE DESTINATION

SOURCE  is a relative / absolute filepath to a file
DEST is a relative / absolute filepath to a dir **OR** file,

NOTE:
mv needs write exec perms at SRC and DST

### Remove file deets

rm \[OPTIONS] FILE/DIR

require write exec perms in that dir

### GREP
get a grep on things

grep \[OPTIONS] PATTERN \[FILE]

FILE can be file in current dir or filepath

finds the PATTERN in FILE, prints entire lines with said pattern found 
when using REGEX in pattern, wrap in single quote ' ', aka strong quotes

if FILE not give, grep will read standard input in cmd line

OPTIONS:
-E for extended regex
### REGEX

| Basic Regex Character(s) | Meaning                                                                                                                                                                   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `.`                      | Any one single character                                                                                                                                                  |
| `[ ]`                    | Any one specified character OR Any one of the specified chars in range.<br>e.g. [0-9], [oe]<br>[oe] basically is a list of specified chars, so will search for 'o' OR 'e' |
| `[^ ]`                   | Not the one specified character<br>NOTE:<br>is not "does not contain specified chars"<br>is "lines which contain not specified chars"                                     |
| `*`                      | Zero or more of the previous character                                                                                                                                    |
| `^`                      | If first character in the pattern, then pattern must be at beginning of the line to match, otherwise just a literal `^`                                                   |
| `$`                      | If last character in the pattern, then pattern must be at the end of the line to match, otherwise just a literal `$`                                                      |

| Extended Regex Character(s) | Meaning                                                           |
| --------------------------- | ----------------------------------------------------------------- |
| `+`                         | One or more of the previous pattern                               |
| `?`                         | The preceding pattern is optional                                 |
| `{ }`                       | Specify minimum, maximum or exact matches of the previous pattern |
| `\|`                        | Alternation - a logical "or"                                      |
| `( )`                       | Used to create groups                                             |
### SHUTDOWN SHUTDOWN

shutdown arranges for system to be brought down safely
will notify all logged in users that system is shutting down  
if scheduled shutdown like at certain time, will prevent logins for 5 mins before shutdown

shutdown \[OPTIONS] TIME \[MESSAGE]

TIME arguments: 
- now
- hh:mm
- +*minutes*
Message will be broadcast to all users

### ifconfig not ipconfig cus Linux baby

interface as in network interface

ifconfig \[OPTIONS]

generally "eth0" is primary wired connection

"lo" interface is special interface for loopback, which is interface for sending network data to self

### "HE'S RIGHT THERE"; "PING PING PING I CANNOT SEE THE HIM"

ping \[OPTIONS] ADDRESS

-c *integer* ; stops after *integer* attempts

### PS, paiseh, here the processes

ps \[OPTIONS]

-e option will show every proccess running on system

-f option for even more deets

- PID
	- processs ID
- TTY
	- name of terminal where process is running
- Time
	- Total processor tie process used
- CMD
	- Which command started this process
### APT by Bruno Mars & Rosé

dpkg tool is most basic bitch, but hard to use

so many use Advanced Package Tool; apt-get
is front-end program meaning users can see and use

- apt-get update
	- refresh list of available packages
- apt-cache search \[keyword]
	- search for keyword within known list
- apt-get install \[package name]
	- install lmao
- apt-get upgrade
	- updates all installed packages and dependencies to latest version in known list. 
	- use apt-get update to update know list and versions
- apt-get remove \[package name]
	- uninstall package
	- leaves config files
- apt-get purge \[package name]
	- PURGE THE HERETIC
	- BURN THEIR NAMES FROM THE ENTIRE SYSTEM
	- ERASE EVEN THEIR CONFIG FILES FROM THE RECORDS

### Passwd? more like pass away

passwd \[OPTIONS] \[USER]

| Options                                  |                                 |
| ---------------------------------------- | ------------------------------- |
| -s                                       | show status                     |
| {no option, no user}                     | reset password for current user |
| {as su, no option, have normal username} | reset password for given user   |

Example output:
sysadmin P 12/20/2017 0 99999 7 -1

| Output Field    | Example      | Meaning                                                                                                     |
| --------------- | ------------ | ----------------------------------------------------------------------------------------------------------- |
| User Name       | `sysadmin`   | The name of the user.                                                                                       |
| Password Status | `P`          | `P` indicates a usable password.<br><br>`L` indicates a locked password.<br><br>`NP` indicates no password. |
| Change Date     | `03/01/2015` | The date when the password was last changed.                                                                |
| Minimum         | `0`          | The minimum number of days that must pass before the current password can be changed by the user.           |
| Maximum         | `99999`      | The maximum number of days remaining for the password to expire.                                            |
| Warn            | `7`          | The number of days prior to password expiry that the user is warned.                                        |
| Inactive        | `-1`         | The number of days after password expiry that the user account remains active.                              |
### omg Vi, like from Arcane 2021

modes:
- Command
	- type commands like move doc, format text
	- return to command mode any time with esc key
	- need return to command mode to use cursor lmao
- Insert
- ex

#### Cursor movement commands:  

format: \[count] motion

| Motion     | Result              | vi alternatives |
| ---------- | ------------------- | --------------- |
| `h`        | Left one character  | ←               |
| `j`        | Down one line       | ↓               |
| `k`        | Up one line         | ↑               |
| `l`        | Right one character | →               |
| `w`        | One word forward    |                 |
| `b`        | One word back       |                 |
| `^`        | Beginning of line   |                 |
| `$`        | End of the line     |                 |
| \[count] G | go to \[count] line |                 |
| gg / 1G    | go to first line    |                 |
| G          | go to last line     |                 |
Note; ↑→↓↓↓

#### Command mode Actions
formats:
action \[count] motion
\[count] action motion

| Standard | Vi         | Meaning |
| -------- | ---------- | ------- |
| cut      | `d`        | delete  |
| copy     | `y`        | yank    |
| paste    | `P` \| `p` | put     |
|          | c          | Change  |

Deleting saves "deleted" content to buffer, like clipboard

| Delete Action | Result                             |
| ------------- | ---------------------------------- |
| `dd`          | Delete current line                |
| `3dd`         | Delete the next three lines        |
| `dw`          | Delete the current word            |
| `d3w`         | Delete the next three words        |
| `d4h`         | Delete four characters to the left |

Change like delete, text remove, save to buffer BUT
Change to insert mode and allow immediate changes to text

| Change Action | Result                             |
| ------------- | ---------------------------------- |
| `cc`          | Change current line                |
| `cw`          | Change current word                |
| `c3w`         | Change the next three words        |
| `c5h`         | Change five characters to the left |

Yank place content into buffer without clearing buffer

| YankAction | Result                      |
| ---------- | --------------------------- |
| `yy`       | Yank current line           |
| `3yy`      | Yank the next three lines   |
| `yw`       | Yank the current word       |
| `y$`       | Yank to the end of the line |

Put places text from buffer before or after cursor.
Does not use motions, only these 2 options

|Action|Result|
|---|---|
|`p`|Put (paste) after cursor|
|`P`|Put before cursor|
#### Searching

/ char will start search forward from Cursor position
? char will start search bbackward from Cursor position
e.g. /red; then hit enter
n - next match
shift + N - previous match

Note; will wrap to top once hit bottom and vice versa

#### Insert mode
Add text to doc
How to enter insert mode have a few ways, will change where you start editing from

| Input | Purpose                                                 |
| ----- | ------------------------------------------------------- |
| `a`   | Enter insert mode **right after** the cursor            |
| `A`   | Enter insert mode at the **end of the line**            |
| `i`   | Enter insert mode **right before** the cursor           |
| `I`   | Enter insert mode at the **beginning of the line**      |
| `o`   | Enter insert mode on a **blank line after the cursor**  |
| `O`   | Enter insert mode on a **blank line before the cursor** |

#### Ex Mode
used to be its own thing, bit Vi was better

use ':' in command mode and following options to get into ex mode
!  char attempts to force the operation

| Input            | Purpose                                         |
| ---------------- | ----------------------------------------------- |
| `:w`             | Write the current file to the filesystem        |
| `:w filename`    | Save a copy of the current file as `filename`   |
| `:w!`            | Force writing to the current file               |
| `:1`             | Go to line number 1 or whatever number is given |
| `:e filename`    | Open `filename`                                 |
| `:q`             | Quit if no changes made to file                 |
| `:q!`            | Quit without saving changes to file             |
| `:ZZ`            | same as `:wq`                                   |
| `:[line number]` | same as \[line number]G in command mode         |
## GDB things

`gdb-multiarch -x .gdbinit`

“.gdbinit” usually contains the target remote localhost:26000 symbol-file kernel/kernel.

`b [pattern]` - create breakpoint at next instance of pattern, if use '\*0x80002845' can even do break point by program counter  

`c` - continue
`q` - quit
`layout [option]` - can layout src, which shows c code, or layout asm, which shows machine code

`backtrace` - shows backtrace of where breakpoint was

`p [options]` - print
- possible options
	- `/x` is privilaged status
	- `*p` is process proc struct
	- `$sstatus` is special status register
	- `p->name` is print process name

`file [filepath]` - let gdb read symbols from filepath



# Chap 1: Intro to OS and xv6

Libraries and APIs are not OS-es  
GUIs are not OS-es  

OS definition:  
Program that acts as an intermediary between user and hardware
However no universally accepted definition  
"Everything the vendor ships when you order an OS" is good approximation but varies wildly  
"The one program running at all times" is the kernel  
Everything else is either a system program (which ships with OS) or application program

OS goals:  
- Provide users with interface to hardware
  - Provide friendly environment (dependant on type of user)
  - execute user applications  
  - make solving user problems easier
- Resource management
  - use hardware in effecient manner
  - cannot leave critcal pplication to run later,
  - come form of heirachy of running programs

Computer system components:  
- Hardware
  - basic computing resources
    - CPU
    - Mem
    - I/O
- OS
  - Control & Coordinate use of hardware among various applications and user
    - Word processor
    - Compiler
    - Web browser
    - database systems
    - video games
- Users
  - People
  - Machines
  - Oher computers

Applications cannot directly manipulate many of the hardware components  
Ask OS to do for them  
You dont want applicaitons poking around your hardware  
dont want users to code  certain actions for hardware that may break it, e.g. moving harddrive arm beyond operating range
is for security  

Various apps/hardware  
Many versions of content or extensions  
Keeps changing  
OS can bridge/manage these updated systems on the users behalf

Hardware abstraction for applications:  
- CPU
- Memory
- I/O

Means OS is a resource allocator:  
- Manages resource
  - CPU
  - Memory
  - I/O
- Decides between conflicting requests for effecient and fair resource use
  - e.g. two processes need to use CPU, how to assign

OS manages user access control, allowing certain actions to be executed by superusers only

OS provides effecient synchronisation for processes

OS provides communication to applications
- Applications can use network for inter-process communication (loop-back devices)
- OS provide local communication
  - Pipes
  - Shared Mem
  - Passing messages


even with all these capabilities it may or may not be enough  

for specialied OS, e.g. rocket launch systems where users know what they are doing, or simple washing machine with less interactino with users,  
May be enough to do just these thigns  

For devices like Iphone, samsung, it must be more flexible and provide powerful APIs. So other users can develop apps and programms for the OS  
e.g. Google developed android focusing on developers, making well documented API that ease implementation of applications

## How is OS organised  

One or more CPU, device controller  connected through common bus, providing shared access to shared mem  

Concurrent executino of CPUs and devices competing tfor memory cycles  

I/O devices and CPU can execute concurrently  
each device controller has local buffer, which CPU uses to move main mem to/from buffers  
CPU does not need to handle individual fragments of data for each device  
I/O is from device to controller buffer  
Device controller informs CPU of completion of op with interrupts  
Device driver provide OS with uniform interface to access device

## Approaches to OS design

- Layered approach
  - start at hardware layer, build on neccessary layers without subcomponents that interact on same layer.
  - one layer is one big essential piece
  - each layer built on top of the last
  - bottom layer 0 is hardware
  - highest layer n is user interface
  - each layer designed to use functions and services of previous layers
  - used in linux, windows, macOS
- Modular approach
  - start at hardware and add on functionality in layers.
  - May contain components that live on same layer that interact with each other
  - uses object oriented approach
  - each core component is seperate
  - each talks to others over known interfaces
  - each loadable as needed within kernel
- Micro-Kernel
  - Split into kernel Space and user spacce
  - Apps and services run in user space
  - essential abstractions run in kernel space
- Monolithic Kernel
  - clear seperation between user and kernel
  - all aspeccts of kernel share same memory space
  - user mode apps do not have access to all instructions
  - certain cpu instructions are limited to kernel mode only
  - many parts are integrated into the kernel
  - like Virtual mem, drivers, User interffacce, mem management, file system
  - if any part is compromised, it exists in the kernal space and may grant access to other parts of the kernel

## Micro Kernel System Structure

Moves as many fucntions as possible into user space
e.g.  
HarmonyOS NEXT (Hwawei) is micro kernel extended with indipendent services  
Communication between user modules uses message passing  


| Benefits                                                    | Detriment                                                             |
| ----------------------------------------------------------- | --------------------------------------------------------------------- |
| Easier to extend a microkernel                              | bigger performance overhead due to user space to kernel communication |
| Easier to port the operating system to new<br>architectures |                                                                       |
| More reliable (less code is running in )                    |                                                                       |
| More secure                                                 |                                                                       |

## Monolithic System Structure

Consists of 2 seprable parts
- System Programs
- Kernel
  - Kernel is everything below system-call interface but above physical hardware
  - Provide large number of functions for 1 level:
    - File system
    - CPU scheduling
    - memory management
    - other OS functions

## Hybrid System

Combine Micro Kernel with extended functionality to enhance performance

## Overall comparison


|               | Layered                                                                 | Modular                                                    | Micro Kernel                                                                | Monolithic Kernel                                           |
| ------------- | ----------------------------------------------------------------------- | ---------------------------------------------------------- | --------------------------------------------------------------------------- | ----------------------------------------------------------- |
| **Structure** | **Heirarchical Layers**; each layer only intereact with one layer below | **independant modules**; dynamically loaded and unloaded   | **Minimal kernel w/ only essential services**; other services in user space | **All Core services in Kernel Space**                       |
| Performance   | **Moderate** <br>(overheads from layering slows execution)              | **High** <br>(Modules run effeciently)                     | **Low** <br>(frequent inter process comms adds overhead)                    | **High** <br>(direcct function calls make quick execcution) |
| Reliability   | **Moderate** <br>(clear seperation, easy debug, limit effeciency)       | **High** <br>(Fault modules isolate easy, replace easy)    | **High** <br>(fault in user space dont affect kernel)                       | **Low** <br>(single fault can crash whole system)           |
| Flexibility   | **High** <br>(easy to modify & replace)                                 | **Very high**<br>(support extensibility and customisation) | **Very high** <br>(modular makes it easier to add services)                 | **Low** <br>(tightly coupled, make changes difficult)       |

## xv6

simple modern version of Unix version 6  
Written in ANSI C  
for x86 and RISC-V multi-processor systems  
10 000 lines of ccoe  
made in MIT 2006  
Provides:  
- processes
- simple scheduler
- virtual memory
- heirarchical file system
- file descriptors
- shell

Deliberatly omit:  
- threads
- memory-mapped files
- advance features

Limited:  
- drivers
- system calls

Simplified hardware assumptions  
realistic Unix-like design  
Open source  
Multi processor support  
good for soid foundation to understand ore complex systems like Linux or BSD  

Is monoithic kernel  
Single address space contains all OS services:  
- Processes
- memory
- file system
- I/O

User vs Kernel Seperation:  

User mode:  
- Apps execute with limited access

Kernel Mode:  
- Privilaged acccess via traps/system calls for procetion

Mode Switch:
- Traps save context
- Dispatch handlers
- return

Key sub-systems / services:  
- kernel init
  - init hardware, mem and process structures
- System calls
  - dispatch user request and kernel functions
- Process Management
  - maintain process table for each process
  - implement scheduler for CPU time alloc
  - handle context switching between processes
- Memory management
  - set up virtual mem
  - provide isolation between proccess
  - manage allocation and freeing of physical mem
- File system
  - implement UNIX-like file system with inodes and directories  
  - provide file desccriptions
  - support pipes and device files
- device driver
  - provide I/O support for hardware

is organised into distinct directories & source files that correspond to major subsystems  
- kernel/:
  - contains all core xv6 kernel source files:
    - main.c: kernel init & boot process
    - syscall.c: system call implementation and dispatch
    - trap.c: trap and interrupt handling
    - proc.c: process management (creation, scheduling, context switchin)
    - vm.c: cirtual memory management and page tables  
    - fs.c, file.c, inode.c: filesystem implementation
- user/: user-level apps, including shells (sh.c), commands (ls.c, cat.c) and utilities
- makefile: Buidl instructions to compile kernel and user programs and run xv6 on QEMU
- README and other docs: Documentation and build/run instructions

xv6 vs Linux  

|                  | xv6                            | Linux                       |
| ---------------- | ------------------------------ | --------------------------- |
| Purpose          | simple unix-like, for teaching | Product grade, feature rich |
| Code Complexity  | ~10 000 lines                  | ~30 000 000 lines           |
| hardware support | x86 and RISC-V on QEMU only    | many diffeerent hardware    |
| Features         | basic unix                     | advanced features n shit    |
| system calls     | 21 basic syscalls              | 300+ syscalls               |
| organisation     | Single file per subsystem      | Modular subsystems          |

## RISC-V

- Open-Source instruction set architecture
- developed in 2010 by University of California, Berkeley
- Based on Reduced instruction Set Computing (RISC) principles
- keep simple and efffecient
- 4 corre
- 32 register  control register
- ALU and Mem Management Unit
- Timer and interrupt logic
- Bus interface
- 128 MB RAM
- UART for console device I/O
- Disk-like storage
- ethernet

# Chap 2 System Calls & Traps

# Chap 3 Processes & Threads

# Chap 4 CPU Scheduling  

# Chap 5 Synchronisation  

# Chap 6 File Systems  

# Chap 7 Mem Management  

# Chap 8 Virtual Memmory