Summary:	XScrnSaver (X11 Screen Saver) extension client library
Summary(pl.UTF-8):	Biblioteka kliencka rozszerzenia XScrnSaver (X11 Screen Saver)
Name:		xorg-lib-libXScrnSaver
Version:	1.2.4
Release:	1
License:	MIT
Group:		X11/Libraries
Source0:	https://xorg.freedesktop.org/releases/individual/lib/libXScrnSaver-%{version}.tar.xz
# Source0-md5:	e613751d38e13aa0d0fd8e0149cec057
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-proto-scrnsaverproto-devel >= 1.2
BuildRequires:	xorg-proto-xextproto-devel
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XScrnSaver (X11 Screen Saver) extension client library.

%description -l pl.UTF-8
Biblioteka kliencka rozszerzenia XScrnSaver (X11 Screen Saver).

%package devel
Summary:	Header files for libXScrnSaver library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libXScrnSaver
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libX11-devel
Requires:	xorg-lib-libXext-devel
Requires:	xorg-proto-scrnsaverproto-devel >= 1.2

%description devel
XScrnSaver (X11 Screen Saver) extension client library.

This package contains the header files needed to develop programs that
use libXScrnSaver.

%description devel -l pl.UTF-8
Biblioteka kliencka rozszerzenia XScrnSaver (X11 Screen Saver).

Pakiet zawiera pliki nagłówkowe niezbędne do kompilowania programów
używających biblioteki libXScrnSaver.

%package static
Summary:	Static libXScrnSaver library
Summary(pl.UTF-8):	Biblioteka statyczna libXScrnSaver
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
XScrnSaver (X11 Screen Saver) extension client library.

This package contains the static libXScrnSaver library.

%description static -l pl.UTF-8
Biblioteka kliencka rozszerzenia XScrnSaver (X11 Screen Saver).

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
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libXss.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README.md
%attr(755,root,root) %{_libdir}/libXss.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libXss.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXss.so
%{_includedir}/X11/extensions/scrnsaver.h
%{_pkgconfigdir}/xscrnsaver.pc
%{_mandir}/man3/XScreenSaver*.3*
%{_mandir}/man3/Xss.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libXss.a
