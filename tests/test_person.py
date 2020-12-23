import pytest

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

###########################################################

def test_Customer():
    
    customer = Customer("John", "Arnold", "Huggins", "123456789", "123 Main Street", "Miami", "FL", "88393", "john@arnold.com", "abc123")

    assert customer.first == "John"
    assert customer.middle == "Arnold"
    assert customer.last == "Huggins"
    assert customer.ssn == "123456789"
    assert customer.street_address == "123 Main Street"
    assert customer.city == "Miami"
    assert customer.state == "FL"
    assert customer.zip_code == "88393"
    assert customer.email == "john@arnold.com"
    assert customer.pin == "abc123"

    customer.email = "john@development.com"
    assert customer.email == "john@development.com"

    customer.pin = "987def"
    assert customer.pin == "987def"

    customer.last = "Johnson"
    assert customer.last == "Johnson"

    with pytest.raises(AttributeError):
        customer.first = "Jack"

###########################################################

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

###########################################################

def test_Employee():
    
    employee = Employee("Bob", "Dell", "Schertz", "889224378", "123 First Ave", "Phoenix", "AZ", "10012", 10000, "Accounting", "Abby Walker")

    assert employee.first == "Bob"
    
    employee.salary = 15000
    assert employee.salary == 15000

    with pytest.raises(AttributeError):
        employee.dept = "Marketing"

    with pytest.raises(ValueError):
        employee.salary = -1000

###########################################################