# Greenwich Student Union Voting Application
Please note, this script is **NOT** production ready, does not depict voting methods at GSU and should not be used in real-world situations.  

This script was initially developed for the module "COMP1811" at the University of Greenwich, demonstrating basic Python programming ability including user interfaces, data storage and data processing.

Basic project features include
- Interactive User Interface
- Login with Username and Password
- Create Candidates
- Submit Candidate For Position
- Cast Votes
- Count Votes
- Visualise Results

## Getting Started
1. This project makes use of multiple PIP packages. To install them and to ensure that you're able to run the application, please execute  
`pip install -r requirements.txt` when in the root directory of the project; alternatively, dependancies can be manually installed one at a time from the list.
2. A MySQL database is required for this application, once one has been created and a user assigned, import `Database\database_design.sql` which will provide base dummy data and schema.
3. Modify `Application\connectionString.py` to use the updated MySQL connection details.
4. The default username and password provided in the dummy data is `Test` and `Test`

## Project Files
`Project\Summary_Report.pdf` - A stripped down copy of the coursework submission including project and code related details.
`Application\classDesign.py` - Contains all classes that can be instanciated as objects throughout the application.
`Application\mainApplication.py` - Main project file that handles object creation, function/method calls and user interface handling.
`Application\userInterfaceDesign.ui` - Pygubu interface design file.
`Database\database_design.sql` - Database schema and dummy data.

## Project Contributors
William Phillips - [@MetallicGloss](https://github.com/MetallicGloss)  
Scott Williams - [@ScottWilliams435](https://github.com/scottwilliams435)  
Aiden Silk - [@AidenSilk](https://github.com/AidenSilk)  