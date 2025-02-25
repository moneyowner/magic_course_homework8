# Создайте класс Employee, который инкапсулирует следующие данные:

# Приватные поля __name, __position, __salary.
# Методы set_name, set_position и set_salary для изменения значений
# этих полей (например, при повышении сотрудника).
# Ограничьте прямой доступ к __salary, добавив проверку,
# чтобы зарплату можно было изменить только через метод, например,
# при повышении. Запрещается устанавливать зарплату ниже текущего значения.

# Метод get_employee_info, который возвращает информацию о сотруднике в
# виде строки.%

class Employee:
    def __init__(self, name: str, position: str, salary: int):
        self.__name = name
        self.__position = position
        self.__salary = salary

    def set_name(self, new_name: str):
        self.__name = new_name
        return f"Имя сотрудника изменено: {new_name}"

    def set_position(self, new_position: str):
        self.__position = new_position

    def set_salary(self, new_salary: int, new_position: str):
        if self.__position == new_position:
            return f"Невозможно повысить ЗП без повышения должности"
        elif self.__salary >= new_salary:
            return  f"Невозможно повысить в должности без повышения ЗП"
        else:
            self.__salary = new_salary
            self.__position = new_position
            return f"Зарплата повышена {new_salary}"

    def get_employee_info(self):
        return f"name: {self.__name}, position: {self.__position}, salary: {self.__salary}"


if __name__ == "__main__":
    worker = Employee("Dmitry", "QA", 80000)

    print(worker.set_name("Dmitrii"))
    print(worker.set_salary(100000, "Middle QA"))
    print(worker.get_employee_info())
