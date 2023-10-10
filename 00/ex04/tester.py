import subprocess

def run_test(command):
	result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	print(result.stdout.decode('utf-8'))
	if result.stderr:
		print(result.stderr.decode('utf-8'))

if __name__ == '__main__':
	print("python whatis.py 14")
	run_test(['python3', 'whatis.py', '14'])
	print("python whatis.py -5")
	run_test(['python3', 'whatis.py', '-5'])
	print("python whatis.py")
	run_test(['python3', 'whatis.py'])
	print("python whatis.py 0")
	run_test(['python3', 'whatis.py', '0'])
	print("python whatis.py Hi!")
	run_test(['python3', 'whatis.py', 'Hi!'])
	print("python whatis.py 13 5")
	run_test(['python3', 'whatis.py', '13', '5'])