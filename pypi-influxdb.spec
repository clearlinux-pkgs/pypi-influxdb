#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-influxdb
Version  : 5.3.1
Release  : 73
URL      : https://files.pythonhosted.org/packages/86/4f/a9c524576677c1694b149e09d4fd6342e4a1d9a5f409e437168a14d6d150/influxdb-5.3.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/86/4f/a9c524576677c1694b149e09d4fd6342e4a1d9a5f409e437168a14d6d150/influxdb-5.3.1.tar.gz
Summary  : InfluxDB client
Group    : Development/Tools
License  : MIT
Requires: pypi-influxdb-license = %{version}-%{release}
Requires: pypi-influxdb-python = %{version}-%{release}
Requires: pypi-influxdb-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(msgpack)
BuildRequires : pypi(python_dateutil)
BuildRequires : pypi(pytz)
BuildRequires : pypi(requests)
BuildRequires : pypi(six)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
===============

%package license
Summary: license components for the pypi-influxdb package.
Group: Default

%description license
license components for the pypi-influxdb package.


%package python
Summary: python components for the pypi-influxdb package.
Group: Default
Requires: pypi-influxdb-python3 = %{version}-%{release}

%description python
python components for the pypi-influxdb package.


%package python3
Summary: python3 components for the pypi-influxdb package.
Group: Default
Requires: python3-core
Provides: pypi(influxdb)
Requires: pypi(msgpack)
Requires: pypi(python_dateutil)
Requires: pypi(pytz)
Requires: pypi(requests)
Requires: pypi(six)

%description python3
python3 components for the pypi-influxdb package.


%prep
%setup -q -n influxdb-5.3.1
cd %{_builddir}/influxdb-5.3.1
pushd ..
cp -a influxdb-5.3.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1672281712
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-influxdb
cp %{_builddir}/influxdb-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-influxdb/00911d51b2df5ac0cc09dc2f5549a55945db02f0 || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-influxdb/00911d51b2df5ac0cc09dc2f5549a55945db02f0

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
