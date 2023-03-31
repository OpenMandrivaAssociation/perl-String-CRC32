# Work around incomplete debug packages
%global _empty_manifest_terminate_build 0

%define modname String-CRC32
%define upstream_version 1.5

Summary:	Perl interface for cyclic redundency check generation
Name:		perl-%{modname}
Version:	%perl_convert_version %{upstream_version}
Release:	2
License:	GPLv2 or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/String/String-CRC32-%{upstream_version}.tar.gz
Buildrequires:	perl-devel

%description 
This packages provides a perl modname to generate checksums from strings
and from files.

%prep
%autosetup -n %{modname}-%{upstream_version} -p1

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%make_install

%files
%doc README
%{perl_vendorarch}/String
%{perl_vendorarch}/auto/String
%doc %{_mandir}/man3/*
