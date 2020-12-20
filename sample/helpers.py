import json
import pathlib
import jsonpickle

def choice_int():
    '''
    Capture user input as an integer
    '''

    return int(input(">>> "))

def choice_text():
    '''
    Capture user input as text
    '''

    return input(">>> ")

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

    if not isinstance(salary, int):
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
            print("What is your first name? ")
            name = choice_text().strip().upper()
            validate_name(name)
            return name
        except ValueError:
            # logger
            print("First Name must contain A to Z characters and cannot be empty. Please try again.")
            return first_name(1)

    else:

        try:
            print("What is the employee's first name? ")
            name = choice_text().strip().upper()
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
            print("What is your middle name? ")
            name = choice_text().strip().upper()
            validate_name(name)
            return name
        except ValueError:
            # logger
            print("Middle name must contain A to Z characters and cannot empty. Please try again.")
            return middle_name(1)

    else:

        try:
            print("What is the employee's middle name? ")
            name = choice_text().strip().upper()
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
                print("What is your new last name? ")
                name = choice_text().strip().upper()
            else:
                print("What is your last name? ")
                name = choice_text().strip().upper()
            validate_name(name)
            return name
        except ValueError:
            # logger
            print("Last name must contain A to Z characters and cannot be empty. Please try again.")
            return last_name(1)

    else:

        try:
            print("What is the employee's last name? ")
            name = choice_text().strip().upper()
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
            print("What is your SSN (Please exclude dashes)? ")
            user_ssn = choice_text().strip()
            validate_ssn(user_ssn)
            return user_ssn
        except ValueError:
            # logger
            print("SSN cannot contain letters, be empty or be less than 9 characters. Please try again.")
            return ssn(1)
    
    else:

        try:
            print("What is the employee's SSN (Please exclude dashes)? ")
            user_ssn = choice_text().strip()
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
                print("What is your new street address? ")
                address = choice_text().strip().upper()
            else:
                print("What is your street address? ")
                address = choice_text().strip().upper()
            validate_address(address)
            return address
        except ValueError:
            # logger
            print("Street address cannot be empty. Please try again.")
            return street_address(1)

    else:

        try:
            print("What is the employee's street address? ")
            address = choice_text().strip().upper()
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
                print("What is your new city? ")
            else:
                print("What is your city? ")
            user_city = choice_text().strip().upper()
            validate_city_state(user_city)
            return user_city
        except ValueError:
            # logger
            print("City cannot be empty. Please try again.")
            return city(1)

    else:

        try:
            print("What is the employee's city? ")
            user_city = choice_text().strip().upper()
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
                print("What is your new state? ")
            else:
                print("What is your state? ")
            user_state = choice_text().strip().upper()
            validate_city_state(user_state)
            return user_state
        except:
            # logger
            print("State cannot be empty. Please try again.")
            return state(1)

    else:

        try:
            print("What is your state? ")
            user_state = choice_text().strip().upper()
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
                print("What is your new zip code? ")
                user_zip_code = choice_text().strip()
            else:
                print("What is your zip code? ")
                user_zip_code = choice_text().strip()
            validate_zip(user_zip_code)
            return user_zip_code
        except ValueError:
            # logger
            print("Zip code can only contain numbers and cannot be empty. Please try again.")
            return zip_code(1)

    else:

        try:
            print("What is the employee's zip code? ")
            user_zip_code = choice_text().strip()
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
        print("What is your new email address? ")
        email = choice_text().strip().upper()
    else:
        print("What is your email address? ")
        email = choice_text().strip().upper()
    
    return email

def pin(update="N"):
    '''
    Prompts user to input value for PIN
    '''

    try:
        if update == "Y":
            print("What is your new PIN? ")
        else:
            print("What is your PIN? ")
        user_pin = choice_text().strip()
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
        print("What is the employee salary? ")
        employee_salary = choice_int()
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

    print("What is the employee's department? ")
    dept = choice_text().strip().upper()
    return dept

def supervisor():
    '''
    Prompts user to input supervisor
    '''

    try:
        print("Who is the employee's supervisor? ")
        lead = choice_text().strip().upper()
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

def read_json_accounts(filename, ssn):


    with open(filename, "r") as json_file:
        data = json.load(json_file)
        stem = pathlib.Path(filename).stem

        accounts = data[stem]

        for account in accounts:
            account = jsonpickle.decode(account)
            if account.ssn == ssn:
                print("Account Number is {} ({}): {}".format(account.account_number, account.account_type, account.balance))

def update_json_account(filename, ssn, account_number, amount, action):

    with open(filename, "r") as json_file:
        data = json.load(json_file)
        stem = pathlib.Path(filename).stem

        accounts = data[stem]

        for account in accounts:
            account_decoded = jsonpickle.decode(account)
            if account_decoded.ssn == ssn and account_decoded.account_number == account_number:
                if action == 1:
                    account_decoded.deposit = amount

                if action == 2:
                    account_decoded.withdrawal = amount

                idx = accounts.index(account)
                accounts.pop(idx)
                account_new = jsonpickle.encode(account_decoded)
                accounts.append(account_new)

        write_json(filename, data)

                