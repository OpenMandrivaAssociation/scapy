Name:		scapy
Version:	2.2.0
Release:	%mkrel 1
Summary:	An interactive packet manipulation tool and network scanner
Group:		Networking/Other
License:	GPLv2
URL:		http://www.secdev.org/projects/scapy
Source:		http://www.secdev.org/projects/scapy/files/%name-%version.tar.gz
BuildArch:	noarch
BuildRequires:	python-devel
Requires:	python >= 2.2
Requires:	nmap
Requires:	tcpdump

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
%__python setup.py build

%install
%__rm -rf %{buildroot}
%__install -Dp -m0644 doc/scapy.1.gz %{buildroot}%{_mandir}/man1/scapy.1.gz
%__python setup.py install -O1 --skip-build --root %{buildroot}
%__rm -f %{buildroot}%{python_sitelib}/*egg-info/requires.txt

%clean
%__rm -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc %{_mandir}/man1/scapy.1*
%{_bindir}/scapy
%{_bindir}/UTscapy
%{py_puresitedir}/scapy/*
%{py_puresitedir}/scapy-*.egg-info
