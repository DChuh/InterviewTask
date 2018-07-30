import json

#constants
# ServiceForVacation is a number of years of service to accrue vacation of VacationDays duration
SERVICE_FOR_VACATION = 1
VACATION_DAYS = 5
FILE_LOCATION = "employees_data_set.json"

# Short representation of emploee type
EMPLOYEE_REPRESENTATION = {"fulltime": "FT",
                              "contractor": "C",
                              "temporary": "T"}

class Employee(object):

    def __init__(self, employee_type, employee_name, employee_longevity):

        self.__employee_name = employee_name
        self.__employee_longevity = employee_longevity
        self.__type = employee_type

    def get_name(self):
        return self.__employee_name

    def get_duration(self):
        return self.__employee_longevity

    def get_type(self):
        return self.__type

    def get_vacation(self):
        return None

    def print_brief(self):
        print("Name: {}[{}], Duration: {} years, Vacation Accrued: {} {}"
              "".format(self.get_name(),
                        EMPLOYEE_REPRESENTATION[self.get_type()],
                        self.get_duration(),
                        self.get_vacation(),
                        "days" if self.get_vacation() else ""))

class Factory(Employee):

    def __new__(self, type, *args):
        if type == "fulltime":
            return Fulltime(type, *args)
        elif type == "contractor":
            return Contractor(type, *args)
        elif type == "temporary":
            return Temporary (type, *args)
        else:
            raise AssertionError("Wrong employee type")

class Fulltime(Employee):
    def __init__(self, *args):
        super().__init__(*args)
    def get_vacation(self):
        vacation_accrued = str(self.get_duration() // SERVICE_FOR_VACATION * VACATION_DAYS)
        return vacation_accrued

class Contractor(Employee):
    def __init__(self, *args):
        super().__init__(*args)

class Temporary(Employee):
    def __init__(self, *args):
        super().__init__(*args)

# open json data set file and save it's representation
with open(FILE_LOCATION) as data_set_file:
    employee_json_list = json.load(data_set_file)

list_of_employees = []

# add every new employee form json to the employees list
for employee in employee_json_list:
    new_mem = Factory(employee["Type"], employee["Name"], employee["Duration"],)
    list_of_employees.append(new_mem)

# print employee brief information
for employee in list_of_employees:
    employee.print_brief()


