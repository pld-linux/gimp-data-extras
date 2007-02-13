Summary:	GIMP - extra brushes and patterns
Summary(pl.UTF-8):	GIMP - dodatkowe pisaki i wypełnienia
Name:		gimp-data-extras
Version:	2.0.1
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	ftp://ftp.gimp.org/pub/gimp/extras/%{name}-%{version}.tar.bz2
# Source0-md5:	17823c4f28ad94bdcbe0233aba3bda16
URL:		http://www.gimp.org/
BuildRequires:	gimp-devel >= 1:2.0
Requires:	gimp >= 1:2.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_gimpdatadir	%(gimptool --gimpdatadir)

%description
This is a collection of additional data files for The GIMP 2. It adds
a couple of brushes and patterns to the set of files that are already
shipped with the GIMP tarball.

%description -l pl.UTF-8
Pakiet ten zawiera zbiór dodatkowych plików danych dla GIMP-a 2.
Dodaje trochę pisaków i wypełnień do zbioru plików załączonych do
pakietu z GIMP-em.

%prep
%setup -q

%build
%configure

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
        DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_gimpdatadir}/brushes/*
%{_gimpdatadir}/patterns/*
