import random
myName = input("Hello! What is your name?")
number = random.randint(1,100)
print("Welcome,"+ myName + ",What is your favourite number?")
guess = int(input("number is,"))
if guess <= 25:
    print("enjoy this joke")
    print("Today a man knocked on my door and asked for a small donation toward the local swimming pool. I gave him a glass of water.")
elif guess > 25 and guess <= 50:
    print("enjoy this joke")
    print("I’m reading a book about anti-gravity. It’s impossible to put down.")
elif guess > 50 and guess <= 75:
    print("enjoy this joke")
    print(" The future, the present, and the past walk into a bar. Things got a little tense.")
elif guess > 75 and guess < 100:
    print("Enjoy this joke: Refusing to go to the gym is a form of resistance training.")
else:
     print("Oops! Better luck next time")