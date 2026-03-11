import abc

# Базовый абстрактный класс Car
class Vehicle(abc.ABC):
    
    # Конструктор принимает марку автомобиля, год выпуска и производителя
    def __init__(self, brand, year_of_release, manufacturer):
        self.brand = brand                # марка авто (открытая переменная)
        self.__year_of_release = year_of_release   # закрытый атрибут года выпуска
        self.__manufacturer = manufacturer      # закрытый атрибут производителя
    
    # Геттеры для закрытых свойств
    def getYearOfRelease(self):
        return self.__year_of_release
    
    def getManufacturer(self):
        return self.__manufacturer
    
    @abc.abstractmethod
    def getInfo(self):
        pass
    
    @abc.abstractmethod
    def Type(self):
        pass
    
    @abc.abstractmethod
    def toString(self):
        pass

# Подкласс Sedan (седан), наследующий базовый класс Vehicle
class Sedan(Vehicle):
    def __init__(self, brand, year_of_release, manufacturer):
        super().__init__(brand, year_of_release, manufacturer)
    
    def getInfo(self):
        return f"Седан марки {self.brand}, выпущен в {self.getYearOfRelease()} г., производитель: {self.getManufacturer()}"
    
    def Type(self):
        return "седан"
    
    def toString(self):
        print(f"{self.Type()} {self.brand}, выпущенный в {self.getYearOfRelease()} г.")

# Подкласс SUV (кроссовер), наследующий базовый класс Vehicle
class SUV(Vehicle):
    def __init__(self, brand, year_of_release, manufacturer):
        super().__init__(brand, year_of_release, manufacturer)
    
    def getInfo(self):
        return f"Кроссовер марки {self.brand}, выпущен в {self.getYearOfRelease()} г., производитель: {self.getManufacturer()}"
    
    def Type(self):
        return "SUV"
    
    def toString(self):
        print(f"{self.Type()} {self.brand}, выпущенный в {self.getYearOfRelease()} г.")

# Списки автомобилей различных типов
vehicles_list = []
sedans_list = []
suvs_list = []