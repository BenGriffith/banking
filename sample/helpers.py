import json
import pathlib
import jsonpickle
from logs import log

def choice_int():
    '''
    Capture user input as an integer
    '''
    try:
        return int(input(">>> "))
    except ValueError:
        return

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
    Action = 1 is for customer
    Action != 1 is for employee
    '''

    if action == 1:

        try:
            print("What is your first name? ")
            name = choice_text().strip().upper()
            validate_name(name)
            return name
        except ValueError:
            log.logging.info("first_name(): customer first name value invalid")
            print("First Name must contain A to Z characters and cannot be empty. Please try again.")
            return first_name(1)

    else:

        try:
            print("What is the employee's first name? ")
            name = choice_text().strip().upper()
            validate_name(name)
            return name
        except ValueError:
            log.logging.info("first_name(): employee first name value invalid")
            print("First Name must contain A to Z characters and cannot be empty. Please try again.")
            return first_name()

def middle_name(action=None):
    '''
    Prompts user to input value for middle name
    Action = 1 is for customer
    Action != 1 is for employee
    '''

    if action == 1:

        try:
            print("What is your middle name? ")
            name = choice_text().strip().upper()
            validate_name(name)
            return name
        except ValueError:
            log.logging.info("middle_name(): customer middle name value invalid")
            print("Middle name must contain A to Z characters and cannot empty. Please try again.")
            return middle_name(1)

    else:

        try:
            print("What is the employee's middle name? ")
            name = choice_text().strip().upper()
            validate_name(name)
            return name
        except ValueError:
            log.logging.info("middle_name(): employee middle name value invalid")
            print("Middle name must contain A to Z characters and cannot empty. Please try again.")
            return middle_name()

def last_name(action=None, update="N"):
    '''
    Prompts user to input value for last name
    Action = 1 is for customer
    Action != 1 is for employee
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
            log.logging.info("last_name(): customer last name value invalid")
            print("Last name must contain A to Z characters and cannot be empty. Please try again.")
            return last_name(1)

    else:

        try:
            print("What is the employee's last name? ")
            name = choice_text().strip().upper()
            validate_name(name)
            return name
        except ValueError:
            log.logging.info("last_name(): employee last name value invalid")
            print("Last name must contain A to Z characters and cannot be empty. Please try again.")
            return last_name()

def ssn(action=None):
    '''
    Prompts user to input value for SSN
    Action = 1 is for customer
    Action != 1 is for employee
    '''

    if action == 1:

        try:
            print("What is your SSN (Please exclude dashes)? ")
            user_ssn = choice_text().strip()
            validate_ssn(user_ssn)
            return user_ssn
        except ValueError:
            log.logging.info("ssn(): customer ssn value invalid")
            print("SSN cannot contain letters, be empty or be less than 9 characters. Please try again.")
            return ssn(1)
    
    else:

        try:
            print("What is the employee's SSN (Please exclude dashes)? ")
            user_ssn = choice_text().strip()
            validate_ssn(user_ssn)
            return user_ssn
        except ValueError:
            log.logging.info("ssn(): employee ssn value invalid")
            print("SSN cannot contain letters, be empty or be less than 9 characters. Please try again.")
            return ssn()

def street_address(action=None, update="N"):
    '''
    Prompts user to input value for street address
    Action = 1 is for customer
    Action != 1 is for employee
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
            log.logging.info("street_address(): customer address value invalid")
            print("Street address cannot be empty. Please try again.")
            return street_address(1)

    else:

        try:
            print("What is the employee's street address? ")
            address = choice_text().strip().upper()
            validate_address(address)
            return address
        except ValueError:
            log.logging.info("street_address(): employee address value invalid")
            print("Street address cannot be empty. Please try again.")
            return street_address()

def city(action=None, update="N"):
    '''
    Prompts user to input value for city
    Action = 1 is for customer
    Action != 1 is for employee
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
            log.logging.info("city(): customer city value invalid")
            print("City cannot be empty. Please try again.")
            return city(1)

    else:

        try:
            print("What is the employee's city? ")
            user_city = choice_text().strip().upper()
            validate_city_state(user_city)
            return user_city
        except ValueError:
            log.logging.info("city(): employee city value invalid")
            print("City cannot be empty. Please try again.")
            return city()

def state(action=None, update="N"):
    '''
    Prompts user to input value for state
    Action = 1 is for customer
    Action != 1 is for employee
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
            log.logging.info("state(): customer state value invalid")
            print("State cannot be empty. Please try again.")
            return state(1)

    else:

        try:
            print("What is your state? ")
            user_state = choice_text().strip().upper()
            validate_city_state(user_state)
            return user_state
        except:
            log.logging.info("state(): employee state value invalid")
            print("State cannot be empty. Please try again.")
            return state()

def zip_code(action=None, update="N"):
    '''
    Prompts user to input value for zip code
    Action = 1 is for customer
    Action != 1 is for employee
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
            log.logging.info("zip_code(): customer zip code value invalid")
            print("Zip code can only contain numbers and cannot be empty. Please try again.")
            return zip_code(1)

    else:

        try:
            print("What is the employee's zip code? ")
            user_zip_code = choice_text().strip()
            validate_zip(user_zip_code)
            return user_zip_code
        except ValueError:
            log.logging.info("zip_code(): employee zip code value invalid")
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
        log.logging.info("pin(): customer pin value invalid")
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
        log.logging.info("salary(): employee salary value invalid")
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
        log.logging.info("supervisor(): employee supervisor value invalid")
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
            # Decode person object
            old_person = jsonpickle.decode(i)

            # If match found, remove old encoded person object and replace with new encoded person object
            if old_person.ssn == person.ssn:
                idx = temp.index(i)
                temp.pop(idx)
                new_person = jsonpickle.encode(person)
                temp.append(new_person)

    write_json(filename, data)

def read_json_accounts(filename, ssn):
    '''
    Read JSON file for particular customer and print all associated accounts (checking and savings)
    '''

    with open(filename, "r") as json_file:
        data = json.load(json_file)
        stem = pathlib.Path(filename).stem

        accounts = data[stem]

        for account in accounts:
            account = jsonpickle.decode(account)
            if account.ssn == ssn:
                print("Account Number is {} ({}): {}".format(account.account_number, account.account_type, account.balance))

def update_json_account(filename, ssn, account_number, amount, action):
    '''
    Read JSON file for particular account and update the account amount (deposit or withdraw) based on action
    '''

    with open(filename, "r") as json_file:
        data = json.load(json_file)
        stem = pathlib.Path(filename).stem

        accounts = data[stem]

        for account in accounts:

            # Decode account object
            old_account = jsonpickle.decode(account)

            # If match found, remove old encoded account object and replace with new encoded account object
            if old_account.ssn == ssn and old_account.account_number == account_number:
                # Deposit
                if action == 1:
                    old_account.deposit = amount

                # Withdraw
                if action == 2:
                    old_account.withdrawal = amount

                idx = accounts.index(account)
                accounts.pop(idx)
                new_account = jsonpickle.encode(old_account)
                accounts.append(new_account)

        write_json(filename, data)

                