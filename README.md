# Design Patterns:
- A design pattern in general is a reusable solution to a common problem within a specific context in software design.
- Patterns are blueprints that can be used in multiple situations. They are not direct piece of code.
- They focus on object interaction, system arcitecture and hoe classes/objects communicate.

## Why do we need Design Patterns?
- Software has many reocurring problem which has already been solved. For instance, let's consider the undo redo functionality. Regardless of what context we want the undo/redo functionality (like game, text editor, etc.), this problem has already been solved in the past in the most elegant way. We can take that already solved pattern and apply it to our context. This is the real use of design patterns.
- Another example: Let's consider in notification system, wha classes or objects or interfaces we want is already designed in the most elegant way. We can just take that pattern and use it in our context.

## Benifits of Design Patterns:
- **Code-reusablity:** Patterns provide proven solutionsthat can e applied in multiple projects.
- **Maintainability:** Encourages clean, understandable ans structured code which is easier to maintain and extend.
- **Communication:** Design patterns act as a common language between developers, inproving communications and understanding.
- **Scalability:** Design patterns help in structuring code in support future scaling with fewer refactors.
- **Efficiency:** Avoids reinventing the wheel by using well tested and widely accepted solutions.

## Behavioral Design Pattern
- Choose behavioral design patterns when you need to manage algorithms, communication, or responsibilities between objects. They're useful for encapsulating behavior that varies and promoting loose coupling between objects.
- Behavioral patterns facilitate code reuse, flexibility, and maintainability by defining how objects interact and communicate.
- Use them to address scenarios like handling complex workflows, managing state transitions, or implementing communication between objects.
- Choose Behavioral Design Patterns when the Problem is related to Object Interactions.

### Catalog:
- **Observer:** Observes and notifies changes in multiple objects.
- **Strategy:** Encapsulates the interchangeable algorithms.
- **Command:** Encapsulates requests as objects for decoupled execution.
- **State:** It Changes the behavior of object with internal state.
- **Visitor:** It separates algorithms from objects.
- **Memento:** Pattern to manage object state and actions.
- **Iterator:** It Sequentially accesses the elements of a collection.
- **Mediator:** Central controller managing communication between objects.
- **Chain of Responsibility:** Pass request through handlers until one handles it.
- **Template Method:** Defines the skeleton of an algorithm.
 
## Creational Design Pattern
- Choose creational design patterns when object creation is complex, involves multiple steps, or requires specific initialization. They're useful for promoting reusability, encapsulating creation logic, and decoupling client code from classes it instantiates.
- Creational patterns enhance flexibility, making it easier to change or extend object creation methods at runtime.
- Choose Creational Design Patterns when the Problem is related to Object Creation.

### Catalog:
- **Singleton:** Makes sure there is just one instance.
- **Factory Method:** Assigns subclasses the task of instantiating objects.
- **Abstract Factory:** Constructs related object families without defining their concrete classes.
- **Prototype:** Clones objects to provide a template example.
- **Builder:** Helps in building the complex objects step by step.
 
## Structural Design Pattern
- Choose structural design patterns when you need to compose objects and classes into larger structures while keeping them flexible and efficient. These patterns are useful for clarifying relationships between classes, managing object hierarchies, and altering interfaces without affecting clients.
- Structural patterns promote code reuse, simplify system design, and enhance scalability.
- They're beneficial when dealing with complex systems, integration of new components, or refactoring existing codebases.
- Choose Structural Design Patterns when the Problem is related to Object Assembly.

### Catalog:
- **Adapter:** Acts as a bridge between two incompatible interfaces.
- **Bridge:** Separates the abstraction from the implementation.
- **Composite:** Handles single and composite objects equally.
- **Decorator:** Adds behaviors to objects dynamically.
- **Facade:** Helps in Simplifying the complex system interfaces.
- **Flyweight:** Shares common parts of state between multiple objects to reduce memory.
- **Proxy:** Controls the access to an object.

# References:
- [Refactoring Guru](https://refactoring.guru/design-patterns)
- [Geeks for Geeks Cheat Sheet](https://www.geeksforgeeks.org/system-design/design-patterns-cheat-sheet-when-to-use-which-design-pattern/)
