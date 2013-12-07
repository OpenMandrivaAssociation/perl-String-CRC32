%define	modname	String-CRC32

Summary:	Perl interface for cyclic redundency check generation
Name:		perl-%{modname}
Version:	1.4
Release:	18
License:	GPLv2 or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	ftp://ftp.perl.org/pub/CPAN/modnames/by-modname/String/%{modname}-%{version}.tar.bz2
Buildrequires:	perl-devel

%description 
This packages provides a perl modname to generate checksums from strings
and from files.

%prep
%setup -qn %{modname}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README
%{perl_vendorarch}/String
%{perl_vendorarch}/auto/String
%{_mandir}/man3/*

