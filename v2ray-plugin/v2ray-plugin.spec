%global commit 606454af70411bacb99a98605f6021b56ccd3586
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global v2ray_ver 4.23.2
%define debug_package %{nil}

Name:           v2ray-plugin
Version:        1.3.1
Release:        1%{?dist}
Summary:        A SIP003 plugin based on v2ray

Group:          Network
License:        MIT
URL:            https://github.com/shadowsocks/v2ray-plugin
Source0:        %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Source1:        https://github.com/v2ray/v2ray-core/archive/v%{v2ray_ver}.zip

BuildRequires:  git golang

%description
Yet another SIP003 plugin for shadowsocks, based on v2ray

%prep
rm -rf %{name}-%{version}
%setup -c -T -D -a 0 -a 1
mkdir -p ./_build
ln -s $(pwd) ./_build/src


%build
export GOPATH=$(pwd)/_build
cd %{name}-%{commit}
go get -insecure v2ray.com/core
export LDFLAGS="-X main.VERSION=%{version}"
CGO_ENABLED=0 go build -v -ldflags "$LDFLAGS" -gcflags "" -o _bin/v2ray-plugin

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 %{name}-%{commit}/_bin/v2ray-plugin %{buildroot}%{_bindir}

%files
%{_bindir}/v2ray-plugin

%changelog
