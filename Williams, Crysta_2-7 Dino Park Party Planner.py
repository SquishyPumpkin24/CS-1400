#Welcome
print("Welcome to the Dinosaur Park Party Planner")

# Loop to keep the program running until the user chooses to quit
while True:
    print("\nChoose the type of party")
    print("1. Group Rate Admission Party")
    print("2. Bare Bones Package")
    print("3. Deluxe Party Package")
    print("4. Quit")

#Party Selection
    question1 = int(input("Please choose the type of party you would like to have: \n"))


#Party 1 Calculation
    if question1 ==1:
        party1a = int(input("\nYou chose the Group Rate Admission Party. How many people will be attending? \n"))
        if party1a >= 10:
            party1b = int(input("You get a group discount! By reserving a group party slot of 10 or more people your group will be admitted to the Park at the group discount rate of $5.00 for Adults (13+), and 4.00 Children (2-12)! \nPlease enter how many adults will be attending: \n"))
            party1c = int(input("Please enter how many children will be attending (2-12): \n"))
            if party1b + party1c < 10:
                print("You must have at least 10 guests for the group discount. The non-group cost is $8 per person. The cost for", party1b + party1c, "guests will be:\n",f"Cost = ${(party1b+party1c)*8:.2f}")
            else:
                print(f"Cost = ${party1b*5 + party1c*4:.2f}")

#note to self - print("Cost = $", party1b*5 + party1*4) did not display the answer as a decimal and , round() didn't work either.
#Enter as an formatted string. {} used for formatted string while () usef for funcions. :. used to signal start of formatting and how many decimal places
#If they enter 10, but the count <10

        if party1a < 10:
            party1d = int(input("Please enter how many adults will be attending (13+): \n"))
            party1e = int(input("Please enter how many children will be attending (2-12): \n"))
            print (f"Cost = ${(party1d+party1e)*8:.2f}")

#Party 2 Calculation
    membercost = 99
    nonmembercost = 119
    if question1 == 2:
        party2a = int(input("You chose the Bare Bones Party Package. This includes admission for up to 12 people and $3.00 per additional guest.\nAre you a Dinosaur Park member? Please enter 1 for 'Yes' and 2 for 'No': "))
        if party2a == 1:
            party2b = int(input("Will you be having more than 12 guests? Please enter 1 for 'Yes' and 2 for 'No': \n"))
            if party2b == 1:
                party2c = int(input("Please enter how many additional guests you will be having: \n"))
                print(F"Cost = ${membercost + party2c*3:.2f}")
        if party2a == 2:
            party2d = int(input("Will you be having more than 12 guests? Please enter 1 for 'Yes' and 2 for 'No': \n"))
            if party2d == 1:
                party2e = int(input("Please enter how many additional guests you will be having: \n"))
            print(f"Cost = ${nonmembercost + party2e*3:.2f}")
            if party2d == 2:
                print(f"Cost = ${nonmembercost:.2f}")

#Party 3 Calculation
    membercost = 175
    nonmembercost = 199
    if question1 == 3:
        party3a = int(input("You chose the Deluxe Party Package. This includes admission for up to 12 people, with $3.00 per additional guest, and a variety of activities & gifts for kids!\nAre you a Dinosaur Park member? Please enter 1 for 'Yes' and 2 for 'No': "))
        if party3a == 1:
            party3b = int(input("Will you be having more than 12 guests? Please enter 1 for 'Yes' and 2 for 'No': \n"))
            if party3b == 1:
                party3c = int(input("Please enter how many additional guests you will be having: \n"))
                print(F"Cost = ${membercost + party3c*3:.2f}")
            if party3b == 2:
                print(f"Cost = ${membercost:.2f} ")
        if party3a == 2:
            party3d = int(input("Will you be having more than 12 guests? Please enter 1 for 'Yes' and 2 for 'No': \n"))
            if party3d == 1:
                party3e = int(input("Please enter how many additional guests you will be having: \n"))
                print(f"Cost = ${nonmembercost + party3e*3:.2f}")
            if party3d == 2:
                print(f"Cost = ${nonmembercost:.2f}")

# Exit condition
    if question1 == 4:
        print("Thank you for using Williams Dinosaur Park Party Calculator!") 
        break 
# Exits the loop

#End
print("Thank you for using Williams Dinosaur Park Party Calculator!") 