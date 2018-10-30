%define	modname	String-CRC32
%define upstream_version 1.5

Summary:	Perl interface for cyclic redundency check generation
Name:		perl-%{modname}
Version:	%perl_convert_version %{upstream_version}
Release:	10
License:	GPLv2 or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/String/String-CRC32-%{upstream_version}.tar.gz
Buildrequires:	perl-devel

%description 
This packages provides a perl modname to generate checksums from strings
and from files.

%prep
%setup -qn %{modname}-%{upstream_version}

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


