# Anit Maleware und anti rootkit tools

## ClamaV
I found a good [tutorial[(https://www.ctrl.blog/entry/how-to-periodic-clamav-scan.html) and copied the commands together for a faster setup for new servers.

### Installation
```bash
dnf install clamav-scanner clamav-scanner-systemd clamav-update
```

### Configuration
```bash
ln -s /etc/clamd.d/scan.conf /etc/clamd.conf

setsebool -P antivirus_can_scan_system 1
```

### Automatic Updates
To automatic the virus database update
```bash
echo '0 */8  *  *  0  nice -n 16  systemd-cat --identifier="clamav-update" /usr/bin/freshclam' >>/etc/cron.d/clamav
```

### start and enable scanner
```bash
systemctl start clamd@scan
systemctl status clamd@scan
systemctl enable clamd@scan
```

### periodic scan
```bash
echo '30 5 * * 7 nice -n 18  systemd-cat --identifier="clamav-scan" clamdscan --quiet --fdpass /' >>/etc/cron.d/clamav
```


## Rootkit Hunter (rkhunter)

### Installation
```bash
dnf install rkhunter
```

### update Database
```bash
rkhunter --update
rkhunter --propupd
```

### setup daily cron

```bash
# vi /etc/cron.daily/rkhunter.sh
#!/bin/sh
(
/usr/local/bin/rkhunter --versioncheck
/usr/local/bin/rkhunter --update
/usr/local/bin/rkhunter --cronjob --report-warnings-only
) | /bin/mail -s 'rkhunter Daily Run (PutYourServerNameHere)' your@email.com
```

```bash
chmod 755 /etc/cron.daily/rkhunter.sh
```

### manual scan
```bash
rkhunter --check
```

### Log files
```bash
cat /var/log/rkhunter.log
```

[source](https://www.tecmint.com/install-rootkit-hunter-scan-for-rootkits-backdoors-in-linux/)


## LMD

[source 1: tecmint 2015](https://www.tecmint.com/install-linux-malware-detect-lmd-in-rhel-centos-and-fedora/)  
[source 2: lmd project](http://www.rfxn.com/projects/linux-malware-detect/)
