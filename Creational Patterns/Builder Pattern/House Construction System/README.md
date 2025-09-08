# Problem
You need to construct a complex object (like a House with walls, roof, plumbing, electrical wiring, etc.).

# Naive Approach
Use constructors overloaded with numerous parameters (telescoping) or create a subclass for each configuration. The problems with this approach is:
- This leads to ugly telescoping constructors or explosion of subclasses, making the system hard to maintain and extend.
- SRP violated: object constructors or subclasses handle creation logic plus business behavior.
- OCP violated: adding new configuration requires modifying constructors or creating new subclasses.
- DIP violated: client depends on concrete constructors rather than abstractions.

# Solution: Builder Pattern
- Introduce a Builder abstraction that defines steps (buildWalls, buildDoor, etc.) for constructing parts of the object.
- Implement different Concrete Builders for each representation (e.g., wooden house, stone castle), following the same steps but building differently.
- Optionally use a Director to encapsulate the sequence of steps for standard configurations.
- SRP: Creation logic is moved to builder classes.
- OCP: New configurations by adding new builder classes.
- DIP: Clients depend on builder abstraction, not concrete classes.