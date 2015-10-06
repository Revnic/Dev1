while True:
    text = raw_input("Enter a word\n")
    numInput = raw_input("Enter a number\n")
   
    num = int(numInput)

    output = ""
    textL = len(text)
    count = 0
    while textL > 0:
        x = text[count]
        count += 1
        textL -= 1
        if x.isalpha(): #a = 97 | A = 65 | z = 122 | Z = 90
            letterN = ord(x) # 26
            while num > 26:
                num -= 26
            while num < -26:
                num -= -26
            newLetterN = letterN + num 
            letterNew = chr(newLetterN)
            if x.islower(): # if lowercase
                if newLetterN > 122: #Als het boven de z uitkomt
                    a = newLetterN - 122
                    b = 96 + a
                    c = chr(b)
                    output += c
                elif newLetterN < 97:
                    a = 97 - newLetterN
                    b = 123 - a
                    c = chr(b)
                    output += c
                else:
                    output += letterNew
            else:
                if newLetterN > 90: #Als het boven de Z uitkomt
                    a = newLetterN - 90
                    b = 64 + a
                    c = chr(b)
                    output += c
                elif newLetterN < 65:
                    a = 97 - newLetterN
                    b = 123 - a
                    c = chr(b)
                    output += c
                else:
                    output += letterNew

        else:
            output += x

    print output

    
    
