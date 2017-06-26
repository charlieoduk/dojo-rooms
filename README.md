# CHECKPOINT 1 - DOJO-ROOMS

[![Build Status](https://travis-ci.org/charlieoduk/dojo-rooms.svg?branch=master)](https://travis-ci.org/charlieoduk/dojo-rooms)
[![Coverage Status](https://coveralls.io/repos/github/charlieoduk/dojo-rooms/badge.svg)](https://coveralls.io/github/charlieoduk/dojo-rooms)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/ea7cce59060e4de3a14b4edfce4c39f9)](https://www.codacy.com/app/charlieoduk/dojo-rooms?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=charlieoduk/dojo-rooms&amp;utm_campaign=Badge_Grade)

[![asciicast](https://asciinema.org/a/uO70YOU772siJpyWS44xzQVyI.png)](https://asciinema.org/a/uO70YOU772siJpyWS44xzQVyI)


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

```USAGE: print_allocations [<filename>]```
Prints a list of allocations onto the screen. Specifying the optional -o option here outputs the registered allocations to a txt file
```ROOM NAME
-------------------------------------
MEMBER 1, MEMBER 2, MEMBER 3

ROOM NAME
-------------------------------------
MEMBER 1, MEMBER 2
```

# Print Unallocated

```USAGE: print_unallocated [<filename>]```
Prints a list of unallocated people to the screen. Specifying the -o option here outputs the information to the txt file provided.

# Reallocate Person

``` USAGE: reallocate_person <person_identifier> <room_type> <new_room_name>``` 
Reallocate the person with person_identifier to new_room_name.

# Allocate Office

``` USAGE: allocate_office <person_identifier> <room_to_allocate>```
Allocate a person from the unallocated list to an office

# Allocate Living Space

```USAGE: allocate_livingspace <person_identifier> <room_to_allocate>```
Allocate a person from the unallocated list to a living space

# Load People

``` USAGE: load_people <filename>```
Adds people to rooms from a txt file. Below is the text input format.

OLUWAFEMI SULE FELLOW Y
DOMINIC WALTERS STAFF
SIMON PATTERSON FELLOW Y
MARI LAWRENCE FELLOW Y
LEIGH RILEY STAFF
TANA LOPEZ FELLOW Y
KELLY McGUIRE STAFF

# Save State

```USAGE: save_state [--db=sqlite_database]```
Persists all the data stored in the app to a SQLite database. Specifying the --db parameter explicitly stores the data in the sqlite_database specified. 

# Load state

```USAGE: load_state <sqlite_database> ```
Loads data from a database into the application.







