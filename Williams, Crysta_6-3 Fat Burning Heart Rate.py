#Crysta Williams
#6-3 Fat Burning Heart Rate

import math

print ('Welcome to the Weber State Univeristy Human Performance Lab!\n Please utilize the following calculator to find your ideal fat burning heart rate and BMI')

#Get age information
while True:
    try:
        age = int(input('Enter Age:'))
        if age < 0:
            raise ValueError ('Invalid Age. Number must be greater than 0')
        else:
            print('Thank you.')
            break
    except ValueError as excpt:
        print(excpt)
        print('Invalid Entry.')

#Get height information
def get_height():
    while True:
        height_input = input("Please enter your height in inches or press 'C' if you need a conversion: ").strip()

        #If user needs to convert to inches
        if height_input.lower() == 'c':
            try:
                feet = int(input('How tall are you? \n Feet:'))
                inches = int(input('Inches: '))
                height = feet*12 + inches
                print("You are", height, "inches tall.")
                break #Exits loop afrter conversion
            except ValueError:
                print("Invalid input. Please enter numbers only.")
                continue
        else:
            #If user knows how many inches, validate
            try:
                height = int(height_input) #Convert input to int
                if height <0:
                    raise ValueError ("Invalid entry. Please enter a positive number.")
                else:
                    print("Thank you!")
                    break #Exits loop after valid height entry
            except ValueError as excpt:
                print('Invalid entry.')
    return height

#Get Height - Note to self. I initially put this towards the end by the BMI formula. Doing that triggered the system to initiate the 'height' block after the weight block rather than in order.
user_height = get_height()

#Get Weight Information
while True:
    try:
        weight_input = int(input('Please enter your weight in pounds: '))
        if weight_input < 0:
            raise ValueError("Weight must be a positive number. Please try again.")
        else:
            print("Thank you!")
            break #Exits loop after valid weight entry
    except ValueError as excpt:
        print(excpt)
        print('Invalid Entry. Please enter a number.')


print ('Age = ', age)
print('Height = ', user_height)
print('Weight =', weight_input)

#Heart Rate Calculation
heartrate = round(((220 - 20)*.7),2)
print('Fat Burning Heart Rate = ', heartrate, 'bpm')

#BMI Calculations
body_mass_index = round((703 * weight_input)/(user_height**2),2)
print('BMI = ', body_mass_index)