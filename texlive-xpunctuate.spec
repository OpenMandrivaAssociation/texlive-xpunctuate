Name:		texlive-xpunctuate
Version:	26641
Release:	2
Summary:	TeXLive xpunctuate package
Group:		Publishing
URL:		https://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xpunctuate.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xpunctuate.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xpunctuate.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive xpunctuate package.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/xpunctuate/xpunctuate.sty
%doc %{_texmfdistdir}/doc/latex/xpunctuate/README
%doc %{_texmfdistdir}/doc/latex/xpunctuate/xpunctuate.pdf
#- source
%doc %{_texmfdistdir}/source/latex/xpunctuate/xpunctuate.dtx
%doc %{_texmfdistdir}/source/latex/xpunctuate/xpunctuate.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
