# Space for imports

def menu():
    print("Hello! What would you like to run?")
    lab = int(input("Here are the different Labs!\n\n  1:  Python Intro\n  2:  Selection Lab\n  3:  Iteration Lab\n  4:  Lists\n  5:  Inbuilt Functions\n  6:  Custom Functions\n  7:  File IO\n  8:  PythonDB\n  9:  Classes\n  10: OOP\n  11: Testing\n  12: Linting\n  13: Flask\n\n Please enter a numerical value for the Lab you want to access: "))

    if lab == 1:
        lab1()
    elif lab == 2:
        lab2()

def lab1():
    # Part 1 + Stretch (variables)

    print("\nHello User! Welcome to Lab 1!")

    movie1 = "THGTTG" # The Hitchhiker's Guide to the Galaxy (Very well done both times, and the books are great)
    movie2 = "MP & THG" # Monty Python & The Holy Grail (Do I even need to explain?)
    movie3 = "GOTG" # Guardians of the Galaxy (Incredible soundtrack)

    print(f"In no particular order, {movie1}, {movie2}, and {movie3} are three of my favourite movies!")

    # Part 2 + Stretch (an array for up to 3 extra toppings)

    name = input("\nWhat is your name? ") # Collecting order data for the user
    drink = input ("What drink do you want? ")
    quantity = int(input("How many drinks would you like? Please enter a valid number: "))
    whippedCream = input("Would you like whipped cream? Y/N: ") # This is to catch some human error, another solution is requesting True/False and then writing bool(input("Message here - True or False only!"))
    toppingsList = []

    while True: # I could've also done this for quantity, but as this is a proof of concept more than anything else there's no need to
        toppings = int(input("You can have up to 3 extra toppings! How many would you like? Please enter a valid number: "))
        
        if (toppings > 3) or (toppings < 0):
            print("You didn't enter a number between 0 and 3")
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
    pass

menu()
print("\n DONE \n")
