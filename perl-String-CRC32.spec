%define module  String-CRC32
%define name	perl-%{module}
%define version 1.4
%define release 15

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Perl interface for cyclic redundency check generation
License:	GPL or Artistic
Group:		Development/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/String/%{module}-%{version}.tar.bz2
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
make test

%install
%makeinstall_std

%files
%doc README
%{_mandir}/*/*
%{perl_vendorarch}/String
%{perl_vendorarch}/auto/String



%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.4-13mdv2012.0
+ Revision: 765658
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.4-12
+ Revision: 764169
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.4-11
+ Revision: 667312
- mass rebuild

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 1.4-10mdv2011.0
+ Revision: 564581
- rebuild for perl 5.12.1

* Tue Jul 20 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.4-9mdv2011.0
+ Revision: 555290
- rebuild

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.4-8mdv2010.1
+ Revision: 426590
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.4-7mdv2009.1
+ Revision: 351737
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.4-6mdv2009.1
+ Revision: 351725
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.4-5mdv2009.0
+ Revision: 224057
- rebuild

* Mon Jan 14 2008 Pixel <pixel@mandriva.com> 1.4-4mdv2008.1
+ Revision: 151364
- rebuild for perl-5.10.0

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Aug 17 2007 Thierry Vignaud <tv@mandriva.org> 1.4-3mdv2008.0
+ Revision: 64826
- rebuild

* Sat May 05 2007 Olivier Thauvin <nanardon@mandriva.org> 1.4-2mdv2008.0
+ Revision: 23318
- rebuild


* Sat Apr 22 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.4-1mdk
- New release 1.4
- optimisations
- better source URL
- %%mkrel

* Mon Apr 25 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.3-1mdk
- New release 1.3
- spec cleanup
- better url

* Mon Nov 15 2004 Michael Scherer <misc@mandrake.org> 1.2-3mdk
- Rebuild for new perl

* Fri Jul 23 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.2-2mdk 
- rpmbuildupdate aware

* Wed Sep 17 2003 Guillaume Rousse <guillomovitch@linux-mandrake.com> 1.2-1mdk
- 1.2

