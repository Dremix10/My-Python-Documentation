print("***Read important theory comments at beginning of code***\n")
# data structure theory: mutability and order
# an object is mutable if it can be modified after it is created (strings are immutable)
# an object is ordered if the order of its elements matters and this is used to be able to access its elements based on indexing/order (strings are ordered)

# lists follow
print("-> Lists:\n\n")

# lists can store a lot of values in one variable (even of different data types)

# lists are mutable and ordered objects

# list to be used in following examples
data = ['loizos',True,64.4,'GET rekt',360]
print("Sample list:", data)

# positive indexing starts from the first element at index 0
print("Element at index 2 is:", data[2])
print("Element at index 0 is:", data[0])

# negative indexing starts from the last element at index = -1
print("Element at index -1 is:", data[-1])
print("Element at index -5 is:", data[-5])

# slicing list[l:r] is a substring indexing which returns a list of all elements from index 'l' to 'r-1' (lower bound is inclusive, but upper is not)
print("\nElements sliced [1:3]:", data[1:3])
print("Elements sliced [:2]", data[:2])
print("Elements sliced [-2:]", data[-2:])

# 'in' and 'not in' operators are used to identify whether an object is included in another object (the list in this case)
print("\nIs element 'True' in?", True in data)
print("Is element 'False' in?", False in data)
print("Is element '64.40' in?", 64.40 in data)
print("Is element '\"george\"' not in?", "george" not in data)

# when mutable objects are copied both variables reference the same object
data_copy = data
print("\nThe 2 lists after copying are:")
print(data)
print(data_copy)

# modifying the copy of the list
data_copy[2] = 3
print("\nAfter modifying the list copy both lists change:")
print(data)
print(data_copy)

# useful functions follow (also used in lists)
sample_list = [2,132,5,-2,68]
print("\n\nThe sample list to be used in the functions that follow is:", sample_list)

# len() function was mentioned at fundamentals
print("\nThe length of the list is:", len(sample_list))

# max() function returns the greatest element of the input
print("\nThe greatest element of the list is:", max(sample_list))
# !!! be careful when using functions that compare elements -> mix of data types will produce an error

# min() function returns the smallest element of the input
print("\nThe smallest element of the list is:", min(sample_list))

# sorted() function returns a copy of the input after being sorted
# can also define the optional argument {reverse=True} for descending sorted
print("\nThe list sorted in ascending order is:", sorted(sample_list))
print("The list sorted in descedning order is:", sorted(sample_list,reverse=True))

# useful methods follow (also used in lists)
sample_list = ["George","Milky way","Neutron","Sun"]
print("\n\nThe sample list to be used in the methods that follow is:", sample_list)

# join() method joins the elements of the input list each separated by the string specified
# the return value is a string
print("\nThe list joined together and separated by '-' is:", "-".join(sample_list))
print("The list joined together and separated by '\\n' is:\n" + "\n".join(sample_list))
# !!! be careful as this method will only work if elements of list are all strings

# append() method inserts element inputed at the end of the list
sample_list.append("Star")
print("\nThe list after appending '\"Star\"' is:", sample_list)

# insert() method inserts element inputed at the index specified shifting elements to the right
sample_list.insert(3,True)
print("\nThe list after inserting 'True' at index 3 is:", sample_list)

# remove() method removes element inputed from list
sample_list.remove("Sun")
print("\nThe list after removing '\"Sun\"' is:", sample_list)
# !!! be careful when removing data from lists -> must exist (care CAPS)
# names.remove("sun") will produce an error because of lowercase 's'



