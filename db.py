import sqlite3


class Database:
    def __init__(self,db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def user_exists(self, user_id):
        with self.connection:
           result = self.cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,)).fetchall()
           return bool(len(result))

    def add_user(self, user_id):
        with self.connection:
            return self.cursor.execute("INSERT INTO users (user_id) VALUES (?)", (user_id,))

    def user_money(self, user_id):
        with self.connection:
           result = self.cursor.execute("SELECT money FROM users WHERE user_id = ?", (user_id,)).fetchmany(1)
           return int(result[0])

    def set_money(self, user_id, money):
        with self.connection:
            return self.cursor.execute("UPDATE users SET money = ? WHERE user_id = ?", (money, user_id,))      
