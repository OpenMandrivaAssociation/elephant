%global debug_package %{nil}

Name:		elephant
# Patch has version change to 1.3.2.
Version:	2.1.0
Release:	1
Source0:	https://github.com/abenz1267/elephant/archive/v%{version}/%{name}-v%{version}.tar.gz
Source1:	%{name}-%{version}-vendor.tar.gz
Summary:	Elephant - cuz it's phat - is a powerful data provider service and backend for building custom application launchers and desktop utilities. It provides various data sources and actions through a plugin-based architecture, communicating via Unix sockets and Protocol Buffers
URL:		https://github.com/abenz1267/elephant
License:	GPL-3.0
Group:		Window Manager/Utility

BuildRequires:	go

Requires:	fd-find
Requires:	qalc

%description
%summary

%prep
%autosetup -p1
tar zxf %{S:1}

%build
export GO111MODULE=on
cd cmd/elephant
go build --buildmode=pie
cd %{builddir}/%{name}-%{version}

for provider in calc clipboard desktopapplications files providerlist runner symbols todo unicode websearch; do
    cd internal/providers/$provider
    go build -buildmode=plugin
    cd %{builddir}/%{name}-%{version}
done

%install
install -Dm 755 cmd/elephant/elephant %{buildroot}%{_bindir}/%{name}

for provider in calc clipboard desktopapplications files providerlist runner symbols todo unicode websearch; do
install -Dm 755 internal/providers/$provider/$provider.so %{buildroot}%{_sysconfdir}/xdg/elephant/providers/$provider.so

done

%files
%license LICENSE
%{_bindir}/%{name}
%{_sysconfdir}/xdg/elephant/providers/*
