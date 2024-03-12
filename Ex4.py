# ask the user for a number and then print the list of all its proper divisors
n = int(input("give a positive number "))
s = int(n ** 0.5)
r0 = list(filter(lambda x: n%x == 0, range(2,s)))
r1 = list(filter(lambda x: n%x == 0, [s,s+1]))
k = len(r0)
l = len(r1)
r2 = [n//r0[k-i-1] for i in range(k)] # list comprehension
print(k*2+l, r0+r1+r2)

