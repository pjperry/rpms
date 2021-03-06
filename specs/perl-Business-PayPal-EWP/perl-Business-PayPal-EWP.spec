# $Id$
# Authority: dag
# Upstream: Thomas Busch <tbusch@cpan.org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Business-PayPal-EWP

Summary: Perl extension for PayPal's Encrypted Website Payments
Name: perl-Business-PayPal-EWP
Version: 1.02
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Business-PayPal-EWP/

Source: http://search.cpan.org/CPAN/authors/id/T/TB/TBUSCH/Business-PayPal-EWP-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc
BuildRequires: openssl-devel
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More)
Requires: openssl

%description
Perl extension for PayPal's Encrypted Website Payments.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL /usr -- INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST MANIFEST.SKIP META.yml README SIGNATURE
%doc %{_mandir}/man3/Business::PayPal::EWP.3pm*
%dir %{perl_vendorarch}/auto/Business/
%dir %{perl_vendorarch}/auto/Business/PayPal/
%{perl_vendorarch}/auto/Business/PayPal/EWP/
%dir %{perl_vendorarch}/Business/
%dir %{perl_vendorarch}/Business/PayPal/
%{perl_vendorarch}/Business/PayPal/EWP.pm

%changelog
* Sat Feb  6 2010 Christoph Maser <cmr@financial.com> - 1.02-1
- Updated to version 1.02.

* Tue Jan  5 2010 Christoph Maser <cmr@financial.com> - 1.01-1
- Updated to version 1.01.

* Tue Aug 19 2008 Dag Wieers <dag@wieers.com> - 1.00-1
- Initial package. (using DAR)
