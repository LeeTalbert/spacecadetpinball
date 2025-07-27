%global debug_package %{nil}
%define rname SpaceCadetPinball-Release
%define uname SpaceCadetPinball

Name:		spacecadetpinball
Version:	2.1.0
Release:	1
Source0:    https://github.com/k4zmu2a/SpaceCadetPinball/archive/refs/tags/Release_%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:    https://archive.org/download/pinballxp/PinballXP.zip
Summary:	Reverse engineered port of 3D Pinball for Windows - Space Cadet
URL:		https://github.com/k4zmu2a/SpaceCadetPinball
License:	MIT
Group:		Games/Arcade

BuildSystem:  cmake
BuildOption:  -DCMAKE_BUILD_TYPE=Release
BuildRequires:	pkgconfig(sdl2)
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  unzip

#BuildSystem:    cmake

%description
Reverse engineering of '3D Pinball for Windows - Space Cadet', a game bundled with Windows.

%install -a
unzip %{S:1} -d %{buildroot}/%{_bindir}

%files
%{_bindir}/*
%{_iconsdir}/hicolor/*/apps/%{uname}.png
%{_datadir}/metainfo/%{uname}.metainfo.xml
%{_datadir}/applications/%{uname}.desktop
