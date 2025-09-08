from NetworkServiceProxy import NetworkServiceProxy

service = NetworkServiceProxy()
print(service.fetch_data(1))
print(service.fetch_data(3))
print(service.fetch_data(2))
print(service.fetch_data(1))