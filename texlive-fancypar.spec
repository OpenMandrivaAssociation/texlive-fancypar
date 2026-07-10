%global tl_name fancypar
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.3
Release:	%{tl_revision}.1
Summary:	Decoration of individual paragraphs
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/fancypar
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fancypar.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fancypar.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fancypar.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Decorates individual paragraphs of a document, offering five pre-defined
styles. The command offers an optional 'key-value' argument with the
user may define parameters of the selected style. Predefined styles
offer a spiral-notebook, a zebra-like, a dashed, a marked design, and an
underlined style. Users may also define their own styles. Decorated
paragraphs may not include displayed mathematics.

