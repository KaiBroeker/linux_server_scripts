#!/usr/bin/env python3

from ftplib import FTP
import math
import os

#curl ftp://ftp.ripe.net/pub/stats/ripencc/delegated-ripencc-latest
ftp = FTP('ftp.ripe.net')     # connect to host, default port
ftp.login()                     # user anonymous, passwd anonymous@
ftp.retrbinary('RETR /pub/stats/ripencc/delegated-ripencc-latest', open('ripeListe', 'wb').write)
ftp.quit()

ripefile = open("ripeListe", "r").readlines()
germanips = []

#ripencc|GB|ipv4|185.97.60.0|1024|20150421|allocated
for entry in ripefile:
    entry = entry.split("|")
    if(entry[1] == "DE" and entry[2] == "ipv4"):
        netmask = str( 32 - int(math.log(int(entry[4]),2)))
        germanips.append(entry[3] + "/" + netmask)

#print(germanips)

for network in germanips:
#    myCmd = 'iptables -A INPUT -i eth1 -s ' + network + " -j ACCEPT"
    myCmd = 'firewall-cmd --permanent --zone=public --add-source=' + network
    print(myCmd)
    os.system(myCmd)

#os.system("iptables -A INPUT -j DROP")
os.system("firewall-cmd --permanent --zone=public --set-target=DROP")
