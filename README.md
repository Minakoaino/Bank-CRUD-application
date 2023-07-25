
## Bank App

Bank App is a simple, yet powerful CRUD (Create, Read, Update, Delete) web application developed with Flask and SQLAlchemy. It manages bank details such as bank name and location.

CRUD refers to the four basic operations you can perform on data in a database or similar storage: create, read, update, and delete. In the context of a web application, this usually translates to POST, GET, PUT/PATCH, and DELETE HTTP methods.

### Features

🏦 Create Bank: Allows you to add new banks with their name and location.

📚 Read/List Banks: Enables you to view a list of all created banks.

✏️ Update Bank: Provides the ability to edit the name or location of an existing bank.

🗑️ Delete Bank: Gives you the option to remove a bank from the system.

## Installation


1. Clone this repository:

```
git clone https://github.com/Minakoaino/Bank-CRUD-application.git
```

2. Navigate to the project directory:

```python
cd bank-app
```

3. Create a Python virtual environment and activate it:

```python3 -m venv venv
source venv/bin/activate
```
    
4. Install the dependencies:

```
pip install -r requirements.txt
```

5. Set up the Flask environment variables:

```
export FLASK_APP=run.py
export FLASK_ENV=development
```

6. Run the application:

```
flask run
```

7. Open your web browser and visit http://localhost:5000.

## Usage
The navigation through the app is handled via the navigation bar at the top of the page. Here you can create a new bank, view the list of existing banks, update bank information, and delete a bank.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.