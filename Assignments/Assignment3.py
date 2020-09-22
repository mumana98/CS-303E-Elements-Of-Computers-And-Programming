import random
import turtle

player_choice = input("Choose rock, paper, or scissors: ")

computer_choice = random.randint(1, 3)

if computer_choice == 1:
    computer_choice = "rock"
elif computer_choice == 2:
    computer_choice = "paper"
else:
    computer_choice = "scissors"

print("Computer is " + computer_choice + "." + " You are " + player_choice + "." )

if player_choice == "rock":
    if computer_choice == "paper":
        print("Computer Wins.")
    elif computer_choice == "scissors":
        print("You win.")
    else:
        print("Draw.")
elif player_choice == "paper":
    if computer_choice == "scissors":
        print("Computer Wins.")
    elif computer_choice == "rock":
        print("You win.")
    else:
        print("Draw.")
else:
    if computer_choice == "rock":
        print("Computer Wins.")
    elif computer_choice == "paper":
        print("You win.")
    else:
        print("Draw.")

shape = input("Would you like to draw a circle, square, or triangle? ")
color = input("What color would you like? ")

turtle.speed(0)

if shape == "triangle":
    turtle.penup()
    turtle.color(color)
    turtle.goto(0, 100)
    turtle.pendown()
    turtle.goto(50, 0)
    turtle.goto(-50, 0)
    turtle.goto(0, 100)
elif shape == "square":
    turtle.penup()
    turtle.color(color)
    turtle.goto(100, 100)
    turtle.pendown()
    turtle.goto(100, -100)
    turtle.goto(-100, -100)
    turtle.goto(-100, 100)
    turtle.goto(100, 100)
else:
    turtle.penup()
    turtle.color(color)
    turtle.goto(0, 100)
    turtle.pendown()
    turtle.circle(-100,360)


ts = turtle.getscreen()
ts.getcanvas().postscript(file='lastname_firstname.eps')



