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
    def __init__(self, username="", password=""):
        # Define class variables.
        self.username = username
        self.password = password
        self._id = ""
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
        # Re-calculate generated hashed version of the password converted to hex.
        self._hashed_password = (binascii.hexlify(hashlib.pbkdf2_hmac('sha512', (self.password).encode('utf-8'), (self._salt).encode('ascii'), 100000))).decode('ascii')
    
    # Verify password
    def verify_password(self):
        # Execute MySQL Query to get password and hash.
        mysql_cursor.execute("SELECT `studentPassword`, `studentSalt` FROM `studentVoters` WHERE `studentLogin` = %s", [self.username])
        
        # Store query_result as all values returned.
        query_result = mysql_cursor.fetchall()
        
        # Set hash to match the hash value returned in the database.
        self._salt = str(query_result[0][1])
        
        # Re-generate hash using passed provided to see it matches the stored DB value.
        self.get_hashed_password()
        
        if(self._hashed_password == query_result[0][0]):
            return True
        else:
            return False
                
    # Get student ID
    def get_student_id(self):
        # Execute MySQL Query
        mysql_cursor.execute("SELECT `studentID` FROM `studentVoters` WHERE `studentLogin` = %s", [self.username])
        
        # Store query_result as all values returned.
        query_result = mysql_cursor.fetchall()
        
        self._id = query_result[0][0]
        
        return self._id
        
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
        global logged_in_student
        mysql_cursor.execute("INSERT INTO `gsuElectionVotes` (`studentID`, `electionID`, `positionID`, `firstVoteCandidateID_FK`, `secondVoteCandidateID_FK`, `thirdVoteCandidateID_FK`, `fourthVoteCandidateID_FK`) VALUES (%s, %s, %s, %s, %s, %s, %s)", [logged_in_student, current_election.get_current_election()[0][0], position_id, candidate_id_one, candidate_id_two, candidate_id_three, candidate_id_four])
        database_connection.commit()
        
            
# Define candidate class.
class Candidate:
    def __init__(self, name="", email="", id=""):
        # Define class variables.
        self.name = name
        self.email = email
        self.id = id
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
        # Execute MySQL Query
        mysql_cursor.execute("SELECT `candidateID` FROM `gsuCandidates` WHERE `candidateName` = %s", [self.name])
        
        # Store query_result as all values returned.
        query_result = mysql_cursor.fetchall()
        
        self.id = query_result[0][0]
        
    # Perform verification on student login credentials to database.
    def get_candidate_name(self):        
        # Execute MySQL Query
        mysql_cursor.execute("SELECT `candidateName` FROM `gsuCandidates` WHERE `candidateID` = %s", [self.id])
        
        # Store query_result as all values returned.
        query_result = mysql_cursor.fetchall()
        
        self.name = query_result[0][0]
        
        return self.name
        
    # Create application for the current election.
    def create_application(self, election_id, position_id):
        self.get_candidate_id()
        mysql_cursor.execute("INSERT INTO `gsuCandidateApplication` (`candidateID`, `positionID`, `electionID`) VALUES (%s, %s, %s)", [self._id, position_id, election_id])
        database_connection.commit()
    
    # Get all candidates created.
    def list_candidates(self):
        # Execute MySQL Query
        mysql_cursor.execute("SELECT * FROM `gsuCandidates`")
        
        # Store query_result as all values returned.
        query_result = mysql_cursor.fetchall()
        
        if(mysql_cursor.rowcount == 0):
            # No current applications.
            return False
        else:
            # Return array of all candidates running.
            return query_result
# Define election class.
class Election:
    def __init__(self, start_time="", end_time=""):
        # Define class variables.
        self.start_time = start_time
        self.end_time = end_time
        self._id = ""
        
    # Create a new election time period in the database.
    def create_election(self):
        # Execute MySQL Query, substitute %s with values with student details.
        mysql_cursor.execute("INSERT INTO `gsuElection` (`electionStartTime`, `electionEndTime`) VALUES (%s, %s)", [self.start_time, self.end_time])
        database_connection.commit()
        
        # Return election ID
        return mysql_cursor.lastrowid
    
    # Check status of any election curretly running.
    def get_current_election(self):
        # Execute MySQL Query
        mysql_cursor.execute("SELECT `electionID`, `electionStartTime`, `electionEndTime` FROM `gsuElection` WHERE `electionStartTime` < %s AND `electionEndTime` > %s", [datetime.datetime.now(), datetime.datetime.now()])
        
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
        mysql_cursor.execute("SELECT * FROM `gsuCandidateApplication` WHERE `electionID` = '%s'", [self._id])
        
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
    def get_positions(self):
        # Execute MySQL Query
        
        election = Election()
        election_id = election.get_current_election()
        
        mysql_cursor.execute("SELECT * FROM `gsuPositions`")
        
        # Store query_result as all values returned.
        query_result = mysql_cursor.fetchall()
        
        return query_result
        
    # List all available positions to apply for.
    def get_available_positions(self):
        # Execute MySQL Query
        
        election = Election()
        election_id = election.get_current_election()
        election_id = election_id[0][0]
        
        # Select all positions where they're not in the list containing positions applied for more than 4 times in a given election.
        mysql_cursor.execute("SELECT * FROM `gsuPositions` WHERE `positionID` NOT IN (SELECT `positionID` FROM `gsuCandidateApplication` WHERE `electionID` = %s GROUP BY `positionID` HAVING COUNT(*) = 4)", [election_id])
        
        # Store query_result as all values returned.
        query_result = mysql_cursor.fetchall()
        
        return query_result
        
        
     # List all available positions to apply for.
    def list_available_voting_positions(self, student_id):        
        election = Election()
        election_id = election.get_current_election()
        election_id = election_id[0][0]
        
        # Select all positions where not in election votes from current student.
        mysql_cursor.execute("SELECT * FROM `gsuPositions` WHERE `positionID` NOT IN (SELECT `positionID` FROM `gsuElectionVotes` WHERE `electionID` = %s AND `studentID` = %s)", [election_id, student_id])
        
        # Store query_result as all values returned.
        query_result = mysql_cursor.fetchall()
        
        return query_result
        
        
    # List all candiates for given position in election.
    def list_candidates_for_position(self):        
        election = Election()
        election_id = election.get_current_election()
        election_id = election_id[0][0]
                
        global voting_position
        
        # Select all positions where not in election votes from current student.
        mysql_cursor.execute("SELECT * FROM `gsuCandidateApplication` WHERE `positionID` =  %s AND `electionID` = %s", [election_id, voting_position])
        
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
        
        # Create position instance, append to list the remaining available positions
        positions = Position()
        available_positions = []
        for position in positions.get_available_positions():
            available_positions.append(str(position[0]) + " - " + position[1])
            
        # Create election instance, append to list the election times
        elections = Election()
        current_election = []
        election_compile = elections.get_current_election()
        
        # Format nicely for combo box.
        current_election.append(str(election_compile[0][0]) + " - Start time: " + str(election_compile[0][1]) + " - End Time: " + str(election_compile[0][2]))
        
        # Create candidate instance, append to list the candidate names
        candidates = Candidate()
        available_candidates = []
        for candidate in candidates.list_candidates():
            available_candidates.append(candidate[1])
        
        # Set choices in combo boxes to lists created.
        self.interfaceBuilder.get_object('candidate_application_election_cmbobx').configure(values=current_election)
        self.interfaceBuilder.get_object('candidate_application_candidate_cmbobx').configure(values=available_candidates)
        self.interfaceBuilder.get_object('candidate_application_position_cmbobx').configure(values=available_positions)
        
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
    #              Student Menu Navigation Control              #
    #############################################################
    
    # Exit page within student menu, return to login.
    def return_to_student(self):
        self.change_frame('student_login_frame')
        
    
    
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
        start_date_time = parse(self.interfaceBuilder.get_object('election_start_time_txtbx').get())
        end_date_time = parse(self.interfaceBuilder.get_object('election_end_time_txtbx').get())
        
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
            
            # If password is valid, login, else, inform user.
            if(student_login.verify_password()):
                self.change_frame('student_vote_position_select_frame')
                
                # Set global variables for 'session'
                global logged_in_student
                logged_in_student = student_login.get_student_id()
        
                # Create election instance, append to list the election times
                elections = Election()
                current_election = []
                election_compile = elections.get_current_election()
                
                # Format nicely for combo box.
                current_election.append(str(election_compile[0][0]) + " - Start time: " + str(election_compile[0][1]) + " - End Time: " + str(election_compile[0][2]))
                
                # Create combo box of positions currently available to vote.
                positions = Position()
                position_list = []
                
                
                for position in positions.list_available_voting_positions(student_login.get_student_id()):
                    position_list.append(str(position[0]) + " - " + position[1])
                
                # Set choices in combo boxes to lists created.
                self.interfaceBuilder.get_object('student_vote_confirm_election_cmbobx').configure(values=current_election)
                self.interfaceBuilder.get_object('student_vote_position_cmbobx').configure(values=position_list)
            else:
                # If not unique, inform user to add custom tag to surname (other option is to change name) to help voters.
                self.interfaceBuilder.get_object('student_login_error_lbl').configure(text="Uh Oh! Wrong username or password or you're not eligible to vote!")
            
        else:
            # Else change label text to error message.
            self.interfaceBuilder.get_object('student_login_error_lbl').configure(text="Please ensure you've entered data into both boxes.")
  
    #############################################################
    #                Create Candidate Application               #
    #############################################################
    
    # Submit application for candidate to current available election.
    def submit_application(self):
        # Get user input from the page.
        election = (self.interfaceBuilder.get_object('candidate_application_election_cmbobx').get()).split()[0]
        candidate = self.interfaceBuilder.get_object('candidate_application_candidate_cmbobx').get()
        position = (self.interfaceBuilder.get_object('candidate_application_position_cmbobx').get()).split()[0]
        
        if(election != ""):
            # Election not selected.
            if((candidate != "") or (position != "")):
                # If other values are not selected
                new_application = Candidate(candidate)
                new_application.create_application(election, position)
                self.return_to_backend()
            else:
                # Else change label text to error message.
                self.interfaceBuilder.get_object('candidate_application_error_lbl').configure(text="Please ensure you've selected one value for all options.")
        else:
            # Else change label text to error message.
            self.interfaceBuilder.get_object('candidate_application_error_lbl').configure(text="Election not selected. Unable to apply.")
            
            
    #############################################################
    #                Student Vote Select Position               #
    #############################################################
        
    def vote_select_position(self):
        voting_position_selected = (self.interfaceBuilder.get_object('student_vote_position_cmbobx').get()).split()[0]
        election = (self.interfaceBuilder.get_object('student_vote_confirm_election_cmbobx').get()).split()[0]
        global voting_position
        voting_position = voting_position_selected
        if((voting_position_selected != "") or (election != "")):
            self.change_frame('student_vote_frame')
            position = Position()
            candidate_data = position.list_candidates_for_position()
            if not position.list_candidates_for_position():
                # List returned empty, no candidates.
                self.interfaceBuilder.get_object('student_vote_error_lbl').configure(text="No candidates. Please contact system administrator.")
            else:
                candidate_formatted = []
                for candidate in candidate_data:
                    candidate_temp = Candidate(id=candidate[1])
                    candidate_formatted.append(str(candidate[1]) + " - " + str(candidate_temp.get_candidate_name()))
            self.interfaceBuilder.get_object('student_vote_first_choice_cmbobx').configure(values=candidate_formatted)
            global candidate_list
            candidate_list = candidate_formatted
        else:
            # Else change label text to error message.
            self.interfaceBuilder.get_object('student_vote_position_error_lbl').configure(text="Please ensure you've selected values for both fields.")
           
    
    #############################################################
    #                      Student Vote Place                   #
    #############################################################
        
    def first_choice_confirm(self):
        selected_value = self.interfaceBuilder.get_object('student_vote_first_choice_cmbobx').get()
        if(selected_value != ""):
            global candidate_list
            candidate_list.remove(selected_value)
            candidate_list.append("N/A")
            self.interfaceBuilder.get_object('student_vote_first_choice_btn').configure(state="disabled")
            self.interfaceBuilder.get_object('student_vote_first_choice_cmbobx').configure(state="disabled")
            self.interfaceBuilder.get_object('student_vote_second_choice_btn').configure(state="normal")
            self.interfaceBuilder.get_object('student_vote_second_choice_cmbobx').configure(state="normal", values=candidate_list)
        
    def second_choice_confirm(self):
        selected_value = self.interfaceBuilder.get_object('student_vote_second_choice_cmbobx').get()
        if(selected_value != ""):
            global candidate_list
            if(selected_value != "N/A"):
                candidate_list.remove(selected_value)
            else: 
                candidate_list = ["N/A",]
            self.interfaceBuilder.get_object('student_vote_second_choice_btn').configure(state="disabled")
            self.interfaceBuilder.get_object('student_vote_second_choice_cmbobx').configure(state="disabled")
            self.interfaceBuilder.get_object('student_vote_third_choice_btn').configure(state="normal")
            self.interfaceBuilder.get_object('student_vote_third_choice_cmbobx').configure(state="normal", values=candidate_list)
        
    def third_choice_confirm(self):
        selected_value = self.interfaceBuilder.get_object('student_vote_third_choice_cmbobx').get()
        if(selected_value != ""):
            global candidate_list
            if(selected_value != "N/A"):
                candidate_list.remove(selected_value)
            else: 
                candidate_list = ["N/A",]
            self.interfaceBuilder.get_object('student_vote_third_choice_btn').configure(state="disabled")
            self.interfaceBuilder.get_object('student_vote_third_choice_cmbobx').configure(state="disabled")
            self.interfaceBuilder.get_object('student_vote_fourth_choice_btn').configure(state="normal")
            self.interfaceBuilder.get_object('student_vote_fourth_choice_cmbobx').configure(state="normal", values=candidate_list)
        
    def fourth_choice_confirm(self):
        selected_value = self.interfaceBuilder.get_object('student_vote_fourth_choice_cmbobx').get()
        if(selected_value != ""):
            student = Student()
            global voting_position
            student.cast_votes(voting_position, (self.interfaceBuilder.get_object('student_vote_first_choice_cmbobx').get()).split()[0], (self.interfaceBuilder.get_object('student_vote_second_choice_cmbobx').get()).split()[0],(self.interfaceBuilder.get_object('student_vote_third_choice_cmbobx').get()).split()[0],(self.interfaceBuilder.get_object('student_vote_fourth_choice_cmbobx').get()).split()[0])
        
if __name__ == '__main__':
    tkinter_app = tk.Tk()
    main_application = voting_application(tkinter_app)
    logged_in_student = 0
    candidate_list = 0
    voting_position = 0
    tkinter_app.mainloop()
