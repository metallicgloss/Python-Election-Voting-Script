import mainApplication
from mainApplication import *


#-----------------------------------------------------------------------------------------------------#
#                                               CONTENTS                                              #
#                                      1. Control Class                                               #
#                                      2. Student Class                                               #
#                                      3. Candidate Class                                             #
#                                      4. Election Class                                              #
#                                      5. Position Class                                              #
#                                      6. Results Class                                               #
#-----------------------------------------------------------------------------------------------------#



#-----------------------------------------------------------------------------------------------------#
#                                           1. Control Class                                          #
#-----------------------------------------------------------------------------------------------------#

# Define control class, parent abstract class to define basic required variables and methods for primary classes.
class Control:
    def __init__(self):
        # Define class variables.
        self._select_query_output = ""

#-----------------------------------------------------------------------------------------------------#
#                                           2. Student Class                                          #
#-----------------------------------------------------------------------------------------------------#

# Define student class.
class Student:
    def __init__(self, username="", password=""):
        # Define class variables.
        self.username = username
        self.password = password
        self._id = ""
        self._salt = ""
        self._hashed_password = ""
        self._select_query_output = ""
        
        
    # Insert a new student voter to the system.
    def insert_new_student(self):
        # Generate hash and salt.
        self.generate_hash_password()
        
        # Execute MySQL Query, substitute %s with values with student details.
        mysql_cursor.execute("INSERT INTO `studentVoters` (`studentLogin`, `studentPassword`, `studentSalt`) VALUES (%s, %s, %s)", [self.username, self._hashed_password, self._salt])
        database_connection.commit()
        
        return mysql_cursor.lastrowid
        
    
    # Get student ID
    def get_student_id(self):
        # Execute MySQL Query
        mysql_cursor.execute("SELECT `studentID` FROM `studentVoters` WHERE `studentLogin` = %s", [self.username])
        
        # Store self._select_query_output as all values returned.
        self._select_query_output = mysql_cursor.fetchall()
        
        self._id = self._select_query_output[0][0]
        
        return self._id
    
    
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
        
        # Store self._select_query_output as all values returned.
        self._select_query_output = mysql_cursor.fetchall()
        
        # Set salt to match the salt value returned in the database.
        self._salt = str(self._select_query_output[0][1])
        
        # Re-generate hash using passed provided to see it matches the stored DB value.
        self.get_hashed_password()
        
        # If passwords match, return true, else, false.
        if(self._hashed_password == self._select_query_output[0][0]):
            return True
        else:
            return False

        
    # Verify username does not already exist.
    def verify_unique_username(self):
        # Execute MySQL Query, substitute %s with values with student username.
        mysql_cursor.execute("SELECT `studentLogin` FROM `studentVoters` WHERE `studentLogin` LIKE %s", [self.username])
        
        # Store self._select_query_output as all values returned.
        self._select_query_output = mysql_cursor.fetchall()
        
        if(mysql_cursor.rowcount == 0):
            # No user found.
            return True
        else:
            # User Found
            return False
            
       
    # Submit votes inputted by the user.
    def cast_votes(self, position_id, student_id, candidate_id_one, candidate_id_two, candidate_id_three, candidate_id_four):
        # Initialise election object to get correct current election.
        current_election = Election()
        
        # Execute MySQL insert into the database.
        mysql_cursor.execute("INSERT INTO `gsuElectionVotes` (`studentID`, `electionID`, `positionID`, `firstVoteCandidateID_FK`, `secondVoteCandidateID_FK`, `thirdVoteCandidateID_FK`, `fourthVoteCandidateID_FK`) VALUES (%s, %s, %s, %s, %s, %s, %s)", [student_id, current_election.get_current_election()[0][0], position_id, candidate_id_one, candidate_id_two, candidate_id_three, candidate_id_four])
        database_connection.commit()
   


#-----------------------------------------------------------------------------------------------------#
#                                          3. Candidate Class                                         #
#-----------------------------------------------------------------------------------------------------#

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
        
        # Inform user of successful creation.
        messagebox.showinfo('Success', 'Created successfully.')
            
            
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
        
        # Get name of candidate.
        self.name = query_result[0][0]
        
        return self.name
        
        
    # Create application for the current election.
    def create_application(self, election_id, position_id):
        self.get_candidate_id()
        mysql_cursor.execute("INSERT INTO `gsuCandidateApplication` (`candidateID`, `positionID`, `electionID`) VALUES (%s, %s, %s)", [self.id, position_id, election_id])
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
            
            
    def return_formatted_candidate_list(self):
        available_candidates = []
        for candidate in self.list_candidates():
            available_candidates.append(str(candidate[0]) + " - " + candidate[1])
            
        return available_candidates



#-----------------------------------------------------------------------------------------------------#
#                                          4. Election Class                                          #
#-----------------------------------------------------------------------------------------------------#
        
# Define election class.
class Election:
    def __init__(self, start_time="", end_time=""):
        # Define class variables.
        self.start_time = start_time
        self.end_time = end_time
        self._id = ""
        
        
    def return_formatted_elections(self):
        current_election = []
        election_compile = self.get_current_election()
        
        # Format nicely for combo box.
        current_election.append(str(election_compile[0][0]) + " - Start time: " + str(election_compile[0][1]) + " - End Time: " + str(election_compile[0][2]))
        return current_election
    
    
    # Create a new election time period in the database.
    def create_election(self):
        # Execute MySQL Query, substitute %s with values with student details.
        mysql_cursor.execute("INSERT INTO `gsuElection` (`electionStartTime`, `electionEndTime`) VALUES (%s, %s)", [self.start_time, self.end_time])
        database_connection.commit()
        
        # Inform user of successful creation.
        messagebox.showinfo('Success', 'Created successfully.')
    
    
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

            
 
#-----------------------------------------------------------------------------------------------------#
#                                          5. Position Class                                          #
#-----------------------------------------------------------------------------------------------------#

# Define position class.
class Position:
    def __init__(self, start_time="", end_time=""):
        # Define class variables.
        self.start_time = start_time
        self.end_time = end_time
        self._id = ""
        
        
    # Return list of positions available formatted for a combobox.
    def list_all_available_positions_formatted(self):
        available_positions = []
        for position in self.get_available_positions():
            available_positions.append(str(position[0]) + " - " + position[1])
            
        return available_positions
        
    def list_all_positions_formatted(self):
        available_positions = []
        for position in self.list_all_positions():
            available_positions.append(str(position[0]) + " - " + position[1])
            
        return available_positions
        
        
    # List all positions currently in the GSU.
    def list_all_positions(self):
        # Execute MySQL Query to get all positions
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
    def list_candidates_for_position(self, voting_position):        
        election = Election()
        election_id = election.get_current_election()
        election_id = election_id[0][0]
        
        # Select all positions where not in election votes from current student.
        mysql_cursor.execute("SELECT * FROM `gsuCandidateApplication` WHERE `positionID` =  %s AND `electionID` = %s", [election_id, voting_position])
        
        # Store query_result as all values returned.
        query_result = mysql_cursor.fetchall()

        
        return query_result
        
        
        
#-----------------------------------------------------------------------------------------------------#
#                                           6. Results Class                                          #
#-----------------------------------------------------------------------------------------------------#

# Define results class.
class Results:
    def __init__(self, election_id="", position_id=""):
        # Define class variables.
        self.election_id = election_id
        self.position_id = position_id
     
    # Return array for counted votes
    def get_count(self, candidate, votes):
        # Initialise function specific variables.
        first_preference = 0
        second_preference = 0
        third_preference = 0
        fourth_preference = 0
        
        for vote in votes:
            if(candidate == vote[0]):
                first_preference += 1
            elif(candidate == vote[1]):
                second_preference += 1
            elif(candidate == vote[2]):
                third_preference += 1
            elif(candidate == vote[3]):
                fourth_preference += 1
                
        # Get candidate name
        candidate = Candidate(id=candidate)
        
        
        return [candidate.get_candidate_name(), first_preference, second_preference, third_preference, fourth_preference]
        
    # Return list of the final results.
    def get_election_results(self, position_id):
        election = Election()
        election_id = election.get_current_election()
        election_id = election_id[0][0]
        
        # Select results for the position provided.
        mysql_cursor.execute("SELECT `firstVoteCandidateID_FK`, `secondVoteCandidateID_FK`, `thirdVoteCandidateID_FK`, `fourthVoteCandidateID_FK` FROM `gsuElectionVotes` WHERE `electionID` = %s AND `positionID` = %s", [election_id, position_id])
                
        # Store query_result as all values returned.
        query_result = mysql_cursor.fetchall()
        
        # Get list of candidates applied for position.
        positions = Position()
        candidates = positions.list_candidates_for_position(position_id)
        
        first = self.get_count(candidates[0][1], query_result)
        second = self.get_count(candidates[1][1], query_result)
        third = self.get_count(candidates[2][1], query_result)
        fourth = self.get_count(candidates[3][1], query_result)
        winner = ""
        totalvotesforwinner = 0
        totalpositionvotes = 0
        
        
        
        ##################################################################
        #                                                                #
        #        Calculating the output for the final vote screen        #
        #                                                                #
        ##################################################################
        
        
        for x in range(1,5):
            if first[x] != second[x] and first[x] != third[x] and first[x] != fourth[x] and second[x] != third[x] and second[x] != fourth[x] and third[x] != fourth[x]:
                pass  #Check whether two candidates have the same number of votes, if they do it will go to the next level of votes
            else:
                if first[x] > second[x] and first[x] > third[x] and first[x] > fourth[x]:
                    winner = first[0]
                    totalvotesforwinner = first[1] + first[2] + first[3] + first[4]
                    break #Find the winner and the total votes for that person
                elif second[x] > first[x] and second[x] > third[x] and second[x] > fourth[x]:
                    winner = second[0]
                    totalvotesforwinner = second[1] + second[2] + second[3] + second[4]
                    break
                elif third[x] > first[x] and thrid[x] > second[x] and third[x] > fourth[x]:
                    winner = third[0]
                    totalvotesforwinner = third[1] + third[2] + third[3] + third[4]
                    break
                elif fourth[x] > first[x] and fourth[x] > second[x] and fourth[x] > third[x]:
                    winner = fourth[0]
                    totalvotesforwinner = fourth[1] + fourth[2] + fourth[3] + fourth[4]
                    break
            
        totalpositionvotes = first[1] + second[1] + third[1] + fourth[1] + first[2] + second[2] + third[2] + fourth[2] + first[3] + second[3] + third[3] + fourth[3] + first[4] + second[4] + third[4] + fourth[4]
        
        return [first, second, third, fourth, winner, str(totalvotesforwinner),str(totalpositionvotes)]

    
        
    # Return list of the final results & formatting data for per-position results.
    def get_position_results(self, position_id):
        # Select results for the position provided.
        mysql_cursor.execute("SELECT `firstVoteCandidateID_FK`, `secondVoteCandidateID_FK`, `thirdVoteCandidateID_FK`, `fourthVoteCandidateID_FK` FROM `gsuElectionVotes` WHERE `electionID` = %s AND `positionID` = %s", [self.election_id, self.position_id])
        
        # Store query_result as all values returned.
        query_result = mysql_cursor.fetchall()
        
        positions = Position()
        candidates_list = positions.list_candidates_for_position()
        
        self.calculate_result_score(candidates_list[0][1], query_result)
        
        
    # Return list to user interface to allow the user to visualise the results for positions they've already voted. 
    def show_visualised_results(self):
        
        root = tk.Tk()
        root.title("Bar Graph")

        c_width = 400  # Define it's width
        c_height = 350  # Define it's height
        c = tk.Canvas(root, width=c_width, height=c_height, bg='white')
        c.pack()

        # The variables below size the bar graph
        y_stretch = 15  # The highest y = max_data_value * y_stretch
        y_gap = 20  # The gap between lower canvas edge and x axis
        x_stretch = 10  # Stretch x wide enough to fit the variables
        x_width = 20  # The width of the x-axis
        x_gap = 20  # The gap between left canvas edge and y axis

        # A quick for loop to calculate the rectangle
        for x, y in enumerate(candidates):

            # coordinates of each bar

            # Bottom left coordinate
            x0 = x * x_stretch + x * x_width + x_gap

            # Top left coordinates
            y0 = c_height - (y * y_stretch + y_gap)

            # Bottom right coordinates
            x1 = x * x_stretch + x * x_width + x_width + x_gap

            # Top right coordinates
            y1 = c_height - y_gap

            # Draw the bar
            c.create_rectangle(x0, y0, x1, y1, fill="blue")

            # Put the y value above the bar
            c.create_text(x0 + 2, y0, anchor=tk.SW, text=str(y))

        root.mainloop()

