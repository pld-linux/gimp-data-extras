Summary:	GIMP - brushes, gradients, palettes and patterns
Summary(pl):	GIMP - pisaki, gradienty, palety i wype³nienia
Name:		gimp-data-extras
Version:	1.0.0
Release:	4
License:	GPL
Group:		X11/Applications/Graphics
Group(pl):	X11/Aplikacje/Grafika
Url:		http://www.gimp.org/
Source0:	ftp://ftp.gimp.org/pub/gimp/0.99/latest/%{name}-%{version}.tar.bz2
Requires:	gimp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Buildarch:	noarch

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
This is the archive of data files for the Gimp.

Contains the latest brushes, gradients, palettes and patterns by
various authors around the internet.

%description -l pl
Pakiet ten zawiera archiwum dodatkowych plików danych dla programu
Gimp. W pakiecie znajduj± siê miêdzy innymi: pisaki, gradienty, palety
i wype³nienia ró¿nych autorów.

%prep
%setup -q

%build
./configure --prefix=%{_prefix}
make

%install
rm -rf $RPM_BUILD_ROOT
%{__make} prefix=$RPM_BUILD_ROOT%{_prefix} install

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%doc *gz
%{_datadir}/gimp/brushes/*
%{_datadir}/gimp/patterns/*
