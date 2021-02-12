# Hangman-game
Coded this independently.
Used the following pseudo code before starting to write the actual code. \n

Find long list of random generated strings, \n
get computer to pick a random word from that list\n
computer shows in terminal how long the chosen word is with length function e.g. 6 characters\n

set lives to be a certain number \n
while lives >=1 :
 user inputs 1 character string
if the user selected character is found in the word 
	 tell user what the index of that character is 
    if not found in the word 
	lives -= 1 
print (“ you lose”) 
