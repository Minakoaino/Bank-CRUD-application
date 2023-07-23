# Bank Management App

This is a Flask application for managing a banking system.

The app folder structure is the following:
app/
├── static/
│   └── css/
│       └── styles.css
├── templates/
│   └── home.html
│   └── create_bank.html
│   └── list_banks.html
│   └── view_bank.html
│   └── update_bank.html
│   └── delete_bank.html

├── models.py
├── routes.py
├── database.py
├── __init__.py
├── requirements.txt
tests/
├── test_app.py

This Flask application consists of several routes to create, list, view, and update banks. Here's a summary of the routes:
/bank/create: This route handles the creation of a bank. It handles both GET and POST requests. If a POST request is made, it retrieves the bank details from the form, creates a new Bank object, adds it to the database, and redirects to the list of banks. If a GET request is made, it renders the template for creating a bank.

/banks: This route lists all the banks in the database. It retrieves all banks from the database and renders the template for listing banks, passing the banks as a variable.

/bank/<int:bank_id>: This route displays the details of a specific bank. It takes the bank ID as a parameter, retrieves the corresponding bank from the database, and renders the template for viewing a bank, passing the bank as a variable.

/bank/update: This route handles the updating of a bank. It handles both GET and POST requests. If a POST request is made, it retrieves the updated bank details from the form, updates the corresponding bank in the database, and redirects to the bank's details page. If a GET request is made, it retrieves all banks from the database and renders the template for updating a bank, passing the banks as a variable.

These routes are defined in the app Flask application instance and import the necessary modules and classes from the app package.

Project directory: The top-level directory for the application, named "bank-management-app".

## app directory: Contains the creation of main application files.

__init__.py: Initializes the Flask application.
routes.py: Defines the routes and their associated functions.
models.py: Placeholder for defining application models.
run.py: Script to run the Flask application.

README.md: A README file with installation instructions and a brief description of the application.

templates directory: Contains HTML templates for different views of the application.

create_bank.html: Template for creating a bank.
view_bank.html: Template for viewing bank details.
update_bank.html: Template for updating bank information.
list_banks.html: Template for listing all banks.
static/css directory: Holds static files, specifically CSS files.

styles.css: A sample CSS file for styling the HTML templates.

## Banks database and table creation
Bank_db_creation.sql
Just run the file in SQL Server

## Banks table random data import
Bank_db_data.py
You can actually skip this step or run this file with python, it is just interensting to import some data in our db
- The code establishes a connection to a SQL Server database, generates random data, and inserts it into the Banks table.
Here's how the code works:
- It imports the pyodbc module, which provides Python access to SQL Server databases.
- The username variable is set to the username of the SQL Server connection.
- The code establishes a connection to the SQL Server database using the connection string DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=BankDB;Trusted_Connection=yes;UID=<username>.
- A cursor is created from the connection. The cursor allows executing SQL statements on the database.
- A loop is used to generate random data for the name and location columns of the Banks table. The loop iterates 5 times, creating 5 rows of data.
- Inside the loop, an SQL INSERT statement is constructed using the generated data. The id column is set to the loop index i, and the name and location columns are set to the generated values.
= The cursor.execute() method is called to execute the INSERT statement and insert the data into the Banks table.
- After the loop, the conn.commit() method is called to commit the changes to the database.
Finally, the connection is closed using conn.close().
This code can be executed to insert random data into the Banks table. Make sure to replace <username> with the actual username for your SQL Server connection. 

## Installation

1. Install the required dependencies.
To add the instruction for installing the requirements.txt file, you can include the following steps:
Make sure you have Python installed on your system. If not, you can download and install Python from the official Python website (https://www.python.org).
Create a new virtual environment (recommended) or navigate to the project directory in your command prompt or terminal.

Install the project dependencies by running the following command:
pip install -r requirements.txt
2. Make sure you have a SQL Server installed on your system. If not, you can download and install SQL Server from the official Microsoft website (https://www.microsoft.com/sql-server).
Open a command prompt or terminal and navigate to the directory where the database file (database.sql) is located.
sqlcmd -S <server_name> -d master -i database.sql
Or just simply open the Bank_db_creation.sql and run it from the SSMS.
If you want to populate the tables with random data, run the following file after the database is created:
Bank_db_data

Run the following command to create the database and tables:
3. Run the `run.py` script to start the application.
4. Navigate to http://127.0.0.1:5000

We can run tests as well with the pytest framework. It is included in requirements. Just run the file with pytest tests/
