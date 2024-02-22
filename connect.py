import argparse, os

parser = argparse.ArgumentParser()

parser.add_argument('--install', '-i',
                    required = False,
                    help = "Instala todos los requerimientos necesarios.")

parser.add_argument('--help', '-h',
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
  os.system("apt-get update && sudo apt-get install git -y && sudo apt-get install python3 && sudo apt-get install python3-pip && pip3 install argparse && sudo apt install -y tor torbrowser-launcher && sudo apt-get install wget gpg && wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg && sudo sh -c 'echo \"deb [arch=amd64,arm64,armhf signed-by=/etc/apt/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main\" > /etc/apt/sources.list.d/vscode.list' && rm -f packages.microsoft.gpg && sudo apt install apt-transport-https && sudo apt update && sudo apt install code")
  
elif args.port:
  os.system(f'python -m SimpleHTTPServer {args.port}')

elif args.help:
  print('Hello')

else:
  print('\n[*] Error: Revisa si has añadido todos los argumentos necesarios.\n')
