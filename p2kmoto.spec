#
%define	_snap	20060321
Summary:	The moto4lin software is intended to be used with Motorola telephones based on the P2K platform
Name:		p2kmoto
Version:	0.1
Release:	0.%{_snap}.1
License:	GPL
Group:		Applications
Source0:	%{name}-CVS-%{_snap}.tar.gz
# Source0-md5:	7db9c27c61626522bf35f034cb31c277
# See also http://sourceforge.net/projects/moto4lin/
URL:		http://moto4lin.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	libusb-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The moto4lin software is intended to be used with Motorola telephones
based on the P2K platform.

%package libs
Summary:	Libraries for p2kmoto
Summary(pl):	Biblioteki dla p2kmoto
Group:		Libraries

%description libs


%package devel
Summary:	Header files for p2kmoto library
Summary(pl):	Pliki nag³ówkowe biblioteki p2kmoto
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
This is the package containing the header files for p2kmoto library.

%description devel -l pl
Ten pakiet zawiera pliki nag³ówkowe biblioteki p2kmoto.

%package static
Summary:	Static p2kmoto library
Summary(pl):	Statyczna biblioteka p2kmoto
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static p2kmoto library.

%description static -l pl
Statyczna biblioteka p2kmoto

%prep
%setup -q -n %{name}

%build
# if ac/am/* rebuilding is necessary, do it in this order and add
# appropriate BuildRequires
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
cp -f /usr/share/automake/config.sub .
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_bindir}/p2ktest

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%{_libdir}/lib*.la
%{_libdir}/lib*.so
%{_includedir}/p2kmoto.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
