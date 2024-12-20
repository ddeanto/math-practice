from random import randint, random, choice


def question():
	while True:
		r1 = randint(2, 15)
		r2 = randint(5, 15)
		if r1 == 10 or r2 == 10:
			continue

		if random() < 0.5:
			r1, r2 = r2, r1
		
		while True:
			answer = input(f"what's {r1} + {r2}: ")
			if int(answer) == int(r1 + r2):
				print("correct\n")
				return
			else:
				print("incorrect. try again.")
			

for n in range(20):
	question()
