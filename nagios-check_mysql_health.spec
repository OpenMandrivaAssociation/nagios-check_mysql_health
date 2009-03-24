%define up_name	check_mysql_health
%define name	nagios-%{up_name}
%define version	2.0.3
%define release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Check MySQL
Group:		Networking/Other
License:	GPL
URL:		http://www.consol.de/opensource/nagios/check-mysql-health/
Source0:	http://www.consol.de/fileadmin/opensource/Nagios/%{up_name}-%{version}.tar.gz
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
This plugin is used to monitor a variety of mysql database metrics.

%prep
%setup -q -n %{up_name}-%{version}

%build
%configure2_5x \
    --libexecdir=%_libdir/nagios/plugins \
    --with-statefiles-dir=%_localstatedir/lib/nagios
%make

%install
rm -rf %{buildroot}

%makeinstall_std

install -d -m 755 %{buildroot}%{_sysconfdir}/nagios/plugins.d
cat > %{buildroot}%{_sysconfdir}/nagios/plugins.d/check_mysql_health.cfg <<'EOF'
define command{
	command_name	check_zone_auth
	command_line	%{_libdir}/nagios/plugins/check_mysql_health
}
EOF

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/nagios/plugins/check_mysql_health
%config(noreplace) %{_sysconfdir}/nagios/plugins.d/check_mysql_health.cfg

