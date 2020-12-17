
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
    Validate the location entered contains A to Z characters and is not empty
    '''

    if not location.isalpha():
        raise ValueError

    if location == '':
        raise ValueError

def validate_zip(zip_code):
    '''
    Validate the zip code does not contain letters and is not empty
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

def first_name():
    '''
    Prompts user to input value for first name
    '''

    try:
        name = input("What is your first name? ")
        validate_name(name)
        return name
    except ValueError:
        # logger
        print("First Name must contain A to Z characters and cannot be empty. Please try again.")
        first_name()

def middle_name():
    '''
    Prompts user to input value for middle name
    '''

    try:
        name = input("What is your middle name? ")
        validate_name(name)
        return name
    except ValueError:
        # logger
        print("Middle name must contain A to Z characters and cannot empty. Please try again.")
        middle_name()

def last_name():
    '''
    Prompts user to input value for last name
    '''

    try:
        name = input("What is your last name? ")
        validate_name(name)
        return name
    except ValueError:
        # logger
        print("Last name must contain A to Z characters and cannot be empty. Please try again.")
        last_name()

def ssn():
    '''
    Prompts user to input value for SSN
    '''

    try:
        user_ssn = input("What is your SSN? ")
        validate_ssn(user_ssn)
        return user_ssn
    except ValueError:
        # logger
        print("SSN cannot contain letters or be empty. Please try again.")
        ssn()

def street_address():
    '''
    Prompts user to input value for street address
    '''

    try:
        address = input("What is your street address? ")
        validate_address(address)
        return address
    except ValueError:
        # logger
        print("Street address cannot be empty. Please try again.")
        street_address()

def city():
    '''
    Prompts user to input value for city
    '''

    try:
        user_city = input("What is your city? ")
        validate_city_state(user_city)
        return user_city
    except ValueError:
        # logger
        print("City must contain A to Z characters and cannot be empty. Please try again.")
        city()

def state():
    '''
    Prompts user to input value for state
    '''

    try:
        user_state = input("What is your state? ")
        validate_city_state(user_state)
        return user_state
    except:
        # logger
        print("State must contain A to Z characters and cannot be empty. Please try again.")
        state()

def zip_code():
    '''
    Prompts user to input value for zip code
    '''

    try:
        user_zip_code = input("What is your zip code? ")
        validate_zip(user_zip_code)
        return user_zip_code
    except ValueError:
        # logger
        print("Zip code cannot contain letters or be empty. Please try again.")
        zip_code()

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
    user_pin = ''

    try:
        user_pin = input("What is your PIN? ")
        validate_pin(user_pin)
        return user_pin
    except ValueError:
        # logger
        print("PIN must be 4 characters and cannot be empty. Please try again.")
        pin()