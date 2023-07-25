# Work around incomplete debug packages
%global _empty_manifest_terminate_build 0

%define modname String-CRC32

Summary:	Perl interface for cyclic redundency check generation
Name:		perl-%{modname}
Version:	2.100
Release:	1
License:	GPLv2 or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/String/%{modname}-%{version}.tar.gz
Buildrequires:	perl-devel

%description 
This packages provides a perl modname to generate checksums from strings
and from files.

%prep
%autosetup -p1 -n %{modname}-%{version}
perl Makefile.PL INSTALLDIRS=vendor

%build
%make_build

%check
make test

%install
%make_install

%files
%doc Changes LICENSE README
%{perl_vendorarch}/String
%{perl_vendorarch}/auto/String
%{_mandir}/man3/*
