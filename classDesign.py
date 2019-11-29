import mainApplication
from mainApplication import *


#-----------------------------------------------------------------------------------------------------#
#                                               CONTENTS                                              #
#                                      1. Student Class                                               #
#                                      2. Candidate Class                                             #
#                                      3. Election Class                                              #
#                                      4. Position Class                                              #
#                                      5. Results Class                                               #
#-----------------------------------------------------------------------------------------------------#



#-----------------------------------------------------------------------------------------------------#
#                                           1. Student Class                                          #
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
            
            
    def cast_votes(self, position_id, candidate_id_one, candidate_id_two, candidate_id_three, candidate_id_four):
        current_election = Election()
        global logged_in_student
        mysql_cursor.execute("INSERT INTO `gsuElectionVotes` (`studentID`, `electionID`, `positionID`, `firstVoteCandidateID_FK`, `secondVoteCandidateID_FK`, `thirdVoteCandidateID_FK`, `fourthVoteCandidateID_FK`) VALUES (%s, %s, %s, %s, %s, %s, %s)", [logged_in_student, current_election.get_current_election()[0][0], position_id, candidate_id_one, candidate_id_two, candidate_id_three, candidate_id_four])
        database_connection.commit()
   


#-----------------------------------------------------------------------------------------------------#
#                                          2. Candidate Class                                         #
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
#                                          3. Election Class                                          #
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

            
 
#-----------------------------------------------------------------------------------------------------#
#                                          4. Position Class                                          #
#-----------------------------------------------------------------------------------------------------#

# Define position class.
class Position:
    # No init class due to its very simple nature, just returning available positions.
    
    def list_formatted_positions(self):
        available_positions = []
        for position in self.get_available_positions():
            available_positions.append(str(position[0]) + " - " + position[1])
            
        return available_positions
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
    def list_positions(self):
        # Execute MySQL Query
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
#                                           5. Results Class                                          #
#-----------------------------------------------------------------------------------------------------#

# Define results class.
class Results:
    def __init__(self, election_id="", position_id=""):
        # Define class variables.
        self.election_id = election_id
        self.position_id = position_id
        self._first_candidate = ""
        self._second_candidate = ""
        self._third_candidate = ""
        self._fourth_candidate = ""
        
        
        self._first_candidate_count = 0
        self._second_candidate_count = 0
        self._third_candidate_count = 0
        self._fourth_candidate_count = 0
     
     
    def calculate_result_score(self, candidate, votes):
        count = 0
        for vote in votes:
            if(candidate == vote[0]):
                count += 4
            elif(candidate == vote[1]):
                count += 3
            elif(candidate == vote[2]):
                count += 2
            elif(candidate == vote[3]):
                count += 1
        
        return [candidate, count]
        
        
    # Return list of the final results & formatting data for per-position results.
    def get_position_results(self):
    
        # Select results for the position provided.
        mysql_cursor.execute("SELECT `firstVoteCandidateID_FK`, `secondVoteCandidateID_FK`, `thirdVoteCandidateID_FK`, `fourthVoteCandidateID_FK` FROM `gsuElectionVotes` WHERE `electionID` = %s AND `positionID` = %s", [self.election_id, self.position_id])
        
        # Store query_result as all values returned.
        query_result = mysql_cursor.fetchall()
        
        global voting_position
        voting_position = self.position_id
        
        positions = Position()
        candidates_list = positions.list_candidates_for_position()
        
        self._first_candidate, self._first_candidate_count = self.calculate_result_score(candidates_list[0][1], query_result)
        self._second_candidate, self._second_candidate_count = self.calculate_result_score(candidates_list[1][1], query_result)
        self._third_candidate, self._third_candidate_count = self.calculate_result_score(candidates_list[2][1], query_result)
        self._fourth_candidate, self._fourth_candidate_count = self.calculate_result_score(candidates_list[3][1], query_result)
        
        compiled_list = [[self._first_candidate, self._first_candidate_count], [self._second_candidate, self._second_candidate_count], [self._third_candidate, self._third_candidate_count], [self._fourth_candidate, self._fourth_candidate_count]]
        
        return compiled_list
        
        
    # Return list to user interface to allow the user to visualise the results for positions they've already voted. 
    def show_visualised_results(self):
        pass