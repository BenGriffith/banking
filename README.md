## Table of Contents
- [General Info](#general-info)
- [Technologies](#technologies)
- [Setup](#setup)

## General Info
In this project, I created a banking system using Python Object-Oriented Programming (OOP) techniques. In my bank, I created entities for customers, employees and accounts. Each of these entities have distinct properties. For example, customer and employee entities include first name, last name, address, email, PIN, salary and other properties. While accounts entities includes account type, account number, balance, deposit and withdrawal properties.

Customer, employee and account records are stored using JSON files.

```core.py``` is the command line driver allowing a user to interact with the following World Bank components:

- Customer Registration
- Customer Basic Authentication
- Customer Account Creation
- Customer Deposit(s) and Withdrawal(s)
- Customer Profile Update
- Employee Registration
- Employee Basic Authentication
- Employee Profile Information and Update

## Technologies
Project is created with: 
* Python 3.8.3

## Setup
To run this project, follow the steps below:

```
$ git clone https://github.com/BenGriffith/banking.git
$ cd sample
$ python3 core.py