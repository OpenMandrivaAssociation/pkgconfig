%define pkgname pkg-config
%define glib 1.2.10
Name:		pkgconfig
Version:	0.23
Release:	%mkrel 6
Summary:	Pkgconfig helps make building packages easier
Source0:	http://pkgconfig.freedesktop.org/releases/%{pkgname}-%version.tar.gz
Patch0:		pkg-config-0.23-biarch.patch
# (fc) 0.19-1mdk add --print-provides/--print-requires (Fedora)
Patch1:		pkgconfig-0.15.0-reqprov.patch
# (gb) 0.19-2mdk 64-bit fixes, though that code is not used, AFAICS
Patch3:		glib-1.2.10-format_not_a_string_literal_and_no_format_arguments.diff
URL:		http://pkg-config.freedesktop.org/
# (fhimpe) Otherwise packages with pc files having
# Requires: pkg-config > X are not installable
Provides:	pkgconfig(pkg-config) = %{version}
License:	GPLv2+
Group:		Development/Other
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
pkgconfig is a program which helps you gather information to make
life easier when you are compiling a program for those programs which support
it.

In fact, it's required to build certain packages.

%prep
%setup -q -n %{pkgname}-%{version}
%patch0 -p1 -b .biarch
%patch1 -p1 -b .reqprov

cd glib-%glib
%patch3 -p1 -b .format_not_a_string_literal_and_no_format_arguments
cd ..

#needed by patch1
autoheader
autoconf

%build
%configure2_5x 
%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std

mkdir -p $RPM_BUILD_ROOT%{_libdir}/pkgconfig
%if "%{_lib}" != "lib"
mkdir -p $RPM_BUILD_ROOT%{_prefix}/lib/pkgconfig
ln -s ../../lib/pkgconfig $RPM_BUILD_ROOT%{_libdir}/pkgconfig/32
%endif

mkdir -p $RPM_BUILD_ROOT%{_datadir}/pkgconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING INSTALL README ChangeLog
%{_bindir}/pkg-config
%{_libdir}/pkgconfig
%{_datadir}/pkgconfig
%if "%{_lib}" != "lib"
%{_prefix}/lib/pkgconfig
%{_libdir}/pkgconfig/32
%endif
%{_datadir}/aclocal/*
%{_mandir}/man1/*
