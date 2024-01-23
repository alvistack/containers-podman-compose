# Copyright 2024 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-podman-compose
Epoch: 100
Version: 1.1.0
Release: 1%{?dist}
BuildArch: noarch
Summary: Run docker-compose.yml using podman
License: GPL-2.0-only
URL: https://github.com/containers/podman-compose/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
An implementation of docker-compose with podman backend. The main
objective of this project is to be able to run docker-compose.yml
unmodified and rootless.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-podman-compose
Summary: Run docker-compose.yml using podman
Requires: python3
Requires: python3-python-dotenv
Requires: python3-PyYAML
Provides: python3-podman-compose = %{epoch}:%{version}-%{release}
Provides: python3dist(podman-compose) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-podman-compose = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(podman-compose) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-podman-compose = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(podman-compose) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-podman-compose
An implementation of docker-compose with podman backend. The main
objective of this project is to be able to run docker-compose.yml
unmodified and rootless.

%files -n python%{python3_version_nodots}-podman-compose
%license LICENSE
%{_bindir}/*
%{python3_sitelib}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-podman-compose
Summary: Run docker-compose.yml using podman
Requires: python3
Requires: python3-python-dotenv
Requires: python3-PyYAML
Provides: python3-podman-compose = %{epoch}:%{version}-%{release}
Provides: python3dist(podman-compose) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-podman-compose = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(podman-compose) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-podman-compose = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(podman-compose) = %{epoch}:%{version}-%{release}

%description -n python3-podman-compose
An implementation of docker-compose with podman backend. The main
objective of this project is to be able to run docker-compose.yml
unmodified and rootless.

%files -n python3-podman-compose
%license LICENSE
%{_bindir}/*
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n podman-compose
Summary: Run docker-compose.yml using podman
Requires: python3
Requires: python3-dotenv
Requires: python3-pyyaml
Provides: python3-podman-compose = %{epoch}:%{version}-%{release}
Provides: python3dist(podman-compose) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-podman-compose = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(podman-compose) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-podman-compose = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(podman-compose) = %{epoch}:%{version}-%{release}

%description -n podman-compose
An implementation of docker-compose with podman backend. The main
objective of this project is to be able to run docker-compose.yml
unmodified and rootless.

%files -n podman-compose
%license LICENSE
%{_bindir}/*
%{python3_sitelib}/*
%endif

%changelog
