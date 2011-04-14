%define up_name	check_mysql_health

Summary:	Check MySQL
Name:		nagios-%{up_name}
Version:	2.1.5.1
Release:	%mkrel 1
Group:		Networking/Other
License:	GPL
URL:		http://www.consol.de/opensource/nagios/check-mysql-health/
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
