#This code is used to check is a sentence is a pangram or not
import string


def pangramCheck():
	input_sentence = set(input("Please type your text here: \t").lower())
	setAlpha = set(string.ascii_lowercase)
	result = list(setAlpha.difference(input_sentence))
	stringed = "".join(result)
	if stringed.isalpha():
		print("Not Pangram")
	else:
		print("Pangram")
		
pangramCheck()