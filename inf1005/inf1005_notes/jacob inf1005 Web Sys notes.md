All work done in this mod is on lvl 5 of tcp/ip, app layer

# Chap 1

Domain Name Service (DNS)  
Translate hostname to and from IP address  
english hostname easier to remember, re-locateable, same site multiple hosts  
DNS Resolver performs 2 funcs: gethostbyname(), gethostbyaddr()

Benefits of internet  
- Fully decentralised, highly robust,
  - part of non-functioning network does not affect others  
- Information is at edge node, routing is simple, 
  - means scalable to heavy traffic  
- Low cost
  - affodable to get connected
  - pay internet service provider to connect, not other costs to end user
  - may pay for new services but not for actual internet
  - VPN allow companies to use internet to create "private" networks
- many established services
  - e.g. Wikipedia
  - e-commerce
  - services

## History of World Wide Web

1989:  
Tim Berners Lee  
English, Study in swiwstzerland
CERN
Internet active but not by everyday user  
used by companies, goverments, militaries

issues then:  
- Doc format different based on OS used  
- how to transfer document in a safe manner  
- finding / looking up things

he creates Hyper Text Markup Language 
- uses ASCII, all computers can read this text
- allows insertion of links to other documents
also creates Hyper Text Transfer Protocol
- dont need FTP and account on destination to tansfer anymore
- as long as both sides have client for http, can transfer html
also creates Universal Reasource Identifier / Universal Resource Link
- solves issue on how to find thigns

## Web Browser History / The Browser wars

1993:  
Marc Anderson + Uni students  
WWW has potential, not intuitive to use, need open terminal, type in commands, recieve only text  
making GUI web browser
"NCSA MOSAIC", closed source but free to download and use

Jim Clark, Silicon Valley, Big money  
Marc try convince Jim make better browser
jim laze, want make game
Marc convince jim  
Make netscape Communication Corp together  
Hire the students who made MOSAIC

1994:  
change name, Netscape Navigator  
marc wants mozilla, mosaic killer  
build new browser, 30 million users in a year  
treid to do free for non commercial, 30usd for commercial  
didnt last, competition  
switched to selling servers or email services  

1995:  
Netscape IPO
microsoft makes IE, and win95 lmao  
cucks Netsccape  
IE was better performance  
Netscape cross platform yes, but also means cannot enhance netscape for only one platform, must enhance for all


## Components of WWW

Uniform Resource Identifier / Link (URI URL)
Hypertext Markup Language (HTML)
Hypertext Transfer protocol (HTTP)

## Web Browser


## Internet VS Web

internet is all forms of digital communication between commputers
Web is just 1 protocol that uses the internet

### Circuit Switched Networks
- telephone calls physically connected caller and receiver on a switchboard
- ineffecient use of bandwidth
- hard to scale

### Packet switched networks
- Came later
- does not need continuous connection
- types:
	- 1960s ARPANET  
	- 1974 X.25  
	- 1979 USENET  
	- 1981 TCP/IP was introduced to unify disparate network
	
## Web Apps VS Desktop Apps

- Advantages of Web Apps
	- can be accessed from any internet-enabled computer
	- different OS / browser ok
	- easier to roll out program updates since software serverside rather than client side
	- Centralised storage, fewer security problem
- Disadvantage
	- Need active internet connections
	- Security concern about sensitive data trasmitted over internet
	- Concern on storage / use / Licensing of uploaded data
	- websites do not have identical appearance across all browsers
	- Restrictions on software from being installed and hardware being accessed
	- additional plugins may interfere with javascript, cookies or advertisments
## HTML 5

Why use proper semantic elements?
ans: acessability, web scraping

Semantic tags give meaning to the machine maybe the dev a bit
E.g.
putting \<figure> and \<figcaption> tags makes it easier for accessibility machines to understand whats important

## What is HTML

Language made to standardize document styles and data format to allow adoption of accompanying HTTP and URI/URL

## Goal of HTML

1. Improve Native Web
	- HTML 5 added syntactic features to web that previously needed plugins to work
		- e.g. \<audio>, \<video> and \<canvas> elements
	- Enables richer desktop-like experience
2. Do more with less code
	- simplify common design patterns (and more) by creating standardized ways to do in HTML alone no plugin
		- e.g.
		- placeholder text in forms
		- autofocus on particular input element
		- client-side validation
		- date time pickers
3. Realize Semantic Web
	- Semantic Web refers to content that is readable and meaningful to both humans and machines


To make it easier to find and access documents on the internet

## Basic HTML syntax and document Structure

## Elements & attributes
element is part of web page, 
attributes are specific settings like the src in the img tag

### Nesting Elements
allows for things like clickable links

## Character Entities
allows display of special chars that could be interpreted as code
e.g. <> is html code but to display you need @lt; and @gt; to print
all char entities must start with @ and end with ;
## Images and links
Named anchors starts with a \# in the \<a href> tag
Scrolls down to element with given ID in same page

figure does not just have to be image, can be graphs and shit
alt tag in \<img> element is what is displayed when browser setting does not load images
title tag in \<img> element is what is displayed when mouse hover over image

## Semantic Markup

### What

### Why


## Header & Footer
Is semantic element for machines to understand and maybe skip
Also for styling


## Navigation


## Section & Articles


## Shld we still use div?
Can still use for styling


# Chap2 CSS & Bootstrap

Responsiveness != Responsive Design

Responsive Design is to adjust the website to cater to different browsers with things like bootstrap

## CSS : Cascading Style Sheets

CSS is a styling language
HTML is a markup / positioning language (position elements on page)
### CSS Rule Sets
Always consists of the below 3 things
#### Selector
- Selects the type of tag or ID or class or element name
	- e.g.
	- section {}
	- figcaption {}
	- \#dogs {} ; ID
	- \. cats {} ; class
- Class selector will attempt to apply the given property to any tags with the given class
	- e.g.
	- \<p> and \<h1> can both have same class and therefore same color
	- \<img> may have same class as \<p> \<h1> but maynot have the color property
- May have sub tags
	- e.g.
	- section h2{}
	- h2 is the sub selector
	- this means all h2 tags within the section tags
#### Property
- Changes the property/characteristic of the selected element
	- e.g.
	- figcaption {color: "darkslategray;}
- 1 ruleset can have as many properties as you want

#### Value
- Value of property
- datatype is dictated by the property
	- e.g. color property can take string or hex (rgb color)

### Including CSS in HTML
order of application
external > internal > inline

this means
- inline settings will override all other settings
- internal will override external

Creating an external stylesheet allows you to write once and apply many times so all your pages look the same

internal is used when one specific page needs additional styles

Generally avoid inline as have to scroll to specific element to edit

#### External
- Write in .css file and include with \<link> tag
- e.g. 
	- \<link rel="stylesheet" href="css/main..css">

#### Internal (aka Embedded)
- Writing styles directly into html file with \<style> tag

#### Inline
- Writing styles into individual tags
	- e.g.
	- \<h1 style="color: green">
- inline overrides both external and internal

## BootStrap

### Intro to framework and Boootstrap

- Is a CSS framework lol
- Open source n free
- is basically a large amount of classes that you can apply to all your elements

### Responsive Design
- as you resize the website, the website should reformat and still look nice
- that is responsive design

### Including Bootstrap in HTML

### Bootstrap Grid System

### Jumbotron
- Title replacement
- Looks like the Giant TV screens in football stadiums i.e. THE jumbotron
- probably only used on main page

### Navigation Menu
- should be replicated on all pages

### Misc. Bootstrap Features