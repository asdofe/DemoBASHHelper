import time
import sys

def delayed_print(words):
    word_delay = 0.1
    for l in words:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(word_delay)

input_script = input('input script name: ')
if input_script == '':
    input_script = 'testcase.sh'
    print('using default testcase.sh')
def execute_bash_cmd(cmd):
    log_on = True
    bash_cmd = cmd
    import subprocess
    process = subprocess.Popen(bash_cmd.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    if log_on:
        print(output.decode('UTF-8'))

with open(input_script, 'r', encoding='UTF-8') as file:
    for line in file:

        delayed_print(line)
        if '#' not in line:
            execute_bash_cmd(line)


