%define		_pre	pre3
Summary:	Configure and monitor Wireless Access Points
Summary(pl):	Konfiguracja i monitoring punktów dostêpu bezprzewodowego (Access Points)
Name:		ap-utils
Version:	1.3.2
Release:	0.%{_pre}.1
License:	GPL
Group:		Networking/Utilities
Source0:	http://dl.sourceforge.net/ap-utils/%{name}-%{version}-%{_pre}.tar.bz2
# Source0-md5:	64a4290526de86746bc94b35b89c53c4
URL:		http://ap-utils.polesye.net/
BuildRequires:	libtool
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Configure and monitor Wireless Access Points.

%description -l pl
Konfiguracja i monitoring punktów dostêpu (Access Points) dla sieci
bezprzewodowych.

%prep
%setup -q -n %{name}-%{version}-%{_pre}

%build
%{__libtoolize}
%configure2_13
%{__make} CC="%{__cc} -I/usr/include/ncurses"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%doc Documentation/FAQ Documentation/*.html
%lang(uk) %doc Documentation/Ukrainian/*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/*
