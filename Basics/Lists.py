print("\nWorking with Lists")

this_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print("\nComplete list: ", this_list)
print("Element 2, 3, 4: ", this_list[2:5])
print("Element 0, 1, 2: ", this_list[:2])
print("Last element: ", this_list[-1])

# Looping
for fruit in this_list:
    print(fruit)

# Searching a list
if "apple" in this_list:
    print("An 'apple' was found")

# Editing to a list
this_list[1] = "peach"
this_list.append("pear")
this_list.insert(5, "raspberry")
this_list.remove("apple")
this_list.pop(3)
print("Here's the edited list: ", this_list)

# Putting two lists together
second_list = ["broccoli", "garlic", "tomatoes"]
third_list = this_list + second_list
print("Mega list: ", third_list)

# Clearing
this_list.clear()
print("The final list: ", this_list)
