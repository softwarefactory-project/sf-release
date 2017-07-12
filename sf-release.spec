%global         sum The Software Factory project

Name:           sf-release
Version:        2.6
Release:        4%{?dist}
Summary:        %{sum}

License:        ASL 2.0
URL:            https://softwarefactory-project.io/r/p/%{name}
Source1:        sf-release.repo

BuildArch:      noarch

Requires:       centos-release-openstack-newton
Requires:       centos-release-opstools
Requires:       centos-release-scl-rh

%description
%{sum}

%prep

%build

%install
install -p -D -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/yum.repos.d/sf-release.repo
echo 2.6 > %{buildroot}%{_sysconfdir}/sf-release

%files
%{_sysconfdir}/yum.repos.d/sf-release.repo
%{_sysconfdir}/sf-release

%changelog
* Tue Jul 11 2017 Fabien Boucher <fboucher@redhat.com> - 2.6-4
- SF Release 2.6

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
