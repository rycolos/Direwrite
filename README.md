# Direwrite
E-ink display for Direwolf APRS decoding on Raspberry Pi Zero

## Requirements
All references to `gktnc` should be replaced with your home directory. All scrips and instructions assume this repo is cloned into your home directory. 

Designed for Pi Zero W and Papirus 2" E-ink display. 

* Direwolf TNC set up for APRS - See https://k5eok.org/2021/01/19/aprs-digipeater-igate-with-direwolf-entry-level/ for a good guide. You must configure daily logging with `LOGDIR /home/gktnc/direwolf-logs` (where `gktnc` is replaced with your home directory) in your `direwolf.conf` file.
* Papirus with Python 3 API - See https://github.com/PiSupply/PaPiRus

```
#TMUX
sudo apt install tmux

#PANDAS
pip3 install pandas

#OPTIONAL - if get Python error "Importing the numpy c-extensions failed."
sudo apt-get install libatlas-base-dev
```
## Enable execution permissions of scripts
`chmod u+x /home/gktnc/Direwrite/direwrite.sh`
`chmod u+x /home/gktnc/Direwrite/kill_dw.sh`

## Run manually
Run manually with `direwolf -t 0 & python3 /home/gktnc/Direwrite/direwrite.py` or with `sh /home/gktnc/Direwrite/direwrite.sh`

May need to kill Direwolf after running manually with `ps -ef | grep direwolf | grep -v grep | awk '{print $2}' | xargs kill` or with `sh /home/gktnc/Direwrite/kill_dw.sh`

## Set to run automatically on boot
Edit user cron with `crontab -e`.
Add the following entry, updating the script directory as needed:
`@reboot sleep 30 && /usr/bin/tmux new-session -d -s direwolf /home/gktnc/Direwrite/direwrite.sh`

Use `tmux attach -t direwolf` to view session.