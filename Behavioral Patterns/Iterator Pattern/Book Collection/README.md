# Problem Statement:
Design a Book Collection class with an iterator to traverse the collection. If the internal structure of the collection changes, client must not need to change their code.

# Naive Approach:
Let the clients traverse the collections. Problem with this approach is:
- Clients must know the internal structure of the collection. Any change to the internal structure in future will break clients code. This violates OCP.
- SRP is also violated because client's business logic is mixed with traversal logic.
- Duplication of traversal code in many clients.
- DIP is violated because clients depend on collection's internal structure and not abstractions.

# Solution - Iterator Pattern:
This pattern separates traversal logic into it's own class. 
- Iterator interface will define methods like has_next() or next() for traversal.
- Implement Concrete Iterators for each collection type (or traversal order).
- Collections expose a method like createIterator() to give clients an iterator.
- Clients use the iterator without knowing the collection’s internals.
- Now OCP, SRP and DIP are followed.

# Note:
- Version 1 is just an example for this pattern.
- Version 2 is a more Pythonic way of doing this.
