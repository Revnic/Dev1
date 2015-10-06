while True:
    print ("Choose a number for a figure\n")
    print ("1: A full square")
    print ("2: A hollow square")
    print ("3: A full rectangle traingle")
    print ("4: A full isosceles traingle")

    figure = int(raw_input())
    number = int(raw_input("Choose a number\n"))
    symbol = ""
    
   
    def square(number, symbol):
        for x in range(number):
           for x in range(number):
                symbol +="*"
           symbol += "\n"
        return symbol

    def hollowSquare(number,symbol):
        for i in range(number):
            if 1 == 0 or i == number-1:
                symbol = number * "*"
            else:
                symbol = "*"," "*number,"*"
                symbol += symbol
        return symbol

    def rectangleTraingle(number, symbol):
        for x in range(number):
            symbol += "*"
            return symbol       
        
    #def isoscelesTraingle(number,symbol)
       
    if figure == 1: 
        x = square(number,symbol)
    elif figure == 2:
        x = hollowSquare(number,symbol)
    elif figure == 3:
        x = rectangleTraingle(number,symbol)
    elif figure == 4:
        x = isoscelesTraingle(number,symbol)

    print x