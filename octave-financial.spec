%global octpkg financial

Summary:	Financial functions for Octave
Name:		octave-%{octpkg}
Version:	0.5.3
Release:	1
Source0:	http://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		https://octave.sourceforge.io/%{octpkg}/
BuildArch:	noarch

BuildRequires:	octave-devel >= 4.4.0
BuildRequires:	octave-io >= 2.4.11
BuildRequires:	octave-statistics >= 1.4.0

Requires:	octave(api) = %{octave_api}
Requires:	octave-io >= 2.4.11
Requires:	octave-statistics >= 1.4.0

Requires(post): octave
Requires(postun): octave

%description
Monte Carlo simulation, options pricing routines,  financial manipulation,
plotting functions and additional date manipulation tools for Octave.

This package is part of community Octave-Forge collection.

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

# remove backup files
#find . -name \*~ -delete

%build
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

