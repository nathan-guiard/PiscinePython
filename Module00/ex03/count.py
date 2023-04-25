from typing import List
import sys
import string

punctuation_mark = [';', '.', ',', ':']

def text_analyzer(text):
	"""Counting certain characters in a string"""
	if type(text) == None:
		text = input("Please provide a string:\n")
	elif type(text) != str:
		print("Argument is not a string")
		return
	
	upper = 0
	lower = 0
	punc = 0
	spaces = 0

	for c in text:
		if c.isupper():
			upper += 1
		elif c.islower():
			lower += 1
		elif c in string.punctuation:
			punc += 1
		elif c.isspace():
			spaces += 1
		
	print("The text contains" + str(len(text)) + "character(s):")
	print("- " + str(upper) + " upper letter(s)")
	print("- " + str(lower) + " lower letter(s)")
	print("- " + str(punc) + " punctuation mark(s)")
	print("- " + str(spaces) + " space(s)")

if __name__ == '__main__':
	if len(sys.argv) == 2:
		text_analyzer(sys.argv[1])
	elif len(sys.argv) == 1:
		text_analyzer(None)
	else:
		print("Too much arguments", file=sys.stderr)
		exit(1)