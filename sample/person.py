import json
import pathlib
import jsonpickle

class Person:

    def __init__(self, first, middle, last, ssn, street_address, city, state, zip_code):
        self._first = first
        self._middle = middle
        self._last = last
        self._ssn = ssn
        self._street_address = street_address
        self._city = city
        self._state = state
        self._zip_code = zip_code

    @property
    def first(self):
        return self._first

    @property
    def middle(self):
        return self._middle

    @property
    def last(self):
        return self._last

    @last.setter
    def last(self, new_last):
        self._last = new_last

    @property
    def ssn(self):
        return self._ssn

    @property
    def street_address(self):
        return self._street_address

    @street_address.setter
    def street_address(self, new_address):
        self._street_address = new_address

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, new_city):
        self._city = new_city

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, new_state):
        self._state = new_state

    @property
    def zip_code(self):
        return self._zip_code

    @zip_code.setter
    def zip_code(self, new_zip_code):
        self._zip_code = new_zip_code

class Customer(Person):

    def __init__(self, first, middle, last, ssn, street_address, city, state, zip_code, email, pin):
        super().__init__(first, middle, last, ssn, street_address, city, state, zip_code)
        self._email = email
        self._pin = pin

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, new_email):
        self._email = new_email

    @property
    def pin(self):
        return self._pin

    @pin.setter
    def pin(self, new_pin):
        self._pin = new_pin

    @staticmethod
    def authentication(filename, ssn_last_4, pin):
        '''
        Reads JSON file and checks whether customer is valid
        '''

        with open(filename, "r") as json_file:
            data = json.load(json_file)
            stem = pathlib.Path(filename).stem
            customers = data[stem]

            # Using ssn and PIN check whether customer is valid or not
            for customer in customers:
                customer = jsonpickle.decode(customer)
                if str(customer.ssn[-4::]) == ssn_last_4 and customer.pin == pin:
                    return customer

            return None

class Employee(Person):
    
    def __init__(self, first, middle, last, ssn, street_address, city, state, zip_code, salary, dept, supervisor):
        super().__init__(first, middle, last, ssn, street_address, city, state, zip_code)
        self._salary = salary
        self._dept = dept
        self._supervisor = supervisor

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, new_salary):
        if new_salary <= 0:
            raise ValueError
        else:
            self._salary = new_salary

    @property
    def dept(self):
        return self._dept

    @property
    def supervisor(self):
        return self._supervisor

    @staticmethod
    def authentication(filename, ssn):
        '''
        Read JSON file and checks whether employee is valid
        '''

        with open(filename, "r") as json_file:
            data = json.load(json_file)
            stem = pathlib.Path(filename).stem
            employees = data[stem]

            # Using ssn check whether employee is valid or not
            for employee in employees:
                employee = jsonpickle.decode(employee)
                if employee.ssn[-4::] == ssn:
                    return employee

            return None