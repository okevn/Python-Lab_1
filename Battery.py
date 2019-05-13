"""
Створити клас “Батарея” котрий містить поля:
- ємність (міліампер-годин)
- напруга
- вага

Створити консольну програму мовою Python і написати клас <Назва_із_завдання> який міститиме:

Три додаткових поля, які найкраще описують даний клас Конструктор (із вказаними дефолтними значеннями) Деструктор
Метод, що повертає стрічкове представлення класу Статичне поле Статичний метод, що повертає значення статичного поля
В main() методі визначіть 3 об’єкти типу із завдання (з-за допомогою передачі різної кількості параметрів) та
виведіть інформацію про них з-за допомогою методу з пункту 4 в консоль
"""


class Battery:
    _amount_of_cycles = 0

    def __init__(self, capacity=0, voltage=0, weight=0, price=0, name="NONAME", manufacturer="NULL"):
        self.capacity = capacity
        self.voltage = voltage
        self.weight = weight
        self.price = price
        self.name = name
        self.manufacturer = manufacturer

    def __del__(self):
        print("Destructor " + self.name + " deleted")

    def __str__(self):
        return str(self.__dict__)

    @staticmethod
    def get_static_amount_of_cycles():
        return Battery._amount_of_cycles


def main():
    b1 = Battery(2500, 12, 120, 180, "ZR18650", "Sony")
    b2 = Battery(2700, 10, 130, 200, "25R", "Samsung")
    b3 = Battery(3000, 11, 140, 220, "WR100", "LG")
    print(b1)
    print(b2)
    print(b3)
    print(Battery.get_static_amount_of_cycles())

if __name__ == '__main__':
    main()
