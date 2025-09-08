from Mediator import Mediator

class Flight:
    def __init__(self, id, mediator: Mediator):
        self.__id = id
        self.__status = "TakeOff"
        self.__mediator = mediator
        self.__mediator.register_flight(self)
        
    def get_id(self):
        return self.__id
    
    def request_takeoff(self):
        print(f"Aircraft {self.get_id()} is requesting for take-off")
        self.__status = self.__mediator.handle_takeoff_request(self)
        if self.__status == "TakingOff":
            print(f"Aircraft {self.get_id()} Take-Off: SUCCESS")
            self.complete_takeoff()
    
    def request_landing(self):
        print(f"Aircraft {self.get_id()} is requesting for landing")
        self.__status = self.__mediator.handle_landing_request(self)
        if self.__status == "Landing":
            print(f"Aircraft {self.get_id()} Landing: SUCCESS")
            self.complete_landing()
    
    def complete_takeoff(self):
        print(f"Aircraft {self.get_id()} has completed take-off")
        self.__status = "TookOff"
        self.__mediator.notify_takeoff_complete(self)
    
    def complete_landing(self):
        print(f"Aircraft {self.get_id()} has completed landing")
        self.__status = "Landed"
        self.__mediator.notify_landing_complete(self)