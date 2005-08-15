# $Rev: 3270 $, $Date: 2005-08-15 12:17:57 $
#
Summary:	XScrnSaver library
Summary(pl):	Biblioteka XScrnSaver
Name:		xorg-lib-libXScrnSaver
Version:	0.99.0
Release:	0.03
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/lib/libXScrnSaver-%{version}.tar.bz2
# Source0-md5:	fee23bc4e3fc7617bdaf8ca89052ab6a
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	xorg-proto-scrnsaverproto-devel
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/libXScrnSaver-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
XScrnSaver library.

%description -l pl
Biblioteka XScrnSaver.


%package devel
Summary:	Header files libXScrnSaver development
Summary(pl):	Pliki nag³ówkowe do biblioteki libXScrnSaver
Group:		X11/Development/Libraries
Requires:	xorg-lib-libXScrnSaver = %{version}-%{release}
Requires:	xorg-lib-libXext-devel
Requires:	xorg-proto-scrnsaverproto-devel

%description devel
XScrnSaver library.

This package contains the header files needed to develop programs that
use these libXScrnSaver.

%description devel -l pl
Biblioteka XScrnSaver.

Pakiet zawiera pliki nag³ówkowe niezbêdne do kompilowania programów
u¿ywaj±cych biblioteki libXScrnSaver.


%package static
Summary:	Static libXScrnSaver libraries
Summary(pl):	Biblioteki statyczne libXScrnSaver
Group:		Development/Libraries
Requires:	xorg-lib-libXScrnSaver-devel = %{version}-%{release}

%description static
XScrnSaver library.

This package contains the static libXScrnSaver library.

%description static -l pl
Biblioteka XScrnSaver.

Pakiet zawiera statyczn± bibliotekê libXScrnSaver.


%prep
%setup -q -n libXScrnSaver-%{version}


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
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}


%clean
rm -rf $RPM_BUILD_ROOT


%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,wheel) %{_libdir}/libXScrnSaver.so.*


%files devel
%defattr(644,root,root,755)
%{_libdir}/libXScrnSaver.la
%attr(755,root,wheel) %{_libdir}/libXScrnSaver.so
%{_pkgconfigdir}/xscrnsaver.pc
%{_mandir}/man3/*.3*


%files static
%defattr(644,root,root,755)
%{_libdir}/libXScrnSaver.a
