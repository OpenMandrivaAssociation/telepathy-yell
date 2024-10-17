%define _disable_ld_no_undefined 1
%define develname %mklibname -d %name

Name:           telepathy-yell
Version:        0.0.4
Release:        1
Summary:        Temporary submodule to implement draft Call APIs

Group:          Networking/Instant messaging
License:        LGPLv2+
URL:            https://telepathy.freedesktop.org/wiki/
Source0:        http://telepathy.freedesktop.org/releases/%{name}/%{name}-%{version}.tar.gz

BuildRequires:  dbus-devel
BuildRequires:	dbus-glib-devel
BuildRequires:  libxslt-proc
BuildRequires:  python-devel
BuildRequires:  telepathy-glib-devel >= 0.14.3
BuildRequires:	libsoup-devel
BuildRequires:	nice-devel >= 0.0.11
BuildRequires:  libuuid-devel
Requires:	telepathy-filesystem

%description
Temporary submodule to implement draft Call APIs

#--------------------------------------------------------------------

%define libtelepathy_yell_major 0
%define libtelepathy_yell %mklibname telepathy-yell %{libtelepathy_yell_major}

%package -n %{libtelepathy_yell}
Summary:	Core %{name} library
Group:		System/Libraries

%description -n %{libtelepathy_yell}
Core %{name} library.

%files -n %{libtelepathy_yell}
%defattr(-,root,root)
%{_libdir}/libtelepathy-yell.so.%{libtelepathy_yell_major}*


#--------------------------------------------------------------------

%package -n %{develname}
Summary:	%{name} development files
Group:		Development/Other
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Requires:	%{libtelepathy_yell} = %{version}-%{release}

%description -n %{develname}
%{name} development files.

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/pkgconfig/*
%{_libdir}/*.so

#--------------------------------------------------------------------

%prep
%setup -q

%build
CFLAGS="%{optflags} -fPIC" %configure2_5x \
	--disable-static \
	--with-ca-certificates=%{_sysconfdir}/ssl/certs/ca-bundle.crt
%make

%install
%makeinstall_std

# don't ship .la
find %{buildroot} -name "*.la" -delete

rm -fr %{buildroot}%{_datadir}/doc/telepathy-yell/
