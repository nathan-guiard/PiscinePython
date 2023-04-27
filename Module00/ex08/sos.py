import sys
import string

morse = { 'A':'.-', 'B':'-...',
	'C':'-.-.', 'D':'-..', 'E':'.',
	'F':'..-.', 'G':'--.', 'H':'....',
	'I':'..', 'J':'.---', 'K':'-.-',
	'L':'.-..', 'M':'--', 'N':'-.',
	'O':'---', 'P':'.--.', 'Q':'--.-',
	'R':'.-.', 'S':'...', 'T':'-',
	'U':'..-', 'V':'...-', 'W':'.--',
	'X':'-..-', 'Y':'-.--', 'Z':'--..',
	'1':'.----', '2':'..---', '3':'...--',
	'4':'....-', '5':'.....', '6':'-....',
	'7':'--...', '8':'---..', '9':'----.',
	'0':'-----', ' ': '/'
}

if len(sys.argv) == 1:
	print("Needs at least one argument")
	exit(1)

argument = " ".join(sys.argv[1::])

supported = string.ascii_letters + string.digits + " "

for c in argument:
	if c not in supported:
		print("Character `%c' not supported" % c)
		exit(1)

to_morse = list(map(lambda x: morse[x], argument.upper()))

print(" ".join(to_morse))