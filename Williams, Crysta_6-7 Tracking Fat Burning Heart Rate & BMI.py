# Crysta Williams
# 6-3 Fat Burning Heart Rate

import math

print("Welcome to the Weber State University Human Performance Lab!")
print("Please utilize the following calculator to find your ideal fat burning heart rate and BMI.")
print("The program will also store this information in a file so that it can be tracked over time.")

while True:
    print("\nMenu:")
    print("1. Create a file")
    print("2. Open a file to add results to")
    print("3. Read results from file")
    print("4. Quit")
    option = int(input("Select: "))

    # Option 1: Creates an empty file
    if option == 1:
        fileName = input("Enter the name of the file you would like to create (no .txt needed): ")
        try:
            with open(f"{fileName}.txt", "x") as newFile:
                print("File created.")
        except FileExistsError:
            print("File already exists. Try opening it instead.")

    # Option 2: Opens file to add results
    elif option == 2:
        fileName = input("Enter the file name (no .txt needed): ")
        try:
            with open(f"{fileName}.txt", "r") as currentFile:
                print("File found. You can now add data.")
        except FileNotFoundError:
            print("File not found. It will be created.")
            with open(f"{fileName}.txt", "w") as newFile:
                pass  # Just creating an empty file

        # Get user data
        while True:
            try:
                age = int(input("Enter Age: "))
                if age <= 0:
                    raise ValueError("Invalid Age. Must be greater than 0.")
                break
            except ValueError as excpt:
                print(excpt)

        # Height input
        def get_height():
            while True:
                height_input = input("Enter height in inches or press 'C' for conversion: ").strip()
                if height_input.lower() == 'c':
                    try:
                        feet = int(input("Feet: "))
                        inches = int(input("Inches: "))
                        return feet * 12 + inches
                    except ValueError:
                        print("Invalid input. Try again.")
                else:
                    try:
                        height = int(height_input)
                        if height <= 0:
                            raise ValueError
                        return height
                    except ValueError:
                        print("Please enter a valid number.")

        user_height = get_height()

        # Weight input
        while True:
            try:
                weight = int(input("Enter your weight in pounds: "))
                if weight <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Please enter a valid weight.")

        # Calculations
        heartrate = round((220 - age) * 0.7, 2)
        bmi = round((703 * weight) / (user_height ** 2), 2)

        print(f"\nResults:")
        print(f"Fat Burning Heart Rate: {heartrate} bpm")
        print(f"BMI: {bmi}")

        # Save results to file
        try:
            with open(f"{fileName}.txt", "a") as f:
                f.write(f"Age: {age}, Height: {user_height} in, Weight: {weight} lbs, ")
                f.write(f"Fat Burning Heart Rate: {heartrate} bpm, BMI: {bmi}\n")
            print("Results saved to file.")
        except Exception as err:
            print("Error saving to file:", err)

    # Option 3: Reads past results
    elif option == 3:
        fileName = input("Enter the file name to read (no .txt needed): ")
        try:
            with open(f"{fileName}.txt", "r") as f:
                print("\nPrevious Results:")
                print(f.read())
        except FileNotFoundError:
            print("File not found.")

    # Option 4: Quit program
    elif option == 4:
        print("Thank you for using the Williams Health Calculator. Stay healthy!")
        break  # Ends the loop and exits program

    else:
        print("Invalid option. Try again.")
