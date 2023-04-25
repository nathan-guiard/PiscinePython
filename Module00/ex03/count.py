from typing import List
import sys

def text_analyzer(text):
	"""Counting certain characters in a string"""
	if type(text) == None or type(text) == str:
		text = input("Please provide a string:\n")
	elif type(text) != str:
		print("Argument is not a string")
		return
	
	stats: tuple

if __name__ == '__main__':
	if len(sys.argv) == 2:
		text_analyzer(sys.argv[1])
	elif len(sys.argv) == 1:
		text_analyzer(None)
	else:
		print("Too much arguments", file=sys.stderr)
		exit(1)