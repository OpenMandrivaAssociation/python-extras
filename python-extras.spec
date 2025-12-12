Name:		python-extras
Version:	1.0.0
Release:	7
Source0:	https://files.pythonhosted.org/packages/source/e/extras/extras-%{version}.tar.gz
Summary:	Useful extra bits for Python
URL:		https://pypi.org/project/extras/
License:	MIT
Group:		Development/Python
BuildRequires:	python%{pyver}dist(pip)
BuildArch:	noarch

%description
Extras is a set of extensions to the Python standard library, originally
written to make the code within testtools cleaner, 
but now split out for general use outside of a testing context.
pydoc extras is your friend. extras currently contains the following functions:
try_import, try_imports and safe_hasattr

%prep
%autosetup -p1 -n extras-%{version}

%build
%py_build

%install
%py_install

%files
%{py_sitedir}/extras
%{py_sitedir}/extras-*.*-info
