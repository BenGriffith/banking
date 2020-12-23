# -*- coding: utf-8 -*-
import time
import os
import helpers
import person
import bank
import jsonpickle
from logs import log

customers = "json/customers.json"
employees = "json/employees.json"
accounts = 'json/accounts.json'

def main_menu():
    '''
    Bank main menu options for customers and employees
    '''

    print("Welcome to the World Bank!")
    print("Customers, please press 1")
    print("Employees, please press 2")

    # Get user input
    menu_choice = helpers.choice_int()
    
    # User input determines next menu
    if menu_choice == 1:
        menu_customer()
    elif menu_choice == 2:
        menu_employee()
    else:
        log.logging.info("main_menu(): invalid option selected")
        print("The option selected is invalid. Please select either 1 or 2.\n")
        time.sleep(2)

        # Redirect user to main menu
        main_menu()

def menu_customer():
    '''
    Customer menu options for customer registration and existing customers
    '''

    print("Customer Registration, please press 1")
    print("Existing Customer, please press 2")
    print("Previous Menu, please press 0")

    # Get user input
    menu_choice = helpers.choice_int()

    # User input determines next menu
    if menu_choice == 1:
        menu_customer_new()
    elif menu_choice == 2:
        menu_customer_existing()
    elif menu_choice == 0:
        main_menu()
    else:
        log.logging.info("menu_customer(): invalid option selected")
        print("The option selected is invalid. Please select either 1, 2 or 0.\n")
        time.sleep(2)

        # Redirect to customer menu
        menu_customer()

def menu_employee():
    '''
    Employee menu options for employee registration and existing employees
    '''

    print("Employee Registration, please press 1")
    print("Existing Employee, please press 2")
    print("Previous Menu, please press 0")  

    # Get user input
    menu_choice = helpers.choice_int()

    # User input determines next menu
    if menu_choice == 1:
        menu_employee_new()
    elif menu_choice == 2:
        menu_employee_existing()
    elif menu_choice == 0:
        main_menu()
    else:
        log.logging.info("menu_employee(): invalid option selected")
        print("The option selected is invalid. Please select either 1, 2 or 0.\n")
        time.sleep(2)

        # Redirect to employee menu
        menu_employee()

def menu_customer_new():
    '''
    Customer registration
    '''

    first = helpers.first_name(1)
    middle = helpers.middle_name(1)
    last = helpers.last_name(1)
    ssn = helpers.ssn(1)
    street_address = helpers.street_address(1)
    city = helpers.city(1)
    state = helpers.state(1)
    zip_code = helpers.zip_code(1)
    email = helpers.email()
    pin = helpers.pin()

    # Instantiate customer object
    customer = person.Customer(
        first,
        middle,
        last,
        ssn,
        street_address,
        city,
        state,
        zip_code,
        email,
        pin
    )

    # Add customer object to customers.json
    helpers.read_append_json(customers, jsonpickle.encode(customer))
    log.logging.info("new customer ({} {}) registered".format(customer.first, customer.last))
    print("Thank you {} for registering with World Bank!".format(first.capitalize()))
    time.sleep(2)
    os.system("clear")

    # Redirect to main menu
    main_menu()

def menu_customer_existing(new_session="Y", customer=None):
    '''
    Existing customer menu
    '''
    
    # Prompt customer for SSN along with PIN and read customers.json to verify customer record exists
    if new_session == "Y":

        # Get customer input for SSN
        print("What are the last 4 digits of your SSN? ")
        ssn_last_4 = helpers.choice_text()

        # If input is empty
        if ssn_last_4 == '':
            log.logging.info("menu_customer_existing(): invalid value for SSN")
            print("Please enter the last four digits of your SSN.\n")
            time.sleep(2)
            menu_employee_existing()

        # Get customer input for PIN
        print("What is your PIN? ")
        pin = helpers.choice_text()

        # If input is empty
        if pin == '':
            log.logging.info("menu_customer_existing(): invalid value for PIN")
            print("Please enter your PIN.\n")
            time.sleep(2)
            menu_customer_existing()

        # Check to see whether SSN and PIN return valid customer record
        customer = person.Customer.authentication(customers, ssn_last_4, pin)

    # If customer record invalid
    if customer == None and new_session == "Y":
        log.logging.info("menu_customer_existing(): invalid customer record")
        print("Hmm, we weren't able to find you in the World Bank system. Please try again.\n")
        time.sleep(2)

        # Redirect to existing customer menu
        menu_customer_existing()
    else:
        print("\nHello, {} {}! Welcome to World Bank!".format(customer.first.capitalize(), customer.last.capitalize()))
        print("New Account(s), please press 1")
        print("Existing Account(s), please press 2")
        print("Update Profile, please press 3")
        print("Previous Menu, please press 0")

        # Get customer input
        menu_choice = helpers.choice_int()

        # Customer input determines next menu
        if menu_choice == 1:
            menu_new_accounts(customer)
        elif menu_choice == 2:
            menu_existing_accounts(customer)
        elif menu_choice == 3:
            menu_update_profile(customer)
        elif menu_choice == 0:
            menu_customer()
        else:
            log.logging.info("menu_customer_existing(): invalid option selected")
            print("The option selected is invalid. Please select either 1, 2, 3 or 0.\n")
            time.sleep(2)

            # Redirect to existing customer menu
            menu_customer_existing("N", customer)

def menu_employee_new():
    '''
    Employee registration
    '''

    first = helpers.first_name()
    middle = helpers.middle_name()
    last = helpers.last_name()
    ssn = helpers.ssn()
    street_address = helpers.street_address()
    city = helpers.city()
    state = helpers.state()
    zip_code = helpers.zip_code()
    salary = helpers.salary()
    dept = helpers.department()
    supervisor = helpers.supervisor()

    # Instantiate employee object
    employee = person.Employee(
        first,
        middle,
        last,
        ssn,
        street_address,
        city,
        state,
        zip_code,
        salary,
        dept,
        supervisor
    )

    # Add employee object to employees.json
    helpers.read_append_json(employees, jsonpickle.encode(employee))
    log.logging.info("new employee ({} {}) registered".format(employee.first, employee.last))
    print("Welcome {} to the wonderful team at World Bank!".format(first.capitalize()))
    time.sleep(2)
    os.system("clear")

    # Redirect to main menu
    main_menu()

def menu_employee_existing():
    '''
    Existing employee menu
    '''

    # Get employee input for SSN
    print("What are the last 4 digits of the employee's SSN? ")
    ssn_last_4 = helpers.choice_text()

    # If input is empty
    if ssn_last_4 == '':
        log.logging.info("menu_employee_existing(): invalid value for SSN")
        print("Please enter the last four digits of the employee's SSN.\n")
        time.sleep(2)
        menu_employee_existing()

    # Check to see whether SSN return valid employee record
    employee = person.Employee.authentication(employees, ssn_last_4)

    # If employee record invalid
    if employee == None:
        log.logging.info("menu_employee_existing(): invalid employee record")
        print("Hmm, we weren't able to find you in the World Bank system. Please try again.\n")
        time.sleep(2)

        # Redirect to existing employee menu
        menu_employee_existing()
    else:
        print("Hello! Welcome to World Bank Employee Portal!")
        print("Employee: {} {}".format(employee.first, employee.last
        ))
        print("Department: {}".format(employee.dept))
        print("Supervisor: {}".format(employee.supervisor))
        print("Salary: {}".format(employee.salary))
        print("To update {} {} salary, please press 1".format(employee.first.capitalize(), employee.last.capitalize()))
        print("To return to the main menu, please press 0")

        # Get employee input
        menu_choice = helpers.choice_int()

        # Update salary
        if menu_choice == 1:
            try:

                # Get employee input for new salary
                print("What is the new salary? ")
                new_salary = helpers.choice_int()

                if new_salary == None:
                    new_salary = 0

                # Update employee salary
                employee.salary = new_salary

                # Update employees.json to reflect salary update
                helpers.read_update_json(employees, employee)

                print("Thank you for updating {} {} salary!\n".format(employee.first.capitalize(), employee.last.capitalize()))
                time.sleep(2)
                main_menu()           
            except ValueError:
                log.logging.info("menu_employee_existing(): invalid value for salary")
                print("Invalid salary. Returning to main menu.\n")
                time.sleep(2)

                # Redirect to main menu
                main_menu()
        elif menu_choice == 0:
            main_menu()
        else:
            log.logging.info("menu_employee_existing(): invalid option selected")
            print("The option selected is invalid. Returning to main menu.\n")
            time.sleep(2)

            # Redirect to main menu
            main_menu()

def menu_new_accounts(customer):
    '''
    Account creation menu
    '''

    print("New Checking Account, please press 1")
    print("New Savings Account, please press 2")

    # Get customer input
    menu_choice = helpers.choice_int()

    # Checking account
    if menu_choice == 1:

        # Get customer input
        print("How much will the initial deposit be for? ")
        initial_deposit = helpers.choice_float()

        # Check for initial deposit
        if initial_deposit == None:
            initial_deposit = 1

        if initial_deposit < 0:
            log.logging.info("initial_deposit checking: invalid deposit value")
            print("Please enter a value greater than 0.\n")
            menu_new_accounts(customer)

        # Instantiate checking account object
        checking_account = bank.CheckingAccount(
            customer.ssn,
            initial_deposit
        )

        # Add checking account record to accounts.json
        helpers.read_append_json(accounts, jsonpickle.encode(checking_account))

        print("Thank you {} for creating a checking account with World Bank!".format(customer.first.capitalize()))
        print("Your account number is {}".format(checking_account.account_number))
        print("Your balance is {}\n".format(checking_account.balance))        
        print("You will be redirected to the previous menu shortly.")
        time.sleep(10)
        os.system("clear")

        # Redirect to existing customer menu
        menu_customer_existing("N", customer)

    # Savings account
    elif menu_choice == 2:

        # Get customer input
        print("How much would like for initial deposit? ")
        initial_deposit = helpers.choice_float()

        # Check for initial deposit
        if initial_deposit == None:
            initial_deposit = 1        
        
        if initial_deposit < 0:
            log.logging.info("initial_deposit savings: invalid deposit value")
            print("Please enter a value greater than 0.\n")
            menu_new_accounts(customer)

        # Instantiate savings account object
        savings_account = bank.SavingsAccount(
            customer.ssn,
            initial_deposit
        )

        # Add savings account record to accounts.json
        helpers.read_append_json(accounts, jsonpickle.encode(savings_account))

        print("Thank you {} for creating a savings account with World Bank!".format(customer.first.capitalize()))
        print("Your account number is {}".format(savings_account.account_number))
        print("Your balance is {}\n".format(savings_account.balance))        
        print("You will be redirected to the previous menu shortly.")
        time.sleep(10)
        os.system("clear")

        # Redirect to existing customer menu
        menu_customer_existing("N", customer)

    else:
        log.logging.info("menu_customer_existing(): invalid option selected")
        print("The option selected is invalid. Returning to previous menu shortly.")
        time.sleep(2)
        menu_customer_existing("N", customer)

def menu_existing_accounts(customer):
    '''
    Account menu for facilitating deposit or withdrawal
    '''
    
    # Display all account number(s) and balance(s) for customer
    helpers.read_json_accounts(accounts, customer.ssn)

    print("If you would like to make a deposit, please press 1")
    print("If you would like to make a withdrawal, please press 2")
    print("Previous menu, please press 0")

    # Get customer input
    menu_choice = helpers.choice_int()

    # 1 is for deposit
    if menu_choice == 1:
        
        # Get customer input
        print("What account number would you like to deposit money into? ")
        account_number = helpers.choice_int()

        # If account exists
        if bank.BankAccount.authentication(accounts, customer.ssn, account_number):

            # Get customer input
            print("How much would you like to deposit? ")
            amount = helpers.choice_float()

            if amount != None:

                try:
                    # Apply deposit and update balance for account number
                    helpers.update_json_account(accounts, customer.ssn, account_number, amount, 1)
                except ValueError:
                    log.logging.info("menu_existing_accounts(): invalid deposit value")
                    print("Please enter a deposit value greater than 0.\n")
                    menu_existing_accounts(customer)

                # Update reflected in listing of accounts
                helpers.read_json_accounts(accounts, customer.ssn)

                print("Thank you for visiting World Bank! Have a great day!")
                time.sleep(2)

                # Redirect to existing customer menu
                menu_customer_existing("N", customer)

            else:
                log.logging.info("menu_existing_accounts(): invalid deposit amount")
                print("Please enter a valid value.\n")
                time.sleep(2)

                # Redirect to existing customer accounts menu
                menu_existing_accounts(customer)

        else:
            log.logging.info("menu_existing_accounts(): invalid account record")
            print("Hmm, we weren't able to find your account in the World Bank system. Please try again.\n")
            time.sleep(2)
            menu_existing_accounts(customer)

    # 2 is for withdrawal
    elif menu_choice == 2:

        # Get customer input
        print("What account number would you like to withdraw money from? ")
        account_number = helpers.choice_int()

        # If account exists
        if bank.BankAccount.authentication(accounts, customer.ssn, account_number):

            # Get customer input
            print("How much would you like to withdraw? ")
            amount = helpers.choice_float()

            if amount != None:

                try:
                    # Apply withdrawal and update balance for account number
                    helpers.update_json_account(accounts, customer.ssn, account_number, amount, 2)
                except ValueError:
                    log.logging.info("menu_existing_accounts(): invalid withdrawal value")
                    print("Please enter a withdrawal value greater than 0.\n")
                    menu_existing_accounts(customer)

                # Update reflected in listing of accounts
                helpers.read_json_accounts(accounts, customer.ssn)

                print("Thank you for visiting World Bank! Have a great day!")
                time.sleep(2)

                # Redirect to existing customer menu
                menu_customer_existing("N", customer)

            else:
                log.logging.info("menu_existing_accounts(): invalid withdrawal amount")
                print("Please enter a valid value.\n")
                time.sleep(2)

                # Redirect to existing customer accounts menu
                menu_existing_accounts(customer)
        else:
            log.logging.info("menu_existing_accounts(): invalid account record")
            print("Hmm, we weren't able to find your account in the World Bank system. Please try again.\n")
            time.sleep(2)
            menu_existing_accounts(customer)

    elif menu_choice == 0:
        menu_customer_existing("N", customer)
    else:
        log.logging.info("menu_customer_existing(): invalid option selected")
        print("The option selected is invalid. Returning to previous menu shortly.")
        time.sleep(2)
        menu_customer_existing("N", customer)

def menu_update_profile(customer):
    '''
    Customer profile menu for updating various attributes
    '''
    
    print("If you would like to update your last name, please press 1")
    print("If you would like to update your street address, please press 2")
    print("If you would like to update your city, please press 3")
    print("If you would like to update your state, please press 4")
    print("If you would like to update your zip code, please press 5")
    print("If you would like to update your email, please press 6")
    print("If you would like to update your PIN, please press 7")

    # Get customer input
    menu_choice = helpers.choice_int()

    # Update customer last name
    if menu_choice == 1:

        # If valid, update customer object with new value
        customer.last = helpers.last_name(1, "Y")

        # Reflect update in customers.json
        helpers.read_update_json(customers, customer)

        print("Thank you for updating your last name!\n")
        time.sleep(2)
        main_menu()

    # Update customer street address
    elif menu_choice == 2:

        # If valid, update customer object with new value
        customer.street_address = helpers.street_address(1, "Y")

        # Reflect update in customers.json
        helpers.read_update_json(customers, customer)

        print("Thank you for updating your street address!\n")
        time.sleep(2)
        main_menu()

    # Update customer city
    elif menu_choice == 3:

        # If valid, update customer object with new value
        customer.city = helpers.city(1, "Y")

        # Reflect update in customers.json
        helpers.read_update_json(customers, customer)

        print("Thank you for updating your city!\n")
        time.sleep(2)
        main_menu()

    # Update customer state
    elif menu_choice == 4:

        # If valid, update customer object with new value
        customer.state = helpers.state(1, "Y")

        # Reflect update in customers.json
        helpers.read_update_json(customers, customer)

        print("Thank you for updating your state!\n")
        time.sleep(2)
        main_menu()

    # Update customer zip code
    elif menu_choice == 5:

        # If valid, update customer object with new value
        customer.zip_code = helpers.zip_code(1, "Y")

        # Reflect update in customers.json
        helpers.read_update_json(customers, customer)

        print("Thank you for updating your zip code!\n")
        time.sleep(2)
        main_menu()

    # Update customer email
    elif menu_choice == 6:

        # Update customer object with new value
        customer.email = helpers.email("Y")

        # Reflect update in customers.json
        helpers.read_update_json(customers, customer)

        print("Thank you for updating your email!\n")
        time.sleep(2)
        main_menu()

    # Update customer PIN
    elif menu_choice == 7:

        # If valid, update customer object with new value
        customer.pin = helpers.pin("Y")

        # Reflect update in customers.json
        helpers.read_update_json(customers, customer)

        print("Thank you for updating your PIN!\n")
        time.sleep(2)
        main_menu()
    else:
        log.logging.info("menu_update_profile(): invalid option selected")
        print("The option selected is invalid. Please try again.\n")
        time.sleep(2)
        menu_update_profile(customer)

if __name__ == "__main__":
    main_menu()