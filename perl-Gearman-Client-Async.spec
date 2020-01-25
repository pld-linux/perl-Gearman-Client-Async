#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests		# do not perform "make test"

%define	pdir	Gearman
%define	pnam	Client-Async
Summary:	Gearman::Client::Async - Asynchronous client module for Gearman for Danga::Socket applications
Name:		perl-Gearman-Client-Async
Version:	0.94
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/B/BR/BRADFITZ/Gearman-Client-Async-%{version}.tar.gz
# Source0-md5:	71dcadfb434202dbdf4798f2ec93b32f
URL:		http://search.cpan.org/dist/Gearman-Client-Async/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with autodeps} || %{with tests}
BuildRequires:	perl-Danga-Socket >= 1.52
BuildRequires:	perl-Gearman >= 1.05
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Asynchronous client module for Gearman for Danga::Socket applications.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README.txt TODO
%{perl_vendorlib}/Gearman/Client/*.pm
%{perl_vendorlib}/Gearman/Client/Async
%{_mandir}/man3/*
