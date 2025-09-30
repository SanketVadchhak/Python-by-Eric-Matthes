'''
4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these
     pizza names in a list, and then use a for loop to print the name of each pizza.
    • Modify your for loop to print a sentence using the name of the pizza,
      instead of printing just the name of the pizza. For each pizza, you should
      have one line of output containing a simple statement like I like pep-
      peroni pizza.
'''

pizzas = ['pepperoni', 'margherita', 'supreme']

for pizza in pizzas:
    print(f"I like {pizza} pizza.")

print("I really love pizza!")

'''
4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1 (page 56).
      Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the
      following:
      • Add a new pizza to the original list.
      • Add a different pizza to the list friend_pizzas.
      • Prove that you have two separate lists. Print the message My favorite piz-
        zas are:, and then use a for loop to print the first list. Print the message My
        friend’s favorite pizzas are:, and then use a for loop to print the second list.
        Make sure each new pizza is stored in the appropriate list.
'''
print()
friend_pizzas = pizzas[:]
pizzas.append("lava")
friend_pizzas.append("tomato")
print("My favorite pizzas are:", end = " ")
for pizza in pizzas:
    print(pizza, end = " ")
print()
print("My friend’s favorite pizzas are:", end = " ")
for friend_pizza in friend_pizzas:
    print(friend_pizza, end = " ")