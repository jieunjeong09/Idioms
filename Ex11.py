# exiting with "correct" status and message m
def finish(m):
  print(n, m)
  exit()
# reading input and checking for correct form
n = input("write integer to test: ")
import re
if re.match("^ *[0-9]*$",n) == None or n == "1":
  exit("it should be integer larger than 1")
n = int(n)
if (n < 2):   finish("is not an integer above 1")
# n = 6000000000000001 # remove commenting if you want to test
# handle cases when n < 49 and when n is divisible by of 2,3,5
if (n < 2*2): finish("is prime")
if (not(n%2)): finish("is divisible by 2")
if (not(n%3)): finish("is divisible by 3")
if (n < 5*5): finish("is prime")
if (not(n%5)): finish("is divisible by 5")
# we will generate possible divisors not divisible by 2,3 or 5
incr = (2,6,4,2,4,2,4,6)
d = 7
incr_i = 2
while 1:
  # if (d < 100): print(d) # remove commenting if you want to test
  if (d*d > n): finish("is prime")
  if not n%d: finish("is divisible by "+str(d)+" ratio is "+str(n//d))
  d = d+incr[incr_i]
  incr_i += 1
  if incr_i == 8: incr_i = 0
