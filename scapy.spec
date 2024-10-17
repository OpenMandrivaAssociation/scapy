Name:		scapy
Version:	2.2.0
Release:	2
Summary:	An interactive packet manipulation tool and network scanner
Group:		Networking/Other
License:	GPLv2
URL:		https://www.secdev.org/projects/scapy
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


%changelog
* Wed Feb 15 2012 Andrey Bondrov <abondrov@mandriva.org> 2.2.0-1
+ Revision: 774366
- New version 2.2.0, add tcpdump to Requires

* Mon Apr 19 2010 Sandro Cazzaniga <kharec@mandriva.org> 2.1.1-1mdv2011.0
+ Revision: 536859
- new release 2.1.1

* Thu Feb 04 2010 Michael Scherer <misc@mandriva.org> 2.1.0-1mdv2010.1
+ Revision: 500613
- update to 2.1.0

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 2.0.0.10-2mdv2010.0
+ Revision: 442817
- rebuild

* Fri Jan 23 2009 Jérôme Soyer <saispo@mandriva.org> 2.0.0.10-1mdv2009.1
+ Revision: 332892
- Add BR
- New upstream release

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.1.1-3mdv2009.0
+ Revision: 242646
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Fri Jul 27 2007 Pascal Terjan <pterjan@mandriva.org> 1.1.1-1mdv2008.0
+ Revision: 56244
- 1.1.1
- 1.1.1
- Import scapy



* Mon Mar 20 2006 Lenny Cartier <lenny@mandriva.com> 1.0.4-1mdk
- 1.0.4

* Wed Mar 01 2006 Nicolas L�cureuil <neoclust@mandriva.org> 1.0.3-1mdk
- New release 1.0.3

* Thu Oct 27 2005 Michael Scherer <misc@mandriva.org> 1.0.1-1mdk
- New release 1.0.1
- mkrel, new url

* Tue Jan 11 2005 Michael Scherer <misc@mandrake.org> 0.9.17-2mdk 
- fix import of module when binary us used directly ( thanks blino for bugreport )

* Sat Aug 28 2004 Michael Scherer <misc@mandrake.org> 0.9.17-1mdk
- New release 0.9.17
- rpmbuildupdate aware

* Thu Mar 18 2004 Michael Scherer <misc@mandrake.org> 0.9.16-1mdk
- 0.9.16
 
* Tue Aug 05 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.9.14-2mdk
- nmap as a dependency

* Fri Aug 01 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.9.14-1mdk
- mandrakized original package from Dag Wieers <dag@wieers.com>

* Sat May 17 2003 Dag Wieers <dag@wieers.com> - 0.9.13-0.beta
- Initial package. (using DAR)
