# Problem Statement:
Design a text editor application that enables users to format their documents using different styles, such as Plain Text, HTML, and Markdown. Each formatting style transforms the document’s content in its own unique way. The application should allow users to switch between these formatting styles at runtime, with the ability to easily incorporate new formatting styles in the future.

# Naive Method: 
Using conditional statements based on the style.

Although this methods works it violates:
1. OCP: Everytime we want to add a new style in future, we will have to modify already existing code.
2. SRP: The TextEditor class have multiple responsiblity.

# Strategy Pattern Solution:
1. Extract each style into its own class that implements a shared interface (FormatterStrategyInterface).
2. These become interchangeable strategy objects.
3. The TextEditor (Context) holds a reference to a strategy and delegates the processing displayment task to it.
4. Clients (User) can swap strategies at runtime.
5. Flexibly changing text editor behavior without touching the TextEditor itself.
6. OCP is followed. Adding a new style won't need any change in TextEditor now.
7. SRP is followed. Every style has it's own class.

This design dramatically simplifies maintenance and enhances flexibility.
