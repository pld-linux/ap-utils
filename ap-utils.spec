Summary:	Configure and monitor Wireless Access Points
Summary(pl):	Konfiguracja i monitoring punkt�w dost�pu bezprzewodowego (Access Points)
Name:		ap-utils
Version:	1.3.1
Release:	1
License:	GPL
Group:		Networking/Utilities
Source0:	http://dl.sourceforge.net/ap-utils/%{name}-%{version}.tar.bz2
URL:		http://ap-utils.polesye.net/
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Configure and monitor Wireless Access Points.

%description -l pl
Konfiguracja i monitoring punkt�w dost�pu (Access Points) dla sieci
bezprzewodowych.

%prep
%setup -q

%build
%{__libtoolize}
%configure2_13
%{__make} CC="gcc -I/usr/include/ncurses"

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
%attr(755,root,root)%{_bindir}/*
%attr(755,root,root)%{_sbindir}/*
%{_mandir}/man8/*
