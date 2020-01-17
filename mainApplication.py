# Import required modules for program.
import os
import sys
import pygubu
import hashlib
import datetime
import binascii
import classDesign
import mysql.connector
import connectionString

import numpy as np
import tkinter as tk
import matplotlib.pyplot as plt

from mysql.connector import Error
from dateutil.parser import parse
from tkinter import messagebox


# --------------------------------------------------------------------------- #
#                                  CONTENTS                                   #
#                            1. MySQL Initialisation                          #
#                            2. Interface Hander Class                        #
#                            2.1 Core Functions                               #
#                            2.2 Main Menu Navigation Functions               #
#                            2.3 Backend Menu Functions                       #
#                            2.4 Backend Extra Functions                      #
#                            2.5 Frontent Menu Functions                      #
#                            2.6 Frontent Extra Functions                     #
#                            3. Main Program init                             #
# --------------------------------------------------------------------------- #


# --------------------------------------------------------------------------- #
#                            1. MySQL Initialisation                          #
# --------------------------------------------------------------------------- #

# Module initialisation
# Open MySQL connection using connection query data, initialise cursor.
try:
    # Define database connection variable.
    db_connect = mysql.connector.connect(
        host=connectionString.dbHost,
        database=connectionString.dbDatabase,
        user=connectionString.dbUsername,
        password=connectionString.dbPassword
    )
    mysql_cursor = db_connect.cursor()

except Error as e:
    print(e)
    sys.exit()


# --------------------------------------------------------------------------- #
#                            2. Interface Hander Class                        #
# --------------------------------------------------------------------------- #

# Define primary class to initiate the user interface.
class voting_application(pygubu.TkApplication):

    # ----------------------------------------------------------------------- #
    #                          2.1 Core Functions                             #
    #                                                                         #
    #                                __init__                                 #
    #        Sets the TK app passed on initial as `master` to a param.        #
    #                                                                         #
    #                               change_frame                              #
    #         Dynamically change between frames and reconnect buttons.        #
    # ----------------------------------------------------------------------- #

    # Initialise voting application interface.
    def __init__(self, master):
        self.master = master
        self.change_frame('startup_menu_frm')

        # List used when voting to temp store data between interface changes
        self._candidate_list = []

        # Replacement of global variable to store user ID that is logged in.
        self.logged_in_student = ""

        # Used to pass position ID between interface changes.
        self.voting_position = ""

    # Function to change/load the frame.
    def change_frame(self, frame):
        # If userInterface not defined yet (startup), bypass destroy.
        # Destroy current view and load frame of desired window.
        try:
            self.userInterface.destroy()
        except AttributeError:
            pass

        # Create Pygubu builder
        self.ui_builder = pygubu.Builder()

        # Load main interface design.
        self.ui_builder.add_from_file('userInterfaceDesign.ui')
        self.userInterface = self.ui_builder.get_object(frame, self.master)

        # Connect buttons to methods.
        self.ui_builder.connect_callbacks(self)
        
    # Function get the ID from a user selected combobox.
    def get_cmbo_id(self, element_id):
        return (self.ui_builder.get_object(element_id).get()).split()[0]
        

    # ----------------------------------------------------------------------- #
    #                    2.2 Main Menu Navigation Functions                   #
    #                                                                         #
    #                          startup_select_student                         #
    #                   Changes frame to `stdnt_login_frm`                    #
    #                                                                         #
    #                          startup_select_backend                         #
    #                   Changes frame to `bkend_menu_frame`                   #
    #                                                                         #
    #                             exit_application                            #
    #            Destroys mainloop, gracefully closes application.            #
    # ----------------------------------------------------------------------- #

    # Navigate to student voter login.
    def startup_select_student(self):
        self.change_frame('stdnt_login_frm')

    # Navigate to backend menu.
    def startup_select_backend(self):
        self.change_frame('bkend_menu_frame')

    # Gracefully closes the application.
    def exit_application(self):
        # Destroy the tkinter mainloop.
        # Don't use quit as it leaves the loop running, use destroy.
        global tkinter_app
        tkinter_app.destroy()

    # ----------------------------------------------------------------------- #
    #                        2.3 Backend Menu Functions                       #
    #                                                                         #
    #                            return_to_startup                            #
    #                      Changes `startup_menu_frm`                       #
    #                                                                         #
    #                            return_to_backend                            #
    #                       Changes `bkend_menu_frame`                      #
    #                                                                         #
    #                        menu_create_student_voter                        #
    #                  Changes `bkend_create_stdnt_fm`                 #
    #                                                                         #
    #                          menu_create_candidate                          #
    #                 Changes `bkend_create_cand_frame`                #
    #                                                                         #
    #                           menu_create_election                          #
    #                 Changes `bkend_create_election_frame`                 #
    #                                                                         #
    #                         menu_create_application                         #
    # Changes frame and loads positions, elections and candidates to screen.  #
    #                                                                         #
    #                            menu_view_results                            #
    #        Changes frame and loads positions and elections to screen.       #
    # ----------------------------------------------------------------------- #

    # Exit backend menu to return to startup.
    def return_to_startup(self):
        self.change_frame('startup_menu_frm')

    # On sub-page access through the backend menu, provide a back button.
    def return_to_backend(self):
        self.change_frame('bkend_menu_frame')

    # Navigate to create student voter.
    def menu_create_student_voter(self):
        self.change_frame('bkend_create_stdnt_fm')

    # Navigate to create candidate.
    def menu_create_candidate(self):
        self.change_frame('bkend_create_cand_frame')

    # Navigate to create election.
    def menu_create_election(self):
        self.change_frame('bkend_create_election_frame')

    # Navigate to create candidate application.
    def menu_create_application(self):
        self.change_frame('bkend_create_cand_application_frame')

        # Create position, append to list the remaining available
        positions = classDesign.Position()
        available_positions = positions.list_all_available_positions_formatted()

        # Create election instance, append to list the election times
        elections = classDesign.Election()
        current_election = elections.list_formatted()

        # Create candidate instance, append to list the candidate names
        candidates = classDesign.Candidate()
        available_candidates = candidates.list_formatted()

        # Set choices in combo boxes to lists created.
        self.ui_builder.get_object(
            'bkend_create_cand_election_cmbobx'
        ).configure(values=current_election)
        
        self.ui_builder.get_object(
            'bkend_create_cand_cand_cmbobx'
        ).configure(values=available_candidates)
        
        self.ui_builder.get_object(
            'bkend_create_cand_pos_cmbobx'
        ).configure(values=available_positions)

    # Navigate to view results page.
    def menu_view_results(self):
        self.change_frame('bkend_sel_results_pos_frm')

        # Create election instance, append to list the election times
        elections = classDesign.Election()
        current_election = elections.list_formatted()

        # Create combo box of positions currently available to vote.
        positions = classDesign.Position()
        position_list = positions.list_all_positions_formatted()

        # Set choices in combo boxes to lists created.
        self.ui_builder.get_object(
            'bkend_sel_results_pos_election_cmbobx'
        ).configure(values=current_election)
        
        self.ui_builder.get_object(
            'bkend_sel_results_pos_pos_cmbobx'
        ).configure(values=position_list)

    # ----------------------------------------------------------------------- #
    #                       2.4 Backend Extra Functions                       #
    #                                                                         #
    #                              create_student                             #
    #      Takes user input, validates it and executes student creation.      #
    #                                                                         #
    #                             create_candidate                            #
    #     Takes user input, validates it and executes candidate creation.     #
    #                                                                         #
    #                             create_election                             #
    #     Takes user input, validates it and executes election creation.      #
    #                                                                         #
    #                            create_application                           #
    #    Takes user input, validates it and executes candidate application.   #
    #                                                                         #
    #                      results_view_select_position                       #
    #                Output the final results for the position.               #
    #                                                                         #
    #                              display_results                            #
    #          Set the labels on screen to match the results values.          #
    #                                                                         #
    #                              display_graph                              #
    # Generate and display a graph to visualise the results for the position. #
    # ----------------------------------------------------------------------- #

    # Create new student on submission from user.
    def create_student(self):
        # Get user input from the page.
        username = self.ui_builder.get_object(
            'stdnt_userame_txtbx'
        ).get()
        password = self.ui_builder.get_object(
            'stdnt_password_txtbx'
        ).get()

        if None not in (username, password):
            # If input is not blank, create user.
            new_student = classDesign.Student(username, password)

            # Generate the hashed version of the password.
            new_student.generate_hash_password()

            if(new_student.verify_unique_username()):
                # Verify that the username hasn't been used before.
                # If unique, insert student.
                new_student.insert_new()

                # Inform user of successful creation.
                messagebox.showinfo('Success', 'Created successfully.')
                self.return_to_backend()
            else:
                # If not unique, alert user.
                self.ui_builder.get_object(
                    'create_stdnt_error_lbl'
                ).configure(text="Error: Username is not unique.")
        else:
            # Else change label text to error message.
            self.ui_builder.get_object(
                'create_stdnt_error_lbl'
            ).configure(text="Error: Missing Entry")

    # Create new candidate that can make applications.
    def create_candidate(self):
        # Get user input from the page.
        name = self.ui_builder.get_object(
            'bkend_create_cand_name_txtbx'
        ).get()
        
        email = self.ui_builder.get_object(
            'bkend_create_cand_email_txtbx'
        ).get()

        if None not in (name, email):
            # If input fields on the page are not empty.
            new_candidate = classDesign.Candidate(name, email)

            if(new_candidate.verify_unique_name()):
                # Check there isn't already a candidate with same name.
                # If unique, insert.
                new_candidate.insert_new()

                self.return_to_backend()
            else:
                # If not unique, inform user to add custom tag to surname
                self.ui_builder.get_object(
                    'bkend_create_cand_error_lbl'
                ).configure(text="Uh Oh! You've got a common name, please add a unique addition to your surname to help voters!")
        else:
            # Else change label text to error message.
            self.ui_builder.get_object(
                'bkend_create_cand_error_lbl'
            ).configure(text="Error: Missing data from input fields.")

    # Create new election period on the system.
    def create_election(self):
        # Get user input from the page, parse input as best as possible using
        # library into standard datetime format.
        start_date_time = parse(self.ui_builder.get_object(
            'bkend_create_election_start_txtbx'
        ).get())
        end_date_time = parse(self.ui_builder.get_object(
            'bkend_create_election_end_txbx'
        ).get())

        if None not in (start_date_time, end_date_time):
            # If input fields on the page are not empty.
            new_election = classDesign.Election(start_date_time, end_date_time)

            # If start date is before the end date, valid input.
            if(start_date_time < end_date_time):
                # End date comes after start time, acceptable input.
                new_election.create_election()

                self.return_to_startup()
            else:
                # If not valid, alert user.
                self.ui_builder.get_object(
                    'bkend_bkend_create_election_error_lbl'
                ).configure(text="Error: Invalid end date.")
        else:
            # Else change label text to error message.
            self.ui_builder.get_object(
                'bkend_bkend_create_election_error_lbl'
            ).configure(text="Error: Missing data from input fields.")

    # Submit application for candidate to current available election.
    def create_application(self):
        # Get user input from the page
        # Then split on newline and get 1st element to get ID of each.
        election = self.get_cmbo_id('bkend_create_cand_election_cmbobx')
        
        candidate = self.get_cmbo_id('bkend_create_cand_cand_cmbobx')
        
        position = self.get_cmbo_id('bkend_create_cand_pos_cmbobx')

        if(election is not None):
            # If election is not blank.
            if None not in (candidate, position):
                # If other values are not selected
                new_application = classDesign.Candidate(candidate)

                # Create the application.
                new_application.create_application(election, position)

                self.return_to_backend()
            else:
                # Else change label text to error message.
                self.ui_builder.get_object(
                    'bkend_create_cand_error_lbl'
                ).configure(text="Error: Select one value for all options.")
        else:
            # Else change label text to error message.
            self.ui_builder.get_object(
                'bkend_create_cand_error_lbl'
            ).configure(text="Election not selected. Unable to apply.")

    # Retrieve list of results.
    # Then format them to display them on the user interface.
    def results_view_select_position(self):
        # Get input from the interface.
        self.voting_position = self.get_cmbo_id('bkend_sel_results_pos_pos_cmbobx')
        
        election = self.get_cmbo_id('bkend_sel_results_pos_election_cmbobx')

        if None not in (self.voting_position, election):
            # If input fields on the page are not empty.
            self.change_frame('bkend_bkend_view_results_frm')

            results = classDesign.Results()
            results_array = results.get_position_total_results(self.voting_position)

            self.display_results(
                "bkend_view_results_cand_one",
                results_array[0][0],
                results_array[0][1],
                results_array[0][2],
                results_array[0][3],
                results_array[0][4]
            )

            self.display_results(
                "bkend_view_results_cand_two",
                results_array[1][0],
                results_array[1][1],
                results_array[1][2],
                results_array[1][3],
                results_array[1][4]
            )
            self.display_results(
                "bkend_view_results_cand_three",
                results_array[2][0],
                results_array[2][1],
                results_array[2][2],
                results_array[2][3],
                results_array[2][4]
            )
            self.display_results(
                "bkend_view_results_cand_four",
                results_array[3][0],
                results_array[3][1],
                results_array[3][2],
                results_array[3][3],
                results_array[3][4]
            )

            # Final labels for the winner and total votes
            self.ui_builder.get_object(
                'bkend_view_results_winner_name_lbl'
            ).configure(text="Winner: " + results_array[4])
            self.ui_builder.get_object(
                'bkend_view_results_winner_votes_lbl'
            ).configure(text="Winner Total Votes: " + results_array[5])
            self.ui_builder.get_object(
                'bkend_view_results_total_votes_lbl'
            ).configure(text="Position total votes: " + results_array[6])

        else:
            # Else change label text to error message.
            self.ui_builder.get_object(
                'stdnt_vote_pos_error_lbl'
            ).configure(text="Error: Enter data for both fields.")

    # Sets results page labels, helps to avoid massive amounts of duplication.
    def display_results(self, element, name, first, second, third, fourth):
        self.ui_builder.get_object(
            element + '_name_lbl'
        ).configure(text=name)
        
        self.ui_builder.get_object(
            element + '_first_lbl'
        ).configure(text=first)
        
        self.ui_builder.get_object(
            element + '_second_lbl'
        ).configure(text=second)
        
        self.ui_builder.get_object(
            element + '_third_lbl'
        ).configure(text=third)
        
        self.ui_builder.get_object(
            element + '_fourth_lbl'
        ).configure(text=fourth)
        pass

    # Generates a graph based on the results for the position.
    def display_graph(self):
        results = classDesign.Results()
        results_array = results.get_position_total_results(self.voting_position)

        # Getting the data for each bar on the graph (below)
        # Grouping votes to different candidates
        candidate_one = tuple([
            results_array[0][1],
            results_array[0][2],
            results_array[0][3],
            results_array[0][4]
        ])

        candidate_two = [
            results_array[1][1],
            results_array[1][2],
            results_array[1][3],
            results_array[1][4]
        ]
        candidate_three = [
            results_array[2][1],
            results_array[2][2],
            results_array[2][3],
            results_array[2][4]
        ]
        candidate_four = [
            results_array[3][1],
            results_array[3][2],
            results_array[3][3],
            results_array[3][4]
        ]

        candidate_names = [
            results_array[0][0],
            results_array[1][0],
            results_array[2][0],
            results_array[3][0]
        ]

        barWidth = 0.25

        # Used to calculate where to place the bars
        # Creates evenly spaced values depending on the legth of candidate_one
        r1 = np.arange(len(candidate_one)) 

        # Used to create the different bars at specific width 
        r2 = [x + barWidth for x in r1] 
        r3 = [x + barWidth for x in r2]
        r4 = [x + barWidth for x in r3]

        plt.bar(
            # Used for locating where the bar should be
            r1, 
            
            # candidate ones votes, 1st, 2nd, 3rd and 4th
            candidate_one, 
            
            # colour of the bar
            color='blue', 
            
            # The bar width as stated earlier
            width=barWidth, 
            
            # Line colour for bar
            edgecolor='white', 
            
            # The label which is shown on the graph so you can identify 
            label='Candidate1' 
        )
        plt.bar(
            r2,
            candidate_two,
            color='green',
            width=barWidth,
            edgecolor='white',
            label='Candidate2'
        )
        plt.bar(
            r3,
            candidate_three,
            color='black',
            width=barWidth,
            edgecolor='white',
            label='Candidate3'
        )
        plt.bar(
            r4,
            candidate_four,
            color='red',
            width=barWidth,
            edgecolor='white',
            label='Candidate4'
        )

        # Using plt to actually create the bars with labels and
        # colour coded so you can tell which is which

        # Bottom title
        plt.xlabel('First, Second, Third and Fourth votes', fontweight='bold')
        plt.xticks(
            [r + barWidth for r in range(len(candidate_one))],
            ['First', 'Second', 'Third', 'Fourth']
        )

        # Automatically creates a legend for any labeled plot elements:
        plt.legend() 
        
        # Show the bar chart
        plt.show() 

    # ----------------------------------------------------------------------- #
    #                       2.5 Frontent Menu Functions                       #
    #                                                                         #
    #                            return_to_student                            #
    #                  Changes frame to `stdnt_login_frm`                 #
    # ----------------------------------------------------------------------- #

    # Exit page within student menu, return to login.
    def return_to_student(self):
        self.change_frame('stdnt_login_frm')

    # ----------------------------------------------------------------------- #
    #                       2.6 Frontent Extra Functions                      #
    #                                                                         #
    #                              student_login                              #
    #  Handles password verification, fill comboboxs on position select page. #
    #                                                                         #
    #                          vote_select_position                           #
    #       Handles selection of position, fill out vote page with data.      #
    #                                                                         #
    #                             toggle_vote_box                             #
    #      Toggles the locking of boxes on vote page to prevent changes.      #
    #                                                                         #
    #                          first_choice_confirm                           #
    #     Select first choice option, remove selected option and add N/A.     #
    #                                                                         #
    #                          second_choice_confirm                          #
    #        Select second choice option, if N/A, skip to submission.         #
    #                                                                         #
    #                          third_choice_confirm                           #
    #                      Select third choice option.                        #
    #                                                                         #
    #                          fourth_choice_confirm                          #
    #       Select fourth choice, submit votes. If 2nd N/A, skip others.      #
    # ----------------------------------------------------------------------- #

    # Perform student login verification.
    def student_login(self):
        # Get user input from the page.
        username = self.ui_builder.get_object(
            'stdnt_login_username_txtbx'
        ).get()
        
        password = self.ui_builder.get_object(
            'stdnt_login_passwd_txtbx'
        ).get()

        if None not in (username, password):
            # If input fields on the page are not empty.

            student_login = classDesign.Student(username, password)

            # If password is valid, login, else, inform user.
            if(student_login.verify_password()):
                self.change_frame('stdnt_vote_pos_sel_frm')

                # Set 'global' class variable for student login.
                self.logged_in_student = student_login.get_id()

                # Create election instance, append to list the election times
                elections = classDesign.Election()
                current_election = elections.list_formatted()

                # Create combo box of positions currently available to vote.
                positions = classDesign.Position()
                position_list = []
                for position in positions.list_available_voting_positions(student_login.get_id()):
                    position_list.append(
                        str(position[0])
                        + " - "
                        + position[1]
                    )

                # Set choices in combo boxes to lists created.
                self.ui_builder.get_object(
                    'stdnt_vote_pos_election_cmbobx'
                ).configure(values=current_election)
                self.ui_builder.get_object(
                    'stdnt_vote_pos_pos_cmbobx'
                ).configure(values=position_list)
            else:
                # If not unique, inform user to add custom tag to surname.
                self.ui_builder.get_object(
                    'stdnt_login_error_lbl'
                ).configure(text="Wrong password / ineligible to vote.")

        else:
            # Else change label text to error message.
            self.ui_builder.get_object(
                'stdnt_login_error_lbl'
            ).configure(text="Error: Missing data from input fields.")

    # Execute vote for the selected positions on the screen.
    def vote_select_position(self):
        try:
            election = self.get_cmbo_id('stdnt_vote_pos_election_cmbobx')
            
            self.voting_position = self.get_cmbo_id('stdnt_vote_pos_pos_cmbobx')
        except IndexError:
            # If error (none selected) change label text to error message.
            self.ui_builder.get_object(
                'stdnt_vote_pos_error_lbl'
            ).configure(text="Please enter data for all fields.")
        else:
            # If not except, continue.
            if None not in (self.voting_position, election):
                # If input fields on the page are not empty.
                self.change_frame('stdnt_vote_frm')

                # Get list of candidates that have an application for the position.
                position = classDesign.Position()
                candidate_data = position.list_for_position(
                    self.voting_position
                )

                if not candidate_data:
                    # List returned empty, no candidates.
                    self.ui_builder.get_object(
                        'stdnt_vote_error_lbl'
                    ).configure(text="Error: No candidates.")
                else:
                    candidate_formatted = []
                    for candidate in candidate_data:
                        candidate_temp = classDesign.Candidate(id=candidate[1])
                        candidate_formatted.append(
                            str(candidate[1])
                            + " - "
                            + str(candidate_temp.get_candidate_name())
                        )

                    # Write formatted list to the combobox.
                    self.ui_builder.get_object(
                        'stdnt_vote_first_choice_cmbobx'
                    ).configure(values=candidate_formatted)

                    self.candidate_list = candidate_formatted

    # Toggle availability of boxes and buttons on the vote page after confirm
    def toggle_vote_box(self, start_element, end_element):
        self.ui_builder.get_object(
            start_element + '_btn'
        ).configure(state="disabled")
        
        self.ui_builder.get_object(
            start_element + '_cmbobx'
        ).configure(state="disabled")
        
        self.ui_builder.get_object(
            end_element + '_btn'
        ).configure(state="normal")
        
        self.ui_builder.get_object(
            end_element + '_cmbobx'
        ).configure(state="normal", values=self.candidate_list)

    def first_choice_confirm(self):
        # Get the user input value for first choice.
        selected_value = self.ui_builder.get_object(
            'stdnt_vote_first_choice_cmbobx'
        ).get()

        if(selected_value is not None):
            # If selection has been made, remove value from list.
            # Make N/A available for future preferences.
            self.candidate_list.remove(selected_value)
            self.candidate_list.append("N/A")

            # Toggle box availability to next preference
            self.toggle_vote_box(
                "stdnt_vote_first_choice",
                "stdnt_vote_second_choice"
            )

    def second_choice_confirm(self):
        # Get the user input value for second choice.
        selected_value = self.ui_builder.get_object(
            'stdnt_vote_second_choice_cmbobx'
        ).get()

        if(selected_value is not None):
            # If selection has been made, continue.
            if(selected_value == "N/A"):
                self.fourth_choice_confirm()
            else:
                self.candidate_list.remove(selected_value)
                self.candidate_list.remove("N/A")

            # Toggle box availability to next preference
            self.toggle_vote_box(
                "stdnt_vote_second_choice",
                "stdnt_vote_third_choice"
            )

    def third_choice_confirm(self):
        # Get the user input value for third choice.
        selected_value = self.ui_builder.get_object(
            'stdnt_vote_third_choice_cmbobx'
        ).get()

        if(selected_value is not None):
            # If selection has been made, continue.
            self.candidate_list.remove(selected_value)

            # Toggle box availability to next preference
            self.toggle_vote_box(
                "stdnt_vote_third_choice",
                "stdnt_vote_fourth_choice"
            )

    def fourth_choice_confirm(self):
        # Get the user input value for first choice.
        selected_value = self.ui_builder.get_object(
            'stdnt_vote_fourth_choice_cmbobx'
            ).get()
        box_two = self.ui_builder.get_object(
            'stdnt_vote_second_choice_cmbobx'
        ).get()
        if(selected_value != "" or box_two == "N/A"):
            student = classDesign.Student()

            # Get user input for votes.
            first_choice = self.get_cmbo_id('stdnt_vote_first_choice_cmbobx')
            second_choice = self.get_cmbo_id('stdnt_vote_second_choice_cmbobx')

            if(second_choice == "N/A"):
                # If user selected to not enter a 2nd pref
                # Set all other preferences to blank.
                second_choice = None
                third_choice = None
                fourth_choice = None
            else:
                # Else get values from user input.
                third_choice = self.get_cmbo_id('stdnt_vote_third_choice_cmbobx')
                fourth_choice = self.get_cmbo_id('stdnt_vote_fourth_choice_cmbobx')

            # Submit votens.
            student.cast_votes(
                self.voting_position,
                self.logged_in_student,
                first_choice,
                second_choice,
                third_choice,
                fourth_choice
            )

            messagebox.showinfo('Success', 'Votes submitted.')
            self.return_to_student()

    # Change page to the results selection page, fill page with data.
    def select_results_details(self):
        self.change_frame('stdnt_results_sel_frm')

        # Create election instance, append to list the election times
        elections = classDesign.Election()
        current_election = elections.list_formatted()

        # Create combo box of positions currently available to vote.
        positions = classDesign.Position()
        position_list = positions.list_election_positions_formatted()

        # Set choices in combo boxes to lists created.
        self.ui_builder.get_object(
            'stdnt_results_sel_election_confirm_cmbobx'
        ).configure(values=current_election)
        self.ui_builder.get_object(
            'stdnt_results_sel_pos_cmbobx'
        ).configure(values=position_list)

    # Change page to allow student to view election results.
    def student_view_election_results(self):
        self.change_frame('stdnt_election_results_frm')

        results = classDesign.Results()

        self.ui_builder.get_object(
            'stdnt_election_results_data_lbl'
        ).configure(text=results.get_election_results())

    def export_election_results(self):
        results = classDesign.Results()
        file = open("election_results.txt", "w")
        file.write(results.get_election_results())
        file.close()

    # Change page to allow student to view per position results.
    def student_view_position_results(self):

        position = self.get_cmbo_id('stdnt_results_sel_pos_cmbobx')

        if position != "":
            self.change_frame('stdnt_pos_results_frm')
            results = classDesign.Results()
            
            results = classDesign.Results()
            results_array = results.get_position_total_results(position)

            self.display_results(
                "stdnt_bkend_view_results_cand_one",
                results_array[0][0],
                results_array[0][1],
                results_array[0][2],
                results_array[0][3],
                results_array[0][4]
            )

            self.display_results(
                "stdnt_bkend_view_results_cand_two",
                results_array[1][0],
                results_array[1][1],
                results_array[1][2],
                results_array[1][3],
                results_array[1][4]
            )
            self.display_results(
                "stdnt_bkend_view_results_cand_three",
                results_array[2][0],
                results_array[2][1],
                results_array[2][2],
                results_array[2][3],
                results_array[2][4]
            )
            self.display_results(
                "stdnt_bkend_view_results_cand_four",
                results_array[3][0],
                results_array[3][1],
                results_array[3][2],
                results_array[3][3],
                results_array[3][4]
            )

            # Final labels for the winner and total votes
            self.ui_builder.get_object(
                'stdnt_bkend_view_results_winner_name_lbl'
            ).configure(text="Winner: " + results_array[4])
            self.ui_builder.get_object(
                'stdnt_bkend_view_results_winner_votes_lbl'
            ).configure(text="Winner Total Votes: " + results_array[5])
            self.ui_builder.get_object(
                'stdnt_bkend_view_results_winner_percentage_lbl'
            ).configure(text="Winner Total Percentage: " + str("%.2f" % ((int(results_array[5]) / int(results_array[6]))*100)) + "%")
            self.ui_builder.get_object(
                'stdnt_bkend_view_results_total_votes_lbl'
            ).configure(text="Position total votes: " + results_array[6])
            

# --------------------------------------------------------------------------- #
#                             3. Main Program init                            #
# --------------------------------------------------------------------------- #

if __name__ == '__main__':
    tkinter_app = tk.Tk()
    main_application = voting_application(tkinter_app)
    tkinter_app.mainloop()
