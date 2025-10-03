'''
5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of
     independent if statements that check for certain fruits in your list.
     • Make a list of your three favorite fruits and call it favorite_fruits.
     • Write five if statements. Each should check whether a certain kind of fruit
       is in your list. If the fruit is in your list, the if block should print a statement,
       such as You really like bananas!
'''

favorite_fruits = ['strawberry', 'mango', 'pineapple']

print(f"My list of favorite fruits is: {favorite_fruits}")
print("-" * 30)
print("Checking for different fruits:")

if 'strawberry' in favorite_fruits:
    print("I checked for strawberry: You really like strawberries!")

if 'mango' in favorite_fruits:
    print("I checked for mango: You really like mangos!")

if 'pineapple' in favorite_fruits:
    print("I checked for pineapple: You really like pineapples!")

if 'banana' in favorite_fruits:
    print("I checked for banana: You really like bananas!")

if 'kiwi' in favorite_fruits:
    print("I checked for kiwi: You really like kiwis!")

print("-" * 30)
print("Check complete. Only the messages for the fruits in the list were printed.")