# Problem:
Suppose, we are building a logistics management app. Initially, it only supports trucks, so your Logistics class directly creates a Truck object. Later, the business expands and requires ships for overseas deliveries.

# Naive Method:
Modify LogisticsApplication to also create Ship objects. This is a problem because:
- Every time a new transport type (like Plane or Train) is introduced, you need to change the existing Logistics code. This violates OCP.
- You also end up with messy conditionals (if transport == "truck"... elif "ship"...) everywhere.
- SRP violation: Logistics is handling both delivery coordination and transport object creation.
- High-level code depends on concrete transport classes instead of abstractions. This violates DIP.

# Solution: Factory Method Pattern
Introduce a factory method in the Logistics base class that creates transport objects, but delegate the actual implementation to subclasses.
- The LogisticsFactory interface declares a factory method createTransport().
- Subclasses (RoadLogistics, SeaLogistics, etc.) override this method to instantiate the right transport.
- The client uses Logistics without caring about the concrete transport type.
- Logistics only coordinates deliveries and subclasses handle transport creation. Hence, SRP is maintained.
- Add a new transport by creating a new subclass without touching existing code. This adheres to OCP.
- Clients depend on the abstract Transport interface, not on Truck/Ship. This follows DIP.
