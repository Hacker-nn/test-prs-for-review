import sqlite3

def register_user(username, password):
    conn = sqlite3.connect("users.db")
    conn.execute(f"INSERT INTO users VALUES ('{username}', '{password}')")