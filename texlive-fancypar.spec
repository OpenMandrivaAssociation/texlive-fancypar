# revision 18018
# category Package
# catalog-ctan /macros/latex/contrib/fancypar
# catalog-date 2010-04-29 12:40:52 +0200
# catalog-license lppl1.3
# catalog-version 1.1
Name:		texlive-fancypar
Version:	1.1
Release:	1
Summary:	Decoration of individual paragraphs
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/fancypar
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fancypar.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fancypar.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fancypar.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Decorates individual paragraphs of a document, offering five
pre-defined styles. The command offers an optional 'key-value'
argument with the user may define parameters of the selected
style. Predefined styles offer a spiral-notebook, a zebra-like,
a dashed, a marked design, and an underlined style. Users may
also define their own styles. Decorated paragraphs may not
include displayed mathematics.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/fancypar/fancypar.sty
%doc %{_texmfdistdir}/doc/latex/fancypar/README
%doc %{_texmfdistdir}/doc/latex/fancypar/fancypar.pdf
#- source
%doc %{_texmfdistdir}/source/latex/fancypar/fancypar.dtx
%doc %{_texmfdistdir}/source/latex/fancypar/fancypar.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
