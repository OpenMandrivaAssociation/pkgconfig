%define pkgname pkg-config

Name:		pkgconfig
Version:	0.28
Release:	1
Summary:	Pkgconfig helps make building packages easier
Source0:	http://pkgconfig.freedesktop.org/releases/%{pkgname}-%version.tar.gz
URL:		http://pkg-config.freedesktop.org/
# (fhimpe) Otherwise packages with pc files having
# Requires: pkg-config > X are not installable
Provides:	pkgconfig(pkg-config) = %{version}
License:	GPLv2+
Group:		Development/Other
BuildRequires:	glib2-devel
BuildRequires:	popt-devel

%description
pkgconfig is a program which helps you gather information to make
life easier when you are compiling a program for those programs which support
it.

In fact, it's required to build certain packages.

%prep
%setup -q -n %{pkgname}-%{version}

%build
%configure2_5x \
		--with-installed-glib \
        --with-installed-popt
%make

%install
%makeinstall_std

rm -fr %{buildroot}%{_datadir}/doc

mkdir -p %{buildroot}%{_libdir}/pkgconfig
%if "%{_lib}" != "lib"
mkdir -p %{buildroot}%{_prefix}/lib/pkgconfig
ln -s ../../lib/pkgconfig %{buildroot}%{_libdir}/pkgconfig/32
%endif

mkdir -p %{buildroot}%{_datadir}/pkgconfig

%check
%make check

%files
%doc AUTHORS INSTALL README ChangeLog pkg-config-guide.html
%{_bindir}/pkg-config
%{_bindir}/*-mandriva-linux-gnu-pkg-config
%dir %{_libdir}/pkgconfig
%{_datadir}/pkgconfig
%if "%{_lib}" != "lib"
%{_prefix}/lib/pkgconfig
%{_libdir}/pkgconfig/32
%endif
%{_datadir}/aclocal/*
%{_mandir}/man1/*


%changelog
* Tue Feb 21 2012 abf
- The release updated by ABF

* Sat May 21 2011 GÃ¶tz Waschk <waschk@mandriva.org> 0.26-1mdv2011.0
+ Revision: 676613
- new version
- drop patch 6
- update patch 0

* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 0.25-2
+ Revision: 667778
- mass rebuild

* Fri Jul 30 2010 Funda Wang <fwang@mandriva.org> 0.25-1mdv2011.0
+ Revision: 563805
- add check section
- new version 0.25
- use system glib2 and popt to build
- drop merged patch1 (--print-provides) and patch4 (crosscompile)
- add fedora patch to deal with autoconf 2.66

* Tue Dec 15 2009 Frederic Crozat <fcrozat@mandriva.com> 0.23-7mdv2010.1
+ Revision: 479028
- Patch4 (GIT): fix crosscompilation support (Mdv bug #55902)

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.23-6mdv2010.0
+ Revision: 426725
- rebuild
- drop obsolete 64 bit patch
- drop useless call to cputoolize

* Mon Dec 22 2008 Oden Eriksson <oeriksson@mandriva.com> 0.23-4mdv2009.1
+ Revision: 317533
- rediffed one fuzzy patch (P2)
- fix build with -Werror=format-security (P3)

* Wed Jul 30 2008 Frederik Himpe <fhimpe@mandriva.org> 0.23-3mdv2009.0
+ Revision: 255591
- Add Provides: pkgconfig(pkg-config) = %%{version} so that packages i
  with pc file having Requires: pkg-config > X are installable
  http://lists.freedesktop.org/archives/telepathy/2008-July/002062.html

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.23-2mdv2009.0
+ Revision: 224972
- rebuild

* Thu Feb 07 2008 GÃ¶tz Waschk <waschk@mandriva.org> 0.23-1mdv2008.1
+ Revision: 163393
- new version
- rediff patch 0
- build fix

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Thu Oct 19 2006 Götz Waschk <waschk@mandriva.org> 0.21-1mdv2007.1
- update and fix patch 0
- New version 0.21

* Sat Apr 01 2006 Helio Castro <helio@mandriva.com> 0.20-2mdk
- Removed --enable-indirect-deps since this leads a undesirable chain of
  dependencies during compilation. New modular xorg suffers heavily on this
  problem.

* Thu Oct 27 2005 David Walluck <walluck@mandriva.org> 0.20-1mdk
- 0.20

* Sat Sep 03 2005 Gwenole Beauchesne <gbeauchesne@mandriva.com> 0.19-2mdk
- some 64-bit fixes, but apparently in dead code
- fix broken patch1 regeneration from 0.17.2-1mdk

* Fri Aug 12 2005 Frederic Crozat <fcrozat@mandriva.com> 0.19-1mdk 
- Release 0.19
- Regenerate patch1
- remove make check, doesn't pass upstream
- Patch2 (Fedora): add --print-provides/--print-requires
- Patch3 (Fedora): fix overflow when using gcc4

* Thu Apr 28 2005 Frederic Crozat <fcrozat@mandriva.com> 0.17.2-2mdk 
- Create /usr/share/pkgconfig for arch independant .pc files

* Thu Apr 28 2005 Frederic Crozat <fcrozat@mandriva.com> 0.17.2-1mdk 
- Release 0.17.2
- don't enable inter-library dependency, it might break many apps
- Remove patch0 (merged upstream)
- Regenerate patch1

* Tue Jan 11 2005 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 0.15.0-5mdk
- biarch pkgconfig support

* Sun Jun 13 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.15.0-4mdk
- small patch to avoid spurious aclocal warning
- spec cleanup

