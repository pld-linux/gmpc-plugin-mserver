%define		source_name gmpc-mserver
Summary:	Mserver plugin for Gnome Music Player Client
Summary(pl.UTF-8):	Wtyczka mserver dla odtwarzacza Gnome Music Player Client
Name:		gmpc-plugin-mserver
Version:	0.20.0
Release:	2
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://downloads.sourceforge.net/musicpd/%{source_name}-%{version}.tar.gz
# Source0-md5:	850de96a29e68df646110894b95cf188
URL:		http://gmpc.wikia.com/wiki/GMPC_PLUGIN_MSERVER
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel >= 2.4
BuildRequires:	gmpc-devel >= 0.19.0
BuildRequires:	gtk+2-devel >= 2:2.4
BuildRequires:	intltool >= 0.21
BuildRequires:	libmicrohttpd-devel
BuildRequires:	libmpd-devel >= 0.19.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	pkgconfig
BuildRequires:	taglib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This Plugin lets you stream music files to your mpd that are not in
your database.

%prep
%setup -qn %{source_name}-%{version}

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
%dir %{_datadir}/gmpc/plugins/gmpc-mserver
%{_datadir}/gmpc/plugins/gmpc-mserver/gmpc-mserver.png
