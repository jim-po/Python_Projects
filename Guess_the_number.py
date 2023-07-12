import random
while True:
    attempts = 0
    success = False
    number_array = [42, 69, 206, 911, 2020]
    value = random.randint(0,len(number_array)-1)
    lucky_number = number_array[value]
    print("Welcome to the Guess-the-Number game")
    print("You have 5 attempts to find the correct number\n")
    if lucky_number == number_array[0]:
        print("Hint: The Ultimate Question of Life, the Universe, and Everything")
    elif lucky_number == number_array[1]:
        print("Hint: Nice!")
    elif lucky_number == number_array[2]:
        print("Hint: The number of bones in a human body")
    elif lucky_number == number_array[3]:
        print("Hint: What's your emergency?")
    elif lucky_number == number_array[4]:
        print("Hint: The year of the Pandemic")
    while True:
        number = input("\nPLease enter a number:")
        if number.isdigit():
            number = int(number)
            attempts += 1
            if number == lucky_number:
                success = True
                break
            if attempts == 5:
                success = False
                break
            if number > lucky_number:
                print("Lower!")
            else:
                print("Higher!")
            print(f"You have {5 - attempts} attempts left!")
            print("Try again!")
        else:
            print("Please type in a valid number (no letters, symbols or decimals)")
    if success == True:
        print("Congrats!! you found the correct number!")
        if attempts == 1:
            print("You managed to find it in the first attempt! Amazing!")
        else:
            print(f"It took you {attempts} attempts to find it!")
    else:
        print("Too bad! you have 0 attempts left")
        print(f"The correct answer was {lucky_number}")
        print("Better luck next time!")
    print("Press any key to restart or q to exit the program")
    choice = input()
    if choice.lower() == "q":
        break