import sqlite3

def create_database():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    
    # Create table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    
    # Clear existing data to avoid duplicates
    cursor.execute('DELETE FROM Products')
    
    # Insert sample data
    cursor.execute('''
        INSERT INTO Products (id, name, category, price)
        VALUES
        (1, 'Laptop', 'Electronics', 799.99),
        (2, 'Coffee Mug', 'Home Goods', 15.99),
        (3, 'Python Book', 'Books', 45.99),
        (4, 'USB Cable', 'Electronics', 9.99),
        (5, 'Desk Lamp', 'Home Goods', 35.50)
    ''')
    
    conn.commit()
    conn.close()
    print("Database created and populated successfully!")

if __name__ == '__main__':
    create_database()