Summary:	GIMP - brushes, gradients, palettes and patterns
Summary(pl):	GIMP - pisaki, gradienty, palety i wype³nienia
Name:		gimp-data-extras
Version:	1.2.0
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Group(pl):	X11/Aplikacje/Grafika
Url:		http://www.gimp.org/
Source0:	ftp://ftp.gimp.org/pub/gimp/v1.2/v%{version}/%{name}-%{version}.tar.bz2
BuildRequires:	gimp-devel >= %{version}
Requires:	gimp >= %{version}
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
%configure  --prefix=%{_prefix}
#./configure --prefix=%{_prefix}
# %{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
        DESTDIR=$RPM_BUILD_ROOT \
        m4datadir=%{_aclocaldir}

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%doc *gz
%{_datadir}/gimp/1.2/brushes/*
%{_datadir}/gimp/1.2/patterns/*
