%define		source_name gmpc-jamendo
Summary:	Jamendo plugin for Gnome Music Player Client
Summary(pl.UTF-8):	Wtyczka udostępniająca dane z Jamendo dla odtwarzacza Gnome Music Player Client
Name:		gmpc-plugin-jamendo
Version:	11.8.16
Release:	3
License:	GPL v2+
Group:		X11/Applications/Sound
Source0:	https://download.sarine.nl/Programs/gmpc/%{version}/%{source_name}-%{version}.tar.gz
# Source0-md5:	7395074612fd7e1eec00427b65c9f188
URL:		https://gmpc.fandom.com/wiki/GMPC_PLUGIN_JAMENDO
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1.6
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.4
BuildRequires:	gmpc-devel >= 0.20.3
BuildRequires:	gob2 >= 2.0.10
BuildRequires:	gtk+2-devel >= 2:2.4
BuildRequires:	intltool >= 0.21
BuildRequires:	libmpd-devel >= 0.19.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.6
BuildRequires:	pkgconfig
BuildRequires:	sqlite3-devel >= 3
BuildRequires:	zlib-devel
Requires:	glib2 >= 1:2.4
Requires:	gmpc >= 0.20.3
Requires:	gtk+2 >= 2:2.4
Requires:	libmpd >= 0.19.0
Requires:	libxml2 >= 2.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Browse and listen to music from Jamendo service.

%description -l pl.UTF-8
Przeglądanie i słuchanie muzyki z usługi Jamendo.

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

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/gmpc/plugins/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gmpc/plugins/jamendoplugin.so
%{_datadir}/gmpc/plugins/jamendo
