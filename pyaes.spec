#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pyaes
Version  : 1.6.1
Release  : 3
URL      : https://files.pythonhosted.org/packages/44/66/2c17bae31c906613795711fc78045c285048168919ace2220daa372c7d72/pyaes-1.6.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/44/66/2c17bae31c906613795711fc78045c285048168919ace2220daa372c7d72/pyaes-1.6.1.tar.gz
Summary  : Pure-Python Implementation of the AES block-cipher and common modes of operation
Group    : Development/Tools
License  : MIT
Requires: pyaes-python3
Requires: pyaes-license
Requires: pyaes-python
BuildRequires : buildreq-distutils3

%description
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
Requires: pyaes-python3

%description python
python components for the pyaes package.


%package python3
Summary: python3 components for the pyaes package.
Group: Default
Requires: python3-core

%description python3
python3 components for the pyaes package.


%prep
%setup -q -n pyaes-1.6.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1534106115
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/pyaes
cp LICENSE.txt %{buildroot}/usr/share/doc/pyaes/LICENSE.txt
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(-,root,root,-)
/usr/share/doc/pyaes/LICENSE.txt

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
