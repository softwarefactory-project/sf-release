%global         sum The Software Factory project

Name:           sf-release
Version:        3.4
Release:        1%{?dist}
Summary:        %{sum}

License:        ASL 2.0
URL:            https://softwarefactory-project.io/r/p/%{name}
Source1:        sf-release.repo
Source2:        RPM-GPG-KEY-SOFTWARE-FACTORY

BuildArch:      noarch

%description
%{sum}

%prep

%build

%install
install -p -D -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/yum.repos.d/sf-release.repo
install -p -D -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-SOFTWARE-FACTORY
echo 3.4 > %{buildroot}%{_sysconfdir}/sf-release

%files
%{_sysconfdir}/yum.repos.d/sf-release.repo
%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-SOFTWARE-FACTORY
%{_sysconfdir}/sf-release

%changelog
* Mon Dec 09 2019 Tristan Cacqueray <tdecacqu@redhat.com> - 3.4-1
- sf-3.4 release
