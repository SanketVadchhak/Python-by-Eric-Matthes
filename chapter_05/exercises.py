'''
5-1. Conditional Tests: Write a series of conditional tests. Print a statement
     describing each test and your prediction for the results of each test. Your code
     should look something like this:
     car = 'subaru'
     print("Is car == 'subaru'? I predict True.")
     print(car == 'subaru')
     print("\nIs car == 'audi'? I predict False.")
     print(car == 'audi')
     • Look closely at your results, and make sure you understand why each line
       evaluates to True or False.
     • Create at least 10 tests. Have at least 5 tests evaluate to True and another
       5 tests evaluate to False.
'''
cars = ['audi', 'bmw', 'subaru', 'toyota', "bugati"]

print("Is car == 'subaru'? I predict True.")
print("subaru" in cars)
print("\nIs car == 'audi'? I predict True.")
print("audi" in cars)
print("\nIs car == 'honda'? I predict False.")
print("honda" in cars)
print("\nIs car == 'suzuki'? I predict False.")
print("suzuki" in cars)
print("\nIs car == 'bmw'? I predict True.")
print("bmw" in cars)
print("\nIs car == 'kia'? I predict False.")
print("kia" in cars)
print("\nIs car == 'bugati'? I predict True.")
print("bugati" in cars)
print("\nIs car == 'ford'? I predict False.")
print("ford" in cars)
print("\nIs car == 'volvo'? I predict False.")
print("volvo" in cars)
print("\nIs car == 'toyota'? I predict True.")
print("toyota" in cars)