# Direwrite
E-ink display for Direwolf

Run with `direwolf -t 0 & python3 ~/Direwrite/direwrite.py` or with `direwrite.sh`

Need to kill Direwolf after with `ps -ef | grep direwolf | grep -v grep | awk '{print $2}' | xargs kill` or with `kill_dw.sh`

https://numpy.org/devdocs/user/troubleshooting-importerror.html to resolve issues installing numpy/pandas on Pi

Papirus API docs - https://github.com/PiSupply/PaPiRus

chmod u+x direwrite.sh

install service file - cp /etc/systemd/system