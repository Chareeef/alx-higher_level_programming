# Python Object-Relational Mapping (ORM) with MySQL Using MySQLdb

## Table of Contents
- [Connecting to a MySQL Database](#connecting-to-a-mysql-database)
- [Selecting Rows in a MySQL Table](#selecting-rows-in-a-mysql-table)
- [Inserting Rows into a MySQL Table](#inserting-rows-into-a-mysql-table)
- [Understanding ORM](#understanding-orm)
- [Mapping a Python Class to a MySQL Table](#mapping-a-python-class-to-a-mysql-table)
- [Creating a Python Virtual Environment](#creating-a-python-virtual-environment)

---

### Connecting to a MySQL Database

To connect to a MySQL database from a Python script using `MySQLdb`, we follow these steps:

```python
import MySQLdb

# Establishing a connection
db = MySQLdb.connect(
    host="localhost",
    user="our_username",
    passwd="our_password",
    db="our_database_name"
)

# Create a cursor object
cursor = db.cursor()

# Execute SQL queries
# ... (other operations)

# Close the connection
db.close()
```

Replace `our_username`, `our_password`, and `our_database_name` with our MySQL credentials.

### Selecting Rows in a MySQL Table

To select rows in a MySQL table using `MySQLdb`:

```python
# Execute SELECT query
cursor.execute("SELECT * FROM our_table_name")

# Fetch all rows
rows = cursor.fetchall()

# Process the rows
for row in rows:
    print(row)  # Or perform other operations
```

Replace `our_table_name` with the name of our MySQL table.

### Inserting Rows into a MySQL Table

To insert rows into a MySQL table using `MySQLdb`:

```python
# Sample data for insertion
data = ("value1", "value2", "value3")

# Execute INSERT query
cursor.execute("INSERT INTO our_table_name (column1, column2, column3) VALUES (%s, %s, %s)", data)

# Commit changes
db.commit()
```

Replace `our_table_name` and specify the column names and values for insertion.

### Understanding ORM

Object-Relational Mapping (ORM) is a programming technique that facilitates the conversion between data stored in a relational database and the objects used in object-oriented programming languages.

### Mapping a Python Class to a MySQL Table

To map a Python class to a MySQL table, we can use ORMs like SQLAlchemy or Django's ORM. Here's a basic example using SQLAlchemy:

```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Define a class representing a table
class OurTable(Base):
    __tablename__ = 'our_table_name'

    id = Column(Integer, primary_key=True)
    column1 = Column(String)
    column2 = Column(String)
    # Add more columns as needed
```

Replace `our_table_name` and define columns based on our table structure.

### Creating a Python Virtual Environment

To create a Python virtual environment:

1. Open our terminal/command prompt.
2. Navigate to our project directory.
3. Run the command:

   ```bash
   python3 -m venv myenv
   ```

   Replace `myenv` with the name we want for our virtual environment.

4. Activate the virtual environment:

   - **Windows:**

     ```bash
     myenv\Scripts\activate
     ```

   - **Mac/Linux:**

     ```bash
     source myenv/bin/activate
     ```

Now, we have a virtual environment set up for our project.
