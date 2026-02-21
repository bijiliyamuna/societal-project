import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS waste (
id INTEGER PRIMARY KEY AUTOINCREMENT,
plastic_type TEXT,
quantity INTEGER,
recyclable TEXT
)
""")

conn.commit()
conn.close()

print("Database Created Successfully!")