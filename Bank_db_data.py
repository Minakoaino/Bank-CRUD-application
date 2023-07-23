import pyodbc

username = 'DESKTOP-P8GGH21\HP'
# Establish a connection to the SQL Server database
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=BankDB;Trusted_Connection=yes;UID=' + username)
cursor = conn.cursor()

# Generate and insert random data into the Banks table

for i in range(5):
    name = f"Bank {i}"
    location = f"Location {i}"
    query = f"INSERT INTO Banks (id, name, location) VALUES ({i}, '{name}', '{location}')"
    cursor.execute(query)

# Commit the changes and close the connection
conn.commit()
conn.close()