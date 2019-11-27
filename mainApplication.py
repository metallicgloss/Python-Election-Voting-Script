# Import required modules for program.
import os, mysql.connector, datetime, connectionString, pygubu, hashlib, binascii
from mysql.connector import Error
from dateutil.parser import parse
import tkinter as tk
from tkinter import messagebox

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
        self._salt = ""
        self._hashed_password = ""
        
    # Insert a new student voter to the system.
    def insert_new_student(self):
        # Generate hash and salt.
        self.generate_hash_password()
        
        # Execute MySQL Query, substitute %s with values with student details.
        mysql_cursor.execute("INSERT INTO `studentVoters` (`studentLogin`, `studentPassword`, `studentSalt`) VALUES (%s, %s, %s)", [self.username, self._hashed_password, self._salt])
        database_connection.commit()
        return mysql_cursor.lastrowid
    
    # Generate and store new hashed password
    def generate_hash_password(self):
        # Generate random salt key using hashlib, a random string generated.
        self._salt = hashlib.sha256(os.urandom(64)).hexdigest().encode('ascii')
        
        # Generate hashed version of the password converted to hex.
        self._hashed_password = binascii.hexlify(hashlib.pbkdf2_hmac('sha512', self.password.encode('utf-8'), self._salt, 100000))
    
    # Generate and return hashed password
    def get_hashed_password(self):
        return binascii.hexlify(hashlib.pbkdf2_hmac('sha512', self.password.encode('utf-8'), self._salt, 100000))
    
    # Verify password
    def verify_password(self):
        # Execute MySQL Query to get password and hash.
        mysql_cursor.execute("SELECT `studentPassword`, `studentSalt` FROM `studentVoters` WHERE `studentLogin` = %s", [self.username])
        
        # Store query_result as all values returned.
        query_result = mysql_cursor.fetchall()
        
        messagebox.showinfo('Success', query_result[1])
        
        self._hash = query_result['studentSalt']
        
        if(self.get_hashed_password() == query_result['studentPassword']):
            messagebox.showinfo('Success', 'Yes.')
        else:
            messagebox.showinfo('Success', 'No')
                
         
    # Verify username does not already exist.
    def verify_unique_username(self):
        # Execute MySQL Query, substitute %s with values with student username.
        mysql_cursor.execute("SELECT `studentLogin` FROM `studentVoters` WHERE `studentLogin` LIKE %s", [self.username])
        
        # Store query_result as all values returned.
        query_result = mysql_cursor.fetchall()
        
        if(mysql_cursor.rowcount == 0):
            # No user found.
            return True
        else:
            # User Found
            return False
        return mysql_cursor.lastrowid
            
    def cast_votes(self, position_id, candidate_id_one, candidate_id_two, candidate_id_three, candidate_id_four):
        current_election = Election()
        # Loop to iterate the voting for all positions.
        while True:
            break
            # Handled primarily by the user interface so holding off, shouldn't be performed within this class.
            # List all positions
            # Get user to select position to vote
            # List all candidates for that position
            # Take 4 input values
            # Validate input
            # Exit position, display positions remaining from array.
            
# Define candidate class.
class Candidate:
    def __init__(self, name, email):
        # Define class variables.
        self.name = name
        self.email = email
        self._id = ""
        self._position = ""
        
    # Insert a new candidate to the system.
    def insert_new_candidate(self):
        # Execute MySQL Query, substitute %s with values with student details.
        mysql_cursor.execute("INSERT INTO `gsuCandidates` (`candidateName`, `candidateEmail`) VALUES (%s, %s)", [self.name, self.email])
        database_connection.commit()
        return mysql_cursor.lastrowid
            
    # Verify candidate does not have name matching another.
    def verify_unique_name(self):
        # Execute MySQL Query, substitute %s with values with student username.
        mysql_cursor.execute("SELECT `candidateName` FROM `gsuCandidates` WHERE `candidateName` = %s", [self.name])
        
        # Store query_result as all values returned.
        query_result = mysql_cursor.fetchall()
        
        if(mysql_cursor.rowcount == 0):
            # No user found.
            return True
        else:
            # User Found
            return False
        return mysql_cursor.lastrowid
    
    # Perform verification on student login credentials to database.
    def get_candidate_id(self):
        ###
        ### NOTE: This section may have to be changed dependant on how the candidate is used later in the application.
        ###
        
        # Execute MySQL Query
        mysql_cursor.execute("SELECT `candidateID` FROM `gsuCandidates` WHERE `candidateName` = %s", [self.name])
        
        # Store query_result as all values returned.
        query_result = mysql_cursor.fetchall()
        
        self._id = query_result
        
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

            mysql_cursor.execute("INSERT INTO `gsuCandidateApplication` (`candidateID`, `positionID`, `electionID`) VALUES (%s, %s, %s)", [self._id, input("Please enter the position you would like to apply for: "), election_id])
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
        self._id = ""
        
    # Create a new election time period in the database.
    def create_election(self):
        # Execute MySQL Query, substitute %s with values with student details.
        mysql_cursor.execute("INSERT INTO `gsuElection` (`electionStartTime`, `electionEndTime`) VALUES (%s, %s)", [parse(start_time), parse(end_time)])
        database_connection.commit()
        
        # Return election ID
        return mysql_cursor.lastrowid
    
    # Check status of any election curretly running.
    def get_current_election(self):
        # Execute MySQL Query
        mysql_cursor.execute("SELECT `electionID` FROM `gsuElection` WHERE `electionStartTime` < %s AND `electionEndTime` > %s", [parse(datetime.datetime.now())])
        
        # Store query_result as all values returned.
        query_result = mysql_cursor.fetchall()
        self._id = query_result
        
        if(mysql_cursor.rowcount == 0):
            # No election currently running.
            return False
        else:
            # Return ID of the election currently running.
            return query_result
            
    # Get all candidates running in the election.
    def get_all_candidates(self):
        # Execute MySQL Query
        mysql_cursor.execute("SELECT * FROM `gsuCandidateApplications` WHERE `electionID` = '%s'", [self._id])
        
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
    
    # List all positions currently in the GSU.
    def get_positions():
        # Execute MySQL Query
        
        election = Election()
        election_id = election.get_current_election()
        
        mysql_cursor.execute("SELECT * FROM `gsuPositions`")
        
        # Store query_result as all values returned.
        query_result = mysql_cursor.fetchall()
        
        return query_result
        
    # List all available positions to apply for.
    def get_available_positions():
        # Execute MySQL Query
        
        election = Election()
        election_id = election.get_current_election()
        
        # Select all positions where they're not in the list containing positions applied for more than 4 times in a given election.
        mysql_cursor.execute("SELECT * FROM `gsuPositions` WHERE `positionID` NOT IN (SELECT `positionID` FROM `gsuCandidateApplications` WHERE `electionID` = '%s' AND COUNT(SELECT `positionID` FROM `gsuCandidateApplications` WHERE `electionID` = '%s') < 5)", [election_id, election_id])
        
        # Store query_result as all values returned.
        query_result = mysql_cursor.fetchall()
        
        return query_result
        
# Define primary class to initiate the user interface.
class voting_application(pygubu.TkApplication):
    def __init__(self, master):
        self.master = master
        self.change_frame('startup_menu_frame')
    
    # Function to change/load the frame.
    def change_frame(self, frame):
        # If userInterface not defined yet (startup), bypass destroy. Destroy current view and load frame of desired window. 
        try:
            self.userInterface.destroy()
        except AttributeError:
            pass
            
        # Create Pygubu builder
        self.interfaceBuilder = pygubu.Builder()
        
        # Load main interface design.
        self.interfaceBuilder.add_from_file('userInterfaceDesign.ui')
        self.userInterface = self.interfaceBuilder.get_object(frame, self.master)
        
        # Connect buttons to methods.
        self.interfaceBuilder.connect_callbacks(self)
    
    #############################################################
    #              Backend Menu Navigation Control              #
    #############################################################
    
    # Exit backend menu to return to startup.
    def menu_backend_return(self):
        self.change_frame('startup_menu_frame')
    
    # Navigate to create student voter.
    def menu_create_student_voter(self):
        self.change_frame('backend_create_student_frame')
    
    # Navigate to create candidate.
    def menu_create_candidate(self):
        self.change_frame('backend_create_candidate_frame')
    
    # Navigate to create election.
    def menu_create_election(self):
        self.change_frame('backend_create_election_frame')
    
    # Navigate to create candidate application.
    def menu_create_candidate_application(self):
        self.change_frame('backend_create_candidate_application_frame')
    
    # Navigate to view results page.
    def menu_view_results(self):
        self.change_frame('backend_view_results_frame')
    
    # Navigate to visualise results page.
    def menu_visualise_results(self):
        self.change_frame('backend_visualise_results_frame')
    
    # On sub-page access through the backend menu, provide a back button.
    def return_to_backend(self):
        self.change_frame('backend_menu_frame')
    
    
    #############################################################
    #              Backend Menu Navigation Control              #
    #############################################################
    
    # Navigate to student voter login.
    def startup_select_standard_mode(self):
        self.change_frame('student_login_frame')
        
    # Navigate to backend menu.
    def startup_select_admin_mode(self):
        self.change_frame('backend_menu_frame')
    
    def exit_application(self):
        # Destroy the tkinter mainloop. Quit leaves the loop running, use destroy.
        global tkinter_app
        tkinter_app.destroy()
    
    
    #############################################################
    #                       Create Student                      #
    #############################################################
    
    # Create new student on submission from user.
    def create_student(self):
        # Get user input from the page.
        username = self.interfaceBuilder.get_object('student_userame_txtbx').get()
        password = self.interfaceBuilder.get_object('student_password_txtbx').get()
        
        if ((username != "") and (password != "")):
            # If input is not blank, create user.
            new_student = Student(username, password)
            new_student.generate_hash_password()
            
            if(True):
                #Verify that the username hasn't been used before. If unique, insert student.
                new_student.insert_new_student()
                messagebox.showinfo('Success', 'Created successfully.')
                self.menu_backend_return()
            else:
                # If not unique, alert user.
                self.interfaceBuilder.get_object('create_student_error_lbl').configure(text="Username is not unique. Please try again.")
            
        else:
            # Else change label text to error message.
            self.interfaceBuilder.get_object('create_student_error_lbl').configure(text="Please ensure you've entered both a username and password.")
  
    #############################################################
    #                       Create Election                     #
    #############################################################
    
    # Create new election period on the system.
    def create_election(self):
        # Get user input from the page.
        start_date_time = parse(self.interfaceBuilder.get_object('election_start_date_txtbx').get())
        end_date_time = parse(self.interfaceBuilder.get_object('election_end_date_txtbx').get())
        
        if ((start_date_time != "") and (end_date_time != "")):
            new_election = Election(start_date_time, end_date_time)
            
            if(start_date_time < end_date_time):
                # End date comes after start time, acceptable input.
                new_election.create_election()
                messagebox.showinfo('Success', 'Created successfully.')
                self.menu_backend_return()
            else:
                # If not valid, alert user.
                self.interfaceBuilder.get_object('create_election_error_lbl').configure(text="Please double check your end date. Please try again.")
            
        else:
            # Else change label text to error message.
            self.interfaceBuilder.get_object('create_election_error_lbl').configure(text="Please ensure you've entered both a start and end datetime.")
  
    #############################################################
    #                      Create Candidate                     #
    #############################################################
    
    # Create new candidate that can make applications.
    def create_candidate(self):
        # Get user input from the page.
        name = self.interfaceBuilder.get_object('candidate_name_txtbx').get()
        email = self.interfaceBuilder.get_object('candidate_email_txtbx').get()
        
        if ((name != "") and (email != "")):
            new_candidate = Candidate(name, email)
            
            if(new_candidate.verify_unique_name()):
                # Check there isn't already a candidate with same name.
                new_candidate.insert_new_candidate()
                messagebox.showinfo('Success', 'Created successfully.')
                self.menu_backend_return()
            else:
                # If not unique, inform user to add custom tag to surname (other option is to change name) to help voters.
                self.interfaceBuilder.get_object('create_candidate_error_lbl').configure(text="Uh Oh! You've got a common name, please add a unique addition to your surname to help voters!")
            
        else:
            # Else change label text to error message.
            self.interfaceBuilder.get_object('create_candidate_error_lbl').configure(text="Please ensure you've entered data into both boxes.")
  
    #############################################################
    #                       Student Login                       #
    #############################################################
    
    # Perform student login verification.
    def student_login(self):
        # Get user input from the page.
        username = self.interfaceBuilder.get_object('student_login_username_txtbx').get()
        password = self.interfaceBuilder.get_object('student_login_password_txtbx').get()
        
        if ((username != "") and (password != "")):
            student_login = Student(username, password)
            student_login.verify_password()
            
            if(student_login.verify_student_details()):
                self.change_frame('student_vote_frame')
            else:
                # If not unique, inform user to add custom tag to surname (other option is to change name) to help voters.
                self.interfaceBuilder.get_object('student_login_error_lbl').configure(text="Uh Oh! Wrong username or password!")
            
        else:
            # Else change label text to error message.
            self.interfaceBuilder.get_object('student_login_error_lbl').configure(text="Please ensure you've entered data into both boxes.")
  
if __name__ == '__main__':
    tkinter_app = tk.Tk()
    main_application = voting_application(tkinter_app)
    tkinter_app.mainloop()
