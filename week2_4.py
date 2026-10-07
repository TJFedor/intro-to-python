# Functions
# Fucntions are essentially a mini-program whithin a program.
#? Functions can be defined using def keyword.
import time

def npc_greeting():
    print("welcome to the world of Python!")
    print("what is your name, adventurer?")
    player_name = input()
    print(f"hello, {player_name}! Nice to meet you.")

npc_greeting()

favorite_food = input("what food do you want to eat")

def chef_make_food(food):
    print(f"Chef is making {food}! It will be ready soon!")
    time.sleep(2) 
    print(f"Chef has made {food}! Enjoy your meal!")

chef_make_food(favorite_food)