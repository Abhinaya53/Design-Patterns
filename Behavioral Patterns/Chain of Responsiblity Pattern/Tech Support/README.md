# Problem:
- Consider a complex systems, where a series of objects that can handle a request, but it's not sure in advance which one will handle it.
- For example in a Tech Support system, a customer has a query and reaches out. 
- They way the query is handled is it's first given to chatbot. If it can't handle the query then it connects the customer to a tech support staff. 
- The tech support staff tries to resolve the query but if he can't handle it then the customer is connected to his supervisor. 
- Similarly if not supervisor then its his manager. 

# Naive Approach:
The naive way to handle this is by having the customer (request sender) have conditional statements for all request handlers and gets their query resolved. But the problem with this approach is:
- Tight coupling between sender and all handlers.
- Hard to add, remove, or reorder handlers.
- Violates the Open/Closed Principle; changes require modifying the sender.
- Difficult to reuse handlers in other contexts.
- SRP is violated as sender handles both request logic and handler selection.
- LSP is violated as handlers aren’t easily replaceable due to tight coupling.
- DIP is violated as sender depends on concrete handler implementations.

# Solution: Chain of Responsiblity Pattern:
Instead of one big handler, break the processing into a chain of linked handlers. 
- Each handler has:
    - A method to process the request.
    - A reference to the “next” handler in the chain.
- If it can handle the request, it does so. Otherwise, it passes it to the next handler.
- The client only talks to the first handler in the chain.
- SRP is followed now since each handler does only one kind of check.
- OCP is honoured as we can now add new handlers without changing existing ones. Just link them into the chain.
- Handlers depend only on the handler abstraction, not concrete classes, so DIP is fixed.
