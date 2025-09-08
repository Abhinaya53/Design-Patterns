# Problem:
Suppose you are developing a graphic editor application that supports multiple shapes (like Circle, Rectangle) and multiple rendering methods (like Vector rendering, Raster rendering). 

# Naive Approach:
In a naive approach, you might create separate classes for each combination of shape and rendering method. For example, you would have classes like `VectorCircle`, `RasterCircle`, `VectorRectangle`, and `RasterRectangle`. The problems with this approach are:
- It leads to a combinatorial explosion of classes as the number of shapes and rendering methods increases.
- Each shape class would have similar methods for rendering, leading to duplicated code across classes.
- Adding a new shape or rendering method would require creating multiple new classes.
- It violates the Open/Closed Principle, as existing classes would need to be modified to accommodate new shapes or rendering methods.
- It makes the codebase harder to maintain and extend.

# Solution: Bridge Pattern
The Bridge Pattern is a structural design pattern that decouples an abstraction from its implementation, allowing the two to vary independently. In the context of our graphic editor application, we can use the Bridge Pattern to separate the shape hierarchy from the rendering method hierarchy.
- We define an interface for the rendering method (e.g., `Renderer`) and implement concrete classes for each rendering method (e.g., `VectorRenderer`, `RasterRenderer`).
- We define an abstract class for shapes (e.g., `Shape`) that contains a reference to a `Renderer` object. Concrete shape classes (e.g., `Circle`, `Rectangle`) extend the `Shape` class and implement their specific drawing logic using the `Renderer` interface.
- This way, we can add new shapes or rendering methods independently without affecting existing code. The Bridge Pattern promotes code reusability, maintainability, and adherence to the Open/Closed Principle.