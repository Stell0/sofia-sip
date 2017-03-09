
Name:		sofia-sip
Version:	1.12.11
Release:	1%{?dist}
Summary:	Open-source SIP User-Agent library

Group:		Network
License:	LGPL
URL:		http://sofia-sip.sourceforge.net/
Source0:	%{name}-%{version}.tar.gz
Patch0:		0001-fix-undefined-behaviour.patch

BuildRequires:	autoconf nethserver-devtools
AutoReq: no

%description
Sofia-SIP is an open-source SIP User-Agent library, compliant with the
IETF RFC3261 specification.

It can be used as a building block for SIP client software for uses such
as VoIP, IM, and many other real-time and person-to-person communication services.

The primary target platform for Sofia-SIP is GNU/Linux. Sofia-SIP is based on
a SIP stack developed at the Nokia Research Center. Sofia-SIP is licensed
under the LGPL.


%prep
%setup -q
%patch0 -p1

%build
%configure --prefix=%{_prefix} \
  --exec-prefix=%{_prefix} \
  --sysconfdir=%{_sysconfdir} \
  --bindir=%{_bindir} \
  --datadir=%{_var}/www

make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
rm -rf %{buildroot}/usr/share/man/man1
find %{buildroot}
%{genfilelist} %{buildroot} > %{name}-%{version}-filelist

%clean
rm -rf %{buildroot}

%files -f %{name}-%{version}-filelist
%defattr(-,root,root,-)

%doc


%changelog
* Thu Mar 9 2017 Giovanni Bezicheri <giovanni.bezicheri@nethesis.it> - 1.12.11-1
- First Release.

