%global         sum The Software Factory project

Name:           sf-release
Version:        3.3
Release:        5%{?dist}
Summary:        %{sum}

License:        ASL 2.0
URL:            https://softwarefactory-project.io/r/p/%{name}
Source1:        sf-release.repo
Source2:        RPM-GPG-KEY-SOFTWARE-FACTORY
Source3:        RPM-GPG-KEY-CentOS-SIG-SCLo-python35
Source4:        RPM-GPG-KEY-CentOS-SIG-Cloud

BuildArch:      noarch

%description
%{sum}

%prep

%build

%install
install -p -D -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/yum.repos.d/sf-release.repo
install -p -D -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-SOFTWARE-FACTORY
install -p -D -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-CentOS-SIG-SCLo-python35
install -p -D -m 0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-CentOS-SIG-Cloud
echo 3.3 > %{buildroot}%{_sysconfdir}/sf-release

%files
%{_sysconfdir}/yum.repos.d/sf-release.repo
%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-SOFTWARE-FACTORY
%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-CentOS-SIG-SCLo-python35
%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-CentOS-SIG-Cloud
%{_sysconfdir}/sf-release

%changelog
* Thu Sep 19 2019 Tristan Cacqueray <tdecacqu@redhat.com> - 3.3-5
- Add openstack-queens mirror

* Wed Sep 18 2019 Tristan Cacqueray <tdecacqu@redhat.com> - 3.3-4
- Ensure mirror repos is picked first

* Tue Sep 17 2019 Tristan Cacqueray <tdecacqu@redhat.com> - 3.3-3
- Vendor the rh-python35 repository

* Wed May 22 2019 Nicolas Hicher <nhicher@redhat.com> - 3.3-2
- Release 3.3

* Wed May 22 2019 Nicolas Hicher <nhicher@redhat.com> - 3.3-1
- Release 3.3

* Wed Nov 28 2018 Nicolas Hicher <nhicher@redhat.com> - 9999-10
- Remove centos only requirements

* Thu Jul 12 2018 Tristan Cacqueray <tdecacqu@redhat.com> - 9999-9
- Re-add depends

* Mon Apr 9 2018 Nicolas Hicher <nhicher@redhat.com> - 9999-8
- Remove depends (moved in sfconfig)

* Tue Nov 14 2017 Fabien Boucher <fboucher@redhat.com> - 9999-7
- Add SF repository public key

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
