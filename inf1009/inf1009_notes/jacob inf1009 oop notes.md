Java

start w/ class definition & main method as entry
emphasise OOP nature

c uses int main()
python use print() [ no type decleration ]

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
ArrayList<Type> arraList = new ArrayList<> ();

LinkedList also part of collections  
doubly-linked list: fast insertion/deletion at ends or when have reference node

NOTE  
- there is no == in java.  use .equals()
- attempting to access a uninitialised object will throw NullPointerException and crash