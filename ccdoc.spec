Summary:	A program that generates HTML documentation from C++ source code.
Name:		ccdoc
Version:	0.7a
Release:	1
Copyright:	Freely distributable
Group:		Development/Tools
URL:		http://www.joelinoff.com/ccdoc/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Source0:	http://www.joelinoff.com/ccdoc_old/ccdoc_v07a_src_taz.exe
Source1:	ctf2xml.tar.gz
Patch0:		ccdoc_v07a.medoosa.patch

%description
The CcDoc tool is a javadoc like tool that automatically generates web
documentation from C++ programs by parsing the source file headers.
This release includes ctf2xml, required by the Medoosa project.

%prep
%setup -q -n ccdoc_v07a
mv doc/*.exe .
(cd ccdoc_dev/ccdoc; tar xfz %{SOURCE1})
(cd ccdoc_dev; perl tools/ccdoc_pc2unix.pl)
%patch -p1


%build
cd ccdoc_dev
perl tools/ccdoc_bld.pl
%{__make} -C ccdoc/ctf2xml

%install
rm -rf $RPM_BUILD_ROOT
pwd
install -d $RPM_BUILD_ROOT%{_bindir}
install -s ccdoc_dev/ccdoc/bin_linux_opt/ccdoc.exe $RPM_BUILD_ROOT%{_bindir}/ccdoc
install -s ccdoc_dev/ccdoc/ctf2xml/ctf2xml2 $RPM_BUILD_ROOT%{_bindir}/ctf2xml2


%clean
rm -fr $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
%doc doc/*
%attr(755,root,root) %{_bindir}/ccdoc
%attr(755,root,root) %{_bindir}/ctf2xml2
