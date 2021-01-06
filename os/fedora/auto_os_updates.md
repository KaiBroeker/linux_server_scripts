# Automatic OS updates
It's important to update the OS frequently to avoid security issues. There are a few ways to do this.

## Installation
The first way is to install a rpm package to do the job direkt on the host.
```bash
dnf install dnf-automatic
```

## Configuration
The first step is to enable the tool: 
```bash
# vi /etc/dnf/automatic.conf
...
apply_updates = yes
```

The next step is to enable the automatic service, so that the auto update run periodic:
```bash
systemctl enable dnf-automatic.timer
systemctl start dnf-automatic.timer
```
You can also overwrite the timer with your own to only make updates at less important times. 

### Check the timer
We can also check the timer:

```bash
# systemctl list-timers 'dnf*'
NEXT                        LEFT          LAST                        PASSED   UNIT                ACTIVATES
Wed 2021-01-06 19:35:15 CET 1h 49min left Wed 2021-01-06 17:38:41 CET 7min ago dnf-makecache.timer dnf-makecache.service
Thu 2021-01-07 06:12:03 CET 12h left      Wed 2021-01-06 06:36:29 CET 11h ago  dnf-automatic.timer dnf-automatic.service

2 timers listed. 
```
