# ReverseConnections

`[*]` Este es un programa en `Python` para establecer `conexiones` con otras máquinas.

`[*]` Está hecho en `Python` y es para `Linux.`

<hr>

`[*]` Soporte:

- Debian
- Kali Linux (Debian)
- Parrot OS (Debian)
- Windows (En desarrollo, próxima versión)

<hr>

## _¡DESCARGO DE RESPONSABILIDAD!_

_`[*]` No me responsabilizo del `daño` que pueda causar esta herramienta haciendo un `mal uso` de ella._

<hr>

## _VERSIÓN:_

_`[*]` 1.0_

<hr>
        
`[*]` Instalación en `Linux:`

`[1]` Clonar el `repositorio:`

    git clone https://github.com/ZombieGeeK0/ReverseConnections
`[2]` Acceder a la `carpeta:` 

    cd ReverseConnections
`[3]` Darle permisos al `instalador:`

    chmod +x install.sh && chmod 777 install.sh
`[4]` Ejecutar el `instalador` con `bash:`

    sudo bash install.sh

<hr>

`[*]` Comandos del `install.sh:`

- sudo apt-get update
- sudo apt-get install git -y
- sudo apt-get install python3
- sudo apt-get install python3-pip
- pip3 install argparse
- sudo apt install -y tor torbrowser-launcher (Escribe "torbrowser-launcher" para inciarlo)
  
<hr>

- VS CODE:
- sudo apt-get install wget gpg
- wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
- sudo sh -c 'echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" > /etc/apt/sources.list.d/vscode.list'
- rm -f packages.microsoft.gpg
- sudo apt install apt-transport-https
- sudo apt update
- sudo apt install code

<hr>

`[*]` Funcionalidades `(ejemplos)`:

    python3 connect.py -i True  [Instala todos los requerimientos]
    python3 connect.py -a True  [Muestra todos los comandos]
    python3 connect.py -s True -p 4444  [Levanta un servidor en Python desde el puerto 4444]
    python3 connect.py -u https://www.example.com/  [Escanea la URL especificada con SQLmap en busca de DBS]
    python3 connect.py -l True -p 4444  [Inicia una escucha en el puerto 4444]
    python3 connect.py -c True -u https://github.com/ZombieGeeK0/ReverseConnections  [Clona el repositorio especificado]
    python3 connect.py -r True -name Example  [Busca un nombre en plataformas de Internet con Sherlock]
    python3 connect.py -v True -n NombreDelPayload -p 4445 -t 127.0.1.1 -e .exe  [Genera un payload con msfvenom para Windows, en este caso. El sistema operativo se controla por la extensión]

<hr>

`[*]` Comandos:

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

`- EN LOS COMANDOS QUE NO REQUIEREN EXTENSIÓN SE DEBERÁ COLOCAR EL PARÁMETRO "True".`

<hr>

`[*]` Extensiones:

- .apk  [Android]
- .exe  [Windows]
- .elf [Linux]

<hr>

explicacion del uso mostrar codigo que se ejecuta como en quackify

<hr>

![imagen](https://github.com/ZombieGeeK0/GodZilla/assets/158185295/156e5b7e-3cf9-4a3d-b018-34cc8e4532b9)

<hr>

`[#]` Puedes contactar conmigo por `Discord` mandando una `invitación a qwfkr:`

    qwfkr
`[#]` Si no, mándame un Email a `3xpl017.contact@proton.me:`

    3xpl017.contact@proton.me:
