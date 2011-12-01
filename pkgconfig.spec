%define pkgname pkg-config

Name:		pkgconfig
Version:	0.26
Release:	%mkrel 1
Summary:	Pkgconfig helps make building packages easier
Source0:	http://pkgconfig.freedesktop.org/releases/%{pkgname}-%version.tar.gz
Patch0:		pkg-config-0.26-biarch.patch
URL:		http://pkg-config.freedesktop.org/
# (fhimpe) Otherwise packages with pc files having
# Requires: pkg-config > X are not installable
Provides:	pkgconfig(pkg-config) = %{version}
License:	GPLv2+
Group:		Development/Other
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
BuildRequires:	glib2-devel
BuildRequires:	popt-devel

%description
pkgconfig is a program which helps you gather information to make
life easier when you are compiling a program for those programs which support
it.

In fact, it's required to build certain packages.

%prep
%setup -q -n %{pkgname}-%{version}
%patch0 -p1 -b .biarch

%build
autoreconf -fi
%configure2_5x --with-installed-glib --with-installed-popt
%make

%install
rm -rf %{buildroot}
%makeinstall_std

rm -fr %buildroot%_datadir/doc

mkdir -p %{buildroot}%{_libdir}/pkgconfig
%if "%{_lib}" != "lib"
mkdir -p %{buildroot}%{_prefix}/lib/pkgconfig
ln -s ../../lib/pkgconfig %{buildroot}%{_libdir}/pkgconfig/32
%endif

mkdir -p %{buildroot}%{_datadir}/pkgconfig

%check
%make check

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS COPYING INSTALL README ChangeLog pkg-config-guide.html
%{_bindir}/pkg-config
%dir %{_libdir}/pkgconfig
%{_datadir}/pkgconfig
%if "%{_lib}" != "lib"
%{_prefix}/lib/pkgconfig
%{_libdir}/pkgconfig/32
%endif
%{_datadir}/aclocal/*
%{_mandir}/man1/*
