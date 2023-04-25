import sys

args = sys.argv

if len(args) == 1:
	exit()

if len(args) > 2:
	print("AssertionError: more than one argument is provided", file=sys.stderr)
	exit(1)

nb = args[1]

if not nb.isdigit():
	print("AssertionError: argument is not an integer", file=sys.stderr)
	exit(1)

nb = int(nb)

if nb == 0:
	print("I'm Zero.")
elif nb % 2 == 0:
	print("I'm Even.")
else:
	print("I'm Odd.")
