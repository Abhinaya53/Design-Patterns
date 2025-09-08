# Problem:
- In systems with many interacting components (like GUIs), direct communication between components leads to complex dependencies.
- Example: In a dialog window, a checkbox enables a text field and button; clicking the button resets the checkbox and clears the text field.
- As the number of components grows, the code becomes harder to maintain, understand, and extend.

# Naive Approach:
- Each UI element has direct references to other elements.
- When an event occurs (e.g., checkbox checked), the component directly calls methods on other components to update their state. (Example: Checkbox in Without Pattern Version)
- The problem with this approach is:
    - This leads to a web of dependencies as more components are added.
    - Tight coupling between components.
    - Poor maintainability; changes require modifying many classes.
    - Difficult to reuse components elsewhere.
    - Components handle their own logic and communication. Hence SRP is violated.
    - Adding new interactions requires modifying existing components. Hence OCP is violated.
    - Components are not easily replaceable due to tight coupling. Hence LSP is violated.
    - Components may depend on methods they do not need. Hence ISP is violated.
    - High-level modules depend on low-level modules. Hence DIP is violated.

# Solution: Mediator Pattern
- Introduce a mediator object to centralize and manage interactions.
- Components communicate only with the mediator, not with each other.
- Mediator coordinates responses and interactions.
- All communication logic is handled in one place.
- Components only handle their own logic; mediator handles communication. SRP is followed.
- New interactions are added by changing the mediator, not components. OCP is followed.
- Components can be replaced independently. LSP is followed.
- Components only depend on mediator interface. ISP is followed.
- Components depend on mediator abstraction, not concrete implementations. DIP is followed.
