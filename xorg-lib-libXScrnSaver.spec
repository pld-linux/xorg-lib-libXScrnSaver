Summary:	XScrnSaver library
Summary(pl.UTF-8):	Biblioteka XScrnSaver
Name:		xorg-lib-libXScrnSaver
Version:	1.1.3
Release:	1
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXScrnSaver-%{version}.tar.bz2
# Source0-md5:	93f84b6797f2f29cae1ce23b0355d00d
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-proto-scrnsaverproto-devel >= 1.1
BuildRequires:	xorg-proto-xextproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XScrnSaver library.

%description -l pl.UTF-8
Biblioteka XScrnSaver.

%package devel
Summary:	Header files for libXScrnSaver library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libXScrnSaver
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libXext-devel
Requires:	xorg-proto-scrnsaverproto-devel >= 1.1

%description devel
XScrnSaver library.

This package contains the header files needed to develop programs that
use libXScrnSaver.

%description devel -l pl.UTF-8
Biblioteka XScrnSaver.

Pakiet zawiera pliki nagłówkowe niezbędne do kompilowania programów
używających biblioteki libXScrnSaver.

%package static
Summary:	Static libXScrnSaver library
Summary(pl.UTF-8):	Biblioteka statyczna libXScrnSaver
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
XScrnSaver library.

This package contains the static libXScrnSaver library.

%description static -l pl.UTF-8
Biblioteka XScrnSaver.

Pakiet zawiera statyczną bibliotekę libXScrnSaver.

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
%doc COPYING ChangeLog
%attr(755,root,root) %{_libdir}/libXss.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXss.so
%{_libdir}/libXss.la
%{_pkgconfigdir}/xscrnsaver.pc
%{_mandir}/man3/*.3x*

%files static
%defattr(644,root,root,755)
%{_libdir}/libXss.a
