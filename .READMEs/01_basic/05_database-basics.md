# Setting up new tina4_python project

## Database Basics in Tina4

### Guide for setting up database connection and creating ORMs

> [Official Tina4 database guide](https://www.tina4.com/getting-started/python/-Basics/d-database-connections.html)   
> [Comparisons of Different Databases](05.1_database_comparisons.md)   
> Note: You will need to install connectors for the different databases, only sqlite3 is built in   
> Example for MySql: run `poetry add mysql-connector-python` in the console

- Tina4 is set up to work with almost any database, you just need to give it the correct connection path
- convention for database connection path:

```text
<driver-name>:<host>/<port>:<database-name>
```

- where `driver-name` is the database connector
- MySql Example:

```python
from tina4_python.Database import Database

dba = Database("mysql.connector:localhost/3306:test", "root", "")
```

### quick-setup: sqlite3

> [Have sqlite3 installed](https://www.sqlite.org/download.html)   

- you can instantiate this in `app.py` and import it when needed, or you can make a separate `db.py` file
- add the following code:

```python
from tina4_python.Database import Database

dba = Database("sqlite3:test.db")
```

- this will automatically create the database if it is not already present
- to use the db connection, add the following to your file that needs db access:

```python
from app import dba
# or if in db.py
from db import dba
```

> Hint: go to [Tina4 Database Queries](https://www.tina4.com/getting-started/python/-Basics/f-database-communication.html)
> to see possible queries

### Migrations - Creation

- to actually create tables in your database, you will need migrations, stored in the `migrations` folder
- create a migration file using the following naming convention: `00001_initial_table_creation.sql`
- incrementing the initial number with each migration ensures the migrations remain organized
- the sql style of the migration will depend on what database you are using
- sqlite3 example of `user` table:

```sql
create table user (
    id integer primary key autoincrement,
    first_name varchar(255) default 'John',
    last_name varchar(255) default 'Doe',
    email text not null,
    phone varchar(50),
    date_created timestamp default current_timestamp,
    date_modified timestamp default current_timestamp
);
```

### Migrations - Running

- this can be done at any point in the code, by adding this:

```python
from tina4_python.Migration import migrate
from db import dba

migrate(dba)
```

- the best is usually to do it at start-up
- add the following code to `__init__.py`:

```python
from tina4_python.Migration import migrate
from db import dba

migrate(dba)
```

- this will insure that your migrations always run at start-up
- migrations running will provide a log of which migrations were run and their response
- if a migration fails, you can alter it and run migrations again

#### Bonus

- you can also use the below code instead, which will let you only run migrations when you decide
- just set `RUN_MIGRATIONS_SWITCH=True` in your .env file

```python
from tina4_python.Migration import migrate
from db import dba
import os

run_migrations = os.getenv("RUN_MIGRATIONS_SWITCH")
if run_migrations and run_migrations == "True":
    print("RUNNING MIGRATIONS")
    migrate(dba)
else:
    print("RUN MIGRATIONS IS DEACTIVATED")
```

### ORMs

> ORM stands for Object-Relational Mapping   
> this lets you interact with the database through ORM objects  
> it makes it a lot easier to handle and use db tables and data

- creating ORMs can be tedious, but only had to be done once per table   
- example for the `user` table from earlier:

```python

```






