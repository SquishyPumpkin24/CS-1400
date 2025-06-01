#Trivia Quiz

question1 = input("Who provided the voice of Groot in the Guardians of the Galexy?\n")
question2 = input("What was the first Disney animated feature movie that was not based on an already existing story?\n")
question3 = input("What was the coffee shop named in the the TV show 'Friends'?\n")
question4 = input("Who was the actor to first portray James Bond?\n")
question5 = input("On 'The Mandelorian', what is Baby Yoda's real name?\n")

score = 0
if question1 == "Vin Diesel" or question1 == "vin diesel":
    score +=1
if question2 == "The Lion King" or question2 == "the lion king":
    score +=1
if question3 == "Central Perk" or question3 == "central perk":
    score +=1
if question4 == "Sean Connery" or question4 =="sean connery":
    score +=1
if question5 == "Grogu" or question5 == "grogu":
    score +=1

print("Your score is: ", score)

