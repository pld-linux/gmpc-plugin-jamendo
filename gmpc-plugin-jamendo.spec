%define		source_name gmpc-jamendo
Summary:	Jamendo plugin for Gnome Music Player Client
Summary(pl.UTF-8):	Wtyczka udostępniająca dane z Jamendo dla odtwarzacza Gnome Music Player Client
Name:		gmpc-plugin-jamendo
Version:	0.18.0
Release:	0.1
License:	GPL v2+
Group:		X11/Applications/Sound
Source0:	http://dl.sourceforge.net/musicpd/%{source_name}-%{version}.tar.gz
# Source0-md5:	d77583b8952917336b8efb83752189ad
URL:		http://gmpc.wikia.com/wiki/GMPC_PLUGIN_JAMENDO
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	gmpc-devel >= 0.18.0
BuildRequires:	gob2 >= 2.0.10
BuildRequires:	gtk+2-devel >= 2:2.4
BuildRequires:	libglade2-devel
BuildRequires:	libmpd-devel >= 0.18.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	pkgconfig
BuildRequires:	sqlite3-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Browse and listen to music from Jamendo service.

%prep
%setup -q -n %{source_name}-%{version}

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
install -d $RPM_BUILD_ROOT%{_libdir}/gmpc

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%{_libdir}/gmpc/plugins/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gmpc/plugins/*.so
