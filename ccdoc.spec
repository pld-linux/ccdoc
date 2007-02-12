Summary:	A program that generates HTML documentation from C++ source code
Summary(pl.UTF-8):   Program generujący dokumentację w HTML-u z kodu źródłowego w C++
Name:		ccdoc
Version:	0.7a
Release:	1
License:	Freely distributable
Group:		Development/Tools
Source0:	http://www.joelinoff.com/ccdoc_old/%{name}_v07a_src_taz.exe
# Source0-md5:	dd9a24a374d10b00391d09a659878b28
Source1:	ctf2xml.tar.gz
# Source1-md5:	a6cdb81755e5d06e9d64162658127d76
Patch0:		%{name}_v07a.medoosa.patch
Patch1:		%{name}-opt.patch
URL:		http://www.joelinoff.com/ccdoc/
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The CcDoc tool is a javadoc like tool that automatically generates web
documentation from C++ programs by parsing the source file headers.
This release includes ctf2xml, required by the Medoosa project.

%description -l pl.UTF-8
CcDoc to narzędzie podobne do javadoc, automatycznie generujące
dokumentację w formacie HTML z programów w C++ poprzez analizę plików
nagłówkowych ze źródeł. Ten pakiet zawiera ctf2xml, wymagany przez
projekt Medoosa.

%prep
%setup -q -n ccdoc_v07a
mv doc/*.exe .
cd ccdoc_dev/ccdoc
tar xfz %{SOURCE1}
cd ../../ccdoc_dev
perl tools/ccdoc_pc2unix.pl
cd ..
%patch0 -p1
%patch1 -p1

%build
cd ccdoc_dev
OPTFLAGS="%{rpmcflags}"; export OPTFLAGS
perl tools/ccdoc_bld.pl

%{__make} -C ccdoc/ctf2xml

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install ccdoc_dev/ccdoc/bin_linux_opt/ccdoc.exe $RPM_BUILD_ROOT%{_bindir}/ccdoc
install ccdoc_dev/ccdoc/ctf2xml/ctf2xml2 $RPM_BUILD_ROOT%{_bindir}/ctf2xml2

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*
%attr(755,root,root) %{_bindir}/ccdoc
%attr(755,root,root) %{_bindir}/ctf2xml2
