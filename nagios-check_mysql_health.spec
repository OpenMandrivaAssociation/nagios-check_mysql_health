%define up_name	check_mysql_health

Summary:	Check MySQL
Name:		nagios-%{up_name}
Version:	2.1.5.1
Release:	2
Group:		Networking/Other
License:	GPL
URL:		https://www.consol.de/opensource/nagios/check-mysql-health/
Source0:	http://labs.consol.de/wp-content/uploads/2011/04/check_mysql_health-2.1.5.1.tar.gz
BuildArch:	noarch
BuildRequires:	perl
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This plugin is used to monitor a variety of mysql database metrics.

%prep
%setup -q -n %{up_name}-%{version}

%build
autoreconf -fi

%configure2_5x \
    --build=%{_arch}-mandriva-linux-gnu \
    --libexecdir=%{_datadir}/nagios/plugins \
    --with-statefiles-dir=%{_localstatedir}/lib/nagios
%make

%install
rm -rf %{buildroot}

%makeinstall_std

install -d -m 755 %{buildroot}%{_sysconfdir}/nagios/plugins.d
cat > %{buildroot}%{_sysconfdir}/nagios/plugins.d/check_mysql_health.cfg <<'EOF'
define command{
	command_name	check_mysql_health
	command_line	%{_datadir}/nagios/plugins/check_mysql_health
}
EOF

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/nagios/plugins.d/check_mysql_health.cfg
%{_datadir}/nagios/plugins/check_mysql_health


%changelog
* Thu Apr 14 2011 Oden Eriksson <oeriksson@mandriva.com> 2.1.5.1-1mdv2011.0
+ Revision: 652918
- 2.1.5.1

* Sun Apr 10 2011 Oden Eriksson <oeriksson@mandriva.com> 2.1.5-1
+ Revision: 652250
- 2.1.5

* Thu Mar 17 2011 Oden Eriksson <oeriksson@mandriva.com> 2.1.1-5
+ Revision: 645846
- relink against libmysqlclient.so.18

* Sat Jan 01 2011 Oden Eriksson <oeriksson@mandriva.com> 2.1.1-4mdv2011.0
+ Revision: 627264
- rebuilt against mysql-5.5.8 libs, again

* Thu Dec 30 2010 Oden Eriksson <oeriksson@mandriva.com> 2.1.1-3mdv2011.0
+ Revision: 626545
- rebuilt against mysql-5.5.8 libs

* Wed Nov 17 2010 Oden Eriksson <oeriksson@mandriva.com> 2.1.1-1mdv2011.0
+ Revision: 598383
- 2.1.1
- it's really noarch

* Mon Nov 15 2010 Oden Eriksson <oeriksson@mandriva.com> 2.0.3-3mdv2011.0
+ Revision: 597624
- duh!

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Tue Mar 24 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.0.3-1mdv2009.1
+ Revision: 360944
- import nagios-check_mysql_health


* Tue Mar 24 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.0.3-1mdv2009.1
- first mdv release
