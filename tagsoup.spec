Summary:	A SAX-compliant parser written in Java that parses HTML as it is found in the wild: nasty and brutish
Summary(pl.UTF-8):	Zgodny z SAX, napisany w Javie analizator HTML-a występującego w rzeczywistości
Name:		tagsoup
Version:	1.0.1
Release:	0.1
Epoch:		0
License:	GPL
Source0:	http://home.ccil.org/~cowan/XML/tagsoup/%{name}-%{version}-src.zip
# Source0-md5:	35088ab782cb31bbf63e745302379fa5
Group:		Applications/Text
URL:		http://mercury.ccil.org/~cowan/XML/tagsoup/
BuildRequires:	ant
BuildRequires:	ant-trax
BuildRequires:	jpackage-utils
BuildRequires:	rpmbuild(macros) >= 1.300
BuildRequires:	xalan-j
Requires:	jpackage-utils >= 0:1.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TagSoup is a SAX-compliant parser written in Java that, instead of
parsing well-formed or valid XML, parses HTML as it is found in the
wild: nasty and brutish, though quite often far from short. TagSoup is
designed for people who have to process this stuff using some
semblance of a rational application design. By providing a SAX
interface, it allows standard XML tools to be applied to even the
worst HTML.

%description -l pl.UTF-8
TagSoup to zgodny z SAX, napisany w Javie analizator, który zamiast
analizowania dobrze sformułowanego czy poprawnego XML-a analizuje
HTML w postaci w jakiej występuje w rzeczywistości: brzydkiej i
okrutnej, zwykle dalekiej od krótkiej. TagSoup jest przeznaczony dla
potrzebujących przetwarzać HTML z pozorami racjonalnego projektu
aplikacji. Udostępniając interfejs SAX TagSoup pozwala na stosowanie
standardowych narzędzi XML-owych nawet na najgorszym HTML-u.

%package javadoc
Summary:	Javadoc for TagSoup
Summary(pl.UTF-8):	Dokumentacja Javadoc do TagSoup
Group:		Documentation
Requires:	jpackage-utils

%description javadoc
Javadoc for TagSoup.

%description javadoc -l pl.UTF-8
Dokumentacja Javadoc do TagSoup.

%prep
%setup -q

%build
required_jars="xalan"
export CLASSPATH=$(build-classpath $required_jars)
%ant \
	-Dversion=%{version} \
	-Dj2se.apiurl=%{_javadocdir}/java \
	dist docs-api

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}
install dist/lib/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
ln -snf %{name}-%{version} %{_javadocdir}/%{name}

%files
%defattr(644,root,root,755)
%doc CHANGES README
%{_javadir}/*.jar

%files javadoc
%defattr(644,root,root,755)
%doc %{_javadocdir}/%{name}-%{version}
%ghost %doc %{_javadocdir}/%{name}
