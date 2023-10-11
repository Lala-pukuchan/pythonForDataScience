import subprocess

def run_test(command):
	result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	print(result.stdout.decode('utf-8'))
	if result.stderr:
		print(result.stderr.decode('utf-8'))

if __name__ == '__main__':
	print("python building.py 'Python 3.0, released in 2008, was a major revision that is not completely backward-compatible with earlier versions. Python 2 was discontinued with version 2.7.18 in 2020.'")
	run_test(['python3', 'building.py', 'Python 3.0, released in 2008, was a major revision that is not completely backward-compatible with earlier versions. Python 2 was discontinued with version 2.7.18 in 2020.'])
