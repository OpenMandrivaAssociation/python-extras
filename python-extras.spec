# Created by pyp2rpm-2.0.0
%global pypi_name extras
%global with_python2 1
%define version 1.0.0

Name:           python-%{pypi_name}
Version:        %{version}
Release:        3
Group:          Development/Python
Summary:        extras is a set of extensions to the Python standard library 

License:        MIT
URL:            https://github.com/testing-cabal/extras
Source0:        https://files.pythonhosted.org/packages/be/18/0b7283f0ebf6ad4bb6b9937538495eadf05ef097b102946b9445c4242636/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python-setuptools
 
%if %{with_python2}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
%endif # if with_python2


%description
Extras is a set of extensions to the Python standard library, originally written to make the code within testtools cleaner, 
but now split out for general use outside of a testing context.
pydoc extras is your friend. extras currently contains the following functions
try_import, try_imports and safe_hasattr


%if %{with_python2}
%package -n     python2-%{pypi_name}
Summary:        extras is a set of extensions to the Python standard library 

%description -n python2-%{pypi_name}
Extras is a set of extensions to the Python standard library, originally written to make the code within testtools cleaner, 
but now split out for general use outside of a testing context.
pydoc extras is your friend. extras currently contains the following functions
try_import, try_imports and safe_hasattr

%endif # with_python2


%prep
%setup -q -n %{pypi_name}-%{version}

%if %{with_python2}
rm -rf %{py2dir}
cp -a . %{py2dir}
find %{py2dir} -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python2}|'
%endif # with_python2


%build
%{__python} setup.py build

%if %{with_python2}
pushd %{py2dir}
%{__python2} setup.py build
popd
%endif # with_python2


%install

%if %{with_python2}
pushd %{py2dir}
%{__python2} setup.py install --skip-build --root %{buildroot}
popd
%endif # with_python2

%{__python} setup.py install --skip-build --root %{buildroot}


%files
%doc  README.rst LICENSE
%{python_sitelib}/*/*


%if %{with_python2}
%files -n python2-%{pypi_name}
%doc  README.rst LICENSE
%{python2_sitelib}/*/*
%endif # with_python2

