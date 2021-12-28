# thomas_google_api
This project is for 8th Light's technical assessment. 

Introduction:
Welcome to You Pick It You'll Read It. This is a terminal application that allows a user to search for books utilizing google's public search api and save those books in a personal reading list.

System Requirements:
This application was built on mac, but should be easy to adapt to linux or any other system that can run the lastest version of python.

System Setup:
1. You will need the most up to date version of python to run this application. See the following link for installation instructions at the official documentation https://wiki.python.org/moin/BeginnersGuide/Download or a more reader friendly version at https://docs.python-guide.org/starting/installation/ .
2. If you will not be using this longterm please utilize python's virtual environment to contain the project. You may do this after you have installed python.
  a. Run "python -m venv .venv" (this creates a virtual envirnonment called ".venv")
  b. Run "source .venv/bin/activate" (this enters the virtual environment)
3. Be sure to install the requirements.txt and run the installation file.
  a. Run "pip install -r requirements.txt"
  b. Run "python installation.py" (this creates a new database for the reading list)

Running the program:
1. Change your directory to the same level as the README and start the application.
  a. Run "python runner.py"
2. You will be prompted with a set of instructions to create your very own reading list!
After Running:
1. When finished with the application, make sure to leave the virtual environment.
  a. Run "deactivate" (this exits the virtual environment)

Running the tests:
In order to run the tests you must follow the installation instructions above.
This will ensure that your system is set up to run the program and has all of the dependencies installed.

1. Change directory to be on the same level as the google_api_test.py file.
  a. Run "python google_api_test.py"
  b. The tests will run and give you feedback if any of the tests fail.
  c. There are currently 17 tests. If all of the tests succeed you should see the following:
  .................
  ----------------------------------------------------------------------
  Ran 17 tests in 0.626s
  OK
