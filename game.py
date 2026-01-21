import random
secret = random.randint(1, 100)

while True:
    guess = int(input("Guess a number between 1 and 100: "))


    if guess > secret:
        print("wala as7bi b3dti")

    elif guess < secret:
        print("ziyd chwiya a bro")

    else:
        print("mbrok 3lik Bro🎉")
        break



