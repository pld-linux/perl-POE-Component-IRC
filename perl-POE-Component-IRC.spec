#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	POE
%define		pnam	Component-IRC
Summary:	POE::Component::IRC - a fully event-driven IRC client module
Summary(pl):	POE::Component::IRC - modu³ w pe³ni sterowanego zdarzeniami klienta IRC
Name:		perl-POE-Component-IRC
Version:	5.11
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	624c4f967479a9a51599b39da89251ca
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-POE >= 0.06_07
BuildRequires:	perl-POE-Component-Client-DNS >= 1:0.99
BuildRequires:	perl-POE-Filter-IRCD
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
POE::Component::IRC is a POE component (who'd have guessed?) which
acts as an easily controllable IRC client for your other POE
components and sessions. You create an IRC component and tell it what
events your session cares about and where to connect to, and it sends
back interesting IRC events when they happen. You make the client do
things by sending it events. That's all there is to it. Cool, no?

%description -l pl
POE::Component::IRC to komponent POE (któ¿by zgad³?), który
funkcjonuje jako ³atwo sterowalny klient IRC dla innych komponentów i
sesji POE. Tworzy siê komponent IRC i mówi mu, którymi zdarzeniami
zajmuje siê sesja oraz gdzie ma siê po³±czyæ, a on wysy³a z powrotem
interesuj±ce zdarzenia IRC, kiedy wyst±pi±. Poprzez wysy³anie zdarzeñ
powoduje siê, ¿e klient wykonuje ró¿ne rzeczy. To wszystko, co trzeba
zrobiæ. Fajnie, nie?

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

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
%doc Changes README docs/*
%{perl_vendorlib}/POE/Component/IRC.pm
%dir %{perl_vendorlib}/POE/Component/IRC
%{perl_vendorlib}/POE/Component/IRC/*.pm
%dir %{perl_vendorlib}/POE/Component/IRC/Plugin
%{perl_vendorlib}/POE/Component/IRC/Plugin/*.pm
%dir %{perl_vendorlib}/POE/Component/IRC/Qnet
%{perl_vendorlib}/POE/Component/IRC/Qnet/*.pm
%dir %{perl_vendorlib}/POE/Component/IRC/Test
%{perl_vendorlib}/POE/Component/IRC/Test/*.pm
%{perl_vendorlib}/POE/Filter/IRC.pm
%{perl_vendorlib}/POE/Filter/CTCP.pm
%dir %{perl_vendorlib}/POE/Filter/IRC
%{perl_vendorlib}/POE/Filter/IRC/Compat.pm

%attr(755,root,root) %{_examplesdir}/%{name}-%{version}
%{_mandir}/man3/*
