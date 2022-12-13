import random, statistics 

def menu():
    print("Hello! What would you like to run?")
    lab = float(input("Here are the different Labs!\n\n  1:  Python Intro\n  2:  Selection Lab\n  3:  Iteration Lab\n  4:  Lists\n  5:  Inbuilt Functions\n  6:  Custom Functions\n  7:  File IO\n  8:  PythonDB\n  9:  Classes\n  10: OOP\n  11: Testing\n  12: Linting\n  13: Flask\n\nPlease enter a numerical value for the Lab you want to access: "))

    if lab == 1:
        lab1()
    elif lab == 2:
        lab2()
    elif lab == 3:
        lab3()
    elif lab == 4:
        lab4()
    elif lab == 5:
        lab5()
    elif lab == 6:
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

    word = list(input("\nWhat word would you like us to search? ").lower())
    numberOfCons = int(input("How many consonants would you like to check for? Please enter an integer between 1 and 3: "))
    letters = ["a", "e", "i", "o" , "u"]
    counter = 0

    for i in range(1,numberOfCons+1):
        letters.append(input(f"Consonant {i}: ").lower())

    while (len(word)) > 0:

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
    # Task 1 - Working with large list

    ages =[12,18,33,84,45,67,12,82,95,16,10,23,43,29,40,34,30,16,44,69,70,74,38,65,36,83,50,11,79,64,78,37,3,8,68,22,4,60,33,82,45,23,5,18,28,99,17,81,14,88,50,19,59,7,44,93,35,72,25,63,11,69,11,76,10,60,30,14,21,82,47,6,21,88,46,78,92,48,36,28,51]

    # Subtask 1 - Record the length of the list and save this as a variable
    lengthOfAges = len(ages)

    # Subtask 2 - Using a loop, display all the numbers in the list line by line
    print("\nHere are all the current ages: ")
    for i in range(0,lengthOfAges):
        print(ages[i])

    # Subtask 3 - Looping through the list, increase the value of each age by 1
    for i in range(0,lengthOfAges):
        ages[i] = ages[i] + 1
    
    # Subtask 4 - Create a new list which only contains the ages in the age range of 16 – 65, display the new list
    rangedAgesList1665 = []

    for i in range(lengthOfAges): 
        if (16 <= ages[i] <= 65):
            rangedAgesList1665.append(ages[i])

    print("\nHere is the age range limited list, from 16-65: ", rangedAgesList1665)

    #5)	Display the count of 16 – 25 year olds in the new list
    noOf1625 = 0

    for i in range(0,len(rangedAgesList1665)):
        if (16 <= ages[i] <= 25):
            noOf1625 += 1

    print(f"\nThere are {noOf1625} ages between 16-25 in your new list")

    #6)	Sort the ages of the new list
    rangedAgesList1665.sort()

    #7)	What proportion of people belong in the 16 – 25 category within the new list
    proportionOfAges = round(100*(noOf1625/len(rangedAgesList1665)), 2)
    print(f"\nThere are {noOf1625} ages (between 16 - 25) out of {len(rangedAgesList1665)} ages (between 16 - 65), which is a proportion of {proportionOfAges}%!")

    # Task 2 (changed) - Movie Directors
        # Initialise a Dictionary with the key being Directors and value being movie titles,
        # Write a program which asks the user for a director name and returns all movies directed by that person

    directorMovies = {"tarantino" : ["Reservoir Dogs", "Django Unchained", "Kill Bill", "Pulp Fiction"], "lucas" : ["Star Wars", "Red Tails"], "waititi" : ["Thor Ragnarok", "Love and Thunder", "Boy", "Jojo Rabbit", "Free Guy", "Green Lantern"]}
    print("\nThis is some of Tarantino's work: ", directorMovies["tarantino"])
    info = input("Who would you like to see? Please enter either 'Lucas' or 'Waititi': ")
    print(f"This is some of {info}'s work: ", directorMovies[info.lower()])

def lab5():
    # Task 1 - Inbuilt Functions
    
    data="100,30,53,67,85,87,50,45,51,72,64,69,59,17,22,23,44,25,16,67,85,87,50,45,51,72,59,14,50,55,32,23,24,25,37,28,39,30,33,35,40,34,41,43,94,95,59,98,99,44,45,47,48,49,53,61,63,69,75,77,60,83"

    # Subtask 1 - Convert the string into a list of values
    dataList = data.split(",")

    for i in range(0, len(dataList)):
        dataList[i] = int(dataList[i])

    # Subtask 2 - Display the minimum and maximum value of grades
    print("\nThe biggest score is", max(dataList))
    print("The smallest score is", min(dataList))

    # Subtask 3 - If your code displayed 100 as minimum and 99 as maximum work out why it has done this
        # My code did not do this. This would happen if the 'for' loop wasn't there, as this converts each string into an integer number
    
    # Subtask 4 - Display the average of grades to 2 decimal points
    averageMean = 0

    for i in range(0, len(dataList)):
        averageMean += dataList[i]

    print(f"\nUsing no imports, the mean average of the data list is: {round((averageMean/len(dataList)), 2)}")

    # Subtask 5 - Import the statistics library using - `import statistics`
        # This was imported on line 1

    # Subtask 6 - Use the statistics.mean() function to get the average grade to 2 decimal points
    print(f"Using Statistics, the mean average of the data list is: {round(statistics.mean(dataList), 2)}")

    # Subtask 7 - Display the median() value of this list
    print(f"Using Statistics, the median average of the data list is: {statistics.median(dataList)}")

    # Subtask 8 - Use the string.format() to display the min, max, average, mean and median values 
        # This has already been done in the subtasks above. String.format
    
    print("You have seen the statistics!")

def lab6():
    # Task 1 + Stretch (functions calling eachother) - Basic Functions

    def rollFour():
        return random.randint(1, 4)

    def rollSix(): # Pre-written
        return random.randint(1, 6)

    def rollEight():
        return random.randint(1, 8)

    def rollTen():
        return random.randint(1, 10)

    def rollDice(num):  # Pre-written
        return random.randint(1, num)

    def lotsOfDice():
        fourNumbers = [random.randint (1, 6) for _ in range (4)] # A very cool way of generating numbers repeatedly
        fourNumbers.remove(min(fourNumbers))
        return fourNumbers

    def generatingStats():
        numbersRolled = []
        for i in range(4):
            numbersRolled.append(lotsOfDice())

        return numbersRolled

    print("\nLet's roll some dice!")
    print("Rolling d4:", rollFour())
    print("Rolling d6:", rollSix())
    print("Rolling d8:", rollEight())
    print("Rolling d10:", rollTen())
    print("Here are your Generated Stats:", generatingStats())
    print("Rolling a random number between 1 and 10, and then rolling another dice with the results:", rollDice(rollTen()))
    
    # Task 2 + Stretch ('Complex version: Bracketed salary taken into account') - Basic Functions

    def autoCalculating(salary, taxBracket):
        pass

    def taxCalculations():
        pass

    def taxCalculations1(salary):
        if salary < 12570:
            return 0
        elif salary < 23000:
            return (salary*0.19)
        elif salary < 40000:
            return (salary*0.30)
        elif salary < 150000:
            return (salary*0.41)
        else:
            return (salary*0.46)

    


    salary = round(float(input("\nEnter a salary - Please enter a valid number: ")), 2)
    print("You will pay tax of £", taxCalculations1(salary), f"for salary £{salary}")
    
# No tax paid on £12,570 personal allowance.
# £12,571 to £23,000 starter rate of 19%
# £23,000 to £40,000 intermediate rate of 30%
# £40,001 to £150,000 higher rate of 41%
# Above £150,000 top rate of 46%

# Complex version: With the salary it is taxed correctly with it being bracketed, this should be done with a series of loops and conditional statements

    
menu()
print("\nDONE\n")
