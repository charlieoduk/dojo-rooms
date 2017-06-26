[![Codacy Badge](https://api.codacy.com/project/badge/Grade/ea7cce59060e4de3a14b4edfce4c39f9)](https://www.codacy.com/app/charlieoduk/dojo-rooms?utm_source=github.com&utm_medium=referral&utm_content=charlieoduk/dojo-rooms&utm_campaign=badger)
[![Build Status](https://travis-ci.org/charlieoduk/dojo-rooms.svg?branch=master)](https://travis-ci.org/charlieoduk/dojo-rooms)
[![Coverage Status](https://coveralls.io/repos/github/charlieoduk/dojo-rooms/badge.svg)](https://coveralls.io/github/charlieoduk/dojo-rooms)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/ea7cce59060e4de3a14b4edfce4c39f9)](https://www.codacy.com/app/charlieoduk/dojo-rooms?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=charlieoduk/dojo-rooms&amp;utm_campaign=Badge_Grade)
# BOOTCAMP WEEK 2 PROJECT - DOJO-ROOMS

# Introduction

When a new Fellow joins Andela they are assigned an office space and an optional living space if they choose to opt in. When a new Staff joins they are assigned an office space only. This program randomizes a room allocation system for one of Andela Kenya’s facilities called The Dojo.

# Overview
This is version 1 of this product and it has 5 core functions. 

# Create Room
   ```USAGE: create_room <room_type> <room_name>...```

Creates rooms in the Dojo. Using this command, the user can create as many rooms as possible by specifying multiple room names after the create_room command.

* Sample input with one office
>>> create_room office Orange

* Sample output with one office
An office called Orange has been successfully created!

* Sample input with multiple offices
>>> create_room office Blue Black Brown

* Sample output with multiple offices
An office called Blue has been successfully created!
An office called Black has been successfully created!
An office called Brown has been successfully created!

# Add Person
```USAGE: add_person <person_name> <FELLOW|STAFF> [wants_accommodation]```

Adds a person to the system and allocates the person to a random room. wants_accommodation here is an optional argument which can be either Y or N. The default value if it is not provided is N. 

```# Sample input for adding Staff
>>> add_person Neil Armstrong Staff

# Sample output for adding Staff
Staff Neil Armstrong has been successfully added.
Neil has been allocated the office Blue

# Sample input for adding Fellow with accommodation option
>>> add_person Nelly Armweek Fellow Y

# Sample output for adding Fellow with accommodation option
Fellow Nelly Armweek has been successfully added.
Nelly has been allocated the office Blue
```
# Print Room
```USAGE: print_room <room_name>```
Prints  the names of all the people in room_name on the screen.
```ROOM NAME
-------------------------------------
MEMBER 1, MEMBER 2, MEMBER 3
```
# Print Allocations

```USAGE: print_allocations [-o=filename]```
Prints a list of allocations onto the screen. Specifying the optional -o option here outputs the registered allocations to a txt file
```ROOM NAME
-------------------------------------
MEMBER 1, MEMBER 2, MEMBER 3

ROOM NAME
-------------------------------------
MEMBER 1, MEMBER 2
```

# Print Unallocated
```USAGE: print_unallocated [-o=filename]```
Prints a list of unallocated people to the screen. Specifying the -o option here outputs the information to the txt file provided.




