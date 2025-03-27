%define module cbor2

Name:		python-cbor2
Version:	5.6.5
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/c/%{module}/%{module}-%{version}.tar.gz
Summary:	CBOR (de)serializer with extensive tag support
URL:		https://pypi.org/project/cbor2/
License:	MIT
Group:		Development/Python
BuildSystem:	python

BuildRequires:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python-hypothesis
BuildRequires:	python-pip
BuildRequires:	python-setuptools
BuildRequires:	python-setuptools_scm
BuildRequires:	python-wheel
BuildRequires:	python-pytest

%description
This library provides encoding and decoding for the Concise Binary Object
Representation (CBOR) (RFC 8949) serialization format.

The specification is fully compatible with the original RFC 7049.

Read the docs to learn more.

It is implemented in pure python with an optional C backend.

%prep
%autosetup -p1 -n %{module}-%{version}

%build
export LDFLAGS="%{optflags}"
export CBOR2_BUILD_C_EXTENSION=1
%py_build

%install
%py3_install

%files
%{_bindir}/%{module}
%{python3_sitearch}/*.so
%{python3_sitearch}/%{module}
%{python3_sitearch}/%{module}-*.*-info
%doc README.rst
%license LICENSE.txt
