class House:
    def __init__(self):
        self.__house_type = None
        self.__num_walls = 0
        self.__num_windows = 0
        self.__roof_type = None
        self.__has_garage = False
        self.__has_swimming_pool = False
        self.__has_porch = False
    
    def __str__(self):
        return ("House<" + self.__house_type +  "> {\n" +
                "\tnum_walls = " + str(self.__num_walls) + ",\n" + 
                "\tnum_windows = " + str(self.__num_windows) + ",\n" +
                "\troof_type = \"" + self.__roof_type + "\",\n" +
                "\thas_swimming_pool = " + str(self.__has_swimming_pool) + ",\n" +
                "\thas_garage = " + str(self.__has_garage) + ",\n" +
                "\thas_porch = " + str(self.__has_porch) + "\n" +
                "}\n")
    
    def set_house_type(self, house_type):
        self.__house_type = house_type

    def set_num_walls(self, num_walls):
        self.__num_walls = num_walls

    def set_num_windows(self, num_windows):
        self.__num_windows = num_windows
    
    def set_roof_type(self, roof_type):
        self.__roof_type = roof_type
    
    def set_has_garage(self, has_garage):
        self.__has_garage = has_garage
    
    def set_has_swimming_pool(self, has_swimming_pool):
        self.__has_swimming_pool = has_swimming_pool
    
    def set_has_porch(self, has_porch):
        self.__has_porch = has_porch