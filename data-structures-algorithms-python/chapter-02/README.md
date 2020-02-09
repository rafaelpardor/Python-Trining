# 2 - Object Oriented Programming

## 2.1 - Goal, Principles and Patterns

### 2.1.1 - OO Design Goal

- Robustness

  Building roubust software we low the probability of unexpected errors.

- Adaptability

  Thus, another important goal of quality software is that it achieves adaptability (also called evolvability). Related to this concept is portability, which is the ability of software to run with minimal change on different hardware and operating system platforms.

- Reusability

  Going hand to hand with 'Adaptability', is the desire that software should be reusable, the code should be usable as a component of different systems.

### 2.1.2 - OO Desing Principles

- Modularity

  Modern software systems typically consist of several different components that must interact correctly in order for the entire system to work properly. Keeping these interactions straight requires that these different components be well organized. Modularity refers to an organizing principle in which different components of a software system are divided into separate functional units.

- Abstraction

  The notion of abstraction is to distill a complicated system down to its most fundamental parts. Typically, describing the parts of a system involves naming them and explaining their functionality.

- Encaptulation

  Different components of a software system should not reveal the internal details of their respective implementations. One of the main advantages of encapsulation is that it gives one programmer freedom to implement the details of a component, without concern that other programmers will be writing code that intricately depends on those internal decisions.

### 2.1.3 - OO Desing Patterns

Object-oriented design facilitates reusable, robust, and adaptable software. Designing good code takes more than simply understanding object-oriented methodologies, however. It requires the effective use of object-oriented design techniques.

A pattern provides a general template for a solution that can be applied in many different situations. It describes the main elements of a solution in an abstract way that can be specialized for a specific problem at hand.

## 2.2 - Sofware Development

### 2.2.1 - Desing

The design step is perhaps the most important phase in the process of developing software.

- Responsabilities

  Divide the work into different actors, each with a different responsibility. Try to describe responsibilities using action verbs. These actors will form the classes for the program.

- Independence

  Define the work for each class to be as independent from other classes as possible. Subdivide responsibilities between classes so that each class has autonomy over some aspect of the program.

- Behaviors

  Define the behaviors for each class carefully and precisely. These behaviors will define the methods that this class performs, and the set of behaviors for a class are the interface to the class.

UML (Unified Modeling Language) diagrams to express the organization of a program. UML diagrams are a standard visual notation to express object-oriented software designs.

### 2.2.2 - Pseudo-Code

Pseudo-code is not a computer program, but is more structured than usual prose. It is a mixture of natural language and high-level programming constructs that describe the main ideas behind a generic implementation of a data structure or algorithm.

### 2.2.3 - Coding style and Documentation

Good programmers should therefore be mindful of their coding style, and develop a style that communicates the important aspects of a program’s design for both humans and computers.

Sometimes in the software development team, should have some type coding style, or generalized, however, some programming languagues, like Python, have their own style.

Adding to that, the documentation of a piece of code, or software is very importat, if is not obligatory. All though, we have code conventios, having some comments explaining the code will save a lot of work.

### 2.2.4 - Testing and Debugging

Testing is the process of experimentally checking the correctness of a program, while debugging is the process os tracking the execution of a program and discovering the errors in it.

#### Testing

A cereful testing plan is an essential part of writing a program. While verifying the correctness of a program over all possible inputs is usually infeasible, we should aim at executing the program on a representative subset of inputs. Programs often tend to fail on special cases of the input. Such cases need to be carefully indentified and tested. In addition to special inputs to the program, we should also consider special conditions for the structures used by the program. For example, if we use a Python list to store data, we should make sure that boundary cases, such as inserting or removing at the beginning or end of the list, are properly handled.

The dependecies among the classes and functions of a program induce a hierarchy. Namely, a component A is above a component B in the hierarchy if A depends upon B, such as when function A is above a component B in the hierarchy if A depends upon B, such as when function A calls function B, or function A relies on a parameter that is an instance of class B. There are two main testing strategies, top-down and bootom-up, which differ in the order in which components are tested.

Top-down testing proceeds from the top the bottom of the program hierarchy. It is typically used in conjuction with stubbing, a boot-strapping technique that replaces a lower-level component with a stub, a replacement for the componet that simulates the functionality of the original. For example, if function A calls function B to get the first line of a file, when testing A we can replace B with a stub that returns a fices string.

Bottom-up testing proceeds from lower-level components to higher-level components. For example, bottom-level functions, which do not invoke other functions, are tested first, followed by functions that call only bottom-level functions, and so on. Similarly a class that does not depend upon any other classes can be tested before another class that depends on the former. This form of testing is usually described as unit testing, as the functionality of a specific component is tested in isolation of the larger software project. If used properly, this strategy better isolates the cause of errors to the component being tested, as lower-level components upon which it relies should have already been thoroughly tested.

#### Debugging

The simplest debugging technique consist of using print statements to track the values of variables during the execution of the program. A problem with this approach is that eventually the print statements need to be removed or commented out, so they are not executed when the software is finally released.

A better approach is to run the program within a debugger, which is a specialized eviroment for controlling and monitoring the execution of a program. The basic functionality provided by a debugger is the insertion of breakpoints within the code. When the program is executed within the debugger, it stops at each breakpoint. While the program is stopped, the current value of variables can be inspected.


