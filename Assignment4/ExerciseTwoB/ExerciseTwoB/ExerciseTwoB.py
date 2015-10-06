paper = 1
rock = 2 
scissor = 3
lizard = 4
spock = 5

play = True

while(play):
    playerOne = input("\nChoose rock, paper, scissor, lizard and spock\n\n")

    from random import randint
    computer = randint(1,5)
    
    if playerOne == 1 and computer == 2:
        print "Player one choose paper \nComputer choose rock \nPaper cover rock \nYou win!"
    elif playerOne == 1 and computer == 3:
        print "Player one choose paper \nComputer choose scissor \nScissor cuts paper \nComputer wins!"
    elif playerOne == 1 and computer == 4:
        print "Player one choose paper \nComputer choose lizard \nLizard eats paper \nComputer wins!"
    elif playerOne == 1 and computer == 5:
        print "Player one choose paper \nComputer choose spock \nPaper disaproves spock \nYou win!"
    elif playerOne == 1 and computer == 1:
        print "Player one choose paper \nComputer choose paper \nIt's a draw!"

    if playerOne == 2 and computer == 1:
        print "Player one choose rock \nComputer choose paper \nPaper cover rock \nComputer wins!"
    elif playerOne == 2 and computer == 3:
        print "Player one choose rock \nComputer choose scissor \nRock crushes scissor \nYou win!"
    elif playerOne == 2 and computer == 4:
        print "Player one choose rock \nComputer choose lizard \nRock crushes lizard \nYou win!"
    elif playerOne == 2 and computer == 5:
        print "Player one choose rock \nComputer choose spock \nSpock vaporizes rock \nComputer wins!"
    elif playerOne == 2 and computer == 2:
        print "Player one choose rock \nComputer choose Rock \nIt's a draw!"

    if playerOne == 3 and computer == 1:
        print "Player one choose scissor \nComputer choose paper \nScissor cuts paper \nYou win!"
    elif playerOne == 3 and computer == 2:
        print "Player one choose scissor \nComputer choose rock \nRock crushes scissor \nComputer wins!"
    elif playerOne == 3 and computer == 4:
        print "Player one choose scissor \nComputer choose lizard \nScissor decapitates lizard \nYou win!"
    elif playerOne == 3 and computer == 5:
        print "Player one choose scissor \nComputer choose spock \nSpock smashes scissor \nComputer wins!"
    elif playerOne == 3 and computer == 3:
        print "Player one choose scissor \nComputer choose scissor \nIt's a draw!"

    if playerOne == 4 and computer == 1:
        print "Player one choose lizard \nComputer choose paper \nLizard eats paper \nYou win!"
    elif playerOne == 4 and computer == 2:
        print "Player one choose lizard \nComputer choose rock \nRock crushes lizard \nComputer wins!"
    elif playerOne == 4 and computer == 3:
        print "Player one choose lizard \nComputer choose scissor \nScissor decapitates lizard \nComputer wins!"
    elif playerOne == 4 and computer == 5:
        print "Player one choose lizard \nComputer choose spock \nLizard poisons spock \nYou win!"
    elif playerOne == 4 and computer == 4:
        print "Player one choose lizard \nComputer choose lizard \nIt's a draw!"

    if playerOne == 5 and computer == 1:
        print "Player one choose Spock \nComputer choose paper \nPaper disaprove spock \nComputer wins!"
    elif playerOne == 5 and computer == 2:
        print "Player one choose Spock \nComputer choose rock \nSpock vaperizes rock \nYou win!"
    elif playerOne == 5 and computer == 3:
        print "Player one choose Spock \nComputer choose scissor \nSpock smashes scissor \nYou win!"
    elif playerOne == 5 and computer == 4:
        print "Player one choose Spock \nComputer choose lizard \nLizard poisons spock \nComputer wins!"
    elif playerOne == 5 and computer == 5:
        print "Player one choose Spock \nComputer choose spock \nIt's a draw!"