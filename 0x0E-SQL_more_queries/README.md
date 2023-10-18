# Understanding Databases and SQL - Second part

This learning project aims to provide a fundamental understanding of MySQL, a widely used relational database management system. We will cover various aspects of MySQL, from user management to working with data across multiple tables.

### How to Create a New MySQL User

In MySQL, you can create a new user using the `CREATE USER` command. Here's an example:

```sql
CREATE USER 'new_user'@'localhost' IDENTIFIED BY 'password';
```

This creates a new user with the username 'new_user' and the password 'password'. The `@'localhost'` part restricts the user to connections from the local machine.

### How to Manage Privileges for a User to a Database or Table

MySQL uses the `GRANT` statement to manage user privileges. For example, to grant all privileges to a user on a specific database:

```sql
GRANT ALL PRIVILEGES ON database_name.* TO 'user'@'localhost';
```

To grant specific privileges on a table:

```sql
GRANT SELECT, INSERT, UPDATE ON database_name.table_name TO 'user'@'localhost';
```

### What's a PRIMARY KEY

A PRIMARY KEY is a column or set of columns in a table that uniquely identifies each row in that table. It enforces data integrity and ensures that each row is unique. For example:

```sql
CREATE TABLE users (
    user_id INT PRIMARY KEY,
    username VARCHAR(50) NOT NULL
);
```

In this example, `user_id` is the primary key.

### What's a FOREIGN KEY

A FOREIGN KEY is a column or set of columns in a table that establishes a link between the data in two tables. It ensures referential integrity, allowing you to create relationships between tables. For example:

```sql
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);
```

Here, `customer_id` in the `orders` table is a foreign key that references the `customer_id` in the `customers` table.

### How to Use NOT NULL and UNIQUE Constraints

You can use the `NOT NULL` constraint to ensure a column doesn't contain null values:

```sql
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL
);
```

The `UNIQUE` constraint ensures that all values in a column are unique:

```sql
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(50) UNIQUE
);
```

### How to Retrieve Data from Multiple Tables in One Request

To retrieve data from multiple tables in a single query, you can use SQL JOINs. For example:

```sql
SELECT users.username, orders.order_date
FROM users
JOIN orders ON users.user_id = orders.customer_id;
```

### What Are Subqueries

A subquery is a query nested inside another query. It's used to retrieve data that will be used by the main query. For example, to find the average salary of employees with the highest salary:

```sql
SELECT AVG(salary)
FROM employees
WHERE salary = (SELECT MAX(salary) FROM employees);
```

### What Are JOIN and UNION

- `JOIN`: A JOIN is used to combine rows from two or more tables based on a related column between them. It allows you to retrieve data from multiple tables in a single result set.

- `UNION`: UNION combines the result sets of two or more SELECT statements into a single result set, removing duplicate rows.

For instance, a UNION query to combine results from two tables:

```sql
SELECT column1 FROM table1
UNION
SELECT column1 FROM table2;
```
