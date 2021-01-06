# Automatic OS updates
It's important to update the OS frequently to avoid security issues.
There are a few ways to do this.

## unattended upgrade on the host
The first way is to install a debian package to do the job direkt on the host.

### Installation
```bash
sudo apt-get install unattended-upgrades
```

### Konfiguration

#### Interactive
```bash
sudo dpkg-reconfigure -plow unattended-upgrades
```

#### edit files

Enable the automatic update and upgrade (apt-get update & apt-get upgrade)
```bash
# vi /etc/apt/apt.conf.d/20auto-upgrades
APT::Periodic::Update-Package-Lists "1";
APT::Periodic::Unattended-Upgrade "1";
```

Configure the service:
```bash
# vi /etc/apt/apt.conf.d/10periodic
APT::Periodic::Update-Package-Lists "1";
APT::Periodic::Download-Upgradeable-Packages "1";
APT::Periodic::AutocleanInterval "5";
APT::Periodic::Unattended-Upgrade "1";
```
