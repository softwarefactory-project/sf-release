%global         sum The Software Factory project

Name:           sf-release
Version:        2.7
Release:        1%{?dist}
Summary:        %{sum}

License:        ASL 2.0
URL:            https://softwarefactory-project.io/r/p/%{name}
Source1:        sf-release.repo
Source2:        RPM-GPG-KEY-SOFTWARE-FACTORY

BuildArch:      noarch

Requires:       centos-release-openstack-pike
Requires:       centos-release-opstools
Requires:       centos-release-scl-rh

%description
%{sum}

%prep

%build

%install
install -p -D -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/yum.repos.d/sf-release.repo
install -p -D -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-SOFTWARE-FACTORY
echo 2.7 > %{buildroot}%{_sysconfdir}/sf-release

%files
%{_sysconfdir}/yum.repos.d/sf-release.repo
%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-SOFTWARE-FACTORY
%{_sysconfdir}/sf-release

%changelog
* Mon Nov 13 2017 Fabien Boucher <fboucher@redhat.com> - 2.7-1
- SF Release 2.7

* Wed Oct 11 2017 Fabien Boucher <fboucher@redhat.com> - 9999-6
- Use the koji sf-master-el7-build tag instead of the mash one

* Sat Sep 30 2017 Tristan Cacqueray <tdecacqu@redhat.com> - 9999-5
- Bump RDO requirements from newton to pike

* Tue Aug 29 2017 Tristan Cacqueray <tdecacqu@redhat.com> - 9999-4
- Update koji url

* Mon Jun 19 2017 Tristan Cacqueray <tdecacqu@redhat.com> - 9999-3
- Add scl-rh requirement

* Tue May 23 2017 Tristan Cacqueray <tdecacqu@redhat.com> - 9999-2
- Fix typo...

* Tue May 23 2017 Tristan Cacqueray <tdecacqu@redhat.com> - 9999-1
- Write 'master' to /etc/sf-release

* Wed Apr 19 2017 Tristan Cacqueray <tdecacqu@redhat.com> - 2.5-3
- Switch to new koji target el7

* Mon Apr 17 2017 Tristan Cacqueray <tdecacqu@redhat.com> - 2.5-2
- Add sf-release

* Tue Apr 11 2017 Tristan Cacqueray <tdecacqu@redhat.com> - 2.5-1
- Initial packaging
