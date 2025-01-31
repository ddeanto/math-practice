from random import randint, random, choice
from tokenize import Funny


def question():
	while True:
		add_or_subtract = "add" if randint(0, 1) else "subtract"
		r1 = randint(1, 20)
		r2 = randint(1, 9)
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
* * * 
* * *
* * *
* * *
* * *
"""


