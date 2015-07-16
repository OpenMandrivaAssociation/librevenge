%define major 0
%define abi 0.0
%define devname %mklibname revenge -d

Name: librevenge
Version: 0.0.2
Release: 1
Source0: http://downloads.sourceforge.net/project/libwpd/librevenge/librevenge-%{version}/librevenge-%{version}.tar.xz
Summary: Base library for writing document import filters
URL: http://sf.net/p/libwpd/wiki/librevenge/
License: LGPLv2.1/MPL
Group: System/Libraries
BuildRequires: pkgconfig(cppunit)
BuildRequires: pkgconfig(zlib)
BuildRequires: boost-devel
BuildRequires: doxygen

%libpackage revenge %{abi} %{major}
%libpackage revenge-generators %{abi} %{major}
%libpackage revenge-stream %{abi} %{major}

%define libname %mklibname revenge %{abi} %{major}
%define glibname %mklibname revenge-generators %{abi} %{major}
%define slibname %mklibname revenge-stream %{abi} %{major}

%description
librevenge is a base library for writing document import filters.
It has interfaces for text documents, vector graphics, spreadsheets
and presentations.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}
Requires: %{glibname} = %{EVRD}
Requires: %{slibname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

librevenge is a base library for writing document import filters.
It has interfaces for text documents, vector graphics, spreadsheets
and presentations.

%package doc
Summary: Documentation for %{name}
Group: Development/C

%description doc
Documentation for %{name}.

librevenge is a base library for writing document import filters.
It has interfaces for text documents, vector graphics, spreadsheets
and presentations.

%prep
%setup -q
%configure

%build
%make

%install
%makeinstall_std

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

%files doc
%{_docdir}/%{name}
