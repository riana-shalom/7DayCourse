import random

def menu():
    print("Hello! What would you like to run?")
    lab = int(input("Here are the different Labs!\n\n  1:  Python Intro\n  2:  Selection Lab\n  3:  Iteration Lab\n  4:  Lists\n  5:  Inbuilt Functions\n  6:  Custom Functions\n  7:  File IO\n  8:  PythonDB\n  9:  Classes\n  10: OOP\n  11: Testing\n  12: Linting\n  13: Flask\n\nPlease enter a numerical value for the Lab you want to access: "))

    if lab == 1:
        lab1()
    elif lab == 2:
        lab2()
    elif lab == 3:
        lab3()
    elif lab == 4:
        lab4()
    elif lab == 4:
        lab5()
    elif lab == 4:
        lab6()

def lab1():
    # Task 1 + Stretch (variables) - Python Intro

    print("\nHello User! Welcome to Lab 1!")

    movie1 = "THGTTG" # The Hitchhiker's Guide to the Galaxy (Very well done both times, and the books are great)
    movie2 = "MP & THG" # Monty Python & The Holy Grail (Do I even need to explain?)
    movie3 = "GOTG" # Guardians of the Galaxy (Incredible soundtrack)

    print(f"In no particular order, {movie1}, {movie2}, and {movie3} are three of my favourite movies!")

    # Task 2 + Stretch (an array for up to 3 extra toppings) - Input fields

    name = input("\nWhat is your name? ") # Collecting order data for the user
    drink = input ("What drink do you want? ")
    quantity = int(input("How many drinks would you like? Please enter a valid integer: "))
    whippedCream = input("Would you like whipped cream? Y/N: ") # This is to catch some human error, another solution is requesting True/False and then writing bool(input("Message here - True or False only!"))
    toppingsList = []

    while True: # I could've also done this for quantity, but as this is a proof of concept more than anything else there's no need to
        toppings = int(input("You can have up to 3 extra toppings! How many would you like? Please enter a valid integer: "))
        
        if (toppings > 3) or (toppings < 0):
            print("You didn't enter an integer between 0 and 3")
        else:
            break

    for i in range(1,toppings+1): # User enters toppings here
        toppingsList.append(input(f"Topping {i}: "))

    if (whippedCream.lower() == "y") or (whippedCream.lower() == "yes"):
        whippedCream = True

        if len(toppingsList) > 0:
            print(f"Hello {name}, we are making you {quantity} {drink} with whipped cream! Your toppings are {toppingsList}!")
        else:
            print(f"Hello {name}, we are making you {quantity} {drink} with whipped cream!")

    else:
        whippedCream = False

        if len(toppingsList) > 0:
            print(f"Hello {name}, we are making you {quantity} {drink}! Your toppings are {toppingsList}")
        else:
            print(f"Hello {name}, we are making you {quantity} {drink}!")

def lab2():
    # Task 1 + Stretch (if/else statements) - Flow Statements

    age = 0

    while True: # POC - validating a numerical input
        age = input("\nPlease enter your age as a valid integer: ")

        try:
            age = int(age)
            if age > 0: # Valid must be greater than 0 for an age
                break
            else:
                print("You did not enter a valid integer")
        except:
            print("You did not enter a valid integer")
        
    if age >= 18:
        print("You are in Category A")
    elif age == 16:
        print("You are in Category B")
    if age <= 16:  # Valid between 1 and 16 due to the restrictions in the try-except
        print("You are in Category C")
    else:
        print("The task does not outline a Category for you") # Age 17 is not accounted for in the task

    # Task 2 - Part 1 - Calculator

    while True: # Sometimes you gotta calculate more than once
        number = int(input("\nHere are the options for the Calculator:\n\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Power\n\nWhat would you like our simple calculator to do for you? Please enter a valid integer: "))
        num1 = int(input("Enter your first number: "))
        num2 = int(input("Enter your second number: "))

        if number == 1: # Add
            print(f"According to my records, {num1} + {num2} = {num1+num2}")
        elif number == 2:# Subtract
            print(f"According to my records, {num1} - {num2} = {num1-num2}")
        elif number == 3:# Multiply
            print(f"According to my records, {num1} x {num2} = {num1*num2}")
        elif number == 4:# Divide
            print(f"According to my records, {num1} / {num2} = {num1/num2}")
        elif number == 5:# Power
            print(f"According to my records, {num1} to the power of {num2} = {num1**num2}")

        satisfied = input("Are you finished using the calculator? Y/N: ")

        if (satisfied.lower() == "yes") or (satisfied.lower() == "y"):
            break
        else:
            print("Let's go again!\n")

    # Task 2 - Part 2 + Stretch (number validation and grade boundary moving) – Exam Grades

    while True: # Forcing 1-100 integer input
        grade = int(input("\nWhat grade would you like to check? Please enter a valid integer between 1 and 100: "))

        try:
            grade = int(grade)

            if (grade >= 0) or (grade <= 100): # Valid must be greater than 0 and less than 100
                break
            else:
                print("You did not enter a valid integer between 1 and 100")
        except:
            print("You did not enter a valid integer between 1 and 100")

    boundaries = input("What boundaries would you like to use?\n\n 1. Level 1 Boundaries (higher)\n 2. Level 2 Boundaries (lower)\n\nPlease enter either 1 or 2: ")

    if boundaries == "1":    
        if grade > 70:
            print("This grade is a distinction")
        elif (60 <= grade <= 70):
            print("This grade is a merit")
        elif (50 <= grade <= 60):
            print("This grade is a pass")
        else:
            print("This grade is a fail")
    else:
        if grade > 65:
            print("This grade is a distinction")
        elif (50 <= grade <= 65):
            print("This grade is a merit")
        elif (40 <= grade <= 50):
            print("This grade is a pass")
        else:
            print("This grade is a fail")

# Task 2 - Part 3 + Stretch (choose side) - Pythagoras

    while True: # Forcing 1-100 integer input
        missingSide = input("\nFor the Pythagorean Theorem, there is 1 longer side and 2 shorter sides. Would you like to calculate the longer side or a shorter side? Please enter either 'longer' or 'shorter': ")

        if (missingSide == "longer") or (missingSide == "shorter"):
            break
        else:
            print("You did not enter either 'longer' or 'shorter'")

    side1 = int(input("Length 1 - Please enter a valid integer: "))
    side2 = int(input("Length 2 - Please enter a valid integer: "))

    if missingSide == "longer":
        print(f"The missing longer value is {round(((side1**2)+(side2**2))**0.5)}.")
    elif missingSide == "shorter":
        if (side1 > side2):
            print(f"The missing shorter value is {round(((side1**2)-(side2**2))**0.5)}.")
        else:
            print(f"The missing shorter value is {round(((side2**2)-(side1**2))**0.5)}.")

def lab3():
    # Task 1 - Part 1 – Squares

    number = 1
    print("\n\n")

    while number < 100:
        numberSqr = number * number
        print(numberSqr)

        if numberSqr > 2000:
            break
        else:
            number += 1

    # Task 1 - Part 2 + Stretch (custom values) – Investment

    print("Let's calculate your investment statistics!")
    initInvest = int(input("\nWhat is the initial investment value? Please enter a valid integer: "))
    targetValue = int(input("\nWhat is target value of the investment? Please enter a valid integer: "))
    intRate = int(input("\nWhat is the interest rate on the investment (as a percentage)? Please enter a valid number: "))
    years = 0

    #while initInvest <= targetValue:
    #    initInvest = initInvest*intRate


    #    years += 1


    # Time = (Simple Interest x 100)/(Principal x Interest Rate)

    #Calculates how many years it will take an initial investment of X to grow to a target value of Y if the interest rate is Z%.
    
    # Task 1 - Part 3 + Stretch (seekable letters) – Count Vowels

    word = list(input("\nWhat word would you like us to search? "))
    numberOfCons = int(input("How many consonants would you like to check for? Please enter an integer between 1 and 3: "))
    letters = ["a", "e", "i", "o" , "u"]
    counter = 0

    for i in range(1,numberOfCons+1):
        letters.append(input(f"Consonant {i}: "))

    while len(word) > 0:
        
        if word[0] in letters:
            counter += 1

        word.pop(0)

    print(f"Your letters {letters} appeared a total of {counter} times!\n")

    # Task 2 - Part 1 – Counting Down

    for number in range(31, 0, -3):
        if number < 10:
            print(f"{number} is less than 10")
            break
        else:
            print(number)

    # Task 2 - Part 2 + Stretch (custom values and hot-or-cold game) – Integer Between two limits

    minValue = int(input("\nWhat is the minimum value? Please enter a valid integer: "))
    maxValue = int(input("What is the maximum value? Please enter a valid integer: "))
    noOfGuesses = int(input("What is number of guesses? Please enter an integer: "))

    number = random.randint(minValue, maxValue)
    print("NUMBER", number)

    for i in range(0, noOfGuesses):
        guess = int(input(f"What is your guess between {minValue} and {maxValue}? Please enter a valid integer: "))

        if guess == number:
            print("You won!")
            break
        elif ((number - (maxValue/8) < guess < (number + (maxValue/8)))):
            print(f"Warm, {noOfGuesses-i-1} guesses left")
        else:
            print(f"Cold, {noOfGuesses-i-1} guesses left")

        i += 1
    
    # Task 2 - Part 3 – Factorials

    factNumber = int(input("\nWhat number would you like the factorial of? Please enter a valid integer: "))
    factorial = 1

    for i in range(1, factNumber+1):
        factorial = factorial*i

    print(factorial)

def lab4():




menu()
print("\nDONE\n")
