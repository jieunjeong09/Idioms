# Take a list, e.g.  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#  Prints out all the elements of the list that are less than 5.

# Extras:

# 1. Instead of printing the elements one by one, make a new list that has all
#    the elements less than 5 from this list in it and print out this new list.
#    Write this in one line of Python.
# 2. Ask the user for a number,return a list that contains only elements from
#    the original list a that are smaller than that number given by the user.
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print(a)
print(list(filter(lambda x: x < 5, a)))
lim = int(input("type upper limit (exclusive): "))
print(list(filter(lambda x: x < lim, a)))
