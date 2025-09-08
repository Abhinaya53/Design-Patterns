# Problem:
Design an application to manage access to a network service that retrieves data from a remote server. The objective is to create a proxy that can control access to the network service and cache responses to optimize performance.

# Requirements:
- Create a NetworkService interface with the following method:
    - fetch_data(): This method will be responsible for fetching data from a network service.

- Implement a RealNetworkService class that:
    - Represents the actual network service and implements the NetworkService interface.
    - Simulates fetching data from a remote server.

- Implement a NetworkServiceProxy class that:
    - Also implements the NetworkService interface.
    - Manages access to the RealNetworkService.
    - Checks if the data is already cached; if not, fetch it from the real service and cache it for future use.

- Create a client class that demonstrates the use of the proxy. This class should:
    - Fetch data through the NetworkServiceProxy.
    - Display the results.