from Vehicle import Vehicle

class LuxuryCar(Vehicle):
    def __init__(self, number_plate: str = None):
        super().__init__(number_plate)
    
    def __str__(self) -> str:
        strng = super().__str__()
        return f"Vehicle: Luxury Car\n" + strng
    
    def get_fare_per_km(self) -> float:
        return 15.0