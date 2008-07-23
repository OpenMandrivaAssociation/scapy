%define name scapy
%define version 1.1.1
%define release %mkrel 3

Summary: An interactive packet manipulation tool and network scanner
Name: %name
Version: %version
Release: %release
Group: Networking/Other
License: GPL
URL: http://www.secdev.org/projects/scapy
Source: http://www.secdev.org/projects/scapy/files/%name-%version.tar.gz
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildArch: noarch
Requires: python >= 2.2 nmap

%description
Scapy is a powerful interactive packet manipulation tool, packet generator,
network scanner, network discovery, packet sniffer, etc. It can for the
moment replace hping, 85% of nmap, arpspoof, arp-sk, arping, tcpdump,
tethereal, p0f, ....

Scapy uses the python interpreter as a command board. That means that you
can use directly python language (assign variables, use loops, define
functions, etc.) If you give a file as parameter when you run scapy, your
session (variables, functions, intances, ...) will be saved when you leave
the interpretor, and restored the next time you launch scapy. 

%prep

%setup -q

%build

%install
mkdir -p %{buildroot}/%{_libdir}/python%pyver/
install -m 755 scapy.py %{buildroot}/%{_libdir}/python%pyver/
#ln -f %{buildroot}%{_bindir}/scapy.py %{buildroot}%{_libdir}/python%pyver/scapy.py
mkdir -p %{buildroot}%{_bindir}/

echo -e "#!/bin/bash\ncd %{_libdir}/python%pyver/\n./scapy.py" > %{buildroot}%{_bindir}/scapy
chmod 0755  %{buildroot}%{_bindir}/scapy
mkdir -p %{buildroot}/%{_mandir}/man1/
cp %{name}.1 %{buildroot}/%{_mandir}/man1/%{name}.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING changelog.txt README
%{_bindir}/*
%{_libdir}/python%pyver/*
%{_mandir}/man1/*
