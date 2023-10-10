import sys

def whatis(object: any):
	if object % 2 == 0:
		print("I'm Even.\n")
	else:
		print("I'm Odd.\n")

try:
	if len(sys.argv) == 1:
		print("")
		sys.exit(1)
	if len(sys.argv) > 2:
		raise AssertionError("more than one argument is provided\n")

	try:
		number = int(sys.argv[1])
		whatis(number)
	except ValueError:
		raise AssertionError("argument is not an integer.\n")

except AssertionError as error:
	print(AssertionError.__name__ + ":", error)
