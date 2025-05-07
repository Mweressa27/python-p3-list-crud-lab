# CREATING A LIST
my_list = [1, 2, 3]
print(f"Created list: {my_list}")

# Append
my_list.append(3)
print(f"Appended 3 to list: {my_list}")

# Insert at index
my_list.insert(1, 10)
print(f"Inserted 10 at index 1: {my_list}")

# Extend with another list
my_list.extend([4, 5])
print(f"Extended list with [4, 5]: {my_list}")

# Create a new list using +
new_list = my_list + [6, 7]
print(f"New list using + [6, 7]: {new_list}")


# READING A LIST
print(f"First element: {my_list[0]}")
print(f"Last element: {my_list[-1]}")
print(f"Element at index 2: {my_list[2]}")
print(f"Sliced list [1:4]: {my_list[1:4]}")
print(f"Count of 3 in list: {my_list.count(3)}")


# UPDATING A LIST
# Modify element
my_list[1] = 99
print(f"Updated index 1 to 99: {my_list}")

# Sort 
my_list.sort()
print(f"Sorted list: {my_list}")

# Reverse (in-place)
my_list.reverse()
print(f"Reversed list: {my_list}")

# Repeat list elements
repeated_list = [1] * 3
print(f"Repeated [1] three times: {repeated_list}")


# DELETING ELEMENTS
# Remove last item
my_list.pop()

# Remove item at index 1
my_list.pop(1)

# Remove first occurrence of 99
my_list.remove(99)

# Delete item at index 2
del my_list[2]

print(f"List after deletions: {my_list}")

# Clear all elements
my_list.clear()
print(f"List after clearing: {my_list}")
