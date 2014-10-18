Summary:	Web content rendering for the GNOME Platform
Name:		gtk+3-webkit2
Version:	2.6.1
Release:	1
License:	BSD-like
Group:		X11/Libraries
Source0:	http://webkitgtk.org/releases/webkitgtk-%{version}.tar.xz
# Source0-md5:	adf4a5b1cafa85b6c341341989549559
URL:		http://www.webkitgtk.org/
BuildRequires:	EGL-devel
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	bison
BuildRequires:	cmake
BuildRequires:	curl-devel
BuildRequires:	enchant-devel
BuildRequires:	flex
BuildRequires:	fontconfig-devel
BuildRequires:	geoclue2-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	gperf
BuildRequires:	gstreamer-plugins-base-devel
BuildRequires:	gtk+-devel
BuildRequires:	gtk+3-devel
BuildRequires:	icu-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	librsvg-devel
BuildRequires:	libsecret-devel
BuildRequires:	libsoup-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	libwebp-devel
BuildRequires:	libxslt-devel
BuildRequires:	pkg-config
BuildRequires:	ruby
BuildRequires:	sqlite3-devel
BuildRequires:	xorg-libXft-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	    %{_libdir}/webkit2gtk-4.0

# unresolved, not sure how bad is it
#   _ZSt11__once_call
#   _ZSt15__once_callable
%define		skip_post_check_so  libwebkit2gtk-4.0.so.* libjavascriptcoregtk-4.0.so.*

%description
Web content rendering for the GNOME Platform.

%package devel
Summary:	Development files for webkit
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Development files for webkit.

%package apidocs
Summary:	WebKitGTK API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
WebKitGTK API documentation.

%package demo
Summary:	Demo GTK+/webkit application
Group:		Applications
Requires:	%{name} = %{version}-%{release}

%description demo
Simple GTK+/webkit based browser.

%prep
%setup -qn webkitgtk-%{version}

%build
install -d build
cd build
%cmake .. \
    -DPORT=GTK	\
    -DLIBEXEC_INSTALL_DIR=%{_libexecdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang WebKit2GTK-4.0

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files -f WebKit2GTK-4.0.lang
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libjavascriptcoregtk-4.0.so.18
%attr(755,root,root) %ghost %{_libdir}/libwebkit2gtk-4.0.so.37
%attr(755,root,root) %{_libdir}/libjavascriptcoregtk-4.0.so.*.*.*
%attr(755,root,root) %{_libdir}/libwebkit2gtk-4.0.so.*.*.*
%{_libdir}/girepository-1.0/*.typelib

%dir %{_libexecdir}
%dir %{_libexecdir}/injected-bundle
%attr(755,root,root) %{_libexecdir}/WebKitNetworkProcess
%attr(755,root,root) %{_libexecdir}/WebKitPluginProcess
%attr(755,root,root) %{_libexecdir}/WebKitPluginProcess2
%attr(755,root,root) %{_libexecdir}/WebKitWebProcess
%attr(755,root,root) %{_libexecdir}/injected-bundle/libwebkit2gtkinjectedbundle.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/jsc
%attr(755,root,root) %{_libdir}/*.so
%{_includedir}/webkitgtk-4.0
%{_pkgconfigdir}/*.pc
%{_datadir}/gir-1.0/*.gir
%if 0
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/webkit2gtk
%{_gtkdocdir}/webkitdomgtk
%{_gtkdocdir}/webkitgtk
%endif

