# Problem
Suppose you are designing a microservices-based application that consists of multiple services, each responsible for a specific functionality. 

# Naive Approach:
Let clients interact with these services to perform various operations by calling those themselves. The problems with this approach are:
- Clients need to understand the details of each service, leading to tight coupling and increased complexity.
- Directly exposing each service to the clients can lead to complexity, increased latency, and security concerns.
- SRP is violated as clients are responsible for managing multiple service interactions.
- OCP is violated as adding new services or modifying existing ones requires changes in client code.
- DIP is violated as clients depend on concrete service implementations rather than abstractions.
- ISP is violated as clients may be forced to depend on services they do not use.
- LSP is violated as clients may not be substitutable if they depend on specific service implementations.

# Solution: Facade Pattern
Facade pattern solves this by:
- Introducing an API Gateway that acts as a single entry point for clients to interact with the microservices.
- The API Gateway acts as a facade, providing a unified interface to the client while handling communication with the underlying microservices. 
- It simplifies client interactions, reduces network calls, and abstracts away the complexity of dealing with multiple services.
- SRP is followed as the API Gateway is responsible for managing service interactions, allowing clients to focus on their specific tasks.
- OCP is followed as new services can be added or existing ones modified without changing client code.
- DIP is followed as clients depend on the API Gateway abstraction rather than concrete service implementations.
- ISP is followed as clients can interact with the API Gateway without being forced to depend on services they do not use.
- LSP is followed as clients can be substituted with other clients that interact with the API Gateway without affecting functionality.