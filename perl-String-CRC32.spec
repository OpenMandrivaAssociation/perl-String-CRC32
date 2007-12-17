%define module  String-CRC32
%define name	perl-%{module}
%define version 1.4
%define release %mkrel 3

Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Summary: 	Perl interface for cyclic redundency check generation
License: 	GPL or Artistic
Group: 		Development/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/String/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}
Buildrequires:	perl-devel

%description 
This packages provides a perl module to generate checksums from strings
and from files.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make CFLAGS="%{optflags}"

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{_mandir}/*/*
%{perl_vendorarch}/String
%{perl_vendorarch}/auto/String

