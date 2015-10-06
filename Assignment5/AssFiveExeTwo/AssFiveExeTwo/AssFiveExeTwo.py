check = True
while check:
    points = 0
    passw = raw_input("Check password\n")
    passwL = len(passw)

    if passwL >= 6 and passwL<= 8:
        points += 2
    elif passwL >=9:
        points += 3

    passwU = sum(1 for var in passw if var.isupper())
    if passwU == 1:
        points += 2
    elif passwU == 2 :
        points += 3
    elif passwU > 3:
        points += 4

    passwLo = sum(1 for var in passw if var.islower())
    if passwLo == 1:
        points += 2
    elif passwLo == 2:
        points += 3
    elif passwLo > 3:
        points += 4

    passwD = sum(1 for var in passw if var.isdigit())
    if passwD == 1:
        points += 2
    elif passwD == 2:
        points += 3
    elif passwD > 3:
        points += 4

    specialC = 0
    while passwL > 0:
        a = passw[passwL -1]
        passwL -= 1
        if a.isalpha() == False:
            if a.isdigit() == False:
                specialC += 1
                
    if specialC == 1:
        points += 3
    elif specialC == 2:
        points += 5
    elif specialC > 3:
        points += 6 

    #print points
    
    if points <= 10:
        print "Weak"
    elif points >= 10 and points <= 15:
        print "Medium"
    elif points > 15:
        print "Strong"
    elif points > 19:
        print "Very strong"