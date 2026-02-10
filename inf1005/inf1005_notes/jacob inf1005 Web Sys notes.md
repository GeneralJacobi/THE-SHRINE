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

| Advantage                                                                            | Disadvantage                                                               |
| ------------------------------------------------------------------------------------ | -------------------------------------------------------------------------- |
| can be accessed from any internet-enabled computer                                   | Need active internet connections                                           |
| different OS / browser ok                                                            | Security concern about sensitive data transmitted over internet            |
| easier to roll out program updates since software serverside rather than client side | Concern on storage / use / Licensing of uploaded data                      |
| Centralised storage, fewer security problem                                          | websites do not have identical appearance across all browsers              |
|                                                                                      | Restrictions on software from being installed and hardware being accessed  |
|                                                                                      | additional plugins may interfere with javascript, cookies or advertisments |

## HTML 5

Why use proper semantic elements?
ans: acessability, web scraping

Semantic tags give meaning to the machine maybe the dev a bit
E.g.
putting \<figure> and \<figcaption> tags makes it easier for accessibility machines to understand whats important

## What is HTML

Language made to standardize document styles and data format to allow adoption of accompanying HTTP and URI/URL

## Goal of HTML

| Improve Native Web                                                                                                                  | Do more with less code                                                                                                                                                                                                                                    | Realize Semantic Web                                                                       |
| ----------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| HTML 5 added syntactic features to web that previously needed plugins to work<br><br>e.g. \<audio>, \<video> and \<canvas> elements | simplify common design patterns (and more) by creating standardized ways to do in HTML alone no plugin<br><br>- e.g.<br>		- placeholder text in forms<br>		- autofocus on particular input element<br>		- client-side validation<br>		- date time pickers | Semantic Web refers to content that is readable and meaningful to both humans and machines |
| Enables richer desktop-like experience                                                                                              |                                                                                                                                                                                                                                                           |                                                                                            |

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


# Chap 2 CSS & Bootstrap

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
	- \<img> may have same class as \<p> \<h1> but may not have the color property
- ID and Class allow application to multiple types of elements
	- Class meant to apply to multiple elements (may be of varying types) regardless of position in document tree
	- ID meant to apply to single element regardless of position in docuent tree
	- both can be used across pages
- May have sub tags
	- e.g.
	- section h2{}
	- h2 is the sub selector
	- this means all h2 tags within the section tags
- Attribute Selector
	- select HTML elements by presence of element attribute / value of attribute
	- e.g. style hyperlinks
	- can combine with ID and class selector
	- uses square brackets
- Pseudo element selector

|             | Matcher                                                                                                          | Example                                                                                                                          |
| ----------- | ---------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| []          | a Specific attribute                                                                                             | [title] Matches any element with a tiltle attribute                                                                              |
| [=]         | a specific attribute with a specific value                                                                       | a[title="posts from this country"]  <br>Matches any \<a> element whose title attribute is exactly “posts from  <br>this country” |
| [~=]        | A specific attribute whose value  <br>matches at least one of the words in a  <br>space-delimited list of words. | \[title~="Countries"]  <br>Matches any title attribute that contains the word “Countries“                                        |
| \[^=]  <br> | A specific attribute whose value begins  <br>with a specified value.  <br>a\[href^="mailto"]                     | Matches any \<a> element whose href attribute begins with “mailto“                                                               |
| \[*=]       | A specific attribute whose value  <br>contains a substring.                                                      | img\[src*="flag"]<br>Matches any \<img> element whose src attribute contains somewhere  <br>within it the text “flag             |
| \[$=]       | A specific attribute whose value ends  <br>with a specified value                                                | a\[href$=".pdf"]  <br>Matches any <a> element whose href attribute ends with the text “.pdf“                                     |

#### Property
- Changes the property/characteristic of the selected element
	- e.g.
	- figcaption {color: "darkslategray;}
- 1 ruleset can have as many properties as you want

#### Value
- Value of property
- datatype is dictated by the property
	- e.g. color property can take string or hex (rgb color)
- special tag !important will FORCE the value regardless of position in the cascade (e.g. in external but bootstrap has own value for this property)
	- be careful when using

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
- Since HTML reads top to bottom, take care to link the stylesheets in the correct order
	- e.g.
	- bootstrap first
	- then own stylesheet

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


# Chap 3 JavaScript

## Intro to JS

### History

Servers used many languages
- ASP
- PHP
- PERL
all serverside, needed send post req to use

Made demand for client side script, running on browser

attempts:
- java applets
	- not good due to lack of control over access to machine
- active X
- plugins

want somethin 
- interpreted
- fast

Brenden Eich - worked at netscape later founded mozilla
wrote the basics of javascript
Sun Oracle, owner off Java name, suggested naming it Javascript, as it was a "we-hate-microsoft" together phase
so its not really related to Java, more related from C

IEEE has a specific name for Javascript as it is official but everyone calls is js lol

wont talk much about XML or JSON in the course but can use in project if you want

Java using var for all variables makes it prone to error if you dont handle the type of your variables well

Does not cascade / overwrite like css when having same function / variable name

Script tag does not have to be in header like style tag
Can be put at bottom of body, ensures script is only loaded when whole page is loaded
Location in code does matter since loading still loads from the top down

Now can just use defer tag in the script tag, rather than having to place it 

Or have a onload code in js to only add listeners when page fully loaded

or async, which implies your JS is all functions that do not require any information from the page and can be loaded before page is fully loaded
### Event Handling

Inline js is not secure, pls dont use

need to initialize listeners on load
make init function and add listeners for different things like banner or each caption


### Debugging

Use breakpoints

alt is like alt name for this specific tag, its like ID

### Advantages & Disadvantages of Client-side scripting
Advantages
- processing offload to client, reduce load on server
- browser responds rapidly to user events; improve user experience
- JS interact with HTML in a way that server cannot

Disadvantages:
- Client can disable to code, or admins can turn off js with policy
	- Means functionality req redundancy on server
- JS heavy web apps are complicated; hard to maintain
- Not fault tolerant
	- Will cease execution on invalid line
- Java script constantly being worked on, newer features may not be supported on all browsers

## Document Object Model (DOM)

Each tag is an element and becomes and object when the page is loaded

open using F12 inspect, elements tab

## JavaScript Libraries & frameworks

- Bootstrap JS
- jQuery
- Ajax
	- out of fashion, FetchAPI (2015) gaining popularity
- JSON
- Typescript


## TypeScript


# Chap 4 Web Accessibility and testing

## W3C Web accessibility Initiative

pre 2000
IE and netscape fighting, didnt care for standardisation
Developers  have to cook up funky javascript for netscape or for IE
Webpages may not work the same on diff browsers


- W3C overview
	- Who governs web
		- is the body set standands for browser maker and developers to follow
		- if both follow standard, all browsers work with all pages
- Web Standards
- Validating Web Pages
	- W3C Markup validation service
	- made to promote / make easier for people to follow the standard
	- can take public domain names
	- can take source code

## Web Content Accessibility
- Four principles (POUR)
	- Perceivable
		- Provide Text alternative for non-text content
		- Provide captions & other alternatives for multimedia
		- Create content that can be presented in different ways including assistive technologies w/o losing meaning
		- Make it easier to see and hear content (e.g. font size)
	- Operable
		- Make all functionality available from keyboard
		- Give users enough time to read and use content
		- Do not use content that can induce seizures or physical reactions
		- Help users navigate and find content
		- Make it easier to use inputs other than keyboard
	- Understandable
		- Make text readable / understandable
		- Make content appear and operate in predictable ways
		- Help users avoid and correct mistakes
	- Robust


## Accessibility Testing Tools
- deque's axe browser plugin
- used to test website for WCAG POUR

# Chap 5 Serverside web dev PHP

Some servers only return files  e.g, send html then .css then .js
those do not process any logic, all done by browser software

PHP Hypertext Preproccessor

Extensions that use php files require server to process logic as browser does not have ability to process raw php file
so server processes logic and makes / fetches correct html and/or css and/or js

can use echo() to execute string to html e.g. echo "\<h1>hello world\</h1>"

others
• ASP (Active Server Pages). This was Microsoft’s first server-side technology (also called ASP Classic).  
• ASP.NET. This replaced Microsoft’s older ASP technology.  
• JSP (Java Server Pages). JSP uses Java as its programming language and like ASP.NET it uses an explicit  
object-oriented approach and is used in large enterprise web systems and is integrated into the J2EE  
environment.  
• Node.js (or just Node). Uses JavaScript on the server side  
• Perl. excels in the manipulation of text.  
• PHP. Like ASP, PHP is a dynamically typed language that can be embedded directly within the HTML  
• Python. This terse, object-oriented programming language has many uses, including being used to create web  
applications.  
• Ruby on Rails. This is a web development framework that uses the Ruby programming language

## PHP
advantage
- secret / security 
- cross platform compatibility (php chooses correct format to display)
- access to server-side resources like database
- works even if js disable by client, php always runs as is on server
disadvantage
- increased response time / latency may become an issue
- server requiers more processing power
- more work required serverside / more overhead serverside
- little bbit arcer to debug

75% of pages in world use php
- wordpress and wooCommerce use php thats why

php made from perl made from C so similar syntax, easier to learn
php has many existing examples, easy to find examples or implementations

PHP is dynamically typed w/ optional static typing
- boolean
- int
- float
- string
- array (any type)
	- actually ordered map
	- each val has key
	- like python dict
	- keys are innt by default and start from 0 like other langs like normal
	- unless explicitly defined by using =>, "KEY" => VAL, KEY => VAL
	- multidimensional arrays work too
	- array var needs \[] after name
- objects

## Php code
PHP can embed directly into html, will have .php extension
Code must be contained in tag; start with \<?php end with ?>
Code in tags interpreted and executed, code outside tag sent to client raw
uses JS style commenting

PHP constants use define(); args name of const and value
Once defined no need $ to reference const
other vars need $ to define and reference

echo() to output to console
use "." to concatenate

printf() exists, works like C but vars must reference with $
if else same format as C condition in () and html code in {}
	alt syntax replace brackets with endif tag
	kinda trash tho
switch case condition in () cases in {} with each case after :
while same as c
do while same as c
for

include "";    //    include_once "";    //    require "";    //    require_once "";

define funcs format
	`function FUNC_NAME($parameter){`
	`code;`
	`}`
 and if need explicit return type (implemented in php 7.0)
	 `function FUNC_NAME($parameter) : RETURN_TYPE{`
	`code;`
	`}`
and if need default value
`function FUNC_NAME($parameter = VALUE){`
	`code;`
	`}`
 
use & to pass value by reference

iterate through array like normal with while, for and foreach loop
can add to array with exact index or empty \[] to add to end of array
delete explicitly elements with unset()
check if val in array with isset()

define class
`class CLASS_NAME {`
	`public $SOME_VAR;`
	`private $SOME_VAR_2;`
	`protected $SOME_VAR_3;`
	`function __construct($some_param){`
	`}`
	`public function SOME_METHOD($some_param_2){`
	`}`
`}`

use `new` to instantiate obj
access object properties with `->`; e.g. `$Student->name`
constructor must be declared per class like OOP
methods same as java OOP
extends like Java for inheritance

PHP special predefined associative arrays \[superglobal arrays]
allows access to HTTP headers, query string params, other impt http shit

| $GLOBAL                                             | $\_COOKIES                                           | $\_ENV                           | $\_FILES                                   | $\_GET                                                      | $\_POST                                                             | $\_REQUEST                                                          | $\_SESSIONS                      | $\_SERVER                                                     |
| --------------------------------------------------- | ---------------------------------------------------- | -------------------------------- | ------------------------------------------ | ----------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | -------------------------------- | ------------------------------------------------------------- |
| Array for storing data that needs superglobal scope | Array of cookie data passed to page via HTTP request | Array of server environment data | Array of file items uploaded to the server | Array of query string data passed to the server via the URL | Array of query string data passed to the server via the HTTP header | Array containing the contents of \$\_GET, \$\_POST, and \$\_COOKIES | Array that contains session data | Array containing information about the request and the server |
### flow of \$\_GET array
![[get_array.png]]

### flow of \$\_POST array
![[post_array.png]]

### \$\_POST detection
![[post_detecction.png]]

### jQuery strings in hyperlinks
![[query_in_link.png]]
important to actively distrust all user input
need to sanitize
![[sanatize.png]]

## Http header
PHP can use to add content after HTTP response header but can also modify response header using header() function to create ability to redirect using location header or set content-type header

### redirect
![[redirection.png]]

### content type
The Content-Type HTTP header is used to tell the browser what type of content (using a MIME type) it is receiving in the response.  

Normally, the PHP environment automatically sets this header to text/html.  

However, you might want to change this header value.
2 common examples are:  
• Returning JSON Data  
• Outputting Custom Images


# Wk 6 Form Processing with HML5 and PHP

## Client-Side form validation
Validation can be done by HTML5 or Java script
Bootstrap has responsive forms with javascript
Even though Java script gives better experience, it cannot be relied on

html5 can be trusted a bit more as it has ways to limit inputs to forms
e.g. 
- limit  to 45 chars w/ maxlength attribute
	- avoid buffer overflow attack
	- optimize for storage reasons
- create mandatory field w/ required attribute
- create mandatory format w/ type attribute
	- e.g. type="email"; checks for @ symbol, but not for .com
	- type="password"

other libraries required for more complex validation e.g. validation for password complexity

sanatize may change input value
validation does not
## Server-side form validation & sanitisation

### POST vs GET

post sends data to server
format ?????????????????????????????????????????????//

implement with method attribute e.g. method = "post"

get puts data into page on client side

has ways to detect if form request failed and php is displayed by itself, can do error handling

| Advantage                                          | Disadvantage                        |
| -------------------------------------------------- | ----------------------------------- |
| Passes data without changing clientside hyper-link | Not encrypted                       |
|                                                    | can be intercepted unless SSL HTTPS |


### Security Concern -- XSS & SQL Injection

### filter_var()
sanitize + validate

has multiple flags
FILTER_VALIDATE_EMAIL flag checks against known email format pattern
return true if match, false if not match
### htmlspecialchars()
remove html tag things

### trim()
trim whitespace, tabs, newlines, breaks

### stripslashes
remove / and  \

## Security
Why do both?
Client-side can bypass
server-side cannot


## Lab shit

`if(!empty(\$\_POST("frame")){`

`}`

`function sanitise_input($data){`
`	$data = trim($data)`
`	$data = stripslashes($data)`
`	$data = htmlspecialchars($data)`
`	return $data`
`}`




`$pwd_hashed = password_hash($_POST("pwd"), PASSWORD_DEFAULT);`

shld not sanitize password, special chars allowed
never display or store as plaintext, always hash
# Wk7