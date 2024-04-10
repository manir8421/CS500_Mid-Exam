from abc import ABC, abstractmethod
from enum import Enum
from typing import List, Dict

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

class ConstructionCompanyType(Enum):
    GENERAL_CONTRACTOR = 1
    SUBCONTRACTOR = 2
    CONSTRUCTION_MANAGER = 3


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

    def remove_employee(self, employee_name: str) -> None:
        self.__employees = [e for e in self.__employees if e.employee_name != employee_name]

    def get_top_five_employees(self) -> list[Employee]:
        sorted_employees = sorted(self.__employees, key=lambda e: e.annual_income, reverse=True)
        return sorted_employees[:5]

    def get_employee(self, employee_id: int) -> Employee:
        for employee in self.__employees:
            if employee.employee_id == employee_id:
                return employee
        raise ValueError(f"Employee with ID {employee_id} not found")

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

    def remove_employee(self, employee_name: str) -> None:
        self.__employees = [e for e in self.__employees if e.employee_name != employee_name]

    def get_top_five_employees(self) -> list[Employee]:
        sorted_employees = sorted(self.__employees, key=lambda e: e.annual_income, reverse=True)
        return sorted_employees[:5]

    def get_employee(self, employee_id: int) -> Employee:
        for employee in self.__employees:
            if employee.employee_id == employee_id:
                return employee
        raise ValueError(f"Employee with ID {employee_id} not found")

    @property
    def company_name(self):
        return self.__company_name

    @property
    def employees(self):
        return self.__employees
    
class ConstructionCompany(Displayable):
    def __init__(self, company_name: str, category: ConstructionCompanyType):
        self.__company_name = company_name
        self.__category = category
        self.__buildings = []
    
    def add_building(self, building: Building):
        self.__buildings.append(building)
    
    def get_building_by_type(self) -> Dict[BuildingType, List[Building]]:
        buildings_by_type = {}
        for building in self.__buildings:
            if building.building_type not in buildings_by_type:
                buildings_by_type[building.building_type] = [building]
            else:
                buildings_by_type[building.building_type].append(building)
        return buildings_by_type
    
    def assign_employee_to_building(self, employee_id: int, building_type: BuildingType):
        employee = next((emp for emp in self.employees if emp.employee_id == employee_id), None)
        if not employee:
            raise ValueError(f"Employee with ID {employee_id} not found")
        for building in self.__buildings:
            if building.building_type == building_type:
                building.add_employee(employee)
                return
        raise ValueError(f"No building of type {building_type} found")
    
    def display(self):
        building_info = "\n".join([bld.display() for bld in self.__buildings])
        return (f"Construction Company Name: {self.__company_name}, "
                f"Type: {self.__category.name}\nBuildings:\n{building_info}")

    @property
    def employees(self):
        all_employees = []
        for building in self.__buildings:
            all_employees.extend(building.employees)
        return all_employees
        

def main():
    emp1 = Employee(1, "Green Lee", 75000)
    emp2 = Employee(2, "Steven Smith", 80000)
    emp3 = Employee(3, "Carl Hopper", 55000)
    emp4 = Employee(4, "Ken Yung", 60000)
    emp5 = Employee(5, "Jenny May", 90000)
    employees = [emp1, emp2, emp3, emp4, emp5]


    building = Building("Warehouse", 2500.0, BuildingType.WAREHOUSE, employees)
    company = Company("SFBU Corp", employees)


    print("Initial state of the building:")
    print(building)
    print("\nInitial state of the company:")
    print(company)


    building.remove_employee("Green Lee")
    company.remove_employee("Steven Smith")


    print("\nAfter removing employees:")
    print("Building:")
    print(building)
    print("Company:")
    print(company)


    print("\nTop five employees in the building:")
    for emp in building.get_top_five_employees():
        print(emp)
    print("\nTop five employees in the company:")
    for emp in company.get_top_five_employees():
        print(emp)


    print("\nRetrieving a specific employee from the building and company:")
    try:
        print("Building:", building.get_employee(3))
        print("Company:", company.get_employee(3))
    except ValueError as e:
        print(e)

    construction_company = ConstructionCompany("BuildItRight Inc.", ConstructionCompanyType.GENERAL_CONTRACTOR)
    
    construction_company.add_building(building)
    

    try:
        construction_company.assign_employee_to_building(3, BuildingType.WAREHOUSE)
    except ValueError as e:
        print(e)

    print("\nBuildings by type:")
    buildings_by_type = construction_company.get_building_by_type()
    for building_type, buildings in buildings_by_type.items():
        print(f"{building_type}:")
        for bld in buildings:
            print(bld.display())

if __name__ == "__main__":
    main()
