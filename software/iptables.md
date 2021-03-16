# iptables

## Map IP to another IP
In some cases a IP-Natting like this:
```
iptables -t nat -A OUTPUT -d 192.168.1.15 -j DNAT --to-destination 54.3.22.1
```
[source](https://serverfault.com/questions/692415/map-ip-to-another-ip)
