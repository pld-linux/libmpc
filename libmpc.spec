Summary:	Complex floating-point library with high precision and exact rounding
Summary(pl.UTF-8):	Biblioteka do obliczeń na liczbach zespolonych z wielokrotną precyzją i poprawnym zaokrąglaniem
Name:		libmpc
Version:	1.0.3
Release:	1
License:	LGPL v3+
Group:		Libraries
#Source0Download: http://www.multiprecision.org/index.php?prog=mpc&page=download
Source0:	http://multiprecision.org/mpc/download/mpc-%{version}.tar.gz
# Source0-md5:	d6a1d5f8ddea3abd2cc3e98f58352d26
URL:		http://multiprecision.org/
BuildRequires:	gmp-devel >= 4.3.2
BuildRequires:	mpfr-devel >= 2.4.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The MPC library is a C library for the arithmetic of complex numbers
with arbitrarily high precision and correct rounding of the result. It
is built upon and follows the same principles as MPFR.

%description -l pl.UTF-8
Biblioteka MPC to biblioteka C do obliczeń na liczbach zespolonych z
wielokrotną precyzją i poprawnym zaokrąglaniem wyników. Zbudowana jest
na tych samych założeniach co biblioteka MPFR.

%package devel
Summary:	Header files for MPC library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki MPC
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gmp-devel >= 4.3.2
Requires:	mpfr-devel >= 2.4.2

%description devel
Header files for MPC library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki MPC.

%package static
Summary:	Static MPC library
Summary(pl.UTF-8):	Statyczna biblioteka MPC
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static MPC library.

%description static -l pl.UTF-8
Statyczna biblioteka MPC.

%prep
%setup -q -n mpc-%{version}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_libdir}/libmpc.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmpc.so.3

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmpc.so
%{_libdir}/libmpc.la
%{_includedir}/mpc.h
%{_infodir}/mpc.info*

%files static
%defattr(644,root,root,755)
%{_libdir}/libmpc.a
