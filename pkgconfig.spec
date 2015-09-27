%define pkgname pkg-config
%bcond_with crosscompile

Summary:	Pkgconfig helps make building packages easier
Name:		pkgconfig
Version:	0.28
Release:	11
License:	GPLv2+
Group:		Development/Other
Url:		http://pkg-config.freedesktop.org/
Source0:	http://pkgconfig.freedesktop.org/releases/%{pkgname}-%version.tar.gz
Source1:	pkgconfig.rpmlintrc
Patch0:		pkg-config-large-fs.patch
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(popt)
# (fhimpe) Otherwise packages with pc files having
# Requires: pkg-config > X are not installable
Provides:	pkgconfig(pkg-config) = %{version}

%description
pkgconfig is a program which helps you gather information to make
life easier when you are compiling a program for those programs which support
it.

In fact, it's required to build certain packages.

%prep
%setup -qn %{pkgname}-%{version}
%apply_patches
# lfs patch touches config.h.in; need this hack to prevent autoreconf and automake
touch aclocal.m4 config.h.in Makefile.in

%build
%if %{with crosscompile}
export glib_cv_stack_grows=no
export glib_cv_uscore=yes
export ac_cv_func_posix_getpwuid_r=yes
export ac_cv_func_posix_getgrgid_r=yes
%configure \
        --with-internal-glib \
        --with-installed-popt
%make

%else
%configure \
	--with-installed-glib \
        --with-installed-popt
%make
%endif

%install
%makeinstall_std

rm -fr %{buildroot}%{_datadir}/doc

mkdir -p %{buildroot}%{_libdir}/pkgconfig
%if "%{_lib}" != "lib"
mkdir -p %{buildroot}%{_prefix}/lib/pkgconfig
ln -s ../../lib/pkgconfig %{buildroot}%{_libdir}/pkgconfig/32
%endif

mkdir -p %{buildroot}%{_datadir}/pkgconfig

# (tpg) disable checks for now
#%check
#%make check

%files
%doc AUTHORS INSTALL README ChangeLog pkg-config-guide.html
%{_bindir}/pkg-config
%{_bindir}/*-mandriva-*-pkg-config
%dir %{_libdir}/pkgconfig
%{_datadir}/pkgconfig
%if "%{_lib}" != "lib"
%{_prefix}/lib/pkgconfig
%{_libdir}/pkgconfig/32
%endif
%{_datadir}/aclocal/*
%{_mandir}/man1/*

