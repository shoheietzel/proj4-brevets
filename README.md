# Project 4:  Brevet time calculator with Ajax #
### Author: Shohei Etzel, sse@uoregon.edu ###

### Summary ###
A RUSA ACP controle time calculator implemented flask and ajax

### AJAX and Flask reimplementation ###

The reimplementation will fill in the input fields are filled.  Each time a distance is filled in, the corresponding open and close times should be filled in.
The client-side HTML interacts with the server side python program using javascript with the aid of AJAX and flask. This is what allows immediate response to the user inputs, therefore not requiring form submission or page refreshing.

### Running and Testing ##

To start the server, go to the main repository and type commands 'make install' (for first time users) and then 'make start' into the terminal. To stop the server, type 'make stop'

In order to run the integrated tests, type the command 'make test' into the terminal.

### More on test ###
Test 1: tests a series of consoles on the default brevit distance/start time
Test 2: tests consoles on a different starting time
Test 3: tests consoles on a different brevet distance
Test 4: test on a console that is over the brevit distance but within 110%
Test 5: tests two consoles on a brevet that occurs over the daylight savings time change
