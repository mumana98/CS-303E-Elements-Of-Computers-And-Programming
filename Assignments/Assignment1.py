#The purpose of this assignment is to practice taking in user input and do calculations with the given input

# User input of their name, then prints it
name = input("What is your name? ")
print("Hello", name + "!", "You’ve just delved into Python.")

# Converts user input number to Fahrenheit
celsius = eval(input("Enter a degree in Celsius: "))
Fahrenheit = (9/5) * celsius + 32
print(celsius, "Celsius is", Fahrenheit, "Fahrenheit")

# Calculates final bill given the base bill and gratuity rate
bill, rate = eval(input("Enter the bill and gratuity rate: "))
gratuity = round(bill * (rate / 100), 2)
total = float(round(bill + gratuity, 2))
print("The gratuity is", "$" + str(gratuity), "and the total is", "$" + str(total))

# Calculates the sum of the digits in a user given number between 0 and 999
digit = int(input("Enter a number between 0 and 999: "))
sum = digit % 10
sum = sum + ((digit // 10) % 10)
sum = sum + (((digit // 10) // 10) % 10)
print("The sum of the digits is", sum)

# Caluculate the population in the next 5 years given current population
pop = int(input("Enter the current population: "))
sec_per_yr = 31536000;
bpy = sec_per_yr // 7;
dpy = sec_per_yr // 13;
ipy = sec_per_yr // 45;
new_pop = bpy - dpy + ipy;
y1 = pop + new_pop;
print("The population in 1 year will be:", y1)
y2 = y1 + new_pop;
print("The population in 2 year will be:", y2)
y3 = y2 + new_pop;
print("The population in 3 year will be:", y3)
y4 = y3 + new_pop;
print("The population in 4 year will be:", y4)
y5 = y4 + new_pop;
print("The population in 5 year will be:", y5)

# Calculates your BMI given your weight and height
weight = input("Enter your weight in pounds: ")
feet, inches = eval(input("Enter your height (feet, inches): "))
w_kg = float(weight) * .454
h_m = (feet + (inches / 12)) * .3048
BMI = round((w_kg / h_m**2), 2)
print("Your BMI is", BMI)


