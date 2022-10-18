
print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0


answer = input("What country has the highest life expectancy?")
if answer.lower() == "hong kong":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What company was originally called Cadabra?")
if answer.lower() == "amazon":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("The logo for luxury car maker Porsche features which animal? ")
if answer.lower() == "horse":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What is the capital of Argentina? ")
if answer.lower() == "buenos aires":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")
