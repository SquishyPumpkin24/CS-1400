#Import
import math
import random

#Welcome Message
print("Williams Winnings!")
tokens = int(input("Enter the starting number of tokens you wish to use: \n"))
balance = 0

#Loop to keep player rolling until they cash out. Change cash out to non int, otherwise system thinks player wants to quit if they bet 4. 
while True:
    bet_input = input("How much do you wish to bet? (Press 'C' to Cash Out): \n")
        #If user inputs C, cash out
    if bet_input.lower() == 'c':
        print("Balance: ", tokens, "Thank you for playing!")
        break

#Make sure bet is valid
    try:
        bet = int(bet_input)
        if bet > tokens or bet <0:
            print("Invalid bet amount. Please enter a valid bet.")
            continue
            #Note to self: Continue has the program move on to the next iteration. 
    except ValueError:
        print("Invalid input. Please enter a number or 'C' to cash out.")
        continue

#Rolls
    roll1 = random.randrange(1,6)
    roll2 = random.randrange(1,6)
    roll3 = random.randrange(1,6)
    winner = math.pow(roll1,bet)

    print(roll1, roll2, roll3)


#Win
    if roll1 == roll2 == roll3:
        print("You won: ", winner)
        tokens = tokens+winner
        balance += tokens
        print("Balance: ", tokens)

#Lose 
    else:
        print("You lose!")
        tokens -= bet
        print("Balance: ", tokens)

#Ask if user wants to keep playing
        while True:
            try:
                question1 = int(input("Would you like to play again? Press 1 to play again, or press 2 to cash out."))
                if question1 in [1,2]:
                #Note to self: 'in' checks for value in a list, which are done in []
                    break
                else:
                    invalid_option1=int(input("Invalid input. Please enter 1 to play again, or 2 to cash out: "))
            except ValueError:
                print = int(input("Invalid input. Please enter a number (1 or 2): \n"))
        if question1 == 2:
            print("Balance: ", tokens, "Thank you for playing!")
            break

       

        




