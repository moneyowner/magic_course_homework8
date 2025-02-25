# Создайте классы для представления структуры магазина техники.

# Требования:

# Базовый класс Device, который будет представлять общие атрибуты
# для любой техники:

# атрибуты: brand, model, price.
# метод get_info(), который возвращает строку с кратким описанием устройства.
# Дочерние классы:

# Laptop с дополнительными атрибутами ram и storage.
# Smartphone с атрибутами camera_megapixels и battery_capacity.

# Каждый из классов должен переопределить метод get_info()
# для включения специфичной информации.
# Создайте класс Store, содержащий список устройств:

# Метод add_device(device), который добавляет устройство в магазин.
# Метод list_devices(), который выводит информацию обо всех устройствах.

class Device:
    def __init__(self, brand: str, model: str, price: int):
        self.brand = brand
        self.model = model
        self.prise = price

    def get_info(self):
        return f"brand: {self.brand}, model: {self.model}, price: {self.prise}"

    def __repr__(self):
        return f"brand: {self.brand}, model: {self.model}, price: {self.prise}"


class Laptop(Device):
    def __init__(self, brand: str, model: str, price: int, ram: str, storage: str):
        super().__init__(brand, model, price)
        self.ram = ram
        self.storage = storage

    def get_info(self):
        return f"{super().get_info()}, ram: {self.ram}, storage: {self.storage}"

    def __repr__(self):
        return f"{super().__repr__()}, ram: {self.ram}, storage: {self.storage}"


class Smartphone(Device):
    def __init__(self, brand: str, model: str, price: int, camera_megapixels: str, battery_capacity: str):
        super().__init__(brand, model, price)
        self.camera_megapixels = camera_megapixels
        self.battery_capacity = battery_capacity

    def get_info(self):
        return f"{super().get_info()}, camera_megapixels: {self.camera_megapixels}, battery_capacity: {self.battery_capacity}"

    def __repr__(self):
        return f"{super().__repr__()}, camera_megapixels: {self.camera_megapixels}, battery_capacity: {self.battery_capacity}"


class Store:
    def __init__(self, devices=None):
        if devices is None:
            devices = []
        self.__devices = devices

    def add_devices(self, device):
        if not isinstance(device, Device):
            raise ValueError
        self.__devices.append(device)

    def list_devices(self):
        list_of_devices = []
        for i in self.__devices:
            list_of_devices.append(i)
        return list_of_devices


if __name__ == "__main__":
    device1 = Device("JBL", "Headphones", 3000)
    laptop1 = Laptop("ACER", "NITRO-5", 55000, "Kingston Fury DDR4 8 GB", "SSD 512 GB")
    smartphone1 = Smartphone("Xiaomi", "Redmi 6", 15000, "30 Mgpx", "3000 mA/h")

    device_list = []
    store = Store(device_list)

    store.add_devices(smartphone1)
    store.add_devices(laptop1)
    store.add_devices(device1)

    print(store.list_devices())

