import argparse, os

parser = argparse.ArgumentParser()

parser.add_argument('--port', '-p',
                    required = False,
                    help = "Indicación del puerto en el que levantar el servidor.")

parser.add_argument('--install', '-i',
                    required = False,
                    help = "Indicación del tipo de servidor.")

args = parser.parse_args()

if args.install:
  os.system('sudo apt update && sudo apt-get install python3 -y && sudo apt install python3-pip')
  
elif args.port:
  os.system(f'python -m SimpleHTTPServer {args.port}')

else:
  print('\n[*] Error: Revisa si has añadido todos los argumentos necesarios.\n')
