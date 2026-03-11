import Present
import os

class View:
    
    def __init__(self):
        self.presenter = Present.Presenter()
    
    def registerCar(self):
        brand = input("Введите марку машины: ")
        year_of_release = input("Введите год выпуска: ")
        manufacturer = input("Введите производителя: ")
        return self.presenter.addVehicle(brand, year_of_release, manufacturer)
    
    def start(self):
        os.system('cls' if os.name == 'nt' else 'clear')  # Очистка экрана
        print("\\nАвтомобильная регистрация\\nВыберите действие:\\n")
        print("1 - Зарегистрировать машину")
        print("2 - Просмотреть список зарегистрированных автомобилей")
        print("3 - Выход")
        
        while True:
            try:
                choice = int(input("Ваш выбор: "))
            except ValueError:
                print("Нужно ввести число!")
                continue
                
            match(choice):
                case 1:
                    result = self.registerCar()
                    print(result)
                    input("Нажмите Enter для продолжения...")
                    self.start()
                    
                case 2:
                    self.presenter.listVehicles()
                    input("Нажмите Enter для возвращения в меню...")
                    self.start()
                    
                case 3:
                    print("Завершение работы.")
                    break
                
                case _:
                    print("Некорректный ввод. Попробуйте снова.")
                    continue