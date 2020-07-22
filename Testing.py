#import time

import time

#intro classic    PART ONE
name = input ("What is your name?")
print("Hello, " + name, "Time to play hangman!")
Print("")

#sleep
time.sleep(1)

print("Start guessing...")
time.sleep(0.5)

#set your keyword
word = "secret"

# creats a variable with empty value
guesses = ''

turns = 10       #number of turns


#create a while loop    PART TWO

while turns> 0:             #check if the  no. of turns more than 