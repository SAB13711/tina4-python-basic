import os

from tina4_python.Database import Database

dba = Database(os.getenv("DATABASE_URL_SQLITE", "sqlite3:test.db"))

