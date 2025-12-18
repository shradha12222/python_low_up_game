from art import logo,vs
from random import choice
from data import data
from os import system
def format_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, {description}, from {country}"
def check_answer(guess,a_followers,b_followers):
    if a_followers > b_followers and guess == "a":
        return guess=="a"
    else:
        return guess=="b"
print(logo)
score = 0
account_b = choice(data)
game_continue = True
while game_continue:
    account_a=account_b
    account_b=choice(data)
    if account_a==account_b:
        account_b=choice(data)
    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Compare B: {format_data(account_b)}")
    guess=input("who has more folower? [A or B]").lower()
    a_followers=account_a["follower_count"]
    b_followers=account_b["follower_count"]
    is_correct=check_answer(guess,a_followers,b_followers)
    system('cls')

    if is_correct:
        score +=1
        print(f"You are correct! and your scoure is {score} ")
    else:
        print(f"You are not correct and your final scoure is{score}")
        game_continue = False
