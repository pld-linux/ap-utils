Summary:	Configure and monitor Wireless Access Points
Summary(pl):	Konfiguracja i monitoring punktów dostêpu bezprzewodowego (Access Points)
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
Konfiguracja i monitoring punktów dostêpu (Access Points) dla sieci
bezprzewodowych.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%doc Documentation/FAQ Documentation/*.html
%lang(uk) %doc Documentation/Ukrainian/*
%{_bindir}/*
%{_sbindir}/*
%{_mandir}/man8/*
