Python Version: Python 3.8.2

Pre-requisites:

Python 3.8 or higher

Instructions:

* Download repo from github with 'git clone git@github.com:cliveyg/rover'
* Go to repo root.
* Create a virtual environment using 'python -m venv <name>
* Use virtual environment with 'source <name>/bin/activate
* Run command to install needed modules: 'pip install -r requirements.txt'
* Remember to set PYTHONPATH to repo root if needed
* To run tests from main directory use command 'pytest --cov=rover tests/'
* Run cmd 'python rover/main.py' for interactive session and follow instructions

Notes:
-----

Originally I was going to have various map types (hence a separate map class) as it 
wasn't clear from the spec if the place where the rover lands is an unbounded plain,
bounded i.e. the map has edges that the rover cannot go beyond or a planet type map 
i.e. going off the top of the map puts you back on the bottom. 
I ran out of time for all these map types so I have treated the map as an unbounded
plain for now.  

settings.py contains the settings used such as map type, directions and commands.
This enables these to be changed in the future more easily

Mars Rover: Version: 1.2, Last updated: 2020-10-26
