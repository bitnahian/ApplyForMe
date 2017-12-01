import sqlite3
from flask import Flask, render_template, request

try:
    conn = sqlite3.connect('database.db')
    print("Database successfully opened")
    conn.execute('''CREATE TABLE IF NOT EXISTS Jobs(
                job_id INTEGER,
                username VARCHAR
                );''')
    print("Table successfully created")
    conn.close()
except:
    print("Failed to open database")
