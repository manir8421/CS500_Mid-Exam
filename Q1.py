from abc import ABC, abstractmethod
from enum import Enum
from typing import List

class Displayable(ABC):
    @abstractmethod
    def display(self):
        pass

    def __str__(self):
        return self.display()


class BuildingType(Enum):
    WAREHOUSE = 1
    DISTRIBUTION_CENTER = 2
    FLEX_SPACE = 3
    MANUFACTURING_BUILDING = 4


class Employee(Displayable):
    def __init__(self, employee_id: int, employee_name: str, annual_income: float):
        self.__employee_id = employee_id
        self.__employee_name = employee_name
        self.__annual_income = annual_income
    
    def display(self):
        return f"ID: {self.__employee_id}, Name: {self.__employee_name}, Income: ${self.__annual_income}"

    @property
    def employee_id(self):
        return self.__employee_id
    
    @property
    def employee_name(self):
        return self.__employee_name

    @property
    def annual_income(self):
        return self.__annual_income


class Building(Displayable):
    def __init__(self, building_name: str, area: float, building_type: BuildingType, employees: List[Employee]):
        self.__building_name = building_name
        self.__area = area
        self.__building_type = building_type
        self.__employees = employees
    
    def display(self):
        employee_info = "\n".join([emp.display() for emp in self.__employees])
        return f"Building Name: {self.__building_name}, Area: {self.__area}, Type: {self.__building_type.name}\nEmployees:\n{employee_info}"

    def add_employee(self, employee: Employee):
        self.__employees.append(employee)
    
    @property
    def building_name(self):
        return self.__building_name

    @property
    def area(self):
        return self.__area

    @property
    def building_type(self):
        return self.__building_type.name

    @property
    def employees(self):
        return self.__employees

class Company(Displayable):
    def __init__(self, company_name: str, employees: List[Employee]):
        self.__company_name = company_name
        self.__employees = employees
    
    def display(self):
        employee_info = "\n".join([emp.display() for emp in self.__employees])
        return f"Company Name: {self.__company_name}\nEmployees:\n{employee_info}"

    def add_employee(self, employee: Employee):
        self.__employees.append(employee)
    
    @property
    def company_name(self):
        return self.__company_name

    @property
    def employees(self):
        return self.__employees


def main():
    emp1 = Employee(1, "Green Lee", 75000)
    emp2 = Employee(2, "Steven Smith", 80000)
    emp3 = Employee(3, "Carl Hopper", 55000)
    emp4 = Employee(4, "Ken Yung", 60000)
    employees = [emp1, emp2, emp3, emp4]

    building1 = Building("Warehouse", 2500.0, BuildingType.WAREHOUSE, employees)


    company = Company("SFBU Corp", employees)

    print(building1)

    print("\n")
    print(company)

if __name__ == "__main__":
    main()
