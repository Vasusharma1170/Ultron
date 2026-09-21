import sqlite3

connection = sqlite3.connect("database/knowledge.db")
cursor = connection.cursor()

cursor.execute("SELECT id, topic, information FROM knowledge")

rows = cursor.fetchall()

for row in rows:
    print(row)

connection.close()