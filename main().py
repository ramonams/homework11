import datetime
import json
import random

secret = random.randint(1, 30)
attempts = 0


with open("score_list.json", "r") as score_file:
    score_list = json.loads(score_file.read())
    print("top scores:" + str(score_list))
    


for score_dict in score_list:
    print("name" + " " + score_dict["name"],str(score_dict["attempts"]) + ": attempts,date:" + str(score_dict["date"]))

name = input("Insert your name:")

while True:
    guess = int(input("guess the secret number (1-30)"))
    attempts = attempts + 1
    wrong_guesses = attempts - 1

    if guess == secret:
        score_list.append({"name": name, "attempts": attempts, "date": str(datetime.datetime.now()),
                           "wrong guesses": wrong_guesses, "secret number": str(secret)})

        with open("score_list.json", "w") as score_file:
            score_file.write(json.dumps(score_list))

        print("you have guessed. it is number: " + str(secret))
        print("attempts needed:" + str(attempts))
        print("wrong guesses:" + str(wrong_guesses))
        break

    elif guess > secret:
        print("Your guess is not correct. Try smaller.")
    elif guess < secret:
        print("Your guess is not correct. Try bigger.")
