%define kloxo /usr/local/lxlabs/kloxo
%define productname kloxomr
%define timestamp 2013031805

Name: %{productname}
Summary: Kloxo-MR web panel
Version: 6.5.0.f
Release: %{timestamp}%{?dist}
License: GPL
Group: Applications/Internet

Source0: %{name}-%{version}-%{timestamp}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch

%description
This is special edition (fork) of Kloxo with many features not existing on 
Kloxo official release (6.1.12+).

This fork named as Kloxo-MR (meaning 'Kloxo fork by Mustafa Ramadhan').

%prep
%setup -q -n %{name}-%{version}-%{timestamp}

%build

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__mkdir} -p -m0755 $RPM_BUILD_ROOT%{kloxo}/
%{__cp} -rp * $RPM_BUILD_ROOT%{kloxo}/
%{__mkdir} -p $RPM_BUILD_ROOT/script/
%{__cp} -rp $RPM_BUILD_ROOT%{kloxo}/pscript/* $RPM_BUILD_ROOT/script/
%{__cp} -rp $RPM_BUILD_ROOT%{kloxo}/httpdocs/htmllib/script/* $RPM_BUILD_ROOT/script/

%clean
#%{__rm} -rf $RPM_BUILD_ROOT

%pre
/usr/sbin/useradd -s /sbin/nologin -M -r -d /home/lxlabs/ \
    -c "Kloxo-MR Website Control Panel" lxlabs &>/dev/null || :

%files
%defattr(644,lxlabs,lxlabs,755)
%{kloxo}
%defattr(644,root,root,755)
/script

%post
if [ "$1" = "1" ]; then
    echo
    echo " --- Kloxo-MR Web Panel ------------------------------------------------- "
    echo "|                                                                        |"
    echo "|  Attention:                                                            |"
    echo "|                                                                        |"
    echo "|  Run 'sh /usr/local/lxlabs/kloxo/install/setup.sh' completely install  |"
    echo "|                                                                        |"
    echo " ----------------------------------------------------------- MRatWork --- "
    echo
elif [ "$1" = "2" ]; then
    echo
    echo " --- Kloxo-MR Web Panel ------------------------------------------------- "
    echo "|                                                                        |"
    echo "|  Attention:                                                            |"
    echo "|                                                                        |"
    echo "|  Run 'sh /script/cleanup' completely update                            |"
    echo "|                                                                        |"
    echo " ----------------------------------------------------------- MRatWork --- "
    echo
fi

%changelog
* Mon Mar 25 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.0.f-2013031805.mr
- no need running full installer.sh twice just function step2 if running setup.sh
* Mon Mar 25 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.0.f-2013031804.mr
- fix bugs relate to install/setup
* Sat Mar 23 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.0.f-2013031803.mr
- remove php modules (except php-pear) because conflict between centos and other repos
* Sat Mar 23 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.0.f-2013031802.mr
- fix critical bug (don't install php-mysqli on install/setup process)
* Mon Mar 18 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.0.f-2013031801.mr
- first release of Kloxo-MR
