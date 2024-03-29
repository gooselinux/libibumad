Summary: OpenFabrics Alliance InfiniBand umad (user MAD) library
Name: libibumad
Version: 1.3.4
Release: 1%{?dist}
License: GPLv2 or BSD
Group: System Environment/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Source: http://www.openfabrics.org/downloads/management/%{name}-%{version}.tar.gz
Url: http://openfabrics.org
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires: libtool, automake, autoconf, glibc-static
ExcludeArch: s390 s390x

%description
libibumad provides the user MAD library functions which sit on top of 
the user MAD modules in the kernel. These are used by the IB diagnostic
and management tools, including OpenSM. 

%package devel
Summary: Development files for the libibumad library
Group: System Environment/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
Development files for the libibumad library.

%package static
Summary: Static version of the libibumad library
Group: System Environment/Libraries
Requires: %{name}-devel = %{version}-%{release}

%description static
Static version of the libibumad library.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=${RPM_BUILD_ROOT} install
# remove unpackaged files from the buildroot
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_libdir}/libibumad*.so.*
%{_mandir}/man3/*
%doc AUTHORS COPYING ChangeLog 

%files devel
%defattr(-,root,root)
%{_libdir}/libibumad.so
%{_includedir}/infiniband/*.h

%files static
%defattr(-,root,root)
%{_libdir}/libibumad.a

%changelog
* Sat Feb 27 2010 Doug Ledford <dledford@redhat.com> - 1.3.4-1
- New upstream release

* Mon Jan 11 2010 Doug Ledford <dledford@redhat.com> - 1.3.3-2
- ExcludeArch s390(x) as there is no hardware support there

* Thu Dec 03 2009 Doug Ledford <dledford@redhat.com> - 1.3.3-1
- Update to latest upstream version

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 20 2009 Doug Ledford <dledford@redhat.com> - 1.3.2-2
- Forgot to remove both instances of the libibcommon requires
- Add build requires on glibc-static

* Mon Jul 20 2009 Doug Ledford <dledford@redhat.com> - 1.3.2-1
- Update to latest upstream version
- Remove requirement on libibcommon since that library is no longer needed
- Fix a problem with man page listing

* Wed Apr 22 2009 Doug Ledford <dledford@redhat.com> - 1.3.1-1
- Update to latest upstream version

* Sat Mar 21 2009 Robert Scheck <robert@fedoraproject.org> - 1.2.0-3
- Rebuilt against libtool 2.2

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jun 08 2008 Doug Ledford <dledford@redhat.com> - 1.2.0-1
- Initial package for Fedora review process
