%global commit 606454af70411bacb99a98605f6021b56ccd3586
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global fscrypt_ver 0.2.9
%define debug_package %{nil}

Name:           fscrypt
Version:        0.2.9
Release:        1%{?dist}
Summary:        fscrypt is a high-level tool for the management of Linux filesystem encryption.
Group:          Encryption
License:        Apache 2.0
URL:            https://github.com/google/fscrypt
Source0:        %{url}/archive/v%{fscrypt_ver}.zip

BuildRequires:  git gcc pam-devel golang

%description
fscrypt is a high-level tool for the management of Linux filesystem encryption.

%prep
rm -rf %{name}-%{version}
%setup -c -T -D -a 0
mkdir -p ./_build
ln -s $(pwd) ./_build/src

%build
export GOPATH=$(pwd)/_build
cd %{name}-%{version}
export LDFLAGS="-X main.VERSION=%{version}"
make

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}/usr/local/lib/security/
mkdir -p %{buildroot}/usr/local/share/pam-configs/pam_fscrypt/
install -m 755 %{name}-%{version}/bin/fscrypt %{buildroot}%{_bindir}
install -m 644 %{name}-%{version}/bin/pam_fscrypt.so %{buildroot}/usr/local/lib/security/
install -m 644 %{name}-%{version}/pam_fscrypt/config %{buildroot}/usr/local/share/pam-configs/pam_fscrypt/

%files
%{_bindir}/fscrypt
/usr/local/lib/security/pam_fscrypt.so
/usr/local/share/pam-configs/pam_fscrypt/config

%changelog
