# Toy Robot Code Challenge
## _This is a simple command line application_

## Description
This application is completed as a task following this [brief]. The result is a simulation of a toy robot moving on a square tabletop, of dimensions 5 units x 5 units.


## Basic environments

- Python 3
- virtual env
- pip
- Pytest

## Usage
This is a coding challenge so we do not expect it to be installed on any system or distributed in any form other than a git checkout.

Create and activate the virtual environment:
```sh
python3 -m venv .venv
source .venv/bin/activate
```

To install the package(s) - pytest:
```sh
pip install -r requirements.txt
```

Run test cases using below CLI:
```sh
pytest
```
You should be able to see a prompt that 23 cases passed.

To run the robot:
```sh
python run.py
```

To exit this application:
```sh
bye
```

## Example Input and Output
Input:
```sh
PLACE 0,0,NORTH
MOVE
REPORT
```
Output:
```
0,1,NORTH
```

[brief]: https://github.com/HenryW6789/toy-robot/blob/main/brief.md
