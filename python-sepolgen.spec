Summary:	sepolgen - Python module for policy generation
Summary(pl.UTF-8):	Moduł Pythona sepolgen do generowania polityki
Name:		python-sepolgen
Version:	1.2.1
Release:	1
License:	GPL v2
Group:		Development/Languages/Python
Source0:	http://userspace.selinuxproject.org/releases/current/sepolgen-%{version}.tar.gz
# Source0-md5:	ce662a83188bc3a9b40c15792fcaf2c8
URL:		http://userspace.selinuxproject.org/trac/wiki
BuildRequires:	python-modules >= 2
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
sepolgen - Python module for policy generation.

%description -l pl.UTF-8
Moduł Pythona sepolgen do generowania polityki.

%prep
%setup -q -n sepolgen-%{version}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PYTHONLIBDIR=%{py_sitescriptdir}

%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%dir %{py_sitescriptdir}/sepolgen
%{py_sitescriptdir}/sepolgen/*.py[co]
%dir /var/lib/sepolgen
/var/lib/sepolgen/perm_map
