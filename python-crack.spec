Summary:	Python bindings for cracklib
Name:		python-crack
Version:	0.5.1
Release:	2
License:	MIT
Group:		Libraries/Python
Source0:	http://download.savannah.gnu.org/releases/python-crack/%{name}-%{version}.tar.gz
# Source0-md5:	0a0cadc8679e8dcb052dd9c22a5e032e
URL:		http://www.nongnu.org/python-crack/
BuildRequires:	cracklib-devel
BuildRequires:	python-devel >= 1:2.5
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module brings to Python programs the capability of evaluating
password strength. To achieve this noble aim it uses the well known
cracklib toolkit, hence the name.

%prep
%setup -q

%build
%configure \
	DEFAULT_DICTPATH=%{_datadir}/dict/cracklib_dict
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README doc/html
%attr(755,root,root) %{py_sitedir}/*.so
%{py_sitescriptdir}/*.py[co]
