import subprocess

command = 'ls -l'

result = subprocess.run(command, shell=True, text=True, capture_output=True)

if result.returncode == 0:
    print("Saida")
    print(result.stdout)
else:
    print("Erro ao rodar comando")
    print(result.stderr)

