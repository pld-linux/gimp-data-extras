Summary:	GIMP - brushes, gradients, palettes and patterns
Summary(pl):	GIMP - pisaki, gradienty, palety i wype³nienia
Name:		gimp-data-extras
Version:	1.2.0
Release:	4
License:	GPL
Group:		X11/Applications/Graphics
Source0:	ftp://ftp.gimp.org/pub/gimp/v1.2/v%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	8c18380debbffb23bee9c8f787680b29
URL:		http://www.gimp.org/
BuildRequires:	autoconf
BuildRequires:	gimp-devel >= 1:%{version}
Requires:	gimp >= 1:%{version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_gimpdatadir	%(gimptool --gimpdatadir)

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
%{__autoconf}
%configure

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
        DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{_gimpdatadir}/brushes/*
%{_gimpdatadir}/patterns/*
