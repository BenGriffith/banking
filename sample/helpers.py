
def choice():
    '''
    Capture user input
    '''

    return int(input(">>> "))

def menu_question(*args):
    '''
    Provide structure to menu questions
    '''

    return input("What {} {} {}? ".format(args[0], args[1], args[2])).upper()

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
    Validate the SSN entered does not contain letters and is not empty
    '''

    if not ssn.isdecimal():
        raise ValueError

    if ssn == '':
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

def last_name(action=None):
    '''
    Prompts user to input value for last name
    '''

    if action == 1:

        try:
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
            user_ssn = input("What is your SSN? ")
            validate_ssn(user_ssn)
            return user_ssn
        except ValueError:
            # logger
            print("SSN cannot contain letters or be empty. Please try again.")
            return ssn(1)
    
    else:

        try:
            user_ssn = input("What is the employee's SSN? ")
            validate_ssn(user_ssn)
            return user_ssn
        except ValueError:
            # logger
            print("SSN cannot contain letters or be empty. Please try again.")
            return ssn()

def street_address(action=None):
    '''
    Prompts user to input value for street address
    '''

    if action == 1:

        try:
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

def city(action=None):
    '''
    Prompts user to input value for city
    '''

    if action == 1:

        try:
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

def state(action=None):
    '''
    Prompts user to input value for state
    '''

    if action == 1:

        try:
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

def zip_code(action=None):
    '''
    Prompts user to input value for zip code
    '''

    if action == 1:

        try:
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

def email():
    '''
    Prompts user to input value for email
    '''
    
    email = input("What is your email address? ")
    return email

def pin():
    '''
    Prompts user to input value for PIN
    '''

    try:
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