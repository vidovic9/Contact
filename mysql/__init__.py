import mysql.connector
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

class Database:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASS"),
            database=os.getenv("DB_NAME")
        )
        self.cursor = self.connection.cursor(dictionary=True)

    def add_contact(self, name, phone):
        query = "INSERT INTO contacts (name, phone) VALUES (%s, %s)"
        self.cursor.execute(query, (name, phone))
        self.connection.commit()

    def get_all_contacts(self):
        self.cursor.execute("SELECT * FROM contacts")
        return self.cursor.fetchall()

    def delete_contact(self, contact_id):
        query = "DELETE FROM contacts WHERE id = %s"
        self.cursor.execute(query, (contact_id,))
        self.connection.commit()

    def close(self):
        self.cursor.close()
        self.connection.close()
