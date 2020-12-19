import json
import pathlib
import jsonpickle

def choice():
    '''
    Capture user input
    '''

    return int(input(">>> "))

def main_menu_options():
    print("Welcome to the World Bank!")
    print("Customers, please press 1")
    print("Employees, please press 2")

def menu_customer_options():
    print("Customer Registration, please press 1")
    print("Existing Customer, please press 2")
    print("Previous Menu, please press 0")

def menu_employee_options():
    print("Employee Registration, please press 1")
    print("Existing Employee, please press 2")
    print("Previous Menu, please press 0")  

def validate_name(name):
    '''
    Validate the name entered contains A to Z characters and is not empty
    '''

    if not name.isalpha():
        raise ValueError

    if name == '':
        raise ValueError

def validate_ssn(ssn):
    '''
    Validate the SSN entered does not contain letters, is not empty and is not less than 9 characters
    '''

    if not ssn.isdecimal():
        raise ValueError

    if ssn == '':
        raise ValueError

    if len(ssn) < 9:
        raise ValueError

def validate_address(address):
    '''
    Validate the address entered is not empty
    '''

    if address == '':
        raise ValueError

def validate_city_state(location):
    '''
    Validate the location is not empty
    '''

    if location == '':
        raise ValueError

def validate_zip(zip_code):
    '''
    Validate the zip code contains only numbers and is not empty
    '''

    if not zip_code.isdecimal():
        raise ValueError

    if zip_code == '':
        raise ValueError

def validate_pin(pin):
    '''
    Validate the pin is not less than 4 characters and is not empty
    '''

    if len(pin) < 4:
        raise ValueError

    if pin == '':
        raise ValueError

def validate_salary(salary):
    '''
    Validate the salary contains only numbers and is not empty
    '''

    if not salary.isdecimal():
        raise ValueError

    if salary == '':
        raise ValueError

def validate_lead(supervisor):
    '''
    Validate supervisor is not empty
    '''

    if supervisor == '':
        raise ValueError

def first_name(action=None):
    '''
    Prompts user to input value for first name
    '''

    if action == 1:

        try:
            name = input("What is your first name? ")
            validate_name(name)
            return name
        except ValueError:
            # logger
            print("First Name must contain A to Z characters and cannot be empty. Please try again.")
            return first_name(1)

    else:

        try:
            name = input("What is the employee's first name? ")
            validate_name(name)
            return name
        except ValueError:
            # logger
            print("First Name must contain A to Z characters and cannot be empty. Please try again.")
            return first_name()

def middle_name(action=None):
    '''
    Prompts user to input value for middle name
    '''

    if action == 1:

        try:
            name = input("What is your middle name? ")
            validate_name(name)
            return name
        except ValueError:
            # logger
            print("Middle name must contain A to Z characters and cannot empty. Please try again.")
            return middle_name(1)

    else:

        try:
            name = input("What is the employee's middle name? ")
            validate_name(name)
            return name
        except ValueError:
            # logger
            print("Middle name must contain A to Z characters and cannot empty. Please try again.")
            return middle_name()

def last_name(action=None, update="N"):
    '''
    Prompts user to input value for last name
    '''

    if action == 1:

        try:
            if update == "Y":
                name = input("What is your new last name? ")
            else:
                name = input("What is your last name? ")
            validate_name(name)
            return name
        except ValueError:
            # logger
            print("Last name must contain A to Z characters and cannot be empty. Please try again.")
            return last_name(1)

    else:

        try:
            name = input("What is the employee's last name? ")
            validate_name(name)
            return name
        except ValueError:
            # logger
            print("Last name must contain A to Z characters and cannot be empty. Please try again.")
            return last_name()

def ssn(action=None):
    '''
    Prompts user to input value for SSN
    '''

    if action == 1:

        try:
            user_ssn = input("What is your SSN (Please exclude dashes)? ")
            validate_ssn(user_ssn)
            return user_ssn
        except ValueError:
            # logger
            print("SSN cannot contain letters, be empty or be less than 9 characters. Please try again.")
            return ssn(1)
    
    else:

        try:
            user_ssn = input("What is the employee's SSN (Please exclude dashes)? ")
            validate_ssn(user_ssn)
            return user_ssn
        except ValueError:
            # logger
            print("SSN cannot contain letters, be empty or be less than 9 characters. Please try again.")
            return ssn()

def street_address(action=None, update="N"):
    '''
    Prompts user to input value for street address
    '''

    if action == 1:

        try:
            if update == "Y":
                address = input("What is your new street address? ")
            else:
                address = input("What is your street address? ")
            validate_address(address)
            return address
        except ValueError:
            # logger
            print("Street address cannot be empty. Please try again.")
            return street_address(1)

    else:

        try:
            address = input("What is the employee's street address? ")
            validate_address(address)
            return address
        except ValueError:
            # logger
            print("Street address cannot be empty. Please try again.")
            return street_address()

def city(action=None, update="N"):
    '''
    Prompts user to input value for city
    '''

    if action == 1:

        try:
            if update == "Y":
                user_city = input("What is your new city? ")
            else:
                user_city = input("What is your city? ")
            validate_city_state(user_city)
            return user_city
        except ValueError:
            # logger
            print("City cannot be empty. Please try again.")
            return city(1)

    else:

        try:
            user_city = input("What is the employee's city? ")
            validate_city_state(user_city)
            return user_city
        except ValueError:
            # logger
            print("City cannot be empty. Please try again.")
            return city()

def state(action=None, update="N"):
    '''
    Prompts user to input value for state
    '''

    if action == 1:

        try:
            if update == "Y":
                user_state = input("What is your new state? ")
            else:
                user_state = input("What is your state? ")
            validate_city_state(user_state)
            return user_state
        except:
            # logger
            print("State cannot be empty. Please try again.")
            return state(1)

    else:

        try:
            user_state = input("What is your state? ")
            validate_city_state(user_state)
            return user_state
        except:
            # logger
            print("State cannot be empty. Please try again.")
            return state()

def zip_code(action=None, update="N"):
    '''
    Prompts user to input value for zip code
    '''

    if action == 1:

        try:
            if update == "Y":
                user_zip_code = input("What is your new zip code? ")
            else:
                user_zip_code = input("What is your zip code? ")
            validate_zip(user_zip_code)
            return user_zip_code
        except ValueError:
            # logger
            print("Zip code can only contain numbers and cannot be empty. Please try again.")
            return zip_code(1)

    else:

        try:
            user_zip_code = input("What is the employee's zip code? ")
            validate_zip(user_zip_code)
            return user_zip_code
        except ValueError:
            # logger
            print("Zip code can only contain numbers and cannot be empty. Please try again.")
            return zip_code()

def email(update="N"):
    '''
    Prompts user to input value for email
    '''
    
    if update == "Y":
        email = input("What is your new email address? ")
    else:
        email = input("What is your email address? ")
    
    return email

def pin(update="N"):
    '''
    Prompts user to input value for PIN
    '''

    try:
        if update == "Y":
            user_pin = input("What is your new PIN? ")
        else:
            user_pin = input("What is your PIN? ")
        validate_pin(user_pin)
        return user_pin
    except ValueError:
        # logger
        print("PIN must be 4 characters and cannot be empty. Please try again.")
        return pin()

def salary():
    '''
    Prompts user to input salary
    '''

    try:
        employee_salary = input("What is the employee salary? ")
        validate_salary(employee_salary)
        return employee_salary
    except ValueError:
        # logger
        print("Salary can only contain numbers and cannot be empty. Please try again.")
        return salary()

def department():
    '''
    Prompts user to input department
    '''

    dept = input("What is the employee's department? ")
    return dept

def supervisor():
    '''
    Prompts user to input supervisor
    '''

    try:
        lead = input("Who is the employee's supervisor? ")
        validate_lead(lead)
        return lead
    except:
        # logger
        print("Supervisor cannot be empty. Please try again.")
        return supervisor()

def write_json(filename, data):
    '''
    Write to JSON file
    '''

    with open(filename, "w") as json_file:
        json.dump(data, json_file, indent=4)

def read_append_json(filename, data_dict):
    '''
    Read JSON file and append data before invoking write_json()
    '''
    
    with open(filename, "r") as json_file:
        data = json.load(json_file)
        stem = pathlib.Path(filename).stem
        
        temp = data[stem]
        temp.append(data_dict)

    write_json(filename, data)

def read_update_json(filename, person):
    '''
    Read JSON file and update data before invoking write_json()
    '''

    with open(filename, "r") as json_file:
        data = json.load(json_file)
        stem = pathlib.Path(filename).stem

        temp = data[stem]

        for i in temp:
            j = jsonpickle.decode(i)
            if j.ssn == person.ssn:
                idx = temp.index(i)
                temp.pop(idx)
                j = jsonpickle.encode(person)
                temp.append(j)

    write_json(filename, data)
        

