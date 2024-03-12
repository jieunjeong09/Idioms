# for two lists, return the list of common elements without duplicates
# use list comprehension

# generation of list examples with possible duplicates
import random
a = random.choices(range(90),k=30) # random.sample makes no duplicates
print("a",a)
print("sorted a", sorted(a)) # for easy visual check
b = random.choices(range(90),k=30)
print("sorted b", sorted(b)) # for easy visual check
# pick elements of a sequence/list if the occur in a for the first time,
# hence w/o duplicates, and in b, hence common
c = [a[i] for i in range(len(a)) if a[i] in b and not a[i] in a[0:i-1]]
print("common", c, "order as in a")
