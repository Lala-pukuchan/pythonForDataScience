import subprocess


def run_test(command):
    result = \
        subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(result.stdout.decode('utf-8'))
    if result.stderr:
        print(result.stderr.decode('utf-8'))


if __name__ == '__main__':
    print("python sos.py 'sos'")
    run_test(['python3', 'sos.py', 'sos'])
    print("python sos.py 'so s'")
    run_test(['python3', 'sos.py', 'so s'])
    print("python sos.py 'hello'")
    run_test(['python3', 'sos.py', 'hello'])
    print("python sos.py")
    run_test(['python3', 'sos.py'])
    print("python sos.py, 'sos', 'sos'")
    run_test(['python3', 'sos.py', 'sos', 'sos'])
