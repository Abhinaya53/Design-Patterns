# Problem:
Suppose we have a shape generator which generates various shapes like circle, rectangle, etc. Now we have to make a clone of the shape object.

# Naive Approach:
We can manually copy all field values into another object. The problems with this approach are:
- Some private fields may be hidden and we might not access them.
- If the object has nested objects, we have to manually clone them too. This can lead to a lot of boilerplate code.
- If the class structure changes, we have to change the cloning code too.
- Violates SRP: Object creation logic is mixed with business logic.
- Violates OCP: Adding new ways of creating similar objects requires modifying code.
- Violates DIP: Client depends on concrete classes instead of abstraction.
- Code duplication, performance overhead, and harder maintenance when many variations are needed.

# Solution: Prototype Pattern
- Instead of instantiating objects directly, store a prototype object and use it as a “blueprint.”
- New objects are created by cloning the prototype.
- Each subclass implements its own clone() method, ensuring proper duplication of its internal state.
