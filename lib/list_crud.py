# creating an empty list
def create_an_empty_list():    
    return [] #empty list

def create_a_list():
    return [1,2,3,4] #a list with 4 elements

#adding an element at the end of a list 
def add_element_to_end_of_list(l, element):
    l.append(element)
    return l

#adding an element at the start of a list
def add_element_to_start_of_list(l, element):
    l.insert(0, element)
    return l

#removing an element at the end of a list
def remove_element_from_end_of_list(l):
    l.pop()
    return l

#removing an element at the start of a list
def remove_element_from_start_of_list(l):
    del l[0]
    return l

#retrieving first element from a list
def retrieve_first_element_from_list(l):
    return l[0]

#retrieving element at an index
def retrieve_element_from_index(l, index):
    return l[index]

#retrieving last element in a list
def retrieve_last_element_from_list(l):
    return l[-1]
