Summary:     GIMP - brushes, gradients, palettes and patterns
Summary(pl): GIMP - pisaki, gradienty, palety i wype³nienia
Name:        gimp-data-extras
Version:     1.0.0
Release:     1
Copyright:   GPL
Group:       X11/Applications/Graphics
Url:         http://www.gimp.org/
Source:      ftp://ftp.gimp.org/pub/gimp/0.99/latest/%{name}-%{version}.tar.bz2
Requires:    gimp
BuildRoot:   /tmp/%{name}-%{version}-root
BuildArchitectures: noarch
%description
This is the archive of data files for the Gimp.

Contains the latest brushes, gradients, palettes and patterns
by various authors around the internet.

%description -l pl
Pakiet ten zawiera archiwum dodatkowych plików danych dla programu Gimp.

Zawiera on pisaki, gradienty, palety i wype³nienia ró¿nych autorów.

%prep
%setup -q

%build

CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr
make

%install
rm -rf $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT/usr install

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644, root, root, 755)
%doc README
/usr/share/gimp/brushes/*
/usr/share/gimp/patterns/*

%changelog
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
