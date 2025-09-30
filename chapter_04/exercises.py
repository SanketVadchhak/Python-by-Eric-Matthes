'''
4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive.
'''
print()
for value in range(1, 21):
    print(value)
    
'''
4-4. One Million: Make a list of the numbers from one to one million, and then
     use a for loop to print the numbers. (If the output is taking too long, stop it by
     pressing CTRL-C or by closing the output window.)
'''
print()
numbers = []
for value in range(1, 1000001):
    numbers.append(value)
    print(value)
    
'''
4-5. Summing a Million: Make a list of the numbers from one to one million, and
     then use min() and max() to make sure your list actually starts at one and ends
     at one million. Also, use the sum() function to see how quickly Python can add
     a million numbers.
'''
print()
print(min(numbers))
print(max(numbers))
print(sum(numbers))

'''
4-6. Odd Numbers: Use the third argument of the range() function to make a list
     of the odd numbers from 1 to 20. Use a for loop to print each number.
'''
print()
odds = []
for value in range(1, 21, 2):
    odds.append(value)
    print(value)
    
'''
4-7. Threes: Make a list of the multiples of 3, from 3 to 30. Use a for loop to
     print the numbers in your list.
'''
print()
threes = []
for value in range(3, 31, 3):
    threes.append(value)
    print(value)
    
'''
4-8. Cubes: A number raised to the third power is called a cube. For example,
     the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that
     is, the cube of each integer from 1 through 10), and use a for loop to print out
     the value of each cube.
'''
print()
for value in range(1, 11):
    cube = value ** 3
    print(cube)
    
'''
4-9. Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes.
'''
print()
cubes = [number**3 for number in range(1, 11)]
print(cubes)

'''
4-10. Slices: Using one of the programs you wrote in this chapter, add several
      lines to the end of the program that do the following:
      • Print the message The first three items in the list are:. Then use a slice to
        print the first three items from that program’s list.
      • Print the message Three items from the middle of the list are:. Then use a
        slice to print three items from the middle of the list.
      • Print the message The last three items in the list are:. Then use a slice to
        print the last three items in the list.
'''
print()
print("The first three items in the list are:", threes[:3])
print("Three items from the middle of the list are:", threes[3:6])
print("The last three items in the list are:", threes[-3:])

'''
4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five
      simple foods, and store them in a tuple.
      • Use a for loop to print each food the restaurant offers.
      • Try to modify one of the items, and make sure that Python rejects the change.
      • The restaurant changes its menu, replacing two of the items with different
        foods. Add a line that rewrites the tuple, and then use a for loop to print
        each of the items on the revised menu.
'''
menu = ("Roti", "Thepla", "Bhakhri", "Dahi", "Dahi Tikhari")
for item in menu:
  print(item)
print()
menu = ("Khaman", "Dhokla", "Patra", "Fafda", "Jalebi")
for item in menu:
    print(item)