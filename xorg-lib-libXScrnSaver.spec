Summary:	XScrnSaver library
Summary(pl):	Biblioteka XScrnSaver
Name:		xorg-lib-libXScrnSaver
Version:	0.99.1
Release:	0.1
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/lib/libXScrnSaver-%{version}.tar.bz2
# Source0-md5:	706379f7c1105a2edd0a092c3ef40fa8
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 0.19
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-proto-scrnsaverproto-devel
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XScrnSaver library.

%description -l pl
Biblioteka XScrnSaver.

%package devel
Summary:	Header files libXScrnSaver development
Summary(pl):	Pliki nagłówkowe do biblioteki libXScrnSaver
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libXext-devel
Requires:	xorg-proto-scrnsaverproto-devel

%description devel
XScrnSaver library.

This package contains the header files needed to develop programs that
use these libXScrnSaver.

%description devel -l pl
Biblioteka XScrnSaver.

Pakiet zawiera pliki nagłówkowe niezbędne do kompilowania programów
używających biblioteki libXScrnSaver.

%package static
Summary:	Static libXScrnSaver library
Summary(pl):	Biblioteka statyczna libXScrnSaver
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
XScrnSaver library.

This package contains the static libXScrnSaver library.

%description static -l pl
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
%doc ChangeLog
%attr(755,root,root) %{_libdir}/libXss.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXss.so
%{_libdir}/libXss.la
%{_pkgconfigdir}/xscrnsaver.pc
%{_mandir}/man3/*.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libXss.a
