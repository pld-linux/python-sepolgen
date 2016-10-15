#
# Conditional build:
%bcond_without	python2	# Python 2 module
%bcond_without	python3	# Python 3 module

Summary:	sepolgen - Python 2 module for policy generation
Summary(pl.UTF-8):	Moduł Pythona 2 sepolgen do generowania polityki
Name:		python-sepolgen
Version:	1.2.3
Release:	1
License:	GPL v2
Group:		Development/Languages/Python
#Source0Download: https://github.com/SELinuxProject/selinux/wiki/Releases
Source0:	https://raw.githubusercontent.com/wiki/SELinuxProject/selinux/files/releases/20160223/sepolgen-%{version}.tar.gz
# Source0-md5:	d17b4072ed14d1f8d94ffd667ddc2864
URL:		https://github.com/SELinuxProject/selinux/wiki
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python >= 2
BuildRequires:	python-modules >= 2
%endif
%if %{with python2}
BuildRequires:	python3 >= 1:3.2
BuildRequires:	python3-modules >= 1:3.2
%endif
Requires:	%{name}-common = %{version}-%{release}
Requires:	python-selinux >= 2.5
Suggests:	python-setools
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
sepolgen - Python module for policy generation.

%description -l pl.UTF-8
Moduł Pythona sepolgen do generowania polityki.

%package common
Summary:	Common files for sepolgen Python modules
Summary(pl.UTF-8):	Pliki wspólne dla modułów Pythona sepolgen
Group:		Development/Languages/Python

%description common
Common files for sepolgen Python modules.

%description common -l pl.UTF-8
Pliki wspólne dla modułów Pythona sepolgen.

%package -n python3-sepolgen
Summary:	sepolgen - Python 3 module for policy generation
Summary(pl.UTF-8):	Moduł Pythona 3 sepolgen do generowania polityki
Group:		Development/Languages/Python
Requires:	%{name}-common = %{version}-%{release}
Requires:	python3-selinux >= 2.5
# TODO: uncomment when setools supports python 3 (3.3.8 doesn't)
#Suggests:	python3-setools

%description -n python3-sepolgen
sepolgen - Python module for policy generation.

%description -n python3-sepolgen -l pl.UTF-8
Moduł Pythona sepolgen do generowania polityki.

%prep
%setup -q -n sepolgen-%{version}

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PYTHON=%{__python} \
	PYTHONLIBDIR=%{py_sitescriptdir}

%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean
%endif

%if %{with python3}
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PYTHON=%{__python3} \
	PYTHONLIBDIR=%{py3_sitescriptdir}

%py3_comp $RPM_BUILD_ROOT%{py3_sitescriptdir}
%py3_ocomp $RPM_BUILD_ROOT%{py3_sitescriptdir}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{py_sitescriptdir}/sepolgen
%{py_sitescriptdir}/sepolgen/*.py[co]

%files common
%defattr(644,root,root,755)
%doc ChangeLog
%dir /var/lib/sepolgen
/var/lib/sepolgen/perm_map

%files -n python3-sepolgen
%defattr(644,root,root,755)
%dir %{py3_sitescriptdir}/sepolgen
%{py3_sitescriptdir}/sepolgen/*.py
%{py3_sitescriptdir}/sepolgen/__pycache__
