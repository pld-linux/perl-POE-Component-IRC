#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	POE
%define	pnam	Component-IRC
Summary:	POE::Component::IRC - a fully event-driven IRC client module.
#Summary(pl):	
Name:		perl-POE-Component-IRC
Version:	2.9
Release:	1
# same as perl
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{!?_without_tests:1}0
BuildRequires:	perl-POE >= 0.06_07
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
POE::Component::IRC is a POE component (who'd have guessed?) which acts
as an easily controllable IRC client for your other POE components and
sessions. You create an IRC component and tell it what events your session
cares about and where to connect to, and it sends back interesting IRC
events when they happen. You make the client do things by sending it
events. That's all there is to it. Cool, no?

# %description -l pl
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
mkdir -p lib/POE/{Component,Filter}
mv Filter-CTCP.pm lib/POE/Filter/CTCP.pm
mv Filter-IRC.pm  lib/POE/Filter/IRC.pm
mv IRC.pm         lib/POE/Component/IRC.pm

%build
%{__perl} -MExtUtils::MakeMaker -e 'WriteMakefile(NAME=>"POE::Component::IRC")' \
	INSTALLDIRS=vendor
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}
cp -r examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/%{pdir}/*/*.pm
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}
%{_mandir}/man3/*
