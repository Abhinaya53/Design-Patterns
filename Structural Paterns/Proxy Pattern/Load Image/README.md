# Problem: 
Suppose we have an application which loads a heavy object like a large image from disk. It might take time to load the image, and we don’t want to load it until it’s necessary. 

# Naive Approach:
The application (client) would load the image every time it's needed, even if not displayed, wasting resources. The problems with this approach are:
Each client builds or manages the heavy service on its own:
- SRP is violated because client handles both its logic and the service's initialization.
- OCP is violated since any change in service lifecycle requires updating each client.
- DIP is violated as clients depend directly on the concrete service class.

# Solution: Proxy Pattern
Proxy pattern solves this by:
- Creating a Proxy that implements the same interface as the service.
- Clients use the proxy instead of the real service. The proxy handles service creation, access control, caching, or logging transparently before delegating to the real service.
- SRP: Proxy encapsulates initialization and control logic.
- OCP: Changing service behavior only requires updating or replacing the proxy.
- DIP: Clients depend on the interface, not the concrete service.