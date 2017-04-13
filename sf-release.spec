%global         sum The Software Factory project

Name:           sf-release
Version:        2.5.0
Release:        1%{?dist}
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

%files
%{_sysconfdir}/yum.repos.d/sf-release.repo

%changelog
* Tue Apr 11 2017 Tristan Cacqueray <tdecacqu@redhat.com> - 2.5.0-1
- Initial packaging
