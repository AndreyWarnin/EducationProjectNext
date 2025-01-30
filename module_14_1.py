import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)''')

for row in range(1, 11):
    comm = 'INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)'
    val = (f'User{row}', f'example{row}@gmail.com', 10 * row, 1000)
    cursor.execute(comm, val)

for user_id in range(1, 11)[::2]:
    comm2 = 'UPDATE Users SET balance = ? WHERE id = ?'
    val2 = (500, user_id)
    cursor.execute(comm2, val2)

for user_id in range(1, 11)[::3]:
    comm3 = 'DELETE FROM Users WHERE id = ?'
    val3 = (user_id,)
    cursor.execute(comm3, val3)

cursor.execute('SELECT * FROM Users WHERE age != ?', (60,))
for user in cursor.fetchall():
    print(f'Имя: {user[1]} | Почта: {user[2]} | Возраст: {user[3]}, | Баланс: {user[4]}')

connection.commit()
connection.close()
