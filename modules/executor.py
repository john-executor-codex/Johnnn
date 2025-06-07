import subprocess

def executar_codigo(codigo, arquivo='codigo_temp.py'):
    with open(arquivo, 'w') as f:
        f.write(codigo)

    processo = subprocess.run(['python', arquivo], capture_output=True, text=True)
    return processo.stdout, processo.stderr
