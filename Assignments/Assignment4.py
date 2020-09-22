import turtle


secret_num = 1458
num = 1
guesses = 0
while num != 0:
    num = eval(input("I’m thinking of a number from 1 to 10000. \nTry to guess my number!(Enter 0 to stop playing.)\nPlease enter your guess: "))
    guesses += 1
    if num > 10000 or num < 0:
        num = eval(input("Your guess must be between 1 to 10000.\nPlease enter your guess:"))
        guesses += 1
        if num == 0:
            print("Goodbye!")
        elif num > secret_num:
            print("Your guess is too high.")
        elif num < secret_num:
            print("Your guess is too low.")
        else:
            print("That's correct!You win!\nYou guessed my number in " + str(guesses) + " guesses.")
            guesses = 0
    elif num == 0:
        print("Goodbye!")
    elif num > secret_num:
        print("Your guess is too high.")
    elif num < secret_num:
        print("Your guess is too low.")
    else:
        print("That's correct!You win!\nYou guessed my number in " + str(guesses) + " guesses.")
        guesses = 0

for i in range(5):
    ast = ""
    for j in range(i + 1):
        ast += "*"
    print(format(ast, ">5"))


turtle.speed(0)
row = 0
col = 0
x = 0
y = 0
while row < 10:
    x = 0
    while col < 7:
        turtle.circle(10)
        turtle.penup()
        turtle.goto(x,y)
        turtle.pendown()
        turtle.circle(10)
        col += 1
        x += 20
    col = 0
    y -= 20
    row += 1
    
ts = turtle.getscreen()
ts.getcanvas().postscript(file='Umana_Matthew.eps')


    
