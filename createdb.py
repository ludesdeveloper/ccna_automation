import sqlite3

db = sqlite3.connect('automation.db')
cursor = db.cursor()
cursor.execute('''
    CREATE TABLE automation(id INTEGER PRIMARY KEY, katakata TEXT)                    
''')
db.close()