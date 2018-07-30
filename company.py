
#constants
# ServiceForVacation is a number of years of service to accrue vacation of VacationDays duration
SERVICE_FOR_VACATION = 1
VACATION_DAYS = 5

# Short representation of emploee type
EmployeeTypeRepresentation = {"fulltime": "FT",
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
        print("Name: {}[{}], Duration: {} years, Vacation Accrued: {} {}."
              "".format(self.get_name(),
                        EmployeeTypeRepresentation[self.get_type()],
                        self.get_duration(),
                        self.get_vacation(),
                        " days" if self.get_vacation() else ""))

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


new_mem = Factory("temporary","Andy", 1.5)
new_mem.print_brief()
new_mem = Factory("contractor","John", 0.5)
new_mem.print_brief()
new_mem = Factory("fulltime","Myroslava", 2.5)
new_mem.print_brief()



