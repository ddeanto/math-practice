from random import randint, random, choice
from tokenize import Funny


def question():
	while True:
		add_or_subtract = "add" if randint(0, 1) else "subtract"
		r1 = randint(5, 30)
		r2 = randint(3, 30)
		# if r1 == 10 or r2 == 10:
		# 	continue

		# if random() < 0.5:
		# 	r1, r2 = r2, r1

		if r2 < r1:
			r2, r1 = r1, r2

		while True:
			if add_or_subtract == "add":
				answer = input(f"what's {r2} + {r1}: ")
				if int(answer) == int(r2 + r1):
					print("correct\n")
					return
				else:
					print("incorrect. try again.")
			else:
				answer = input(f"what's {r2} - {r1}: ")
				if int(answer) == int(r2 - r1):
					print("correct\n")
					return
				else:
					print("incorrect. try again.")
			
for n in range(10):
	question()


"""
15

5*3 = 3*5

100*4
40*4 + 60*4

and A + B = M

M*N

COMMUNITATIVE PROPERTY
ab = ba

DISTRIBUTIVE PROPERTY
(a+b)c = ac + bc

CORALLARY:
(a + b)(c + d)
we know (c + d) is a number so we can use DISTRIBUTIVE PROPERTY
(a + b)(c + d) = a(c + d) + b(c + d) = (c + d)a + (c + d)b =
ac + ad + bc + bd

AXIOM:



12 * 12 = 144
13 * 11 = 143
(12+1)(12-1)
ac      ad    bc   bd
12*12 + -12 + 12 + -1
144 - 1

* * * 
* * *

* * * 
* * * 
* * *
* * *
* * * 
* * *
* * *

-
* * *
* * *


ac + ad + bc + bd
(n+1)(n-1) = n*n - 1
(n+2)(n-2) = n*n - 4
(n+3)(n-3) = n*n - 9

15*15 = 225
18*12 = 216


"""


