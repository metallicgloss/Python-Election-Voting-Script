# Import required modules for program.
import mysql.connector
from mysql.connector import Error
import connectionString
import tkinter as tk
import pygubu

# Module initialisation - open MySQL connection using connection query data, initialise cursor.
try:
    databaseConnection = mysql.connector.connect(host=connectionString.dbHost, database=connectionString.dbDatabase, user=connectionString.dbUsername, password=connectionString.dbPassword)
    mysqlCursor = databaseConnection.cursor()
except Error as e:
    print(e)

class votingApplication:
    def __init__(self, master):
        self.interfaceBuilder = interfaceBuilder = pygubu.Builder()
        interfaceBuilder.add_from_file('designerFiles/mainMenu.ui')
        self.mainMenu = interfaceBuilder.get_object('mainMenu', master)


if __name__ == '__main__':
    root = tk.Tk()
    app = votingApplication(root)
    root.mainloop()
