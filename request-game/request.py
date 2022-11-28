import requests
import random
import os
import time

score = 0
char_and_alias_dict = {}
res_all = requests.get(f"https://the-best-cohort.herokuapp.com/characters/all").json()
for character in res_all:
        char_and_alias_dict.update({character["name"]: character["Alias"]})

def welcome():
    print("welcome to the alias guessing game to win you need to answer correctly three times in a row")
    time.sleep(3)


incorrect_aliases = [
    "3D Waffle",
    "Papa Smurf",
    "Pepper Legs",
    "Pinball Wizard",
    "Accidental Genius",
    "Bugger",
    "Knuckles",
    "Dangle",
    "Disco Potato",
    "Swerve",
    "Peppermint",
    "Onion King",
    "Macho",
    "Snuggy",
    "Foxy",
    "Sofa King",
    "Spanky",
    "Blueberry",
    "Sparky",
    "Slim",
    "Shady",
    "Chunk",
    "Brainiac",
    "Chip",
    "Fly",
    "Guy",
    "Prettyboy",
    "Gummy",
    "Bear",
    "Mister",
    "Yoda",
    "Guapo",
    "Honey",
    "Bunny",
    "Waldorf"
]

def get_random_char():
    char_list = list(char_and_alias_dict.keys())
    rand_num = random.randint(0, len(char_list) - 1)
    rand_char = char_list[rand_num]
    alias = char_and_alias_dict.get(rand_char)
    return rand_char, alias

def ask_question():
    name, alias = get_random_char()
    incorrect_1 = incorrect_aliases[random.randint(0, len(incorrect_aliases) - 1)]
    incorrect_2 = incorrect_aliases[random.randint(0, len(incorrect_aliases) - 1)]
    incorrect_3 = incorrect_aliases[random.randint(0, len(incorrect_aliases) - 1)]
    correct_ans = alias[0]
    answer_list = [incorrect_1, incorrect_2, incorrect_3, correct_ans]
    random.shuffle(answer_list)
    print(f"Which of the folling answer choices are aliases for {name}?\n")
    print(f"\t 1: {answer_list[0]} \n \t 2: {answer_list[1]} \n \t 3: {answer_list[2]}\n \t 4: {answer_list[3]} \n")
    ans = input("please enter your answer below? \n").lower()
    global score
    if answer_list[int(ans) - 1] == correct_ans:
        score += 1
        print(f"you got the question right! your current score is: {score}")
    else:
        if score > 0:
            score = 0
        print(f"you got the question wrong, your current score is: {score}")
    print(correct_ans)
    time.sleep(2)

def clear():
    os.system("clear")

def menu():
    welcome()
    ask_question()
    while score < 3:
        cont = input("would you like to continue? press enter for yes or type 'q' to quit").lower()
        if cont == 'q':
            break
        clear()
        ask_question()
        clear()
    if score >= 3:
        print("congraulations, you beat the game. Thank you for playing")
    else:
        print("wow .. you didnt do very well. Thanks for playing.")

clear()
menu()
