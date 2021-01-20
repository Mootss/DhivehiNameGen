# Author : Moots (github.com/Mootss)
# This is a script to generate a random dhivehi given-name.
# based of an article by ThatMaldivesBlog,
# read it for yourself here;
# https://thatmaldivesblog.wordpress.com/2020/07/25/whats-in-a-maldivian-name-the-given-name/

from random import choice

commons = ["z", "sh", "j", "l", "r", "n", "y", "f", "m"] # commonly preferred consonants in dhivehi names
vowels = ["a", "e", "i", "o", "u", "ai", "au"]
#consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z"]

# list of common name structures
structures = ["_A_EE_", "_AA_I_", "_I_AA_", "_U_AI_", "_A__AAN", "_A__EEN"]
variations = ["_A__AAN", "A__AAN", "_I__AAN", "I__AAN", "_U__AAN"] # other variations for _A__AAN/names ending with -aan 

# around ~500 possible names

l=[False,True,False]; placeVowel = "_"
def name():
	# name generator function
	structPick = choice(structures) # choose a random name structure from the structures list

	for placeVowel in structPick:
		# replace "_" with a random vowel for each "_" in the name structure
		v1, v2, v3 = choice(commons), choice(commons), choice(commons)

		if structPick == "_A__AAN":
			structPick = choice(variations) # pick a diff struct for this
			# replace underscores with {}, format that with the values, lowercase it, capitalize first letter
			name = structPick.replace("_", "{}").format(v1, v2, v3).lower().capitalize() 
			a = choice(l) # make random choice to have "a" at the end or not
			if a == True:
				return name # return without "a"

			elif a == False:
				return name+"a" # return with "a"

		elif structPick != "_A__AAN": # same as above except if name struct is not _A__AAN, default to other structs
			name = structPick.replace("_", "{}").format(v1, v2, v3).lower().capitalize()
			a = choice(l) 
			if a == True:
				return name

			elif a == False:
				return name+"a"

# print(name())

# last updated: 20/01/2021
