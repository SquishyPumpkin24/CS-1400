#To store the shopping list
groceries = []

#Load Shopping List from file
try:
  #open the file
  groceriesFile = open('groceries.txt', 'r')

  for line in groceriesFile:
    groceries.append(line.strip())
except FileNotFoundError as err:
  print(err)
  print('Creating file for groceries.')
  #Creates empty file
  groceriesFile = open("groceries.txt", "x")
  print('File created.')

groceriesFile.close()

while True:
  print(groceries)
  while True:
    try:
        print('1. Add Item\n2. Remove Item \n3. Quit')
        #Make sure 1, 2, or 3 is entered
        choice = int(input())
        break
    except ValueError as errCheck:
        print(errCheck)
        choice = 3

  if choice == 1:
    print('Add item:')
    toAdd = input()
    groceries.append(toAdd)
  elif choice == 2:
    print('Remove item:')
    toRemove = input()
    groceries.remove(toRemove)
  else:
    break

#Saves the list to the file
try:
    groceriesFile = open('groceries.txt', 'w')
    #write to a file
    for g in groceries:
        groceriesFile.write(g + '\n')
except:
    print('Error writing to file.')

groceriesFile.close()


