This project is an intro to flask, and uses classes to find files with random epithets, and will return as json.

To run:

Have pipenv installed on your machine
Command Line Prompts:
navigate to submissions/sprint_c folder
install dependencies:
$pipenv install
navigate to virtual env and run:
$pipenv shell
flask run

End points to try: '/', '/\<anypositivenumber\>', '/random', '/vocabulary'

Note on the app.py:
Pathing set up that so debugger and flask can both run

Path Notes:
'/' single epithet

\<anypositivenumber\> has no limit currently

/random delivers a random quantity between 1 and 10
