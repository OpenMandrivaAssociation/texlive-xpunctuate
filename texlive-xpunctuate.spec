%global tl_name xpunctuate
%global tl_revision 67918

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.0
Release:	%{tl_revision}.1
Summary:	Process trailing punctuation which may be redundant
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/xpunctuate
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xpunctuate.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xpunctuate.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xpunctuate.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides commands enabling the user (or package writer) to
insert punctuation after a macro. The method is similar to that of
xspace, but goes further. The package provides the commands \xperiod,
\xcomma and \xperiodcomma, which follow a similar procedure to that of
\xspace, and insert punctuation if and only if it is necessary. It also
provides \xperiodafter, \xcommaafter, \xperiodcommaafter and
\xspaceafter, which all take one argument, the word or phrase to be
punctuated. These then avoid problems with the spacing of periods and
commas after emphasised words.

