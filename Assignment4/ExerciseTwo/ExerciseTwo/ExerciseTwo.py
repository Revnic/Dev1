
paper = 1
rock = 2 
scissor = 3
play = True

while(play):
    playerOne = input("\nChoose rock, paper or scissor\n\n")

    from random import randint
    computer = randint(1,3)
    
    if playerOne == 1 and computer == 2:
        print "Player one choose paper \nComputer choose rock \nPaper covers rock \nYou win!"
    elif playerOne == 1 and computer == 3:
        print "Player one choose paper \nComputer choose scissor \nScissor cuts paper \nComputer wins!"
    elif playerOne == 1 and computer == 1:
        print "Player one choose paper \nComputer choose paper \nIt's a draw!"

    if playerOne == 2 and computer == 1:
        print "Player one choose rock \nComputer choose paper \nPaper covers rock \nComputer wins!"
    elif playerOne == 2 and computer == 3:
        print "Player one choose rock \nComputer choose scissor \nRock crushes scissor \nYou win!"
    elif playerOne == 2 and computer == 2:
        print "Player one choose rock \nComputer choose Rock \nIt's a draw!"

    if playerOne == 3 and computer == 1:
        print "Player one choose scissor \nComputer choose paper \nScissor cut paper \nYou win!"
    elif playerOne == 3 and computer == 2:
        print "Player one choose scissor \nComputer choose rock \nRock crushes scissor \nComputer wins!"
    elif playerOne == 3 and computer == 3:
        print "Player one choose scissor \nComputer choose scissor \nIt's a draw!"
 