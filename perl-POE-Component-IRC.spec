#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	POE
%define	pnam	Component-IRC
Summary:	POE::Component::IRC - a fully event-driven IRC client module
Summary(pl):	POE::Component::IRC - modu³ w pe³ni sterowanego zdarzeniami klienta IRC
Name:		perl-POE-Component-IRC
Version:	2.9
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f35b9b619991ac3eae7dacda06455d31
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-POE >= 0.06_07
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
mkdir -p lib/POE/{Component,Filter}
mv Filter-CTCP.pm lib/POE/Filter/CTCP.pm
mv Filter-IRC.pm  lib/POE/Filter/IRC.pm
mv IRC.pm         lib/POE/Component/IRC.pm

%build
%{__perl} -MExtUtils::MakeMaker -e 'WriteMakefile(NAME=>"POE::Component::IRC")' \
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
%doc Changes README
%{perl_vendorlib}/%{pdir}/*/*.pm
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}
%{_mandir}/man3/*
