# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors


import random

def name_to_number(name):
    name = name.lower()
    if name =="rock":
        number = 0
    elif name=="spock":
        number=1
    elif name=="paper":
        number = 2
    elif name=="lizard":
        number = 3
    elif name=="scissors":
        number =4
    else:
        number= -1

    return number


def number_to_name(number):

    if number==0:
        name= "rock"
    elif number==1:
        name = "Spock"
    elif number==2:
        name="paper"
    elif number==3:
        name="lizard"
    elif number==4:
        name="scissors"
    else:
        name =""
    return name


def rpsls(player_choice):

    print ("\n")

    print ("Player chooses "+ player_choice)

    player_number = name_to_number(player_choice)
    if player_number ==-1:
        print ("Invalid option")
        return

    comp_number = random.randrange(0,5)

    comp_choice = number_to_name(comp_number)

    print ("Computer chooses "+comp_choice)

    diferencia = player_number-comp_number
    diferencia2 = diferencia%5

    if player_number==comp_number:
        print("Player and computer tie!")
    elif diferencia2>=0 and diferencia2<=2:
        print("Player wins!")
    else:
        print("Computer wins!")


rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
