# Import required modules for program.
import mysql.connector
from mysql.connector import Error
import connectionString
import tkinter as tk
import pygubu

# Module initialisation - open MySQL connection using connection query data, initialise cursor.
try:
    database_connection = mysql.connector.connect(host=connectionString.dbHost, database=connectionString.dbDatabase, user=connectionString.dbUsername, password=connectionString.dbPassword)
    mysql_cursor = database_connection.cursor()
except Error as e:
    print(e)
		
# Define student class.
class Student:
    def __init__(self, username, password):
		# Define class variables.
        self.username = username
        self.password = password
		
	# Insert a new student voter to the system.
	def insert_new_student(self):
		# Execute MySQL Query, substitute %s with values with student details.
        mysql_cursor.execute("INSERT INTO `studentVoters` (`studentLogin`, `studentPassword`) VALUES (%s, %s)", [username, password])
        database_connection.commit()
		return mysql_cursor.lastrowid
	
	# Perform verification on student login credentials to database.
	def verify_student_details(self):
		# Execute MySQL Query
        mysql_cursor.execute("SELECT `studentLogin` WHERE `studentLogin` = '" . username . "' AND `studentPassword` = '" . password . "'")
        
        # Store query_result as all values returned.
        query_result = mysql_cursor.fetchall()
		
		if(mysql_cursor.rowcount == 0):
			# Query returned nothing, details do not match record.
			return False
		else:
			# Query returned data, user authenticated. Crude way of doing it, but acceptable for this task.
			return True
			
# Define candidate class.
class Candidate:
    def __init__(self, name, email):
		# Define class variables.
        self.name = name
        self.email = email
		
	# Insert a new student voter to the system.
	def insert_new_candidate(self):
		# Execute MySQL Query, substitute %s with values with student details.
        mysql_cursor.execute("INSERT INTO `gsuCandidates` (`candidateName`, `candidateEmail`) VALUES (%s, %s)", [name, email])
        database_connection.commit()
		return mysql_cursor.lastrowid
	
	# Perform verification on student login credentials to database.
	def get_candidate_id(self):
		#
		# NOTE: This section may have to be changed dependant on how the candidate is used later in the application.
		#
		# Execute MySQL Query
        mysql_cursor.execute("SELECT `candidateID` WHERE `candidateName` = '" . name . "'")
        
        # Store query_result as all values returned.
        query_result = mysql_cursor.fetchall()
		
		# Return ID of the candidate searched.
		return query_result
		
# Define primary class to initiate the user interface.
class votingApplication:
    def __init__(self, master):
		# Create PYGUBU builder
        self.interfaceBuilder = interfaceBuilder = pygubu.Builder()
		
		# Load main menu interface design.
        interfaceBuilder.add_from_file('designerFiles/mainMenu.ui')
        self.mainMenu = interfaceBuilder.get_object('mainMenu', master)


if __name__ == '__main__':
    root = tk.Tk()
    app = votingApplication(root)
    root.mainloop()
