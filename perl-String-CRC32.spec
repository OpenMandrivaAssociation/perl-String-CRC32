%undefine _debugsource_packages
%define modname String-CRC32

Summary:	Perl interface for cyclic redundency check generation
Name:		perl-%{modname}
Version:	2.100
Release:	1
License:	GPLv2 or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/String/%{modname}-%{version}.tar.gz
Buildrequires:	perl-devel

%description 
This packages provides a perl modname to generate checksums from strings
and from files.

%prep
%autosetup -p1 -n %{modname}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%make_install

%files
%{perl_vendorarch}/String
%{perl_vendorarch}/auto/String
%doc %{_mandir}/man3/*
