# revision 26641
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-xpunctuate
Version:	20120810
Release:	3
Summary:	TeXLive xpunctuate package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xpunctuate.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xpunctuate.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xpunctuate.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Fri Aug 10 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120810-1
+ Revision: 813869
- Import texlive-xpunctuate
- Import texlive-xpunctuate

