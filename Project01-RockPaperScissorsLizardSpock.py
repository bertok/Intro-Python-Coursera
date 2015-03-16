# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    # convert name to number using if/elif/else
    if name is "rock":
        return 0
    elif name is "Spock":
        return 1   
    elif name is "paper":
        return 2
    elif name is "lizard":
        return 3
    elif name is "scissors":
        return 4
    else:
        return "'" + name + "'", "is not a valid option."   

def number_to_name(number):
    # convert number to a name using if/elif/else
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        return number, "is an invalid number."
          

def rpsls(player_choice):
    # determine a winner based on player_choice versus comp_choice
    
    
    # print a blank line to separate consecutive games
    ## I put this line at the end so as to look more like
    ## the example output in the assignment description

    print "Player chooses", player_choice

    player_number = name_to_number(player_choice)

    import random

    comp_number = random.randrange(0,5)
    
    comp_choice = number_to_name(comp_number)

    print "Computer chooses", comp_choice

    end_result = (player_number - comp_number) % 5

    if (end_result == 1) or (end_result == 2):
        print "Player wins!"
    elif (end_result == 3) or (end_result == 4):
        print "Computer wins!"
    elif end_result == 0:
        print "Player and computer tie!"

    print " "

    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


