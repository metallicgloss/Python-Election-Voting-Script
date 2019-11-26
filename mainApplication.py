# Import required modules for program.
import mysql.connector
from mysql.connector import Error
from dateutil.parser import parse
import datetime
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
        mysql_cursor.execute("INSERT INTO `studentVoters` (`studentLogin`, `studentPassword`) VALUES (%s, %s)", [self.username, self.password])
        database_connection.commit()
        return mysql_cursor.lastrowid
    
    # Perform verification on student login credentials to database.
    def verify_student_details(self):
        # Execute MySQL Query
        mysql_cursor.execute("SELECT `studentLogin` FROM `studentVoters` WHERE `studentLogin` = '%s' AND `studentPassword` = '%s'", [self.username, self.password])
        
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
        self.id = ""
        self.position = ""
        
    # Insert a new candidate to the system.
    def insert_new_candidate(self):
        # Execute MySQL Query, substitute %s with values with student details.
        mysql_cursor.execute("INSERT INTO `gsuCandidates` (`candidateName`, `candidateEmail`) VALUES (%s, %s)", [self.name, self.email])
        database_connection.commit()
        return mysql_cursor.lastrowid
    
    # Perform verification on student login credentials to database.
    def get_candidate_id(self):
        ###
        ### NOTE: This section may have to be changed dependant on how the candidate is used later in the application.
        ###
        
        # Execute MySQL Query
        mysql_cursor.execute("SELECT `candidateID` FROM `gsuCandidates` WHERE `candidateName` = '%s'", [self.name])
        
        # Store query_result as all values returned.
        query_result = mysql_cursor.fetchall()
        
        self.id = query_result
        
        # Return ID of the candidate searched.
        return query_result
        
    # Create application for the current election.
    def create_application(self):
        current_election = Election()
        election_id = current_election.get_current_election()
        if(election_id != False):
            election_positions = Position()
            
            ###
            ### NOTE: Will need to change to output to the user interface and take input from the user interface.
            ###
            for line in election_positions.get_positions():
                print("Position Available: Option " + str(line['positionID']) + " - " + line['positionTitle'])

            mysql_cursor.execute("INSERT INTO `gsuCandidateApplication` (`candidateID`, `positionID`, `electionID`) VALUES (%s, %s, %s)", [self.id, input("Please enter the position you would like to apply for: "), election_id])
            database_connection.commit()
            return mysql_cursor.lastrowid
            
        else:
            print("Error, no election.")
            return False
        
# Define election class.
class Election:
    def __init__(self, start_time, end_time):
        # Define class variables.
        self.start_time = start_time
        self.end_time = end_time
        self.id = ""
        
    # Create a new election time period in the database.
    def create_election(self):
        # Execute MySQL Query, substitute %s with values with student details.
        mysql_cursor.execute("INSERT INTO `gsuElection` (`electionStartTime`, `electionEndTime`) VALUES (%s, %s)", [parse(start_time), parse(end_time)])
        database_connection.commit()
        return mysql_cursor.lastrowid
    
    # Check status of any election curretly running.
    def get_current_election(self):
        # Execute MySQL Query
        mysql_cursor.execute("SELECT `electionID` FROM `gsuElection` WHERE `electionStartTime` < '%s' AND `electionEndTime` > '%s'", [parse(datetime.datetime.now())])
        
        # Store query_result as all values returned.
        query_result = mysql_cursor.fetchall()
        self.id = query_result
        
        if(mysql_cursor.rowcount == 0):
            # No election currently running.
            return False
        else:
            # Return ID of the election currently running.
            return query_result
            
    # Get all candidates running in the election.
    def get_all_candidates(self):
        # Execute MySQL Query
        mysql_cursor.execute("SELECT * FROM `gsuCandidateApplications` WHERE `electionID` = '%s'", [self.id])
        
        # Store query_result as all values returned.
        query_result = mysql_cursor.fetchall()
        
        if(mysql_cursor.rowcount == 0):
            # No current applications.
            return False
        else:
            # Return array of all candidates running.
            return query_result
            
            
# Define position class.
class Position:
    # No init class due to its very simple nature, just returning available positions.
    
    # Create a new election time period in the database.
    def get_positions():
        # Execute MySQL Query
        mysql_cursor.execute("SELECT * FROM `gsuPositions`")
        
        # Store query_result as all values returned.
        query_result = mysql_cursor.fetchall()
        
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
