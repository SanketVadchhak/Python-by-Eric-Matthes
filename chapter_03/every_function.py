# 3-10. Every Function

# Create an initial list of languages.
languages = ["mandarin", "spanish", "english", "hindi", "arabic"]
print(f"Original list: {languages}")

# --- Using len() to find the length of the list ---
print(f"\nThere are {len(languages)} languages in the list.")

# --- Accessing items using indexing ---
print(f"The first language is {languages[0].title()}.")
print(f"The last language is {languages[-1].title()}.")

# --- Modifying an item in the list ---
print(f"\nChanging '{languages[3]}' to 'bengali'.")
languages[3] = "bengali"
print(f"List after modification: {languages}")

# --- Adding items using append() and insert() ---
languages.append("portuguese")
print(f"\nAfter appending 'portuguese': {languages}")
languages.insert(0, "russian")
print(f"After inserting 'russian' at the beginning: {languages}")

# --- Removing items using del, pop(), and remove() ---
del languages[1]
print(f"\nAfter deleting the item at index 1: {languages}")

popped_language = languages.pop()
print(f"We 'popped' the language: {popped_language.title()}")
print(f"List after pop(): {languages}")

languages.remove("english")
print(f"\nAfter removing 'english': {languages}")

# --- Organizing the list with sorted(), reverse(), and sort() ---
print("\n--- Organizing the List ---")
print(f"Original order: {languages}")

# Temporarily sorting with sorted()
print(f"Temporarily sorted with sorted(): {sorted(languages)}")
print(f"Original order is still the same: {languages}")

# Permanently reversing with reverse()
languages.reverse()
print(f"\nPermanently reversed with reverse(): {languages}")

# Permanently sorting with sort()
languages.sort()
print(f"Permanently sorted with sort(): {languages}")

languages.sort(reverse=True)
print(f"Permanently sorted in reverse with sort(reverse=True): {languages}")

# --- Final length of the list ---
print(f"\nThe final length of the list is: {len(languages)}")