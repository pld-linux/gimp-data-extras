Summary:	GIMP - brushes, gradients, palettes and patterns
Summary(pl):	GIMP - pisaki, gradienty, palety i wype³nienia
Name:		gimp-data-extras
Version:	1.0.0
Release:	4
Copyright:	GPL
Group:		X11/Applications/Graphics
Group(pl):	X11/Aplikacje/Grafika
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
