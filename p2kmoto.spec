#
%define	_snap	20060321
Summary:	Software intended to be used with Motorola telephones based on the P2K platform
Summary(pl.UTF-8):   Oprogramowanie do używania z telefonami Motorola opartymi na platformie P2K
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

%description -l pl.UTF-8
Oprogramowanie moto4lin jest przeznaczone do używania z telefonami
Motorola opartymi na platformie P2K.

%package libs
Summary:	Libraries for p2kmoto
Summary(pl.UTF-8):   Biblioteki dla p2kmoto
Group:		Libraries

%description libs
Libraries for p2kmoto.

%description libs -l pl.UTF-8
Biblioteki dla p2kmoto.

%package devel
Summary:	Header files for p2kmoto library
Summary(pl.UTF-8):   Pliki nagłówkowe biblioteki p2kmoto
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
This is the package containing the header files for p2kmoto library.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe biblioteki p2kmoto.

%package static
Summary:	Static p2kmoto library
Summary(pl.UTF-8):   Statyczna biblioteka p2kmoto
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static p2kmoto library.

%description static -l pl.UTF-8
Statyczna biblioteka p2kmoto

%prep
%setup -q -n %{name}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
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
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/p2kmoto.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
