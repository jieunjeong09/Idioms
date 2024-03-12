# List example:
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# Write one Python line of Python that takes list a and makes a new list that
# has only the even elements of this list in it.
b = list(filter(lambda x: 1-x%2, a)) # solution with filter
print(b)
b = [n for n in a if 1-n%2]          # solution with "comprehension"
print(b)


