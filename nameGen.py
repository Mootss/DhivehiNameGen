import random

common = ["z", "sh", "j", "l", "r", "n", "y", "f"]
vowels = ["a", "e", "i", "o", "u"]
consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z"]

types = ["_A_EE_(A)", "sdfghj"] 

opt = 0

def gen():

	v1 = random.choice(consonants)
	v2 = random.choice(consonants)
	v3 = random.choice(consonants)

	l = [1, 2]

	opt = random.choice(l)

	if opt == 1:
		name =  f'{v1}a{v2}ee{v3}'
		return name

	elif opt == 2:
		name = "{}a{}ee{}".format(v1, v2, v3)
		return name

		if name.endswith("y"):
		 	name = name.replace("y", "")
		 	return name



print(gen())

