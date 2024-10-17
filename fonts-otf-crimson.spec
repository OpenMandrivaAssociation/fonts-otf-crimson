%define pkgname crimson

Summary:	Crimson serif font family
Name:		fonts-otf-crimson
Version:	20110816
Release:	2
License:	OFL
Group:		System/Fonts/True type
URL:		https://openfontlibrary.org/font/crimson
Source0:	%{pkgname}.zip
Source1:	OFL.txt
Source2:	OFL-FAQ.txt
BuildArch:	noarch
BuildRequires:	freetype-tools

%description
A Garalde under construction; for the love of the works of Tschichold, Slimbach
and Hoefler. For now, only the cuts Roman, Italic and Bold are kerned.

%prep
%setup -q -c -n %{pkgname}-%{version}

%build

%install
%__rm -rf %{buildroot}

%__mkdir_p %{buildroot}%{_xfontdir}/OTF/crimson

%__install -m 644 *.otf %{buildroot}%{_xfontdir}/OTF/crimson
ttmkfdir %{buildroot}%{_xfontdir}/OTF/crimson -o %{buildroot}%{_xfontdir}/OTF/crimson/fonts.dir
%__ln_s fonts.dir %{buildroot}%{_xfontdir}/OTF/crimson/fonts.scale

%__mkdir_p %{buildroot}%_sysconfdir/X11/fontpath.d/
%__ln_s ../../..%{_xfontdir}/OTF/crimson \
    %{buildroot}%_sysconfdir/X11/fontpath.d/otf-crimson:pri=50

%__install -D -m 644 %{SOURCE1} %{buildroot}%{_docdir}/%name/OFL.txt
%__install -D -m 644 %{SOURCE2} %{buildroot}%{_docdir}/%name/OFL-FAQ.txt

%files
%doc %{_docdir}/%name/OFL.txt
%doc %{_docdir}/%name/OFL-FAQ.txt
%dir %{_xfontdir}/OTF/crimson
%{_xfontdir}/OTF/crimson/*.otf
%verify(not mtime) %{_datadir}/fonts/OTF/crimson/fonts.dir
%{_xfontdir}/OTF/crimson/fonts.scale
%{_sysconfdir}/X11/fontpath.d/otf-crimson:pri=50


%changelog
* Thu Dec 15 2011 Dmitry Mikhirev <dmikhirev@mandriva.org> 20110816-1
+ Revision: 741434
- imported package fonts-otf-crimson

