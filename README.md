# Idioms
Basics like input, output, list comprehension and other Python idioms

Ex1.py: interactive input and output, subprocess module

Ex2.py: method split() of string type

Ex3.py: filter() for making a sublist of list entries satisfying a condition, the sublist so created is not of list type, conversion needed (one of several ways to create a sublist).

Ex4.py: list comprehension to generate the list of all proper divisors of a positive integer input.  The output is the list of all proper divisors preceded by its length.  A trick to avoid divisors above the square root of the input, loops are replaced with filter() and list compehension.

Ex7.py For the input list of integers, make a list of its even elements.
Solution can equivalently use filter() or list comprehension with if. 

Ex10.py For two lists, output the list of common elements without duplicates.
I used list comprehension with if and in, preserving the order of 1st occurrences in the 1st list.
One could also iterate list appending, appending is somewhat slow, but I did not test if list comprehension is faster, comprehension allows to write the solution in one line.
Without preserving the order, one could simplify using set().

Ex11.py For input positive integer, return the smallest proper divisor or the message that it is prime.  Using re (regular expression) to recognize incorrect input and notify the user why is it wrong.
