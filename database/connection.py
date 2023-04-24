import sqlite3
import re
from sqlite3 import Error

class DatabaseConnection:
    def __init__(self, db_name=':memory:'):
        self.db_name = db_name
        self.conn = None

    def create_connection(self):
        try:
            self.conn = sqlite3.connect(self.db_name)
            print(f'successful connection with sqlite version {sqlite3.version}')
        except Error as e:
            print(e)

    def close_connection(self):
        if self.conn:
            self.conn.close()

    def execute_query(self, query):
        try:
            cursor = self.conn.cursor()
            # Use a regular expression to split the query string into individual statements
            # The regex ensures that semicolons within a BEGIN ... END block are not treated as separators
            statements = re.split(r';(?![^()]*\))', query.strip())
            # Execute each statement separately
            for statement in statements:
                if statement:  # Ignore empty statements
                    cursor.execute(statement)
                    rows = cursor.fetchall()
                    [print(row) for row in rows]
        except Error as e:
            print(e)
            raise

    
    def list_items(self, table_name):
        try:
            cursor = self.conn.cursor()
            cursor.execute(f"SELECT * FROM {table_name}")
            rows = cursor.fetchall()
            print(f"Data stored in the {table_name} table:")
            for row in rows:
                print(row)
        except Error as e:
            print(e)