import mainApplication
from mainApplication import *


# --------------------------------------------------------------------------- #
#                                  CONTENTS                                   #
#                            1. Control Class                                 #
#                            2. Student Class                                 #
#                            3. Candidate Class                               #
#                            4. Election Class                                #
#                            5. Position Class                                #
#                            6. Results Class                                 #
# --------------------------------------------------------------------------- #


# --------------------------------------------------------------------------- #
#                              1. Control Class                               #
# --------------------------------------------------------------------------- #

# Define control class
# Set basic required variables and methods for primary classes.
class Control:
    def __init__(self):
        # Define class variables.
        self._select_query_output = ""

    # Insert new to database.
    def insert_new(self):
        raise NotImplementedError("Subclass must implement abstract method.")

    # Get ID of object, not required.
    def get_id(self):
        raise NotImplementedError("Subclass must implement abstract method.")

    # List all, not required.
    def list(self):
        raise NotImplementedError("Subclass must implement abstract method.")

    # Listing all with ID prepended for cmbo box, not required.
    def list_formatted(self):
        raise NotImplementedError("Subclass must implement abstract method.")

# --------------------------------------------------------------------------- #
#                              2. Student Class                               #
# --------------------------------------------------------------------------- #

# Define student class that inherits from the abstract class Control.
class Student(Control):
    
    # Initialise student class.
    def __init__(self, username="", password=""):
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
        database_connection.commit()

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

        # Set salt to match the salt value returned in the database.
        self._salt = str(self._select_query_output[0][1])

        # Re-gen hash using passed given to see it matches the stored DB value.
        self.get_hashed_password()

        # If passwords match, return true, else, false.
        if(self._hashed_password == self._select_query_output[0][0]):
            return True
        else:
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
        database_connection.commit()

# --------------------------------------------------------------------------- #
#                              3. Candidate Class                             #
# --------------------------------------------------------------------------- #

# Define candidate class.
class Candidate:
    
    # Initialise candidate class.
    def __init__(self, name="", email="", id=""):
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
        database_connection.commit()

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

    def list_formatted(self):
        available_candidates = []
        for candidate in self.list():
            available_candidates.append(
                str(candidate[0])
                + " - "
                + candidate[1]
            )

        return available_candidates

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
    def create_application(self, election_id, position_id):
        self.get_id()
        mysql_cursor.execute(
            "INSERT INTO `gsuCandidateApplication` \
            (`candidateID`, `positionID`, `electionID`) \
            VALUES (%s, %s, %s)",
            [self.id, position_id, election_id]
        )
        database_connection.commit()

# --------------------------------------------------------------------------- #
#                              4. Election Class                              #
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
        database_connection.commit()

        # Inform user of successful creation.
        messagebox.showinfo('Success', 'Created successfully.')

    # Check status of any election curretly running.
    def get_current_election(self):
        # Execute MySQL Query
        mysql_cursor.execute(
            "SELECT `electionID`, `electionStartTime`, `electionEndTime` \
            FROM `gsuElection` \
            WHERE `electionStartTime` < %s \
            AND `electionEndTime` > %s",
            [
                datetime.datetime.now(),
                datetime.datetime.now()
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
# --------------------------------------------------------------------------- #

# Define position class.
class Position:

    # Initialise position class.
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

        # Store query_result as all values returned.
        query_result = mysql_cursor.fetchall()

        return query_result

    # List all available positions to apply for.
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

        # Store query_result as all values returned.
        query_result = mysql_cursor.fetchall()

        return query_result

    # List all candiates for given position in election.
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

        # Store query_result as all values returned.
        query_result = mysql_cursor.fetchall()

        return query_result

# --------------------------------------------------------------------------- #
#                              6. Results Class                               #
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

        for vote in votes:
            if(candidate == vote[0]):
                first_preference += 1
            elif(candidate == vote[1]):
                second_preference += 1
            elif(candidate == vote[2]):
                third_preference += 1
            elif(candidate == vote[3]):
                fourth_preference += 1

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
        return ["Invalid Vote", 0, 0, 0, 0, 0]

    def get_election_results(self):
        # Get list of all positions.
        positions = classDesign.Position()
        position_list = positions.list_all_positions()

        output_data = ""

        for position in position_list:
            try:
                totals = self.get_position_total_results(position[0])
                output_data += position[1] + " - " + totals[4] + "\n"
            except IndexError:
                break

        return output_data

    # Return list of the final results for given position.
    def get_position_total_results(self, position_id):
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

        winner = self.get_position_winner(position_id)
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

        winer_count = self.get_count(winner[0], query_result)
        first = self.get_count(candidates[0][1], query_result)
        second = self.get_count(candidates[1][1], query_result)
        third = self.get_count(candidates[2][1], query_result)
        fourth = self.get_count(candidates[3][1], query_result)

        totalpositionvotes = first[1] + second[1] + third[1] + fourth[1] \
            + first[2] + second[2] + third[2] + fourth[2] + first[3] \
            + second[3] + third[3] + fourth[3] + first[4] + second[4] \
            + third[4] + fourth[4]

        return [
            first,
            second,
            third,
            fourth,
            winner[1],
            str(winer_count[5]),
            str(totalpositionvotes)
        ]

    # Return list of the winner results for given position.
    def get_position_winner(self, position_id):
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
        highest_first_preference = self.calculate_highest_votes(
            mysql_cursor.fetchall(),
            candidate_list
        )

        if len(highest_first_preference[0]) > 1:

            candidates_tied = self.generate_preference_data(
                highest_first_preference[0],
                "secondVoteCandidateID_FK",
                election_id,
                position_id,
                candidate_list
            )

            highest_second_preference = self.calculate_highest_votes(
                candidates_tied,
                candidate_list
            )

            if len(highest_second_preference[0]) > 1:
                candidates_tied_second = self.generate_preference_data(
                    highest_second_preference[0],
                    "thirdVoteCandidateID_FK",
                    election_id, position_id,
                    candidate_list
                )

                if (candidates_tied_second == []):
                    candidates_tied_second = candidates_tied

                highest_third_preference = self.calculate_highest_votes(
                    candidates_tied_second,
                    candidate_list
                )

                if len(highest_third_preference[0]) > 1:
                    candidates_tied_third = self.generate_preference_data(
                        highest_third_preference[0],
                        "fourthVoteCandidateID_FK",
                        election_id,
                        position_id,
                        candidate_list
                    )

                    if (candidates_tied_third == []):
                        candidates_tied_third = candidates_tied_second

                    highest_fourth_preference = self.calculate_highest_votes(
                        candidates_tied_third,
                        candidate_list
                    )

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

        winner_id = winner[0][0] - 1
        # Return Winner Candidate ID, Winner Name
        return [
            candidate_list[winner_id][1],
            (
                Candidate(id=candidate_list[winner_id][1])
            ).get_candidate_name()
        ]

    def generate_preference_data(
            self,
            remaining_candidates,
            search_preference,
            election_id,
            position_id,
            candidate_list):

        mysql_format_list = ', '.join(['%s'] * len(remaining_candidates))
        mysql_command_creation = "SELECT `" + search_preference + "` \
        FROM `gsuElectionVotes` \
        WHERE `electionID` = %s \
        AND `positionID` = %s \
        AND `" + search_preference + "` IN (" + mysql_format_list + ")"

        mysql_data_creation = [election_id, position_id]

        for i in range(len(remaining_candidates)):
            mysql_data_creation.extend(
                [candidate_list[remaining_candidates[i] - 1][1]]
            )

        mysql_cursor.execute(mysql_command_creation, mysql_data_creation)
        query_result = mysql_cursor.fetchall()

        return query_result

    def calculate_highest_votes(self, votes, candidates):
        candidate_one_count = 0
        candidate_two_count = 0
        candidate_three_count = 0
        candidate_four_count = 0

        results = {}

        for i in range(len(votes)):
            if (candidates[0][1] == votes[i][0]):
                candidate_one_count += 1
            elif (candidates[1][1] == votes[i][0]):
                candidate_two_count += 1
            elif (candidates[2][1] == votes[i][0]):
                candidate_three_count += 1
            elif (candidates[3][1] == votes[i][0]):
                candidate_four_count += 1

        if len(candidates) > 0:
            results[candidates[0][0]] = candidate_one_count

        if (len(candidates) > 1) and (candidate_two_count != 0):
            results[candidates[1][0]] = candidate_two_count

        if (len(candidates) > 2) and (candidate_three_count != 0):
            results[candidates[2][0]] = candidate_three_count

        if (len(candidates) > 3) and (candidate_four_count != 0):
            results[candidates[3][0]] = candidate_four_count

        highest_values = [i for i, candidate in results.items() if candidate == max(results.values())]

        return(highest_values, results)
