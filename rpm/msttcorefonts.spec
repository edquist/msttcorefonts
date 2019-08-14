%define fontdir /usr/share/fonts/%{name}

Summary: TrueType core fonts for the web
Name: msttcorefonts
Version: 2.6
Release: 1%{?dist}
License: Spec file is GPL, binary sources + rpms are gratis under MS EULA
Group: User Interface/X
BuildArch: noarch
BuildRequires: ttmkfdir
BuildRequires: cabextract
Source0: %{name}-%{version}.tar.gz

%description
The TrueType core fonts for the web that was once available from
http://www.microsoft.com/typography/fontpack/, whose redistributable
font installer .exe files were later made available from
http://corefonts.sourceforge.net/.

The source rpm contains the original redistributable font .exe files,
along with the original EULA.

The binary rpm includes those original .exe files and EULA also, along
with the unpacked .ttf files, which appears to be allowed by the EULA as
"associated media" included in the "SOFTWARE PRODUCT", which may be
reproduced and distributed, "provided that each copy shall be a true and
complete copy including all copyright and trademark notices, and shall
be accompanied by a copy of this EULA."  By including the original
complete downloads and EULA, this requirement appears to be satisfied.

%prep
%setup

%build
mkdir cabx fonts
cabextract --lowercase --directory=cabx downloads/*.exe cabx/viewer1.cab
mv cabx/*.ttf fonts
cd fonts
ttmkfdir > fonts.dir

%install
install -d $RPM_BUILD_ROOT%{fontdir}
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/downloads
install -m 0644 fonts/* $RPM_BUILD_ROOT%{fontdir}
install -m 0644 downloads/* $RPM_BUILD_ROOT%{_datadir}/%{name}/downloads

%post
if [ -x /usr/sbin/chkfontpath -a $1 -eq 1 ]; then
	/usr/sbin/chkfontpath --add %{fontdir}
fi
# something has probably changed, update the font-config cache
if [ -x /usr/bin/fc-cache ]; then
	/usr/bin/fc-cache
fi

%preun
if [ -x /usr/sbin/chkfontpath -a $1 -eq 0 ]; then
	/usr/sbin/chkfontpath --remove %{fontdir}
fi

%files
%attr(-,root,root)
%{fontdir}

# Originals included for EULA compliance
%{_datadir}/%{name}/downloads
%license EULA.html

%changelog
* Tue Aug 13 2019 Carl Edquist <edquist@cs.wisc.edu> - 2.6-1
- Bundle original sources & EULA, rather than download at build time

* Sun Sep 09 2012 Noa Resare <noa@resare.com> 2.5-1
- Various updates from Deven T. Corzine, mirrors etc

* Sun May 07 2006 Noa Resare <noa@resare.com> 2.0-1
- checksums downloads
- random mirror
- use redistributable word 97 viewer as source for tahoma.ttf

* Mon Mar 31 2003 Daniel Resare <noa@resare.com> 1.3-4
- updated microsoft link
- updated sourceforge mirrors

* Mon Nov 25 2002 Daniel Resare <noa@resare.com> 1.3-3
- the install dir is now deleted when the package is uninstalled
- executable permission removed from the fonts
- executes fc-cache after install if it is available

* Thu Nov 07 2002 Daniel Resare <noa@resare.com> 1.3-2
- Microsoft released a new service-pack. New url for Tahoma font.

* Thu Oct 24 2002 Daniel Resare <noa@resare.com> 1.3-1
- removed python hack
- removed python hack info from description
- made tahoma inclusion depend on define
- added some info on the ttmkfdir define

* Tue Aug 27 2002 Daniel Resare <noa@resare.com> 1.2-3
- fixed spec error when tahoma is not included 

* Tue Aug 27 2002 Daniel Resare <noa@resare.com> 1.2-2
- removed tahoma due to unclear licensing
- parametrized ttmkfdir path (for mandrake users)
- changed description text to reflect the new microsoft policy

* Thu Aug 15 2002 Daniel Resare <noa@resare.com> 1.2-1
- changed distserver because microsoft no longer provides them

* Tue Apr 09 2002 Daniel Resare <noa@resare.com> 1.1-3
- fixed post/preun script to actually do what they were supposed to do

* Tue Mar 12 2002 Daniel Resare <noa@resare.com> 1.1-2
- removed cabextact from this package
- added tahoma font from ie5.5 update

* Sat Aug 25 2001 Daniel Resare <noa@metamatrix.se>
- initial version
