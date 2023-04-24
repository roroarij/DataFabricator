import unittest
from database.connection import DatabaseConnection

class TestDatabaseConnection(unittest.TestCase):
    def setUp(self):
        self.db = DatabaseConnection()
        self.db.create_connection()

    def tearDown(self):
        self.db.close_connection()

    def test_single_table_creation(self):
        single_table_schema = """
        CREATE TABLE products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            price REAL NOT NULL
        );
        """
        self.db.execute_query(single_table_schema)
        # Verify that the table exists in the database
        cursor = self.db.conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='products'")
        self.assertIsNotNone(cursor.fetchone())

    def test_multiple_table_creation(self):
        multiple_table_schema = """
        CREATE TABLE authors (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        );

        CREATE TABLE books (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            author_id INTEGER,
            FOREIGN KEY (author_id) REFERENCES authors (id)
        );
        """
        self.db.execute_query(multiple_table_schema)
        # Verify that both tables exist in the database
        cursor = self.db.conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='authors'")
        self.assertIsNotNone(cursor.fetchone())
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='books'")
        self.assertIsNotNone(cursor.fetchone())

    def test_table_with_foreign_key(self):
        foreign_key_schema = """
        CREATE TABLE authors (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        );

        CREATE TABLE books (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            author_id INTEGER,
            FOREIGN KEY (author_id) REFERENCES authors (id)
        );
        """
        self.db.execute_query(foreign_key_schema)
        # Verify that both tables exist in the database
        cursor = self.db.conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='authors'")
        self.assertIsNotNone(cursor.fetchone())
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='books'")
        self.assertIsNotNone(cursor.fetchone())

    def test_table_with_autoincrement(self):
        autoincrement_schema = """
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL
        );
        """
        self.db.execute_query(autoincrement_schema)
        # Verify that the table exists in the database
        cursor = self.db.conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")
        self.assertIsNotNone(cursor.fetchone())

    def test_table_with_default_value(self):
        default_value_schema = """
        CREATE TABLE orders (
            id INTEGER PRIMARY KEY,
            product_name TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            status TEXT DEFAULT 'Pending'
        );
        """
        self.db.execute_query(default_value_schema)
        # Verify that the table exists in the database
        cursor = self.db.conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='orders'")
        self.assertIsNotNone(cursor.fetchone())

    def test_table_with_index(self):
        index_schema = """
        CREATE TABLE products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            price REAL NOT NULL
        );

        CREATE INDEX idx_products_price ON products(price);
        """
        self.db.execute_query(index_schema)
        # Verify that the table and index exist in the database
        cursor = self.db.conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='products'")
        self.assertIsNotNone(cursor.fetchone())
        cursor.execute("SELECT name FROM sqlite_master WHERE type='index' AND name='idx_products_price'")
        self.assertIsNotNone(cursor.fetchone())

    def test_table_with_unique_index(self):
        unique_index_schema = """
    CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL
    );

    CREATE UNIQUE INDEX idx_users_email ON users(email);
    """
        self.db.execute_query(unique_index_schema)
    # Verify that the table and unique index exist in the database
        cursor = self.db.conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")
        self.assertIsNotNone(cursor.fetchone())
        cursor.execute("SELECT name FROM sqlite_master WHERE type='index' AND name='idx_users_email'")
        self.assertIsNotNone(cursor.fetchone())
if __name__ == '__main__':
    unittest.main()
        



    