#!/bin/bash
#remove x728 old installtion
sudo sed -i '/x728/d' /etc/rc.local
sudo sed -i '/ds1307/d' /etc/rc.local
sudo sed -i '/hwclock/d' /etc/rc.local
sudo sed -i '/ds1307/d' /etc/modules
sudo sed -i '/x728/d' ~/.bashrc

sudo rm /usr/local/bin/x728softsd.sh -f
sudo rm /etc/x728pwr.sh -f
