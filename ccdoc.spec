Summary:	A program that generates HTML documentation from C++ source code
Summary(pl):	Program generuj±cy dokumentacjê w HTML-u z kodu ¼ród³owego w C++
Name:		ccdoc
Version:	0.7a
Release:	1
License:	Freely distributable
Group:		Development/Tools
Source0:	http://www.joelinoff.com/ccdoc_old/%{name}_v07a_src_taz.exe
Source1:	ctf2xml.tar.gz
Patch0:		%{name}_v07a.medoosa.patch
Patch1:		%{name}-opt.patch
URL:		http://www.joelinoff.com/ccdoc/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The CcDoc tool is a javadoc like tool that automatically generates web
documentation from C++ programs by parsing the source file headers.
This release includes ctf2xml, required by the Medoosa project.

%description -l pl
CcDoc to narzêdzie podobne do javadoc, automatycznie generuj±ce
dokumentacjê w formacie HTML z programów w C++ poprzez analizê plików
nag³ówkowych ze ¼róde³. Ten pakiet zawiera ctf2xml, wymagany przez
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
