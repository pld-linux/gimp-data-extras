Summary:	GIMP - brushes, gradients, palettes and patterns
Summary(pl):	GIMP - pisaki, gradienty, palety i wype³nienia
Name:		gimp-data-extras
Version:	1.0.0
Release:	4
Copyright:	GPL
Group:		X11/Applications/Graphics
Url:		http://www.gimp.org/
Source:		ftp://ftp.gimp.org/pub/gimp/0.99/latest/%{name}-%{version}.tar.bz2
Requires:	gimp
BuildRoot:	/tmp/%{name}-%{version}-root
Buildarch:	noarch

%description
This is the archive of data files for the Gimp.

Contains the latest brushes, gradients, palettes and patterns
by various authors around the internet.

%description -l pl
Pakiet ten zawiera archiwum dodatkowych plików danych dla programu Gimp.
W pakiecie znajduj± siê miêdzy innymi: pisaki, gradienty, palety i wype³nienia 
ró¿nych autorów.

%prep
%setup -q

%build
./configure --prefix=/usr/X11R6
make

%install
rm -rf $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT/usr/X11R6 install

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%doc *gz
/usr/X11R6/share/gimp/brushes/*
/usr/X11R6/share/gimp/patterns/*

%changelog
* Wed Mar 31 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.0.0-4]
- install prefix changed to /usr/X11R6.

* Tue Mar 16 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.0.0-3]
- added gzipping %doc.

* Wed Sep 15 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [1.0.0-2]
- build against Tornado,
- pixed pl translation.

* Mon Aug  10 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.0.0-1]
- added pl translation.

* Wed May  6 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
- %%{version} macro instead %%{PACKAGE_VERSION},
- added using %%{name} macro in Buildroot and Source field,
- added -q %setup parameter.

* Wed Apr 28 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
- Buildroot changed to /tmp/gimp-data-extras-%%{PACKAGE_VERSION}-root,
- changed version to 0.99a,
- package is now builded as noarch and from bziped2 source tar,
- added %defattr macro in %files (allows building package from
  non-root account); require rpm >= 2.4.99.

* Mon Mar  2 1998 ??? <root@pingviini.kortex.jyu.fi>
- first not commented release.
