%global debug_package %{nil}

Name:		elephant
Version:	1.0.7
Release:	1
Source0:	https://github.com/abenz1267/elephant/archive/v%{version}/%{name}-v%{version}.tar.gz
Source1:	%{name}-%{version}-vendor.tar.gz
Summary:	Elephant - cuz it's phat - is a powerful data provider service and backend for building custom application launchers and desktop utilities. It provides various data sources and actions through a plugin-based architecture, communicating via Unix sockets and Protocol Buffers
URL:		https://github.com/abenz1267/elephant
License:	GPL-3.0
Group:		Window Manager/Utility

BuildRequires:	go

%description
%summary

%prep
%autosetup -p1
tar zxf %{S:1}

%build
cd cmd/elephant
go build --buildmode=pie
go build -buildmode=plugin
cd %{builddir}/%{name}-%{version}/internal/providers/calc
go build -buildmode=plugin
cd %{builddir}/%{name}-%{version}/internal/providers/clipboard
go build -buildmode=plugin
cd %{builddir}/%{name}-%{version}/internal/providers/desktopapplications
go build -buildmode=plugin
cd %{builddir}/%{name}-%{version}/internal/providers/files
go build -buildmode=plugin
cd %{builddir}/%{name}-%{version}/internal/providers/providerlist
go build -buildmode=plugin
cd %{builddir}/%{name}-%{version}/internal/providers/runner
go build -buildmode=plugin
cd %{builddir}/%{name}-%{version}/internal/providers/symbols
go build -buildmode=plugin
cd %{builddir}/%{name}-%{version}/internal/providers/todo
go build -buildmode=plugin
cd %{builddir}/%{name}-%{version}/internal/providers/unicode
go build -buildmode=plugin
cd %{builddir}/%{name}-%{version}/internal/providers/websearch
go build -buildmode=plugin
%install
install -Dm 755 cmd/elephant/elephant %{buildroot}%{_bindir}/%{name}
install -Dm 755 cmd/elephant/elephant.so %{buildroot}%{_sysconfdir}/xdg/elephant/providers/%{name}.so
install -Dm 755 internal/providers/calc/calc.so %{buildroot}%{_sysconfdir}/xdg/elephant/providers/calc.so
install -Dm 755 internal/providers/clipboard/clipboard.so %{buildroot}%{_sysconfdir}/xdg/elephant/providers/clipboard.so
install -Dm 755 internal/providers/desktopapplications/desktopapplications.so %{buildroot}%{_sysconfdir}/xdg/elephant/providers/desktopapplications.so
install -Dm 755 internal/providers/files/files.so %{buildroot}%{_sysconfdir}/xdg/elephant/providers/files.so
install -Dm 755 internal/providers/providerlist/providerlist.so %{buildroot}%{_sysconfdir}/xdg/elephant/providers/providerlist.so
install -Dm 755 internal/providers/runner/runner.so %{buildroot}%{_sysconfdir}/xdg/elephant/providers/runner.so
install -Dm 755 internal/providers/symbols/symbols.so %{buildroot}%{_sysconfdir}/xdg/elephant/providers/symbols.so
install -Dm 755 internal/providers/todo/todo.so %{buildroot}%{_sysconfdir}/xdg/elephant/providers/todo.so
install -Dm 755 internal/providers/unicode/unicode.so %{buildroot}%{_sysconfdir}/xdg/elephant/providers/unicode.so
install -Dm 755 internal/providers/websearch/websearch.so %{buildroot}%{_sysconfdir}/xdg/elephant/providers/websearch.so


%files
%license LICENSE
%{_bindir}/%{name}
%{_sysconfdir}/xdg/elephant/providers/*
