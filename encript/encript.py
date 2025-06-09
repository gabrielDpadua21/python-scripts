import subprocess

file_name = 'passlist.txt'

with open(file_name, 'r') as file:
    for line in file:
        if line != '':
          line = line.replace('\n', '').replace('\r\n', '').strip()
          command = f"echo {line} | md5sum >> passencript.txt"
          result = subprocess.run(command, shell=True, text=True, capture_output=True)

          if result.returncode == 0:
            print("Saida")
            print(result.stdout)
          else:
              print("Error")
              print(result.stderr)

