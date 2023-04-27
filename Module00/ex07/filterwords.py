import sys
import string

if __name__ == '__main__':
	if len(sys.argv) != 3:
		print('Error: Argument number must be 2', file=sys.stderr)
		exit(1)
	
	try:
		cap = int(sys.argv[2])
	except ValueError:
		print('Error: Second argument must be an integer')
		exit(1)
	
	print(list(filter(lambda x: len(x.translate(str.maketrans('', '', string.punctuation))) > cap ,sys.argv[1].split())))