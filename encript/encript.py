import subprocess

file_name = 'passlist.txt'


def clean_file():
    command = 'echo > passencript.txt'
    result = subprocess.run(command, shell=True, text=True, capture_output=True)

    if result.returncode == 0:
        print("Clean file passencript.txt")
        print(result.stdout)
    else:
        print("Error to clean file")
        print(result.stderr)

with open(file_name, 'r') as file:
    clean_file()
    for line in file:
        if line != '':
          line = line.replace('\n', '').replace('\r\n', '').strip()
          command = f"echo -n {line} | md5sum >> passencript.txt"
          result = subprocess.run(command, shell=True, text=True, capture_output=True)

          if result.returncode == 0:
            print("Add line on file")
            print(result.stdout)
          else:
              print("Error")
              print(result.stderr)
