# Security Scanner

## OpenSCAP

### Installation
```bash
dnf install openscap-scanner scap-security-guide
```

### Profile info
```bash
oscap info /usr/share/xml/scap/ssg/content/ssg-fedora-ds.xml
```
Document type describes what format the file is in. Common types include XCCDF, OVAL, Source Data Stream and Result Data Stream.

### Perform scan
```bash
oscap xccdf eval --profile xccdf_org.ssgproject.content_profile_pci-dss --report report.html /usr/share/xml/scap/ssg/content/ssg-fedora-ds.xml
```

[link](https://www.open-scap.org/tools/openscap-base/#download)

## Lynis

### Installation
```bash
git clone https://github.com/CISOfy/lynis.git
```

### Check updates
```bash
cd lynis
sudo ./lynis updates check
```

### Scan system
```bash
cd lynis 
sudo ./lynis audit system
```
