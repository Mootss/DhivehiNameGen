# Author : Moots (github.com/Mootss)
# This is a script to generate random dhivehi given-names, the script used here is based of an article by ThatMaldivesBlog
# you can read it for yourself here;
# source : https://thatmaldivesblog.wordpress.com/2020/07/25/whats-in-a-maldivian-name-the-given-name/
# they got some other interesting blogs that you might like so go check em out

from random import choice

commons = ["z", "sh", "j", "l", "r", "n", "y", "f"] # commonly preferred consonants in dhivehi names
vowels = ["a", "e", "i", "o", "u", "ai", "au"]
#consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z"]

# list of common name structures
structures = ["_A_EE_", "_AA_I_", "_I_AA_", "_U_AI_", "_A__AAN", "_A__EEN"]

# total 336 possible names

def gen():
	# name generator function
	structPick = choice(structures) # choose a random name structure from the structures list
	placeVowel = "_" # place vowels for where "_" is present

	l = [True,False]; a = choice(l)
	if a == True:
		for placeVowel in structPick:
			# replace "_" with a random vowel for each "_" in the name structure
			v1, v2, v3 = choice(commons), choice(commons), choice(commons)
			name = structPick.replace("_", "{}")
			name = name.format(v1, v2, v3).lower().capitalize()

			return name+"a" # with "a" at the end

	elif a == False:		
		for placeVowel in structPick:
			# replace "_" with a random vowel for each "_" in the name structure
			v1, v2, v3 = choice(commons), choice(commons), choice(commons)
			name = structPick.replace("_", "{}")
			name = name.format(v1, v2, v3).lower().capitalize()

			return name # without "a"

# last updated: 19/01/2021
