# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import math
import random
import simplegui

## global variable listing
num_range = 100
guess_remain = 7
secret_number = 0


# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global guess_remain
    global secret_number
    secret_number = random.randrange(0, num_range)
    
    print "Guess the number! 1 -", num_range
    
    if num_range == 100:
        guess_remain = 7
        return
    elif num_range == 1000:
        guess_remain = 10
        return
    print "You have", guess_remain, "guesses remaining."

    
# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global num_range
    num_range = 100
    global guess_remain
    guess_remain = 7
    print " "
    print "New game! Now guessing from 1 -", num_range
    print "You have", guess_remain, "guesses remaining."
    new_game()
    

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global num_range
    num_range = 1000
    global guess_remain
    guess_remain = 10
    print " "
    print "New game! Now guessing from 1 -", num_range
    print "You have", guess_remain, "guesses remaining."
    new_game()


def input_guess(guess):
    # main game logic goes here
    global secret_number
    global guess_remain
    global winner
    global outcome

    guess_int = int(guess)
    print "Your guess:", guess_int

    guess_remain -= 1

    winner = False
    
    if guess_int == secret_number:
        winner = True
    elif guess_int < secret_number:
        outcome = "Higher..."   
    else:
        outcome = "Lower..."

    if winner:
        print " "
        print "Winner! You guessed correctly!"
        print " "
        new_game()
        return
    elif guess_remain == 1:
        print outcome, "This is your FINAL guess!"
        return
    elif guess_remain < 1:
        print " "
        print "Game over. The correct number was:", secret_number
        print " "
        new_game()
        return
    else:
        print outcome, guess_remain, "guesses remaining."
        return
        
        

    
# create frame
f = simplegui.create_frame("Guess the Number, The Game!", 250, 250)                         

# register event handlers for control elements and start frame
f.add_input("Enter your guess:", input_guess, 50)
f.add_button("Range: 0-100", range100, 100)
f.add_button("Range: 0-1000", range1000, 100)
    
# call new_game 
new_game()
f.start()

# always remember to check your completed program against the grading rubric
