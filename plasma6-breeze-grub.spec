%undefine _debugsource_packages

%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)
#define git 20240222
%define gitbranch Plasma/6.0
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")

Summary:	The Breeze theme for the GRUB bootloader
Name:		plasma6-breeze-grub
Version:	6.0.5
Release:	%{?git:0.%{git}.}1
License:	GPL
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
%if 0%{?git:1}
Source0:	https://invent.kde.org/plasma/breeze-grub/-/archive/%{gitbranch}/breeze-grub-%{gitbranchd}.tar.bz2#/breeze-grub-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/plasma/%(echo %{version} |cut -d. -f1-3)/breeze-grub-%{version}.tar.xz
%endif
%ifarch %{ix86} %{x86_64} %{aarch64}
Requires:	grub2
%endif
BuildArch:	noarch

%description
This package contains a version of the KDE Breeze theme for
the GRUB bootloader

%files
/boot/grub2/themes/breeze

%prep
%autosetup -n breeze-grub-%{?git:%{gitbranchd}}%{!?git:%{version}}

%build

%install
mkdir -p %{buildroot}/boot/grub2/themes
cp -a breeze %{buildroot}/boot/grub2/themes/
