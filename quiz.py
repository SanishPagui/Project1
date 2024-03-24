c=0
play=input("Do you want to play the game?\n")

if play.lower() == "yes":
    name = input("Enter your name:")
else:
    quit()

q1 = input("What is the full form of GG\n")
if q1.lower() == "good game":
    print("Correct")
    c+=1
else:
    print("Wrong")


q2 = input("What is the full form of glhf\n")
if q2.lower()=="good luck have fun":
    print("Correct")
    c+=1
else:
    print("Wrong")

q3 = input("What is the full form of gf\n")
if q3.lower()=="good friend" or q3.lower()=="great friend":
    print("Correct")
    c+=1
else:
    print("Wrong")

print(f"{name}, You got {c} answers correct")