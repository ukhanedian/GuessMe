# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random

secret_num = 0
guesses_remaining = 7
max_num = 100

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_num, guesses_remaining
    
    # remove this when you add your code    
    if max_num == 100:
        guesses_remaining = 7
        secret_num = random.randrange(0, 100)
        print "New game. Range is (0, 100)"
        print "Number of remaining guesses is", str(guesses_remaining)
        print "\n"
        
    elif max_num == 1000:
        guesses_remaining = 10
        secret_num = random.randrange(0, 1000)
        print "New game. Range is (0, 1000)"
        print "Number of remaining guesses is", str(guesses_remaining)
        print "\n"
        
# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global max_num
    # remove this when you add your code    
    max_num = 100
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global max_num
    max_num = 1000
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    global max_num, guesses_remaining, secret_num
    
    # remove this when you add your code
    guess = int(guess)
    print "Guess was", str(guess)
    guesses_remaining = guesses_remaining - 1
    print "Number of remaining guesses is", str(guesses_remaining)
    
    if guess == secret_num:
        print "Correct!"
        new_game()
        
    elif guesses_remaining > 0 and guess > secret_num:
        print "Lower!"
        print"\n"
    elif guesses_remaining > 0 and guess < secret_num:
        print "Higher!"
        print "\n"
    
    else:
        print "You ran out of guesses. The number was", secret_num
        new_game()
# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)
frame.add_button("Range of (0,100)", range100)
frame.add_button("Range of (0,1000)", range1000)
inp = frame.add_input("Guess", input_guess, 50)

# register event handlers for control elements and start frame

# call new_game 
new_game()

# always remember to check your completed program against the grading rubric
