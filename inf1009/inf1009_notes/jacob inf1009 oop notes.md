
## Wk1
Java

start w/ class definition & main method as entry
emphasise OOP nature

c uses int main()
python use print() \[ no type decleration ]

public class HelloWorld {
    public static void main(String[] args) {
        system.out.println("Hello, Java");
    }
}

comments: // or /* */ or /** */

class header: public class HelloWorld  
method header: public static void main

system finds main method as entry  
main must be: public, static, void

static methods can be called without instantiating class  
instantiating is creating an object with that class  

static means even if havent make oject with thta class, you can still call the static function

other methods execcuted through main  

space, tabs still whitespace

good practice to start class name with caps

class has:  
method / behaviour  
attributes  

datatypes in java:  
primitive types: int, double, bool, char

when declare a class, it does not have values.  


Class definition: define attribute and methods  
Object instance: an instance of class

e.g.  
public class Student{
    String name;
    int year;
    public Student(String n, int y{
        name = n;
        year = y;
    })
}
student s = new Student("Nisha",3);
// s.name == "Nisha"  
// s.year == 3

UML diagram for this class:  
|Student|
|-|
|+ name|
|+ year|
|+ Student(String,int)|

memory is not allocated to any class until we use 'new' keyword to make an object instance of a class  
declaration of class does not reserve memory

java input using Scanner:  
Scanner class reads user input from console  
System.in is console input  
code:  
Scanner sc = new Scanner(System.in);
System.out.print("Enter name: ");
String name = sc.nextLine();

Output with System.out:  
System.out.print displays prompt and message to users

another input class is BufferedInput
BuffredReader input = new BufferedReader(new InputStreamReader(System.in));
String inputString = input.nextLine()

Arrays in java:  
arrays fixed size like C  
need know max cap at compile time  
Slow search  
addition/deletion of array entry more difficult  

Collections in java  
provvides effecient management of data structures
ArrayList is part of collections and os more dynamic  
ArrayList supports dynamic arrays (built in add, delete and access methods)  
the type can be objects not just primative type  
ArrayList\<Type> arraList = new ArrayList<> ();

LinkedList also part of collections  
doubly-linked list: fast insertion/deletion at ends or when have reference node

NOTE  
- there is no == in java.  use .equals()
- attempting to access a uninitialised object will throw NullPointerException and crash


## Wk2

### Project Yapping

Abstract Engine (wk 1-7):  
- not actual simulation/game
- generic foundation
- contains core functionality
- exists outside of specific context
- supposed to offer re-useable components
- think about it as raw engine, dont need to define anything like cards for specific game context
- just make placeholder entities to build abstract engine functions
- entities will not have anything that has context to the game like HP, damage, color
- entities only have characteristics like: Renderable, Mesh,
- base classes/interfaces/managers
- handle lifecycle and interactions
- implement reusable components
- abstract engine should be done by wk 7 and not recommended to adjust after that
- 
- MUST HAVE:
	- Scene Management  
		- Load scene
		- Unload scene
		- Transition between scenes
	- Entity Management  
		- Create
		- Manage
		- Update
	- Collision Management  
		- Detections
		- Resolution
	- Movement Management  
		- Movement of non-player entities
	- Input/Output Management
		- Manage All input & output

Logic Engine (wk8 -wk14)
- Creates concrete classes in context of game
- defines object properties & behaviors
- simulation rules

Develop a Simulation
- important components
	- entities
	- environment
	- logic
- From devs perspctive, of these componnents:
	- what are the main objects?
	- what is the main characteristics of these objects
- GOAL OF PROJECT
	- to apply OOP fundamentals in the creation of this project
- REQUIERMENTS
	- only use libgdx as the simulation env

Project split into:
- management of simulation elements is app part of abstract/non-contextual engine
- Simulation specific logic (contextual layer)
- 
- note
- is more important to focus on abstract engine
- (no  shortcuts to develop the components, e.g. no libraries).
- box2d extension allowed (wk2 lecture she say one)

Problem Statement Wk1-7: Develop an abstract engine

PROJECT REQUIERMENTS:  
- prototype to demonstrate the abstract engine technology and game mechanics
- Proper usage of OOP concepts  
	- Classes  
	- Objects  
	- Inheritance  
	- Polymorphism  
	- Error Handling
- Re-usability
	- Modularity
- Functionalities
	- Game features

Recommendations:
- UML diagram  
	- Identify the main entities to create classes  
	- Think how you want to structure and connect these classes  
- Code  
	- Store code in a repository  
	- Collaborate with your team-mates  
	- Use it for the entire project  
	- Code structure  
	- File, class and function naming convention should be followed (they should be self explanatory)
- Aim for Innovation/Complexity/Solving for the Problem  
- Should focus on solving a problem better than other solutions to same problem (market value)  
- Think whether proposed solution will work for client/target audience

OOP WEEK 4 DELIVERABLES:
- UML diagram for abstract engine
- Class hierarchies
- Relationships between different classes and interfaces

OOP WK 7 OTHER DELIVERABLES:
- Report
	- Professionally written with clear logic and structure
- Code
	- Dropbox submission of the entire code of prototype
	- Must include DEMO for engine, not just raw engine
- Presentation
	- Presentation Slides to showcase exactly what the team has done  
	- 
	- Innovation and functionalities
- Video
	- One short video to demonstrate all features and design of the system
- Peer eval
	- Gey

### Lecture shit

in switch case: 
if each case has no break
it will run found case, then default case

in java  
\== compares mem address
whereas .equals compares content

in java 
list.remove(0) will automatically shift all indexes down
0 here is the index


### SOLID BIRD BIRD
- The Single Responsibility Principle  
	- A class should only have one job / reason to change
	- e.g a report class that generates, formats and prints a report does not follow this principle
	- shld have Report class, ReportGenerator class, ReportFormatter, Report Printer
	- This way if anythign changes only one class is changed
- The Open-Closed Principle  
	- Open for extension, Closed for modification
	- PaymentService Class (Closed)
	- UPIPayment, CardPayment, Wallet Payment
	- each extends from payment service but is different based on exactly how they pay
- The Liskov Substitution Principle  
- The Interface Segregation Principle  
- The Dependency Inversion Principle

### Encapsulation
Hide mess
- Class:
	- Public variables & methods
		- Private variables & methods

Secures data
Restricts Access


Safe Control Access
- Public getter function returns value of private var
- Public setter function updates variable safely
- provides validation / checks

UML diagrams
- helps developers get overall view on how different classes talk to each other
- Start with title
- the all variables with - as the prefix
- then all methods incld constructors with + as the prefix

SOLID principles helps you write code that doesnt explode when you add new features


## Wk 3

### Inheritance

Parent Class's variables are copied to child class (not by values, just same name)
Child class can access Parent Class's variables if that already have a value
Child class's variables only exist within child class and parent cannot access.

Proper encapsulation should include validation in getter setter functions

### Polymorphism
The capability of a single method to operate on different types of objects

Allows same method name to behave differently based on object it is acting upon

e.g.
one area() function in parent class
but it reads what the this.type of the instance object is, then uses the correct formula to return correct value

overloading is also called compile time polymorphism because when compile function, programmer knows there are 2 funcs with diff arguments

#### Overloading
a func with multiple definitions based on arguments in a single class

#### Overriding
a func in child class has the same name as a func from parent class
it also takes the exacct same arguments as the parent class's func
calling this func from the child class will use the child class implementation, overridng the parent class implementation

## Wk 4