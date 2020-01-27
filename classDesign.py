import mainApplication
from mainApplication import *


# --------------------------------------------------------------------------- #
#                                  CONTENTS                                   #
#                            1. Person Class                                  #
#                            2. Student Class                                 #
#                            3. Candidate Class                               #
#                            4. Election Class                                #
#                            5. Position Class                                #
#                            6. Results Class                                 #
# --------------------------------------------------------------------------- #


# --------------------------------------------------------------------------- #
#                              1. Person Class                                #
#                                                                             #
#                                  insert_new                                 #
#        Creates a function that must be implemented by child classes.        #
#                                                                             #
#                                    get_id                                   #
#        Creates a function that must be implemented by child classes.        #
# --------------------------------------------------------------------------- #

# Define person class
# Set basic required variables and methods for primary classes.
class Person:
    def __init__(self):
        # Define class variables.
        self._select_query_output = ""

    # Insert new to database.
    def insert_new(self):
        raise NotImplementedError("Subclass must implement abstract method.")

    # Get ID of object, not required.
    def get_id(self):
        raise NotImplementedError("Subclass must implement abstract method.")

# --------------------------------------------------------------------------- #
#                              2. Student Class                               #
#                          Inherits from Person class                         #
#                                                                             #
#                                  insert_new                                 #
#        Calls generate hash function, inserts new student to database.       #
#                                                                             #
#                                    get_id                                   #
#           Returns the ID of the student, querying by the username.          #
#                                                                             #
#                            generate_hash_password                           #
#      Generates hash and salt for given plaintext password for storage.      #
#                                                                             #
#                              get_hashed_password                            #
#                  Uses premade salt to re-gen password hash.                 #
#                                                                             #
#                               verify_password                               #
#             Queries db, uses stored data to validate user login.            #
#                                                                             #
#                            verify_unique_username                           #
#             Queries db, checks if username has been used before.            #
#                                                                             #
#                                  cast_votes                                 #
#         Submits parameters passed to as election vote for position.         #
# --------------------------------------------------------------------------- #

# Define student class that inherits from the abstract class Control.
class Student(Person):

    # Initialise student class.
    def __init__(self, username="", password=""):
        Person.__init__(self)
        # Define class variables.
        self.username = username
        self.password = password
        self._id = ""
        self._salt = ""
        self._hashed_password = ""

    # Insert a new student voter to the system.
    def insert_new(self):
        # Generate hash and salt.
        self.generate_hash_password()

        # Execute MySQL Query, substitute %s with values with student details.
        mysql_cursor.execute(
            "INSERT INTO `studentVoters` \
            (`studentLogin`, `studentPassword`, `studentSalt`) \
            VALUES (%s, %s, %s)",
            [self.username, self._hashed_password, self._salt]
        )
        db_connect.commit()

        # Return ID for use if required.
        return mysql_cursor.lastrowid

    # Get student ID
    def get_id(self):
        # Execute MySQL Query
        mysql_cursor.execute(
            "SELECT `studentID` FROM `studentVoters` WHERE \
                `studentLogin` = %s",
            [self.username]
        )

        # Store self._select_query_output as all values returned.
        self._select_query_output = mysql_cursor.fetchall()

        # Set the ID of the student from the query.
        self._id = self._select_query_output[0][0]

        # Return the ID.
        return self._id

    # Generate and store new hashed password
    def generate_hash_password(self):
        # Generate random salt key using hashlib, a random string generated.
        self._salt = hashlib.sha256(os.urandom(64)).hexdigest().encode('ascii')

        # Generate hashed version of the password converted to hex.
        # Use hashlib to create an SHA512 password with the random salt.
        self._hashed_password = binascii.hexlify(
            hashlib.pbkdf2_hmac(
                'sha512',
                self.password.encode('utf-8'),
                self._salt,
                100000
            )
        )

    # Generate and return hashed password
    def get_hashed_password(self):
        # Re-calculate generated hashed version of the pass converted to hex.
        self._hashed_password = (binascii.hexlify(
            hashlib.pbkdf2_hmac(
                'sha512',
                (self.password).encode('utf-8'),
                (self._salt).encode('ascii'),
                100000
            )
        )).decode('ascii')

    # Verify password
    def verify_password(self):
        # Execute MySQL Query to get password and hash.
        mysql_cursor.execute(
            "SELECT `studentPassword`, `studentSalt` \
            FROM `studentVoters` \
            WHERE `studentLogin` = %s",
            [self.username]
        )

        # Store self._select_query_output as all values returned.
        self._select_query_output = mysql_cursor.fetchall()

        try:
            # Set salt to match the salt value returned in the database.
            self._salt = str(self._select_query_output[0][1])

            # Re-gen hash using passed given to see it matches the stored DB value.
            self.get_hashed_password()

            # If passwords match, return true, else, false.
            if(self._hashed_password == self._select_query_output[0][0]):
                return True
            else:
                return False
        except IndexError:
            # Query returned index error when attempting to select user.
            # Username not known.
            return False

    # Verify username does not already exist.
    def verify_unique_username(self):
        # Execute MySQL Query, substitute %s with values with student username.
        mysql_cursor.execute(
            "SELECT `studentLogin` \
            FROM `studentVoters` \
            WHERE `studentLogin` LIKE %s",
            [self.username]
        )

        # Store self._select_query_output as all values returned.
        self._select_query_output = mysql_cursor.fetchall()

        if(mysql_cursor.rowcount == 0):
            # No user found.
            return True
        else:
            # User Found
            return False

    # Submit votes inputted by the user.
    def cast_votes(
        self,
        position_id,
        student_id,
        candidate_id_one,
        candidate_id_two,
        candidate_id_three,
        candidate_id_four
    ):

        # Initialise election object to get correct current election.
        current_election = Election()

        # Execute MySQL insert into the database.
        mysql_cursor.execute(
            "INSERT INTO `gsuElectionVotes` \
            (`studentID`, `electionID`, `positionID`, \
            `firstVoteCandidateID_FK`, `secondVoteCandidateID_FK`, \
            `thirdVoteCandidateID_FK`, `fourthVoteCandidateID_FK`) \
            VALUES (%s, %s, %s, %s, %s, %s, %s)",
            [
                student_id,
                current_election.get_current_election()[0][0],
                position_id,
                candidate_id_one,
                candidate_id_two,
                candidate_id_three,
                candidate_id_four
            ]
        )

        # Save changes to the database.
        db_connect.commit()

# --------------------------------------------------------------------------- #
#                              3. Candidate Class                             #
#                          Inherits from Person class                         #
#                                                                             #
#                                  insert_new                                 #
#                      Inserts new candidate to database.                     #
#                                                                             #
#                                    get_id                                   #
#            Returns the ID of the candidate, querying by the name.           #
#                                                                             #
#                                     list                                    #
#                     List all candidates in the database.                    #
#                                                                             #
#                              verify_unique_name                             #
#               Queries db, checks if name has been used before.              #
#                                                                             #
#                              get_candidate_name                             #
#            Returns candidate name, queries db by by candidate id.           #
#                                                                             #
#                              create_application                             #
#           Creates candidate application for an election position.           #
# --------------------------------------------------------------------------- #

# Define candidate class.
class Candidate(Person):

    # Initialise candidate class.
    def __init__(self, name="", email="", id=""):
        Person.__init__(self)
        # Define class variables.
        self.name = name
        self.email = email
        self.id = id
        self._position = ""

    # Insert a new candidate to the system.
    def insert_new(self):
        # Execute MySQL Query, substitute %s with values with student details.
        mysql_cursor.execute(
            "INSERT INTO `gsuCandidates` \
            (`candidateName`, `candidateEmail`) \
            VALUES (%s, %s)",
            [self.name, self.email]
        )
        db_connect.commit()

        # Inform user of successful creation.
        messagebox.showinfo('Success', 'Created successfully.')

    # Perform verification on student login credentials to database.
    def get_id(self):
        # Execute MySQL Query
        mysql_cursor.execute(
            "SELECT `candidateID` \
            FROM `gsuCandidates` \
            WHERE `candidateName` = %s",
            [self.name]
        )

        # Store query_result as all values returned.
        query_result = mysql_cursor.fetchall()
        
        self.id = query_result[0][0]

    # Get all candidates created.
    def list(self):
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

    # Verify candidate does not have name matching another.
    def verify_unique_name(self):
        # Execute MySQL Query, substitute %s with values with student username.
        mysql_cursor.execute(
            "SELECT `candidateName` \
            FROM `gsuCandidates` \
            WHERE `candidateName` = %s",
            [self.name]
        )

        # Store query_result as all values returned.
        query_result = mysql_cursor.fetchall()

        if(mysql_cursor.rowcount == 0):
            # No user found.
            return True
        else:
            # User Found
            return False

    # Perform verification on student login credentials to database.
    def get_candidate_name(self):
        # Execute MySQL Query
        mysql_cursor.execute(
            "SELECT `candidateName` \
            FROM `gsuCandidates` \
            WHERE `candidateID` = %s",
            [self.id]
        )

        # Store query_result as all values returned.
        query_result = mysql_cursor.fetchall()

        # Get name of candidate.
        self.name = query_result[0][0]

        return self.name

    # Create application for the current election.
    def create_application(self, candidate_id, election_id, position_id):
        mysql_cursor.execute(
            "INSERT INTO `gsuCandidateApplication` \
            (`candidateID`, `positionID`, `electionID`) \
            VALUES (%s, %s, %s)",
            [candidate_id, position_id, election_id]
        )
        db_connect.commit()

# --------------------------------------------------------------------------- #
#                              4. Election Class                              #
#                                                                             #
#                                list_formatted                               #
#            List the current election in a format for comboboxes.            #
#                                                                             #
#                               create_election                               #
#             Create a new election and submit it to the database.            #
#                                                                             #
#                             get_current_election                            #
#         Query the database and return the current election running.         #
# --------------------------------------------------------------------------- #

# Define election class.
class Election:

    # Initialise election class.
    def __init__(self, start_time="", end_time=""):
        # Define class variables.
        self.start_time = start_time
        self.end_time = end_time
        self._id = ""

    def list_formatted(self):
        current_election = []
        election_compile = self.get_current_election()

        # Format nicely for combo box.
        current_election.append(
            str(election_compile[0][0])
            + " - Start time: "
            + str(election_compile[0][1])
            + " - End Time: "
            + str(election_compile[0][2])
        )
        return current_election

    # Create a new election time period in the database.
    def create_election(self):
        # Execute MySQL Query, substitute %s with values with student details.
        mysql_cursor.execute(
            "INSERT INTO `gsuElection` \
            (`electionStartTime`, `electionEndTime`) \
            VALUES (%s, %s)",
            [self.start_time, self.end_time]
        )
        db_connect.commit()

        # Inform user of successful creation.
        messagebox.showinfo('Success', 'Created successfully.')

    # Check status of any election currently running.
    def get_current_election(self):
        # Execute MySQL Query
        mysql_cursor.execute(
            "SELECT `electionID`, `electionStartTime`, `electionEndTime` \
            FROM `gsuElection` \
            WHERE `electionStartTime` < %s \
            AND `electionEndTime` > %s",
            [
                datetime.now(),
                datetime.now()
            ]
        )

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
        mysql_cursor.execute(
            "SELECT * \
            FROM `gsuCandidateApplication` \
            WHERE `electionID` = '%s'",
            [self._id]
        )

        # Store query_result as all values returned.
        query_result = mysql_cursor.fetchall()

        if(mysql_cursor.rowcount == 0):
            # No current applications.
            return False
        else:
            # Return array of all candidates running.
            return query_result

# --------------------------------------------------------------------------- #
#                              5. Position Class                              #
#                                                                             #
#                              list_all_positions                             #
#               Lists all positions stored within the database.               #
#                                                                             #
#                        list_positions_open_for_apps                         #
#   Lists all positions still available to be applied for in the election.    #
#                                                                             #
#                       list_available_voting_positions                       #
#     Lists all positions that the student is currently able to vote for.     #
#                                                                             #
#                           list_election_positions                           #
#     Lists all positions running and with 4 candidates in the election.      #
#                                                                             #
#                              list_for_position                              #
#                 Lists all candidates for a given position.                  #
# --------------------------------------------------------------------------- #

# Define position class.
class Position:

    # Initialise position class.
    def __init__(self):
        # Define class variables.
        self._select_query_output = ""

    # List all positions currently in the GSU.
    def list_all_positions(self):
        # Execute MySQL Query to get all positions
        mysql_cursor.execute("SELECT * FROM `gsuPositions`")

        # Store _select_query_output as all values returned.
        self._select_query_output = mysql_cursor.fetchall()

        return self._select_query_output

    # Return list of positions not at max candidates.
    def list_positions_open_for_apps(self):
        # Execute MySQL Query

        election = Election()
        election_id = election.get_current_election()
        election_id = election_id[0][0]

        # Select all positions where they're not in the list containing
        # positions applied for more than 4 times in a given election.
        mysql_cursor.execute(
            "SELECT * \
            FROM `gsuPositions` \
            WHERE `positionID` NOT IN \
            (SELECT `positionID` FROM `gsuCandidateApplication` \
            WHERE `electionID` = %s \
            GROUP BY `positionID` HAVING COUNT(*) = 4)",
            [election_id]
        )

        # Store _select_query_output as all values returned.
        self._select_query_output = mysql_cursor.fetchall()

        return self._select_query_output


    # Return list of positions for a position that the student hasn't for yet.
    def list_available_voting_positions(self, student_id):
        election = Election()
        election_id = election.get_current_election()
        election_id = election_id[0][0]

        # Select all positions that the user hasn't voted for,
        # and the position has 4 candidates.
        mysql_cursor.execute(
            "SELECT * \
            FROM `gsuPositions` \
            WHERE `positionID` NOT IN \
            (SELECT `positionID` \
            FROM `gsuElectionVotes` \
            WHERE `electionID` = %s \
            AND `studentID` = %s) \
            AND `positionID` IN \
            (SELECT `positionID` \
            FROM `gsuCandidateApplication` \
            WHERE `electionID` = %s\
            GROUP BY `positionID`\
            HAVING COUNT(*) = 4)",
            [
                election_id,
                student_id,
                election_id
            ]
        )

        # Store _select_query_output as all values returned.
        self._select_query_output = mysql_cursor.fetchall()

        return self._select_query_output

    # Return list of positions with candidates in an election.
    def list_election_positions(self):
        election = Election()
        election_id = election.get_current_election()
        election_id = election_id[0][0]

        # Select all positions that the user hasn't voted for,
        # and the position has 4 candidates.
        mysql_cursor.execute(
            "SELECT * \
            FROM `gsuPositions` \
            WHERE `positionID` IN \
            (SELECT `positionID` \
            FROM `gsuCandidateApplication` \
            WHERE `electionID` = %s\
            GROUP BY `positionID`\
            HAVING COUNT(*) = 4)",
            [
                election_id
            ]
        )

        # Store _select_query_output as all values returned.
        self._select_query_output = mysql_cursor.fetchall()

        return self._select_query_output

    # List all candidates for given position in election.
    def list_for_position(self, voting_position):
        election = Election()
        election_id = election.get_current_election()
        election_id = election_id[0][0]

        # Select all positions where not in election votes from current student
        mysql_cursor.execute(
            "SELECT * \
            FROM `gsuCandidateApplication` \
            WHERE `positionID` =  %s \
            AND `electionID` = %s",
            [voting_position, election_id]
        )

        # Store _select_query_output as all values returned.
        self._select_query_output = mysql_cursor.fetchall()

        return self._select_query_output

# --------------------------------------------------------------------------- #
#                              6. Results Class                               #
#                                                                             #
#                                  get_count                                  #
#              Return count of preference for candidate passed.               #
#                                                                             #
#                           generate_invalid_count                            #
#                     Return data for invalid vote count.                     #
#                                                                             #
#                            get_election_results                             #
#             Get results for every position within an election.              #
#                                                                             #
#                            get_pos_total_results                            #
#                      Get results for a given position.                      #
#                                                                             #
#                             get_position_winner                             #
#                   Return the winner for a given position.                   #
#                                                                             #
#                          generate_preference_data                           #
#          Return preference votes from the database for candidate.           #
#                                                                             #
#                           calculate_highest_votes                           #
#               Lists all positions stored within the database.               #
# --------------------------------------------------------------------------- #

# Define results class.
class Results:

    # Initialise results class.
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

        # If candidate is in vote position, add 1 to preference accordingly
        for vote in votes:
            if(candidate == vote[0]):
                first_preference += 1
            elif(candidate == vote[1]):
                second_preference += 1
            elif(candidate == vote[2]):
                third_preference += 1
            elif(candidate == vote[3]):
                fourth_preference += 1

        # Add all preferences to get total votes.
        total_votes = first_preference + second_preference + third_preference \
            + fourth_preference

        # Get candidate name
        candidate = Candidate(id=candidate)

        return [
            candidate.get_candidate_name(),
            first_preference,
            second_preference,
            third_preference,
            fourth_preference,
            total_votes
        ]

    def generate_invalid_count(self):
        # If tie, generate invalid.
        return ["Invalid Vote", 0, 0, 0, 0, 0]

    def get_election_results(self):
        # Get list of all positions.
        positions = classDesign.Position()
        position_list = positions.list_all_positions()

        output_data = ""

        # For every position, get the total votes from position total.
        for position in position_list:
            try:
                totals = self.get_pos_total_results(position[0])
                output_data += position[1] + " - " + totals[4] + "\n"
            except IndexError:
                break

        # Return formatted data with winner of each position in election.
        return output_data

    # Return list of the final results for given position.
    def get_pos_total_results(self, position_id):
        ########################################################################################################
        if(position_id in ['1', '2', '5']):
            # Hackathon task, based only on the CSV file provider not database
            with open('fred.csv', newline='') as csvfile:
                # Open CSV file and store data as data.
                data = list(csv.reader(csvfile))

            candidates = []
            totalpositionvotes = 0
            
            # Implimenting 1st preference vote method, data sample has no tie
            # so will not use STV as in original spec. Sub-task not requested.
            winner_first = 0
            winner_second = 0
            winner_third = 0
            winner_fourth = 0
            
            for result in data:
                # For each line in the database (result), use to calculate.
                if((position_id == '1') and (result[3] == "President")):
                    # Append candidate to seperate list if running for pos.
                    candidates.append(result)
                    
                    # Add all candidate votes to build total
                    totalpositionvotes += int(result[4]) + int(result[5]) \
                    + int(result[6]) + int(result[7])
                    
                    if(int(result[4]) > winner_first):
                        winner_first = int(result[4])
                        winner_second = int(result[5])
                        winner_third = int(result[6])
                        winner_fourth = int(result[7])
                        winner_id = int(result[0])
                elif((position_id == '2') and (result[3] == "GSU Officer")):
                    # Append candidate to seperate list if running for pos.
                    candidates.append(result)
                    
                    # Add all candidate votes to build total
                    totalpositionvotes += int(result[4]) + int(result[5]) \
                    + int(result[6]) + int(result[7])
                    
                    if(int(result[4]) > winner_first):
                        winner_first = int(result[4])
                        winner_second = int(result[5])
                        winner_third = int(result[6])
                        winner_fourth = int(result[7])
                        winner_id = int(result[0])
                elif(
                    (position_id == '5') 
                    and (result[3] == "FLAS Faculty Officer")
                ):
                    # Append candidate to seperate list if running for pos.
                    candidates.append(result)
                    
                    # Add all candidate votes to build total
                    totalpositionvotes += int(result[4]) + int(result[5]) \
                    + int(result[6]) + int(result[7])
                    
                    if(int(result[4]) > winner_first):
                        winner_first = int(result[4])
                        winner_second = int(result[5])
                        winner_third = int(result[6])
                        winner_fourth = int(result[7])
                        winner_id = int(result[0])
            
            # Form list of data to allow integration into existing interface
            # functionality.
            #
            # Firstname Lastname, 1st, 2nd, 3rd, 4th
            first = [
                candidates[0][1] + " " + candidates[0][2], 
                candidates[0][4], 
                candidates[0][5], 
                candidates[0][6], 
                candidates[0][7]
            ]
            second = [
                candidates[1][1] + " " + candidates[1][2],
                candidates[1][4], 
                candidates[1][5], 
                candidates[1][6], 
                candidates[1][7]
            ]
            third = [
                candidates[2][1] + " " + candidates[2][2],
                candidates[2][4],
                candidates[2][5],
                candidates[2][6],
                candidates[2][7]
            ]
            fourth = [
                candidates[3][1] + " " + candidates[3][2],
                candidates[3][4],
                candidates[3][5],
                candidates[3][6],
                candidates[3][7]
            ]
                  
            winner_id_index = [int(i[0]) for i in candidates].index(winner_id)
            the_winner = candidates[winner_id_index][1] \
                + " " + candidates[winner_id_index][2]

            # Return data on all candidates to help with formatting to screen.
            return [
                first,
                second,
                third,
                fourth,
                the_winner,
                str(
                    winner_first \
                    + winner_second \
                    + winner_third \
                    + winner_fourth
                ),
                str(totalpositionvotes)
            ]
            ###################################################################################################
        else:
            election = Election()
            election_id = election.get_current_election()
            election_id = election_id[0][0]

            # Select results for the position provided.
            mysql_cursor.execute(
                "SELECT `firstVoteCandidateID_FK`, `secondVoteCandidateID_FK`, \
                `thirdVoteCandidateID_FK`, `fourthVoteCandidateID_FK` \
                FROM `gsuElectionVotes` \
                WHERE `electionID` = %s \
                AND `positionID` = %s",
                [
                    election_id,
                    position_id
                ]
            )

            # Store query_result as all values returned.
            query_result = mysql_cursor.fetchall()

            # Get list of candidates applied for position.
            positions = Position()
            candidates = positions.list_for_position(position_id)

            # Call function to get the winner details.
            winner = self.get_position_winner(position_id)
            
            # If winner and vote is 0, return invalid vote (complete tie).
            # Means that first, second, third and fourth prefs are the same.
            if(((winner[0]) and (winner[1])) == 0):
                return [
                    self.generate_invalid_count(),
                    self.generate_invalid_count(),
                    self.generate_invalid_count(),
                    self.generate_invalid_count(),
                    "Invalid Vote",
                    "Invalid Vote",
                    "Invalid Vote"
                ]

            # Get the vote count for each preference based on the above query.
            winer_count = self.get_count(winner[0], query_result)
            first = self.get_count(candidates[0][1], query_result)
            second = self.get_count(candidates[1][1], query_result)
            third = self.get_count(candidates[2][1], query_result)
            fourth = self.get_count(candidates[3][1], query_result)

            # Add together all votes to calculate total votes for every candidate
            # First, second, third and fourth preferences.
            totalpositionvotes = first[1] + second[1] + third[1] + fourth[1] \
                + first[2] + second[2] + third[2] + fourth[2] + first[3] \
                + second[3] + third[3] + fourth[3] + first[4] + second[4] \
                + third[4] + fourth[4]

            # If winner scored 0 votes, then no winner as no votes.
            if(winer_count[5] == 0):
                the_winner = "No Winner - No Votes"
            else:
                the_winner = winner[1]
            
            
            # Return data on all candidates to help with formatting to screen.
            return [
                first,
                second,
                third,
                fourth,
                the_winner,
                str(winer_count[5]),
                str(totalpositionvotes)
            ]

    # Return list of the winner results for given position.
    def get_position_winner(self, position_id):
        # Get current election ID.
        election = Election()
        election_id = election.get_current_election()
        election_id = election_id[0][0]

        position = Position()
        candidate_list = position.list_for_position(position_id)

        # Select results for the position provided.
        mysql_cursor.execute(
            "SELECT `firstVoteCandidateID_FK` \
            FROM `gsuElectionVotes` \
            WHERE `electionID` = %s \
            AND `positionID` = %s",
            [
                election_id,
                position_id
            ]
        )
        
        # In PEP8 format, the following block of code looks extremely nasty.
        # In summary, the following section of code does:
        # 1. Calculates the winners of the 1st preference votes.
        # 2. If there are more than one, calculate the 2nd preference votes
        #    based only on the new list of candidates that won the 1st pref.
        # 3. If more than one in 2nd pref, repeat with new list of candidates
        #    on the 3rd preference.
        # 4. If more than one in 3rd pref, repeat with new list of candidates
        #    on the 4th.
        # 5. If 4th preference has more than 2 winners, then call a null vote.
        # NB: If a winner is found at any pref, skip other checks.
        
        # Get highest candidates in first preference.
        highest_first_preference = self.calculate_highest_votes(
            mysql_cursor.fetchall(),
            candidate_list
        )

        if len(highest_first_preference[0]) > 1:
            # If there are more than one candidates that had the same highest
            # number of votes.
            
            # Generate a new set of pref data for just the remaining candidates
            candidates_tied = self.generate_preference_data(
                highest_first_preference[0],
                "secondVoteCandidateID_FK",
                election_id,
                position_id,
                candidate_list
            )

            # Get highest candidates in second preference from new list.
            highest_second_preference = self.calculate_highest_votes(
                candidates_tied,
                candidate_list
            )

            if len(highest_second_preference[0]) > 1:
                # If there are more than one candidates that had the same 
                # highest number of votes.
                
                # Gen a new set of pref data for just the remaining candidates
                candidates_tied_second = self.generate_preference_data(
                    highest_second_preference[0],
                    "thirdVoteCandidateID_FK",
                    election_id, position_id,
                    candidate_list
                )

                # If candidates tied for second didn't get voted for in that 
                # preference, keep candidates so can check on the next
                # level down.
                if (candidates_tied_second == []):
                    candidates_tied_second = candidates_tied

                # Calculate 3rd preference winner(s) from previous wins
                highest_third_preference = self.calculate_highest_votes(
                    candidates_tied_second,
                    candidate_list
                )

                if len(highest_third_preference[0]) > 1:
                    # If more than 1 3rd pref winner.
                    
                    # Get data from remaining cands.
                    candidates_tied_third = self.generate_preference_data(
                        highest_third_preference[0],
                        "fourthVoteCandidateID_FK",
                        election_id,
                        position_id,
                        candidate_list
                    )

                    # If candidates tied for third didn't get voted for in that 
                    # preference, keep candidates so can check on the next
                    # level down.
                    if (candidates_tied_third == []):
                        candidates_tied_third = candidates_tied_second

                    # Get highest candidates in fourth pref from new list.
                    highest_fourth_preference = self.calculate_highest_votes(
                        candidates_tied_third,
                        candidate_list
                    )

                    # Tied through all preferences, revote required.
                    if len(highest_fourth_preference[0]) > 1:
                        return [0, 0, "Revote Required"]
                    else:
                        winner = highest_fourth_preference
                else:
                    winner = highest_third_preference
            else:
                winner = highest_second_preference
        else:
            winner = highest_first_preference

        winner_id = winner[0][0]
        
        # Return Winner Candidate ID, Winner Name
        # To find the index of the candidate list, find all the IDs for
        # candidates, then index the new list based on the winner ID.
        
        winner_id_index = [i[0] for i in candidate_list].index(winner_id)
        
        # Return winner ID and winner name.
        return [
            candidate_list[winner_id_index][1],
            (
                Candidate(
                    id=candidate_list[winner_id_index][1]
                )
            ).get_candidate_name()
        ]

    def generate_preference_data(
            self, remaining_candidates, search_preference, election_id,
            position_id, candidate_list):

        # Make a string list of %s for the number of candidates passed.
        mysql_format_list = ', '.join(['%s'] * len(remaining_candidates))
        
        # Create MySQL command with data substuted.
        # The %s from the last line will have each one replaced by MySQL
        # with a value.
        mysql_command_creation = "SELECT `" + search_preference + "` \
        FROM `gsuElectionVotes` \
        WHERE `electionID` = %s \
        AND `positionID` = %s \
        AND `" + search_preference + "` IN (" + mysql_format_list + ")"

        # Create array for data.
        mysql_data_creation = [election_id, position_id]

        # For every candidate in the list, extend the array.
        for i in range(len(remaining_candidates)):
            mysql_data_creation.extend(
                [candidate_list[remaining_candidates[i] - 1][1]]
            )

        # Execute command and return data.
        mysql_cursor.execute(mysql_command_creation, mysql_data_creation)
        query_result = mysql_cursor.fetchall()

        return query_result

    def calculate_highest_votes(self, votes, candidates):
        # Create 0 values.
        candidate_one_count = 0
        candidate_two_count = 0
        candidate_three_count = 0
        candidate_four_count = 0

        results = {}

        # If vote selects candidate, add 1 to their count.
        for i in range(len(votes)):
            if (candidates[0][1] == votes[i][0]):
                candidate_one_count += 1
            elif (candidates[1][1] == votes[i][0]):
                candidate_two_count += 1
            elif (candidates[2][1] == votes[i][0]):
                candidate_three_count += 1
            elif (candidates[3][1] == votes[i][0]):
                candidate_four_count += 1

        # If there are more than zero candidates in the candidates list
        # Add candidate one count to 2d results array.
        if len(candidates) > 0:
            results[candidates[0][0]] = candidate_one_count

        # Repeat adding to 2d array for every additional candidate.
        if (len(candidates) > 1) and (candidate_two_count != 0):
            results[candidates[1][0]] = candidate_two_count

        if (len(candidates) > 2) and (candidate_three_count != 0):
            results[candidates[2][0]] = candidate_three_count

        if (len(candidates) > 3) and (candidate_four_count != 0):
            results[candidates[3][0]] = candidate_four_count

        # Sort 2d array into largest to smallest by candidate.
        highest_values = [i for i, candidate in results.items() if candidate == max(results.values())]

        return(highest_values, results)
