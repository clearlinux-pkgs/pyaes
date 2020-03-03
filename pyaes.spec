#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pyaes
Version  : 1.6.1
Release  : 14
URL      : https://files.pythonhosted.org/packages/44/66/2c17bae31c906613795711fc78045c285048168919ace2220daa372c7d72/pyaes-1.6.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/44/66/2c17bae31c906613795711fc78045c285048168919ace2220daa372c7d72/pyaes-1.6.1.tar.gz
Summary  : Pure-Python Implementation of the AES block-cipher and common modes of operation
Group    : Development/Tools
License  : MIT
Requires: pyaes-license = %{version}-%{release}
Requires: pyaes-python = %{version}-%{release}
Requires: pyaes-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
A pure-Python implementation of the AES (FIPS-197)
block-cipher algorithm and common modes of operation (CBC, CFB, CTR, ECB,
OFB) with no dependencies beyond standard Python libraries. See README.md
for API reference and details.

%package license
Summary: license components for the pyaes package.
Group: Default

%description license
license components for the pyaes package.


%package python
Summary: python components for the pyaes package.
Group: Default
Requires: pyaes-python3 = %{version}-%{release}

%description python
python components for the pyaes package.


%package python3
Summary: python3 components for the pyaes package.
Group: Default
Requires: python3-core
Provides: pypi(pyaes)

%description python3
python3 components for the pyaes package.


%prep
%setup -q -n pyaes-1.6.1
cd %{_builddir}/pyaes-1.6.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583204212
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pyaes
cp %{_builddir}/pyaes-1.6.1/LICENSE.txt %{buildroot}/usr/share/package-licenses/pyaes/bdd01ad36671fb918c41eef13a00b4957e32c353
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pyaes/bdd01ad36671fb918c41eef13a00b4957e32c353

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
