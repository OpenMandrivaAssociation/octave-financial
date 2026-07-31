%global octpkg financial

Summary:	Financial functions for Octave
Name:		octave-financial
Version:	0.5.4
Release:	1
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		https://packages.octave.org/financial/
Source0:	https://downloads.sourceforge.net/octave/financial-%{version}.tar.gz
# dropped (no longer applies): Patch0:		octave-financial-0.5.4-octave9.patch

BuildRequires:  octave-devel >= 4.4.0
BuildRequires:  octave-io >= 2.4.11
BuildRequires:  octave-statistics >= 1.4.0

Requires:	octave(api) = %{octave_api}
Requires:  	octave-io >= 2.4.11
Requires:  	octave-statistics >= 1.4.0

Requires(post): octave
Requires(postun): octave

BuildArch:	noarch

%description
Monte Carlo simulation, options pricing routines, financial
manipulation, plotting functions and additional date manipulation
tools for Octave.

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n financial-0.5.4

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

