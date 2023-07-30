# Direwrite
E-ink display for Direwolf

## Requirements
Designed for Pi Zero W and Papirus 2" E-ink display. 

* DIREWOLF
See https://k5eok.org/2021/01/19/aprs-digipeater-igate-with-direwolf-entry-level/ for a good guide
* PAPIRUS + PYTHON 3 API
See https://github.com/PiSupply/PaPiRus

```
#TMUX
sudo apt install tmux

#PANDAS
pip3 install pandas

#OPTIONAL - if get Python error "Importing the numpy c-extensions failed."
sudo apt-get install libatlas-base-dev
```
## Enable execution permissions of scripts
`chmod u+x direwrite.sh`
`chmod u+x kill_dw.sh`

## Run manually
Run manually with `direwolf -t 0 & python3 /home/gktnc/Direwrite/direwrite.py` or with `sh /home/gktnc/Direwrite/direwrite.sh`

May need to kill Direwolf after running manually with `ps -ef | grep direwolf | grep -v grep | awk '{print $2}' | xargs kill` or with `sh /home/gktnc/Direwrite/kill_dw.sh`

## Set to run automatically on boot
`crontab -e`
Add the following entry, updating the script directory as needed:
`@reboot sleep 30 && /usr/bin/tmux new-session -d -s direwolf /home/gktnc/Direwrite/direwrite.sh`

Use `tmux attach -t direwolf` to view session.