Summary:	Configure and monitor Wireless Access Points
Summary(pl):	Konfiguracja i monitoring Access Pointów
Name:		ap-utils
Version:	1.3.1
Release:	1
License:	GPL
Group:		Networking/Utilities
Source0:	http://prdownloads.sourceforge.net/ap-utils/%{name}-%{version}.tar.bz2
URL:		http://ap-utils.polesye.net/
BuildRequires:	ncurses-devel

%description
Configure and monitor Wireless Access Points

%description -l pl
Konfiguracja i monitoring Access Pointów

%prep
%setup -q

%build
%configure
%make

%install %clean rm -rf ${RPM_BUILD_ROOT}

rm -rf $RPM_BUILD_ROOT
%files
%defattr(644,root,root,755)
%doc AUTHORS INSTALL NEWS COPYING README TODO ChangeLog
%doc Documentation/FAQ Documentation/*.html Documentation/uk/*
%_bindir/*
%_sbindir/*
%_mandir/man8/*


%clean
rm -rf $RPM_BUILD_ROOT
