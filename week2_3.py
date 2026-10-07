#variable naming
x, y, z = "orange", "banana", "apple"

print(x)
print(y)
print(z)

# Input Output... think of text advanture time.
npc_greeting = "welcome to the world of python"
print(npc_greeting)
npc_question = input("What is your name, adventurer?")
print(f"hello, {npc_question}! Nice to meet you")
gold_coins = input("How many gold coins do you have? ")

gold_coins = float(gold_coins)

npc_troll_collection = (f"The troll collects 1 gold coin from you. You now have {gold_coins - 1} gold coins left")
print(npc_troll_collection)