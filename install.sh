clear
echo ====================================================================================================
echo [?] Instalando...
echo ====================================================================================================
sudo apt-get update && sudo apt-get install git -y && sudo apt-get install python3 && sudo apt-get install python3-pip && pip3 install argparse && pip3 install webbrowser && sudo apt install -y tor torbrowser-launcher && sudo apt-get install wget gpg && wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg && sudo sh -c 'echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" > /etc/apt/sources.list.d/vscode.list' && rm -f packages.microsoft.gpg && sudo apt install apt-transport-https && sudo apt update && sudo apt install code && git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git sqlmap-dev && sudo apt-get install Netcat && git clone https://github.com/sherlock-project/sherlock
echo ====================================================================================================
echo [?] Requerimientos instalados.
