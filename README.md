# Employee Management System

## Description
develop an Employee Management System that encompasses various features for managing companies, departments, and employees. 
The system will allow users to create, read, update, and delete (CRUD) records for each of these entities

## Features

- Create, Read, Update, and Delete (CRUD) operations for companies and employees.
- RESTful API endpoints.


## Prerequisites

- Python 3.10
- Django 5.0

  ## Installation

1. Clone the repository:

```
git clone https://github.com/EslamQadri/Employee-Management-System.git
cd Employee-Management-System
```

2. Create a virtual environment and activate it:
```
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install the dependencies:

```
pip install -r requirements.txt
```
4. Run the development server:

```
python manage.py runserver
```

## End Points 

### Company 

- Get company list

*GET* : http://127.0.0.1:8000/company/company

- Create Company
  
*POST* : http://127.0.0.1:8000/company/company

- Get single Company

*GET* : http://127.0.0.1:8000/company/company/1

- Edit single Company
  
*PUT* : http://127.0.0.1:8000/company/company/1

- Delete single Company
  
*DELETE* : http://127.0.0.1:8000/company/company/1

### department 

- Get department list

*GET* : http://127.0.0.1:8000/department/department

- Create department
  
*POST* : http://127.0.0.1:8000/department/department

- Get single department

*GET* : http://127.0.0.1:8000/department/department/1

- Edit single department
  
*PUT* : http://127.0.0.1:8000/department/department/1

- Delete single department
  
*DELETE* : http://127.0.0.1:8000/department/department/1

### employee 

- Get employee Status 

*GET* : http://127.0.0.1:8000/employee/User-Info

- Get employee list

*GET* : http://127.0.0.1:8000/employee/employee

- Create employee
  
*POST* : http://127.0.0.1:8000/employee/employee

- Get single employee

*GET* : http://127.0.0.1:8000/employee/employee/1

- Edit single employee
  
*PUT* : http://127.0.0.1:8000/employee/employee/1

- Delete single employee
  
*DELETE* : http://127.0.0.1:8000/employee/employee/1

- employee login
  
*POST* : http://127.0.0.1:8000/employee/login 

- employee signup

*POST* : http://127.0.0.1:8000/employee/signup

### User Account 

- Get user accounts list

*GET* : http://127.0.0.1:8000/employee/useraccounts

- Create department
  
*POST* : http://127.0.0.1:8000/employee/useraccounts

- Get single department

*GET* : http://127.0.0.1:8000/employee/useraccounts/1

- Edit single department
  
*PUT* : http://127.0.0.1:8000/employee/useraccounts/1

- Delete single department
  
*DELETE* : http://127.0.0.1:8000/employee/useraccounts/1

