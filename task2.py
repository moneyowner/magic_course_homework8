# Создайте класс Vehicle, представляющий транспортное средство.
# Этот класс должен содержать:

# Поля make, model и year.
# Метод get_info, возвращающий строку с информацией о транспортном средстве.

# Затем создайте подклассы Car и Motorcycle, которые расширяют класс Vehicle:
# Класс Car должен иметь поле number_of_doors и метод get_info,
# который добавляет информацию о количестве дверей.
# Класс Motorcycle должен иметь поле has_sidecar (True или False)
# и метод get_info, который указывает, есть ли у мотоцикла коляска.

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        return f"make: {self.make}, model: {self.model}, year: {self.year}"


class Car(Vehicle):
    def __init__(self, make, model, year, number_of_doors: int):
        super().__init__(make, model, year)
        self.number_of_doors = number_of_doors

    def get_info(self):
        return f"{super().get_info()}, number_of_doors: {self.number_of_doors}"


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, has_sidecar: bool):
        super().__init__(make, model, year)
        self.has_sidecar = has_sidecar

    def get_info(self):
        return f"{super().get_info()}, has_sidecar: {self.has_sidecar}"


if __name__ == "__main__":
    veh = Vehicle("Ford", "Focus", "2002")
    car = Car("Toyota", "Land Cruiser", 2009, 5)
    moto = Motorcycle("ZID", "Voshod", "1965", False)

    print(veh.get_info())
    print(car.get_info())
    print(moto.get_info())

