# CREATING A LIST
#list()
my_list = [1, 2, 3]
print(f"Created list: {my_list}")


# READING A LIST
#Read first element
first_element = my_list[0]
print(f"First element: {first_element}")
#Read last element
last_element = my_list[-1]
print(f"Last element: {last_element}")
#Read at a specific index
indexed_element = my_list[2]
print(f"Element at index 2: {indexed_element}")
#slicing
sliced_list = my_list[1:4]
print(f"sliced list: {sliced_list}")
#count
count_3 = my_list.count(3)
print(f"3 appears {count_3} times")

# UPDATING A LIST
#changing list elements using index
my_list[1] = 99
print("After updating index 1 to 99:", my_list)
#adding an element at the end of a list
my_list.append(3)
print(f"appended list: {my_list}")
#adding an element at at a specific index of a list
my_list.insert(1, 10)
print(f"insert element at index 1: {my_list}")
# adding elements using extend
my_list.extend([4, 5])
print(f"extended list: {my_list}")
# adding using +
new_list = my_list + [6,7]
print(f"new list using +: {new_list}")
#sort
sorted_list = my_list.sort()
print(f"sorted list: {sorted_list}")
#reverse
reversed_list = my_list.reverse()
print(f"reversed list: {reversed_list}")
# using *
repeated_list = [1] * 3
print(f"repeated list: {repeated_list}")




# DELETING
# Remove last item
my_list.pop()  
# pop with index 
my_list.pop(1) 
# remove     
my_list.remove(99)
#del
del my_list[2]      
print("After deletions:", my_list)
#clear
my_list.clear()
print("After clearing the list:", my_list)