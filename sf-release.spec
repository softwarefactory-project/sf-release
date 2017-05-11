%global         sum The Software Factory project

Name:           sf-release
Version:        2.5
Release:        4%{?dist}
Summary:        %{sum}

License:        ASL 2.0
URL:            https://softwarefactory-project.io/r/p/%{name}
Source1:        sf-release.repo

BuildArch:      noarch

Requires:       centos-release-openstack-newton
Requires:       centos-release-opstools

%description
%{sum}

%prep

%build

%install
install -p -D -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/yum.repos.d/sf-release.repo
if [[ %{version} =~ dev ]]; then
   echo %{version} | sed 's/.*dev/dev/' > %{buildroot}%{_sysconfdir}/sf-release
else
   echo %{version} > %{buildroot}%{_sysconfdir}/sf-release
fi

%files
%{_sysconfdir}/yum.repos.d/sf-release.repo
%{_sysconfdir}/sf-release

%changelog
* Tue May 11 2017 Fabien Boucher <fboucher@redhat.com> - 2.5-4
- Target sf-2.5-el7-release

* Wed Apr 19 2017 Tristan Cacqueray <tdecacqu@redhat.com> - 2.5-3
- Switch to new koji target el7

* Mon Apr 17 2017 Tristan Cacqueray <tdecacqu@redhat.com> - 2.5-2
- Add sf-release

* Tue Apr 11 2017 Tristan Cacqueray <tdecacqu@redhat.com> - 2.5-1
- Initial packaging
