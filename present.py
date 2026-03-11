import Model

class Presenter:

    def __init__(self):
        self.vehicleList = Model.vehicles_list  # Используем общий список всех автомобилей

    def addSedan(self, brand, year_of_release, manufacturer):
        try:
            sedan = Model.Sedan(brand, year_of_release, manufacturer)
            self.vehicleList.append(sedan)
            return sedan.getInfo()
        except Exception as e:
            return f"Ошибка добавления седана: {str(e)}"

    def addSUV(self, brand, year_of_release, manufacturer):
        try:
            suv = Model.SUV(brand, year_of_release, manufacturer)
            self.vehicleList.append(suv)
            return suv.getInfo()
        except Exception as e:
            return f"Ошибка добавления внедорожника: {str(e)}"

    def listVehicles(self):
        vehicleList = self.vehicleList
        for vehicle in vehicleList:
            vehicle.toString()