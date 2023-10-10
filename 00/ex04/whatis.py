import sys

def whatis(object: any):
	if object % 2 == 0:
		print("I'm Even.\n")
	else:
		print("I'm Odd.\n")

if __name__ == "__main__":
	if len(sys.argv) == 1:
		print("")
		sys.exit(1)
	if len(sys.argv) > 2:
		print("AssertionError: more than one argument is provided\n")
		sys.exit(1)

	try:
		number = int(sys.argv[1])
		whatis(number)
	except ValueError:
		print("AssertionError: argument is not an integer.\n")
		sys.exit(1)
