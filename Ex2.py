# Ask the user for an integer. Depending on whether the number is even or odd,
# If the number is a multiple of 4, print out a different message.
# If the user types two integers: call the first n, the second c.
# Print if n is a multiple of c.
def odd_even_4(n):
  if not(n % 4):
    return " is divisible by 4"
  if not(n % 2):
    return " is even but not divisible by 4"
  return " is odd"
def multiple(n,c):
  suffix = " a multiple of "+str(c)
  if n % c:
    return " is "+"not"+suffix
  return " is"+suffix

L = input("type one or two positive integers: ").split()
n = int(L[0])
if (len(L) == 1):
  print(L[0]+odd_even_4(n))
else:
  print(L[0]+multiple(n,int(L[1])))
