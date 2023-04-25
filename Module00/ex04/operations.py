import sys

args = sys.argv

if len(args) < 3:
    print("Usage: python operations.py <n1> <n2>", file=sys.stderr)
    exit(1)

if len(args) > 4:
    print("Too many arguments", file=sys.stderr)

one = 0
two = 0

try:
	one = int(args[1])
except:
	print("First argument is not an integer", file=sys.stdout)
	exit(1)

try:
	two = int(args[2])
except:
	print("Second argument is not an integer", file=sys.stdout)
	exit(1)

print("Sum:\t\t%d" % (one + two))
print("Diff:\t\t%d" % (one - two))
print("Product:\t%d" % (one * two))

if two == 0:
	print("Could not devide by 0")
	print("Could not do a modulo by 0")
else:
	print("Quiotien:\t%d" % (one / two))
	print("Remainder:\t%d" % (one % two))

