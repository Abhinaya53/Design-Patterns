class House:
    def __init__(self, house_type, num_walls, num_windows, roof_type, has_garage, has_swimming_pool, has_porch):
        self.__house_type = house_type
        self.__num_walls = num_walls
        self.__num_windows = num_windows
        self.__roof_type = roof_type
        self.__has_garage = has_garage
        self.__has_swimming_pool = has_swimming_pool
        self.__has_porch = has_porch
    
    def __str__(self):
        return ("House<" + self.__house_type +  "> {\n" +
                "\tnum_walls = " + str(self.__num_walls) + ",\n" +
                "\tnum_windows = " + str(self.__num_windows) + ",\n" +
                "\troof_type = \"" + self.__roof_type + "\",\n" +
                "\thas_swimming_pool = " + str(self.__has_swimming_pool) + ",\n" +
                "\thas_garage = " + str(self.__has_garage) + ",\n" +
                "\thas_porch = " + str(self.__has_porch) + "\n" +
                "}")