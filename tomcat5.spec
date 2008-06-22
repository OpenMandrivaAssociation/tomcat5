# Copyright (c) 2000-2008, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

%define section free

%define gcj_support 0

# If you want only apis to be built,
# give rpmbuild option '--with apisonly'
%define with_apisonly %{?_with_apisonly:1}%{!?_with_apisonly:0}
%define without_apisonly %{!?_with_apisonly:1}%{?_with_apisonly:0}

# If you don't want direct ecj support to be built in,
# while ecj isn't available, give rpmbuild option '--without ecj'
%define without_ecj %{?_without_ecj:1}%{!?_without_ecj:0}
%define with_ecj %{!?_without_ecj:1}%{?_without_ecj:0}

%define full_jname jasper5
%define jname jasper
%define majversion 5.5
%define minversion 26
%define servletspec 2.4
%define jspspec 2.0

%define tcuid 91

%define packdname apache-tomcat-%{version}-src

# FHS 2.2 compliant tree structure
# see http://www.pathname.com/fhs/2.2/
%define confdir %{_sysconfdir}/%{name}
# normally this would be _localstatedir instead of _var, see changelog
%define logdir %{_var}/log/%{name}
%define homedir %{_datadir}/%{name}
%define bindir %{_datadir}/%{name}/bin
%define tempdir %{_var}/cache/%{name}/temp
%define workdir %{_var}/cache/%{name}/work
%define appdir %{_var}/lib/%{name}/webapps
%define serverdir %{_var}/lib/%{name}/server
%define commondir %{_var}/lib/%{name}/common
%define shareddir %{_var}/lib/%{name}/shared

Name: tomcat5
Epoch: 0
Version: %{majversion}.%{minversion}
Release: %mkrel 2.0.2
Summary: Apache Servlet/JSP Engine, RI for Servlet 2.4/JSP 2.0 API

Group: Development/Java
License: Apache License
URL: http://tomcat.apache.org
Source0: http://www.apache.org/dist/tomcat/tomcat-5/v%{version}/src/%{packdname}.tar.gz
Source1: %{name}-%{majversion}.init
Source2: %{name}-%{majversion}.conf
Source3: %{name}-%{majversion}.wrapper
Source4: %{name}-%{majversion}.logrotate
Source5: %{name}-%{majversion}.relink
Source6: jasper-OSGi-MANIFEST.MF
Source7: servlet-api-OSGi-MANIFEST.MF
Source8: jsp-api-OSGi-MANIFEST.MF
Source9: %{name}-poms-%{version}.tar.gz
Patch0: %{name}-%{majversion}.link_admin_jar.patch
Patch1: %{name}-%{majversion}-skip-build-on-install.patch
Patch2: %{name}-%{majversion}-jt5-build.patch
Patch3: %{name}-%{majversion}-jtc-build.patch
Patch4: %{name}-%{majversion}-jtj-build.patch
Patch5: %{name}-%{majversion}-javaxssl.patch
Patch7: %{name}-%{majversion}-catalina.sh.patch
Patch8: %{name}-%{majversion}-jasper.sh.patch
Patch9: %{name}-%{majversion}-jspc.sh.patch
Patch10: %{name}-%{majversion}-setclasspath.sh.patch
Patch12: %{name}-%{majversion}-util-build.patch
Patch13: %{name}-%{majversion}-http11-build.patch
Patch14: %{name}-%{majversion}-jk-build.patch
Patch16: %{name}-%{majversion}-jspc-classpath.patch
#FIXME Disable JSP pre-compilation on ppc64, x390x and alpha
Patch18: %{name}-%{majversion}-skip-jsp-precompile.patch
# XXX:
# Seems to be only needed when building with ECJ for java 1.5 since
# the default source type for ecj is still 1.4
Patch19: %{name}-%{majversion}-connectors-util-build.patch
Patch21: %{name}-%{majversion}-acceptlangheader.patch

BuildRoot: %{_tmppath}/%{name}-%{epoch}-%{version}-%{release}-root
%if ! %{gcj_support}
BuildArch: noarch
%endif

Buildrequires: java-rpmbuild >= 0:1.6.0
BuildRequires: ant >= 0:1.6.2
%if %{without_apisonly}
BuildRequires: java-devel >= 0:1.4.2
%endif
%if %{without_apisonly}
%if %{with_ecj}
BuildRequires: ecj >= 0:3.1.1
BuildRequires: eclipse-jdt
%endif
BuildRequires: ant-trax
BuildRequires: xalan-j2
BuildRequires: jakarta-commons-beanutils >= 1.7
BuildRequires: jakarta-commons-collections >= 0:3.1
BuildRequires: jakarta-commons-daemon >= 1.0
BuildRequires: jakarta-commons-dbcp >= 0:1.2.1
BuildRequires: jakarta-commons-digester >= 0:1.7
BuildRequires: jakarta-commons-logging >= 0:1.0.4
BuildRequires: jakarta-commons-fileupload >= 0:1.0
BuildRequires: jakarta-commons-modeler >= 2.0
BuildRequires: jakarta-commons-pool >= 0:1.2
BuildRequires: jakarta-commons-launcher >= 0:0.9
BuildRequires: jakarta-commons-el >= 0:1.0
BuildRequires: jaas
BuildRequires: jdbc-stdext >= 0:2.0
BuildRequires: jndi >= 0:1.2.1
BuildRequires: jndi-ldap
BuildRequires: jsse >= 0:1.0.3
BuildRequires: junit >= 0:3.8.1
BuildRequires: mx4j >= 0:3.0.1
BuildRequires: regexp >= 0:1.3
BuildRequires: struts >= 0:1.2.7
BuildRequires: xerces-j2 >= 0:2.7.1
BuildRequires: zip
# xml-commons-apis is needed by Xerces-J2
BuildRequires: xml-commons-jaxp-1.3-apis >= 1.3
# FIXME taglibs-standard is not listed in the Tomcat build.properties.default
BuildRequires: jakarta-taglibs-standard >= 0:1.1.0
# formerly non-free stuff
# jta can be provided by geronimo-jta-version-api
BuildRequires: geronimo-jta-1.0.1B-api
# jaf can be provided by classpathx-jaf
BuildRequires: jaf >= 0:1.0.1
# javamail can be provided by classpathx-mail
BuildRequires: javamail >= 0:1.3.1
Requires(post): xml-commons-jaxp-1.3-apis >= 1.3
# libgcj aot-compiled native libraries
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel >= 1.0.43
%endif
Requires(post): jpackage-utils >= 0:1.6.0
Requires(post): rpm-helper
Requires(post): findutils
Requires(preun): findutils
Requires(pre): rpm-helper
# Fedora
Requires(post):         jakarta-commons-dbcp-tomcat5
Requires(post):         jakarta-commons-collections-tomcat5
Requires(post):         jakarta-commons-pool-tomcat5
%endif
Requires: jpackage-utils >= 0:1.6.0
# xml parsing packages
Requires: xerces-j2 >= 0:2.7.1
Requires: xml-commons-jaxp-1.3-apis >= 1.3
# jakarta-commons packages
Requires: jakarta-commons-daemon >= 1.0.1
Requires: jakarta-commons-launcher >= 0:0.9
# alternatives
Requires: java-devel >= 0:1.4.2
Requires: jndi-ldap
# And it needs its own API subpackages for running
Requires: %{name}-common-lib = %{epoch}:%{version}-%{release}
Requires: %{name}-server-lib = %{epoch}:%{version}-%{release}
# Fedora
# And it needs its own API subpackages before being installed
Requires(post): %{name}-common-lib = %{epoch}:%{version}-%{release}
Requires(post): %{name}-server-lib = %{epoch}:%{version}-%{release}

%description
Tomcat is the servlet container that is used in the official Reference
Implementation for the Java Servlet and JavaServer Pages technologies.
The Java Servlet and JavaServer Pages specifications are developed by
Sun under the Java Community Process.

Tomcat is developed in an open and participatory environment and
released under the Apache Software License. Tomcat is intended to be
a collaboration of the best-of-breed developers from around the world.
We invite you to participate in this open development project. To
learn more about getting involved, click here.

%if %{without_apisonly}
%package webapps
Group: Development/Java
# Replace PreReq
Requires(pre): %{name} = %{epoch}:%{version}-%{release}
Requires(postun): %{name} = %{epoch}:%{version}-%{release}
Requires: jakarta-taglibs-standard >= 0:1.1.0
Summary: Web applications for Apache Tomcat
Requires(post): jpackage-utils >= 0:1.6.0
Requires(preun): findutils

%description webapps
Web applications for Apache Tomcat

%package admin-webapps
Group: Development/Java
Summary: The administrative web applications for Apache Tomcat
# Replace PreReq
Requires(pre): %{name} = %{epoch}:%{version}-%{release}
Requires: struts >= 0:1.1
Requires(post): jpackage-utils >= 0:1.6.0
Requires(post): findutils
Requires(post): jakarta-commons-beanutils
Requires(post): jakarta-commons-collections
Requires(post): jakarta-commons-digester
Requires(post): jakarta-commons-io
Requires(post): struts
Requires(preun): findutils
Requires(postun): %{name} = %{epoch}:%{version}-%{release}

%description admin-webapps
The administrative web applications (admin and manager) for Apache Tomcat
%endif

%package servlet-%{servletspec}-api
Group: Development/Java
Requires: update-alternatives
Summary: Apache Tomcat Servlet implementation classes
Obsoletes: servletapi5
Provides: servlet
Provides: servlet5
Provides: servlet24
Provides: servletapi5
Provides: servlet_2_4_api
Requires(post): rpm-helper
requires(postun): rpm-helper

%description servlet-%{servletspec}-api
Contains the implementation classes
of the Apache Tomcat Servlet API (packages javax.servlet).

%package servlet-%{servletspec}-api-javadoc
Group: Development/Java
Summary: Javadoc generated documentation for %{name}-servlet-%{servletspec}-api
Obsoletes: servletapi5-javadoc
Provides: servletapi5-javadoc

%description servlet-%{servletspec}-api-javadoc
Contains the javadoc generated documentation for the implementation classes
of the Apache Tomcat Servlet and JSP APIs (packages javax.servlet).

%package jsp-%{jspspec}-api
Group: Development/Java
Requires: update-alternatives
Requires: servlet24
# We need this to indirectly get rid of legacy jsp included in old
# servlet packages (one day we will be able to remove this)
# Replace PreReq
Requires(pre): %{name}-servlet-%{servletspec}-api = %{epoch}:%{version}-%{release}
Requires(postun): %{name}-servlet-%{servletspec}-api = %{epoch}:%{version}-%{release}
Summary: Apache Tomcat Servlet and JSP implementation classes
Provides: jsp
Requires(post): rpm-helper
Requires(postun): rpm-helper

%description jsp-%{jspspec}-api
Contains the implementation classes
of the Apache Tomcat JSP API (packages javax.servlet.jsp).

%package jsp-%{jspspec}-api-javadoc
Group: Development/Java
Summary: Javadoc generated documentation for %{name}-jsp-%{jspspec}-api

%description jsp-%{jspspec}-api-javadoc
Contains the javadoc generated documentation for the implementation classes
of the Apache Tomcat JSP API (packages javax.servlet.jsp).

%if %{without_apisonly}
%package common-lib
Group: Development/Java
Summary: Libraries needed to run the Tomcat Web container (part)
Requires: java >= 0:1.4.2
Requires(post): jpackage-utils >= 0:1.6.0
Requires: jakarta-commons-collections-tomcat5 >= 0:3.1
Requires(post): jakarta-commons-collections-tomcat5 >= 0:3.1
Requires: jakarta-commons-dbcp-tomcat5 >= 0:1.2.1
Requires(post): jakarta-commons-dbcp-tomcat5 >= 0:1.2.1
Requires: jakarta-commons-el >= 0:1.0
Requires(post): jakarta-commons-el >= 0:1.0
# FIXME commons-pool is not listed in the Tomcat build.properties.default
Requires: jakarta-commons-pool-tomcat5 >= 0:1.2
Requires(post): jakarta-commons-pool-tomcat5 >= 0:1.2
%if %{with_ecj}
Requires: ecj >= 0:3.1.1
Requires(post): ecj >= 0:3.1.1
%endif
# Other subpackages must go in first
Requires(post): %{name}-servlet-%{servletspec}-api = %{epoch}:%{version}-%{release}
Requires(post): %{name}-jsp-%{jspspec}-api = %{epoch}:%{version}-%{release}
Requires(post): %{name}-%{jname} = %{epoch}:%{version}-%{release}
Requires: %{name}-servlet-%{servletspec}-api = %{epoch}:%{version}-%{release}
Requires: %{name}-jsp-%{jspspec}-api = %{epoch}:%{version}-%{release}
Requires: %{name}-%{jname} = %{epoch}:%{version}-%{release}
Requires(post): findutils
Requires(preun): findutils

%description common-lib
Libraries needed to run the Tomcat Web container (part)

%package server-lib
Group: Development/Java
Summary: Libraries needed to run the Tomcat Web container (part)
Requires(post): jpackage-utils >= 0:1.6.0
Requires: jakarta-commons-modeler >= 2.0
Requires(post): jakarta-commons-modeler >= 2.0
# Other subpackages must go in first
Requires: %{name}-%{jname} = %{epoch}:%{version}-%{release}
Requires(post): %{name}-%{jname} = %{epoch}:%{version}-%{release}
Requires(post): findutils
Requires(preun): findutils

%description server-lib
Libraries needed to run the Tomcat Web container (part)

%package %{jname}
Group: Development/Java
Requires: %{name}-servlet-%{servletspec}-api = %{epoch}:%{version}-%{release}
Summary: Compiler JARs and associated scripts for %{name}
Obsoletes: jasper5
Provides: jasper5

%description %{jname}
Compiler JARs and associated scripts for %{name}

%package %{jname}-javadoc
Group: Development/Java
Summary: Javadoc generated documentation for %{name}-%{jname}
Obsoletes: jasper5-javadoc
Provides: jasper5-javadoc

%description %{jname}-javadoc
Javadoc for generated documentation %{name}-%{jname}
%endif

%if %{with_ecj}
%package jasper-eclipse
Group: Development/Java
Summary: Jasper OSGi Eclipse plugin

%description jasper-eclipse
Jasper OSGi Eclipse plugin that contains class files from jasper-compiler,
jasper-runtime and ECJ.
%endif

%prep
%{__rm} -rf ${RPM_BUILD_DIR}/%{name}-%{version}

%setup -q -c -T -a 0
gzip -dc %{SOURCE9} |tar xf -
cd %{packdname}
%patch0 -b .p0
%patch1 -b .p1
%patch2 -b .p2
%patch3 -b .p3
%patch4 -b .p4
%patch5 -b .p5
%patch7 -b .p7
%patch8 -b .p8
%patch9 -b .p9
%patch10 -b .p10
%patch12 -b .p12
%patch13 -b .p13
%patch14 -b .p14
%patch16 -b .p16
%ifarch ppc64 s390x alpha
%patch18 -b .p18
%endif
%patch19 -b .p19
%patch21 -b .p21

%if %{without_ecj}
    %{__rm} %{jname}/src/share/org/apache/jasper/compiler/JDTCompiler.java
%endif

%build
# remove pre-built binaries
for dir in ${RPM_BUILD_DIR}/%{name}-%{version}/%{packdname} ; do
    find $dir \( -name "*.jar" -o -name "*.class" \) | xargs -t %{__rm} -f
done
# copy license for later doc files declaration
pushd ${RPM_BUILD_DIR}/%{name}-%{version}/%{packdname}
    %{__cp} build/LICENSE .
popd 
# build jspapi and servletapi as ant dist will require them later
pushd ${RPM_BUILD_DIR}/%{name}-%{version}/%{packdname}/servletapi
    pushd jsr154
        %{ant} -Dservletapi.build="build" \
            -Dservletapi.dist="dist" \
            -Dbuild.compiler="modern" dist
    popd
    pushd jsr152
        %{ant} -Dservletapi.build="build" \
            -Dservletapi.dist="dist" \
            -Dbuild.compiler="modern" dist
    popd
popd
%if %{without_apisonly}
# build jasper subpackage
pushd ${RPM_BUILD_DIR}/%{name}-%{version}/%{packdname}/%{jname}
    %{__cat} > build.properties << EOBP
ant.jar=$(build-classpath ant)
servlet-api.jar=${RPM_BUILD_DIR}/%{name}-%{version}/%{packdname}/servletapi/jsr154/dist/lib/servlet-api.jar
jsp-api.jar=${RPM_BUILD_DIR}/%{name}-%{version}/%{packdname}/servletapi/jsr152/dist/lib/jsp-api.jar
tools.jar=%{java.home}/lib/tools.jar
xerces.jar=$(build-classpath xerces-j2)
xercesImpl.jar=$(build-classpath jaxp_parser_impl)
xmlParserAPIs.jar=$(build-classpath xml-commons-jaxp-1.3-apis)
commons-el.jar=$(build-classpath commons-el)
commons-collections.jar=$(build-classpath commons-collections)
commons-logging.jar=$(build-classpath commons-logging)
commons-daemon.jar=$(build-classpath commons-daemon)
junit.jar=$(build-classpath junit)
jasper-compiler-jdt.jar=$(build-classpath ecj)
EOBP
    %{ant} -Djava.home="%{java_home}" -Dbuild.compiler="modern" javadoc
popd

# build tomcat 5
pushd ${RPM_BUILD_DIR}/%{name}-%{version}/%{packdname}/build
    %{__cat} >> build.properties << EOBP
version=%{version}
version.build=%{minversion}
ant.jar=%{_javadir}/ant.jar
ant-launcher.jar=%{_javadir}/ant.jar
jtc.home=${RPM_BUILD_DIR}/%{name}-%{version}/%{packdname}/connectors/
%{jname}.home=${RPM_BUILD_DIR}/%{name}-%{version}/%{packdname}/%{jname}
commons-beanutils.jar=$(build-classpath commons-beanutils)
commons-fileupload.jar=$(build-classpath commons-fileupload)
commons-collections.jar=$(build-classpath commons-collections)
commons-daemon.jar=$(build-classpath commons-daemon)
commons-dbcp.jar=$(build-classpath commons-dbcp)
commons-digester.jar=$(build-classpath commons-digester)
commons-el.jar=$(build-classpath commons-el)
commons-launcher.jar=$(build-classpath commons-launcher)
commons-logging.jar=$(build-classpath commons-logging)
commons-logging-api.jar=$(build-classpath commons-logging-api)
commons-modeler.jar=$(build-classpath commons-modeler)
commons-pool.jar=$(build-classpath commons-pool)
jmx.jar=$(build-classpath mx4j/mx4j-jmx.jar)
jmx-remote.jar=$(build-classpath mx4j/mx4j-remote.jar)
jmx-tools.jar=$(build-classpath mx4j/mx4j-tools.jar)
jmxri.jar=$(build-classpath mx4j/mx4j-jmx.jar)
junit.jar=$(build-classpath junit)
regexp.jar=$(build-classpath regexp)
servlet-api.jar=${RPM_BUILD_DIR}/%{name}-%{version}/%{packdname}/servletapi/jsr154/dist/lib/servlet-api.jar
jsp-api.jar=${RPM_BUILD_DIR}/%{name}-%{version}/%{packdname}/servletapi/jsr152/dist/lib/jsp-api.jar
servlet.doc=${RPM_BUILD_DIR}/%{name}-%{version}/%{packdname}/servletapi/jsr154/dist/docs/api
xercesImpl.jar=$(build-classpath jaxp_parser_impl)
xml-apis.jar=$(build-classpath xml-commons-jaxp-1.3-apis)
struts.jar=$(build-classpath struts)
struts.lib=%{_datadir}/struts
activation.jar=$(build-classpath jaf)
mail.jar=$(build-classpath javamail)
jta.jar=$(build-classpath geronimo-jta-1.0.1B-api)
jaas.jar=$(build-classpath jaas)
jndi.jar=$(build-classpath jndi)
jdbc20ext.jar=$(build-classpath jdbc-stdext)
jcert.jar=$(build-classpath jsse/jcert)
jnet.jar=$(build-classpath jsse/jnet)
jsse.jar=$(build-classpath jsse/jsse)
servletapi.build.notrequired=true
jspapi.build.notrequired=true
EOBP
%{ant} -Dbuild.compiler="modern" -Djava.home="%{java_home}" init
cp ${RPM_BUILD_DIR}/%{name}-%{version}/%{packdname}/servletapi/jsr154/dist/lib/servlet-api.jar \
        ${RPM_BUILD_DIR}/%{name}-%{version}/%{packdname}/build/build/common/lib/servlet-api.jar
    %{ant} -Dbuild.compiler="modern" -Djava.home="%{java_home}" build
popd

# create jasper-eclipse jar
%if %{with_ecj}
mkdir org.apache.jasper
pushd org.apache.jasper
unzip -qq ../apache-tomcat-%{version}-src/build/build/common/lib/jasper-compiler.jar
unzip -qq ../apache-tomcat-%{version}-src/build/build/common/lib/jasper-runtime.jar \
  -x META-INF/MANIFEST.MF org/apache/jasper/compiler/Localizer.class
unzip -qq %{_javadir}/jdtcore.jar -x META-INF/MANIFEST.MF
cp %{SOURCE6} META-INF/MANIFEST.MF
rm -f plugin.properties plugin.xml about.html jdtCompilerAdapter.jar META-INF/eclipse.inf
zip -qq -r ../org.apache.jasper_5.5.17.v200706111724.jar .
popd
%endif

# inject OSGi manifests
mkdir META-INF
cp %{SOURCE7} META-INF/MANIFEST.MF
zip -u %{packdname}/servletapi/jsr154/dist/lib/servlet-api.jar META-INF/MANIFEST.MF
cp %{SOURCE8} META-INF/MANIFEST.MF
zip -u %{packdname}/servletapi/jsr152/dist/lib/jsp-api.jar META-INF/MANIFEST.MF

# build the connectors
pushd ${RPM_BUILD_DIR}/%{name}-%{version}/%{packdname}/connectors
# use the JARs created above to build
    export CLASSPATH="${RPM_BUILD_DIR}/%{name}-%{version}/%{packdname}/servletapi/jsr154/dist/lib/servlet-api.jar:${RPM_BUILD_DIR}/%{name}-%{version}/%{packdname}/jakarta-tomcat-5/build/server/lib/catalina.jar"
    %{__cat} > build.properties << EOBP
activation.jar=$(build-classpath jaf)
ant.jar=%{_javadir}/ant.jar
junit.jar=$(build-classpath junit)
commons-beanutils.jar=$(build-classpath commons-beanutils)
commons-collections.jar=$(build-classpath commons-collections)
commons-daemon.jar=$(build-classpath commons-daemon)
commons-digester.jar=$(build-classpath commons-digester)
commons-fileupload.jar=$(build-classpath commons-fileupload)
commons-logging.jar=$(build-classpath commons-logging)
commons-logging-api.jar=$(build-classpath commons-logging-api)
commons-modeler.jar=$(build-classpath commons-modeler)
commons-pool.jar=$(build-classpath commons-pool)
regexp.jar=$(build-classpath regexp)
jmx.jar=$(build-classpath mx4j/mx4j-jmx)
activation.jar=$(build-classpath jaf)
mail.jar=$(build-classpath javamail)
jta.jar=$(build-classpath geronimo-jta-1.0.1B-api)
jaas.jar=$(build-classpath jaas)
jndi.jar=$(build-classpath jndi)
jdbc20ext.jar=$(build-classpath jdbc-stdext)
jcert.jar=$(build-classpath jsse/jcert)
jnet.jar=$(build-classpath jsse/jnet)
jsse.jar=$(build-classpath jsse/jsse)
tomcat5.home=../../build/build
EOBP
    %{ant} -Dbuild.compiler="modern" -Djava.home="%{java_home}" build
popd
%endif

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__install} -d -m 755 ${RPM_BUILD_ROOT}%{_javadir}
%if %{without_apisonly}
export CLASSPATH="$(build-classpath xalan-j2 xml-commons-jaxp-1.3-apis jakarta-taglibs-core jakarta-taglibs-standard):${RPM_BUILD_DIR}/%{name}-%{version}/%{packdname}/servletapi/jsr152/dist/lib/jsp-api.jar"
# build initial path structure
%{__install} -d -m 755 \
    ${RPM_BUILD_ROOT}{%{confdir},%{logdir},%{homedir},%{bindir}}
touch ${RPM_BUILD_ROOT}%{logdir}/catalina.out
%{__install} -d -m 755 ${RPM_BUILD_ROOT}{%{serverdir},%{tempdir},%{workdir}}
%{__install} -d -m 755 ${RPM_BUILD_ROOT}{%{appdir},%{commondir},%{shareddir}}
%{__install} -d -m 755 ${RPM_BUILD_ROOT}%{_sysconfdir}/logrotate.d
%{__install} -d -m 755 ${RPM_BUILD_ROOT}%{_initrddir}
%{__install} -d -m 755 ${RPM_BUILD_ROOT}%{_bindir}
%{__install} -d -m 755 ${RPM_BUILD_ROOT}%{_javadir}/%{name}
%{__install} -d -m 755 ${RPM_BUILD_ROOT}%{_datadir}/maven2/poms
%{__install} -m 755 %{SOURCE5} ${RPM_BUILD_ROOT}%{bindir}/relink
# SysV init and configuration
%{__install} -d -m 755 ${RPM_BUILD_ROOT}%{_sysconfdir}/sysconfig
# Service-specific configuration file
cat > %{name} << EOT
# Service-specific configuration file for %{name} services
# This will be sourced by the SysV service script after the global
# configuration file /etc/%{name}/%{name}.conf, thus allowing values
# to be overridden on a per-service way
#
# NEVER change the init script itself:
# To change values for all services make your changes in
# /etc/%{name}/%{name}.conf
# To change values for a specific service, change it here
# To create a new service, create a link from /etc/init.d/<you new service> to
# /etc/init.d/%{name} (do not copy the init script) and make a copy of the
# /etc/sysconfig/%{name} file to /etc/sysconfig/<you new service> and change
# the property values so the two services won't conflict
# Register the new service in the system as usual (see chkconfig and similars)
#
EOT
%{__cat} %{SOURCE2} >> %{name}
%{__install} -m 0644 %{name} ${RPM_BUILD_ROOT}%{_sysconfdir}/sysconfig/%{name}
%{__rm} %{name}
%{__install} %{SOURCE1} \
    ${RPM_BUILD_ROOT}%{_initrddir}/%{name}
# Global configuration file
%{__install} -d -m 0755 ${RPM_BUILD_ROOT}%{confdir}
%{__cat} > %{name}.conf << EOT
# System-wide configuration file for %{name} services
# This will be sourced by %{name} and any secondary service
# Values will be overridden by service-specific configuration
# files in /etc/sysconfig
# Use this one to change default values for all services
# Change the service specific ones to affect only one service
# (see, for instance, /etc/sysconfig/%{name})
#
EOT
%{__cat} %{SOURCE2} >> %{name}.conf
%{__install} -m 0644 %{name}.conf ${RPM_BUILD_ROOT}%{confdir}/%{name}.conf
%{__rm} -f %{name}.conf
pushd ${RPM_BUILD_DIR}/%{name}-%{version}/%{packdname}/build
    export usejikes="false"
    export OPT_JAR_LIST="ant/ant-trax xalan-j2-serializer"
    %{ant} -Dbuild.compiler="modern" -Djava.home=%{java_home} dist
    pushd dist
        %{__mv} bin/* ${RPM_BUILD_ROOT}%{bindir}
        %{__mv} common/* ${RPM_BUILD_ROOT}%{commondir}
        %{__mv} conf/* ${RPM_BUILD_ROOT}%{confdir}
        %{__mv} server/* ${RPM_BUILD_ROOT}%{serverdir}
        %{__mv} shared/* ${RPM_BUILD_ROOT}%{shareddir}
        %{__mv} webapps/* ${RPM_BUILD_ROOT}%{appdir}
    popd
    pushd build/conf
        %{__mv} uriworkermap.properties workers.properties \
            workers.properties.minimal ${RPM_BUILD_ROOT}%{confdir}
    popd
popd
# rename catalina.sh into dtomcat5 to let wrapper take precedence
%{__install} ${RPM_BUILD_ROOT}%{bindir}/catalina.sh \
    ${RPM_BUILD_ROOT}%{_bindir}/d%{name}
%{__rm} -f ${RPM_BUILD_ROOT}%{bindir}/catalina.sh.* \
    ${RPM_BUILD_ROOT}%{bindir}/setclasspath.*
# Remove leftover files
%{__rm} -f ${RPM_BUILD_ROOT}%{bindir}/*.orig
# install wrapper as tomcat5
%{__install} %{SOURCE3} ${RPM_BUILD_ROOT}%{_bindir}/%{name}
# install logrotate support
%{__install} %{SOURCE4} ${RPM_BUILD_ROOT}%{_sysconfdir}/logrotate.d/%{name}
# remove / reorder non-usefull stuff
%{__rm} -rf ${RPM_BUILD_ROOT}%{homedir}/src/
%{__rm} -f  ${RPM_BUILD_ROOT}%{bindir}/*.sh ${RPM_BUILD_ROOT}%{bindir}/*.bat
# FHS compliance patches, not easy to track them all boys :)
for i in ${RPM_BUILD_ROOT}%{confdir}/%{name}.conf \
    ${RPM_BUILD_ROOT}%{_sysconfdir}/sysconfig/%{name} \
    ${RPM_BUILD_ROOT}%{_bindir}/d%{name} \
    ${RPM_BUILD_ROOT}%{_bindir}/%{name} \
    ${RPM_BUILD_ROOT}%{_initrddir}/%{name} \
    ${RPM_BUILD_ROOT}%{bindir}/relink \
    ${RPM_BUILD_ROOT}%{_sysconfdir}/logrotate.d/%{name}; do
    %{__sed} -i -e 's|\@\@\@TCCONF\@\@\@|%{confdir}|g' \
        -e "s|\@\@\@TCCONF\@\@\@|%{confdir}|g" \
        -e "s|\@\@\@TCHOME\@\@\@|%{homedir}|g" \
        -e "s|\@\@\@TCBIN\@\@\@|%{bindir}|g" \
        -e "s|\@\@\@TCCOMMON\@\@\@|%{commondir}|g" \
        -e "s|\@\@\@TCSERVER\@\@\@|%{serverdir}|g" \
        -e "s|\@\@\@TCSHARED\@\@\@|%{shareddir}|g" \
        -e "s|\@\@\@TCAPP\@\@\@|%{appdir}|g" \
        -e "s|\@\@\@TCLOG\@\@\@|%{logdir}|g" \
        -e "s|\@\@\@LIBDIR\@\@\@|%{_libdir}|g" $i
done
# Process bin
# Remove local JARs (to be replaced with jpp links in post)
pushd ${RPM_BUILD_ROOT}%{bindir}
    # tomcat-juli will be installed in a public repository
    %{__mv} tomcat-juli.jar \
        ${RPM_BUILD_ROOT}%{_javadir}/%{name}/tomcat-juli-%{version}.jar
    pushd ${RPM_BUILD_ROOT}%{_javadir}/%{name}
        %{__ln_s} -f tomcat-juli-%{version}.jar tomcat-juli.jar
    popd
    %add_to_maven_depmap tomcat tomcat-juli %{version} JPP/%{name} tomcat-juli
    %{__install} -m 644 \
        ${RPM_BUILD_DIR}/%{name}-%{version}/tomcat5-poms/tomcat-juli-%{version}.pom \
        $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.%{name}-tomcat-juli.pom

    find . -name "*.jar" -not -name "*bootstrap*" \
           -exec %{__rm} -f {} \;
popd
# Process server/lib
# Remove local JARs (to be replaced with jpp links in post)
pushd ${RPM_BUILD_ROOT}%{serverdir}/lib
    find . -name "*.jar" -not -name "catalina*" \
        -not -name "servlets-*" \
        -not -name "tomcat-*" | xargs -t %{__rm} -f
    # catalina-ant will be installed in a public repository
    %{__mv} catalina-ant.jar \
        ${RPM_BUILD_ROOT}%{_javadir}/catalina-ant-%{version}.jar
    pushd ${RPM_BUILD_ROOT}%{_javadir}
        %{__ln_s} -f catalina-ant-%{version}.jar catalina-ant5.jar
    popd
    %add_to_maven_depmap tomcat catalina-ant %{version} JPP catalina-ant5
    %{__install} -m 644 \
        ${RPM_BUILD_DIR}/%{name}-%{version}/tomcat5-poms/catalina-ant-%{version}.pom \
        $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP-catalina-ant5.pom

    # catalina* jars will be installed in a public repository
    for i in catalina*.jar; do
        j="`echo $i | %{__sed} -e 's|\.jar$||'`"
        %{__mv} ${j}.jar \
            ${RPM_BUILD_ROOT}%{_javadir}/%{name}/${j}-%{version}.jar
        pushd ${RPM_BUILD_ROOT}%{_javadir}/%{name}
            %{__ln_s} -f ${j}-%{version}.jar ${j}.jar
        popd
	%add_to_maven_depmap tomcat ${j} %{version} JPP/tomcat5 ${j}
        %{__install} -m 644 \
            ${RPM_BUILD_DIR}/%{name}-%{version}/tomcat5-poms/${j}-%{version}.pom \
            $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.tomcat5-${j}.pom
    done
    # servlets* jars will be installed in a public repository
    for i in servlets-*.jar; do
        j="`echo $i | %{__sed} -e 's|\.jar$||'`"
        %{__mv} ${j}.jar \
            ${RPM_BUILD_ROOT}%{_javadir}/%{name}/${j}-%{version}.jar
        pushd ${RPM_BUILD_ROOT}%{_javadir}/%{name}
            %{__ln_s} -f ${j}-%{version}.jar ${j}.jar
        popd
	%add_to_maven_depmap tomcat ${j} %{version} JPP/tomcat5 ${j}
        %{__install} -m 644 \
            ${RPM_BUILD_DIR}/%{name}-%{version}/tomcat5-poms/${j}-%{version}.pom \
            $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.tomcat5-${j}.pom
    done
    # tomcat* jars will be installed in a public repository
    for i in tomcat-*.jar; do
        j="`echo $i | %{__sed} -e 's|\.jar$||'`"
        %{__mv} ${j}.jar \
            ${RPM_BUILD_ROOT}%{_javadir}/%{name}/${j}-%{version}.jar
        pushd ${RPM_BUILD_ROOT}%{_javadir}/%{name}
            %{__ln_s} -f ${j}-%{version}.jar ${j}.jar
        popd
	%add_to_maven_depmap tomcat ${j} %{version} JPP/tomcat5 ${j}
        %{__install} -m 644 \
            ${RPM_BUILD_DIR}/%{name}-%{version}/tomcat5-poms/${j}-%{version}.pom \
            $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.tomcat5-${j}.pom
    done
popd
# Process admin webapp server/webapps/admin
pushd ${RPM_BUILD_ROOT}%{serverdir}/webapps/admin/WEB-INF/lib
    find . -name "*.jar" -not -name 'catalina-admin*' | xargs -t %{__rm} -f
    for i in catalina-admin; do
        %{__mv} ${i}.jar \
            ${RPM_BUILD_ROOT}%{_javadir}/%{name}/${i}-%{version}.jar
        pushd ${RPM_BUILD_ROOT}%{_javadir}/%{name}
            %{__ln_s} -f ${i}-%{version}.jar ${i}.jar
        popd
	%add_to_maven_depmap tomcat ${i} %{version} JPP/tomcat5 ${i}
        %{__install} -m 644 \
            ${RPM_BUILD_DIR}/%{name}-%{version}/tomcat5-poms/${i}-%{version}.pom \
            $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.tomcat5-${i}.pom
    done
popd
# Process manager webapp server/webapps/manager
pushd ${RPM_BUILD_ROOT}%{serverdir}/webapps/manager/WEB-INF/lib
    find . -name "*.jar" -not -name 'catalina-manager*' | xargs -t %{__rm} -f
    for i in catalina-manager; do
        %{__mv} ${i}.jar \
            ${RPM_BUILD_ROOT}%{_javadir}/%{name}/${i}-%{version}.jar
        pushd ${RPM_BUILD_ROOT}%{_javadir}/%{name}
            %{__ln_s} -f ${i}-%{version}.jar ${i}.jar
        popd
	%add_to_maven_depmap tomcat ${i} %{version} JPP/tomcat5 ${i}
        %{__install} -m 644 \
            ${RPM_BUILD_DIR}/%{name}-%{version}/tomcat5-poms/${i}-%{version}.pom \
            $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.tomcat5-${i}.pom
    done
popd
# Process host-manager webapp server/webapps/host-manager
pushd ${RPM_BUILD_ROOT}%{serverdir}/webapps/host-manager/WEB-INF/lib
    find . -name "*.jar" -not -name 'catalina-host-manager*' \
        | xargs -t %{__rm} -f
    for i in catalina-host-manager; do
        %{__mv} ${i}.jar \
            ${RPM_BUILD_ROOT}%{_javadir}/%{name}/${i}-%{version}.jar
        pushd ${RPM_BUILD_ROOT}%{_javadir}/%{name}
            %{__ln_s} -f ${i}-%{version}.jar ${i}.jar
        popd
	%add_to_maven_depmap tomcat ${i} %{version} JPP/tomcat5 ${i}
        %{__install} -m 644 \
            ${RPM_BUILD_DIR}/%{name}-%{version}/tomcat5-poms/${i}-%{version}.pom \
            $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.tomcat5-${i}.pom
    done
popd
# Process common/lib
pushd ${RPM_BUILD_ROOT}%{commondir}/lib
    find . -name "*.jar" -not -name "%{jname}*" \
        -not -name "naming*" | xargs -t %{__rm} -f
    # jasper's jars will be installed in a public repository
    for i in %{jname}-compiler %{jname}-runtime; do
        j="`echo $i | %{__sed} -e 's|%{jname}-|%{jname}5-|'`"
        %{__mv} ${i}.jar ${RPM_BUILD_ROOT}%{_javadir}/${j}-%{version}.jar
        pushd ${RPM_BUILD_ROOT}%{_javadir}
            %{__ln_s} -f ${j}-%{version}.jar ${j}.jar
        popd
	%add_to_maven_depmap tomcat ${i} %{version} JPP ${j}
        %{__install} -m 644 \
            ${RPM_BUILD_DIR}/%{name}-%{version}/tomcat5-poms/${i}-%{version}.pom \
            $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP-${j}.pom
    done
    # naming* jars will be installed in a public repository
    for i in naming-*.jar; do
        j="`echo $i | %{__sed} -e 's|\.jar$||'`"
        %{__mv} ${j}.jar \
            ${RPM_BUILD_ROOT}%{_javadir}/%{name}/${j}-%{version}.jar
        pushd ${RPM_BUILD_ROOT}%{_javadir}/%{name}
            %{__ln_s} -f ${j}-%{version}.jar ${j}.jar
        popd
	%add_to_maven_depmap tomcat ${j} %{version} JPP/tomcat5 ${j}
        %{__install} -m 644 \
            ${RPM_BUILD_DIR}/%{name}-%{version}/tomcat5-poms/${j}-%{version}.pom \
            $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.tomcat5-${j}.pom
    done
popd
# Process common/endorsed
pushd ${RPM_BUILD_ROOT}%{commondir}/endorsed
    find . -name "*.jar" | xargs -t %{__rm} -f
popd
# avoid duplicate servlet.jar
%{__rm} -f ${RPM_BUILD_ROOT}%{commondir}/lib/servlet.jar
# Add catalina-deployer
%{__install} -m 644 %{packdname}/build/deployer/lib/catalina-deployer.jar \
    ${RPM_BUILD_ROOT}%{_javadir}/%{name}/catalina-deployer-%{version}.jar
        pushd ${RPM_BUILD_ROOT}%{_javadir}/%{name}
            %{__ln_s} -f catalina-deployer-%{version}.jar catalina-deployer.jar
        popd

# Perform FHS translation
# (final links)
pushd ${RPM_BUILD_ROOT}%{homedir}
    [ -d bin ] || %{__ln_s} -f %{bindir} bin
    [ -d common ] || %{__ln_s} -f %{commondir} common
    [ -d conf ] || %{__ln_s} -f %{confdir} conf
    [ -d logs ] || %{__ln_s} -f %{logdir} logs
    [ -d server ] || %{__ln_s} -f %{serverdir} server
    [ -d shared ] || %{__ln_s} -f %{shareddir} shared
    [ -d webapps ] || %{__ln_s} -f %{appdir} webapps
    [ -d work ] || %{__ln_s} -f %{workdir} work
    [ -d temp ] || %{__ln_s} -f %{tempdir} temp
popd
%endif
# begin servlet api subpackage install
pushd ${RPM_BUILD_DIR}/%{name}-%{version}/%{packdname}/servletapi
    %{__install} -m 644 jsr154/dist/lib/servlet-api.jar \
        ${RPM_BUILD_ROOT}%{_javadir}/%{name}-servlet-%{servletspec}-api-%{version}.jar
    pushd ${RPM_BUILD_ROOT}%{_javadir}
        %{__ln_s} -f %{name}-servlet-%{servletspec}-api-%{version}.jar \
            %{name}-servlet-%{servletspec}-api.jar
        # For backward compatibility with old JPP packages
        %{__ln_s} -f %{name}-servlet-%{servletspec}-api-%{version}.jar \
            servletapi5.jar
    popd
    # depmap frag for standard alternative
    %add_to_maven_depmap javax.servlet servlet-api %{servletspec} JPP servlet_2_4_api
    %add_to_maven_depmap tomcat servlet-api %{version} JPP %{name}-servlet-%{servletspec}-api
    %{__install} -m 644 \
            ${RPM_BUILD_DIR}/%{name}-%{version}/tomcat5-poms/servlet-api-%{version}.pom \
            $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP-%{name}-servlet-%{servletspec}-api.pom
    # javadoc servlet
    %{__install} -d -m 755 ${RPM_BUILD_ROOT}%{_javadocdir}/%{name}-servlet-%{servletspec}-api-%{version}
    %{__cp} -pr jsr154/build/docs/api/* \
        ${RPM_BUILD_ROOT}%{_javadocdir}/%{name}-servlet-%{servletspec}-api-%{version}
    # ghost symlink
    %{__ln_s} -f %{name}-servlet-%{servletspec}-api-%{version} \
        ${RPM_BUILD_ROOT}%{_javadocdir}/%{name}-servlet-%{servletspec}-api
popd
# begin jsp api subpackage install
pushd ${RPM_BUILD_DIR}/%{name}-%{version}/%{packdname}/servletapi
    %{__install} -m 644 jsr152/dist/lib/jsp-api.jar \
        ${RPM_BUILD_ROOT}%{_javadir}/%{name}-jsp-%{jspspec}-api-%{version}.jar
    pushd ${RPM_BUILD_ROOT}%{_javadir}
        %{__ln_s} -f %{name}-jsp-%{jspspec}-api-%{version}.jar \
            %{name}-jsp-%{jspspec}-api.jar
        # For backward compatibility with old JPP packages
        %{__ln_s} -f %{name}-jsp-%{jspspec}-api-%{version}.jar \
            jspapi.jar
    popd
    %add_to_maven_depmap javax.servlet jsp-api %{jspspec} JPP jsp_2_0_api
    %add_to_maven_depmap tomcat jsp-api %{version} JPP %{name}-jsp-%{jspspec}-api
    %{__install} -m 644 \
            ${RPM_BUILD_DIR}/%{name}-%{version}/tomcat5-poms/jsp-api-%{version}.pom \
            $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP-%{name}-jsp-%{jspspec}-api.pom
    # javadoc jsp
    %{__install} -d -m 755 ${RPM_BUILD_ROOT}%{_javadocdir}/%{name}-jsp-%{jspspec}-api-%{version}
    %{__cp} -pr jsr152/build/docs/api/* \
        ${RPM_BUILD_ROOT}%{_javadocdir}/%{name}-jsp-%{jspspec}-api-%{version}
    # ghost symlink
    %{__ln_s} %{name}-jsp-%{jspspec}-api-%{version} \
        ${RPM_BUILD_ROOT}%{_javadocdir}/%{name}-jsp-%{jspspec}-api
popd
%if %{without_apisonly}
# begin jasper subpackage install
pushd ${RPM_BUILD_DIR}/%{name}-%{version}/%{packdname}/%{jname}
    %{__install} -m 755 src/bin/jspc.sh \
        ${RPM_BUILD_ROOT}%{_bindir}/jspc5.sh
    %{__install} -m 755 src/bin/%{jname}.sh \
        ${RPM_BUILD_ROOT}%{_bindir}/%{full_jname}.sh
popd
pushd ${RPM_BUILD_DIR}/%{name}-%{version}/%{packdname}/container
    %{__install} -m 755 catalina/src/bin/setclasspath.sh \
        ${RPM_BUILD_ROOT}%{_bindir}/%{full_jname}-setclasspath.sh
popd
# javadoc
%{__install} -d -m 755 ${RPM_BUILD_ROOT}%{_javadocdir}/%{jname}-%{version}
pushd ${RPM_BUILD_DIR}/%{name}-%{version}/%{packdname}/%{jname}
    %{__cp} -pr build/javadoc/* \
        ${RPM_BUILD_ROOT}%{_javadocdir}/%{jname}-%{version}
    # ghost symlink
    %{__ln_s} %{jname}-%{version} ${RPM_BUILD_ROOT}%{_javadocdir}/%{jname}
popd
%endif

%if %{gcj_support}
# Remove non-standard jars from the list for aot compilation 
aot-compile-rpm \
    --exclude var/lib/%{name}/webapps/tomcat-docs/appdev/sample/sample.war \
    --exclude var/lib/%{name}/webapps/servlets-examples/WEB-INF/classes \
    --exclude var/lib/%{name}/webapps/jsp-examples/WEB-INF/classes \
    --exclude var/lib/%{name}/webapps/jsp-examples/plugin/applet \
    --exclude var/lib/%{name}/server/lib/servlets-cgi.renametojar \
    --exclude var/lib/%{name}/server/lib/servlets-ssi.renametojar
%endif

%if %{with_ecj}
%{__install} -d -m 755 ${RPM_BUILD_ROOT}%{_datadir}/eclipse/plugins
%{__cp} org.apache.jasper_5.5.17.v200706111724.jar ${RPM_BUILD_ROOT}%{_datadir}/eclipse/plugins
%endif

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%if %{without_apisonly}
%post
%update_maven_depmap
# install tomcat5 (but don't activate)
/sbin/chkconfig --add %{name}
# Remove old automated symlinks
for repository in %{bindir} ; do
    find $repository -name '*.jar' -type l | xargs %{__rm} -f
done
for repository in %{commondir}/endorsed ; do
    find $repository -name '\[*\]*.jar' -not -type d | xargs %{__rm} -f
done
for repository in %{commondir}/lib ; do
    find $repository -name '\[*\]*.jar' -not -type d | xargs %{__rm} -f
done
for repository in %{serverdir}/lib ; do
    find $repository -name '\[*\]*.jar' -not -type d | xargs %{__rm} -f
done
# Create automated links - since all needed extensions may not have been
# installed for this jvm output is muted
%{__rm} -f %{bindir}/commons-daemon.jar
%{__ln_s} $(build-classpath commons-daemon) %{bindir}  2>&1
%{__rm} -f %{bindir}/commons-logging-api.jar
%{__ln_s} $(build-classpath commons-logging-api) %{bindir}  2>&1
%{__rm} -f %{bindir}/tomcat-juli.jar
%{__ln_s} $(build-classpath tomcat5/tomcat-juli) %{bindir}  2>&1
build-jar-repository %{commondir}/endorsed jaxp_parser_impl \
    xml-commons-jaxp-1.3-apis 2>&1
build-jar-repository %{commondir}/lib commons-collections-tomcat5 \
    commons-dbcp-tomcat5 commons-el commons-pool-tomcat5 jaf javamail jsp \
    %{name}/naming-factory %{name}/naming-resources servlet \
    %{jname}5-compiler %{jname}5-runtime 2>&1
%if %{with_ecj}
    build-jar-repository %{commondir}/lib ecj 2>&1
%endif
build-jar-repository %{serverdir}/lib catalina-ant5 commons-modeler \
    %{name}/catalina-ant-jmx %{name}/catalina-cluster %{name}/catalina \
    %{name}/catalina-optional %{name}/catalina-storeconfig \
    %{name}/servlets-default %{name}/servlets-invoker %{name}/servlets-webdav \
    %{name}/tomcat-ajp %{name}/tomcat-apr %{name}/tomcat-coyote \
    %{name}/tomcat-http %{name}/tomcat-jkstatus-ant %{name}/tomcat-util 2>&1
%if %{gcj_support}
%{update_gcjdb}
%endif

%if %{gcj_support}
%postun
%{clean_gcjdb}
%endif

%if %{gcj_support}
%post common-lib
%{update_gcjdb}
%endif

%if %{gcj_support}
%postun common-lib
%{clean_gcjdb}
%endif

%if %{gcj_support}
%post jasper-eclipse
%{update_gcjdb}
%endif

%if %{gcj_support}
%postun jasper-eclipse
%{clean_gcjdb}
%endif

%if %{gcj_support}
%post server-lib
%{update_gcjdb}
%endif

%if %{gcj_support}
%postun server-lib
%{clean_gcjdb}
%endif

%post webapps 
# Create automated links - since all needed extensions may not have been
# installed for this jvm output is muted
build-jar-repository %{appdir}/jsp-examples/WEB-INF/lib \
    jakarta-taglibs-core jakarta-taglibs-standard 2>&1
%if %{gcj_support}
%{update_gcjdb}
%endif

%if %{gcj_support}
%postun webapps
%{clean_gcjdb}
%endif

%post admin-webapps
# Remove old automated symlinks
find %{serverdir}/webapps/admin/WEB-INF/lib -name '\[*\]*.jar' -type d \
    | xargs %{__rm} -f
# Create automated links - since all needed extensions may not have been
# installed for this jvm output is muted
build-jar-repository %{serverdir}/webapps/admin/WEB-INF/lib \
    commons-beanutils commons-collections commons-digester struts \
    %{name}/catalina-admin 2>&1
build-jar-repository %{serverdir}/webapps/host-manager/WEB-INF/lib \
    %{name}/catalina-host-manager 2>&1
build-jar-repository %{serverdir}/webapps/manager/WEB-INF/lib \
    commons-io commons-fileupload %{name}/catalina-manager 2>&1
%if %{gcj_support}
%{update_gcjdb}
%endif

%if %{gcj_support}
%postun admin-webapps
%{clean_gcjdb}
%endif
%endif

%post servlet-%{servletspec}-api
%{_sbindir}/update-alternatives --install %{_javadir}/servlet.jar servlet \
    %{_javadir}/%{name}-servlet-%{servletspec}-api.jar 20400
%if %{gcj_support}
%{update_gcjdb}
%endif

%post servlet-%{servletspec}-api-javadoc
%{__rm} -f %{_javadocdir}/servletapi # legacy symlink
%{__rm} -f %{_javadocdir}/%{name}-servlet-%{servletspec}-api
%{__ln_s} %{name}-servlet-%{servletspec}-api-%{version} \
    %{_javadocdir}/%{name}-servlet-%{servletspec}-api

%postun servlet-%{servletspec}-api
if [ "$1" = "0" ]; then
    %{_sbindir}/update-alternatives --remove servlet \
        %{_javadir}/%{name}-servlet-%{servletspec}-api.jar
fi
%if %{gcj_support}
%{clean_gcjdb}
%endif

%post jsp-%{jspspec}-api
%{_sbindir}/update-alternatives --install %{_javadir}/jsp.jar jsp \
    %{_javadir}/%{name}-jsp-%{jspspec}-api.jar 20000

%if %{gcj_support}
%{update_gcjdb}
%endif


%post jsp-%{jspspec}-api-javadoc
%{__rm} -f %{_javadocdir}/jsp-api # legacy symlink
%{__rm} -f %{_javadocdir}/%{name}-jsp-%{jspspec}-api
%{__ln_s} %{name}-jsp-%{jspspec}-api-%{version} \
    %{_javadocdir}/%{name}-jsp-%{jspspec}-api

%postun jsp-%{jspspec}-api
if [ "$1" = "0" ]; then
    %{_sbindir}/update-alternatives --remove jsp \
        %{_javadir}/%{name}-jsp-%{jspspec}-api.jar
fi
%if %{gcj_support}
%{clean_gcjdb}
%endif

%if %{without_apisonly}
%preun
# Always clean up workdir and tempdir on upgrade/removal
%{__rm} -fr %{workdir}/* %{tempdir}/*
if [ $1 = 0 ]; then
    [ -f /var/lock/subsys/%{name} ] && %{_initrddir}/%{name} stop
    [ -f %{_initrddir}/%{name} ] && /sbin/chkconfig --del %{name}
    # Remove automated symlinks
    for repository in %{commondir}/endorsed; do
        find $repository -name '\[*\]*.jar' -not -type d | xargs %{__rm} -f
    done
    for repository in %{commondir}/lib ; do
        find $repository -name '\[*\]*.jar' -not -type d | xargs %{__rm} -f
    done
    for repository in %{serverdir}/lib ; do
        find $repository -name '\[*\]*.jar' -not -type d | xargs %{__rm} -f
    done
fi

%preun admin-webapps
if [ $1 = 0 ]; then
    find %{serverdir}/webapps/*/WEB-INF/lib  \
        -name '\[*\]*.jar' -not -type d | xargs %{__rm} -f
fi

%preun webapps
if [ $1 = 0 ]; then
    find %{appdir}/jsp-examples/WEB-INF/lib  \
        -name '\[*\]*.jar' \
        -not -type d | xargs %{__rm} -f
fi

%pre
# Add the "tomcat" user and group
# we need a shell to be able to use su - later
%{_sbindir}/groupadd -g %{tcuid} -r tomcat 2> /dev/null || :
%{_sbindir}/useradd -c "Apache Tomcat" -u %{tcuid} -g tomcat \
    -s /bin/sh -r -d %{homedir} tomcat 2> /dev/null || :
%endif

%if %{without_apisonly}
%files
%defattr(644,root,root,755)
%doc %{packdname}/build/{LICENSE,RELE*,RUNNING.txt,BENCHMARKS.txt}
# symlinks
%{_datadir}/%{name}/common
%{_datadir}/%{name}/temp
%{_datadir}/%{name}/logs
%{_datadir}/%{name}/conf
%{_datadir}/%{name}/server
%{_datadir}/%{name}/shared
%{_datadir}/%{name}/work
%{_datadir}/%{name}/webapps
# Normal directories
%dir %{homedir}
%dir %{bindir}
%dir %{_var}/lib/%{name}
%dir %{_var}/cache/%{name}
%dir %{commondir}
%dir %{commondir}/classes
%dir %{commondir}/lib
%dir %{commondir}/endorsed
%dir %{commondir}/i18n
%dir %{serverdir}
%dir %{serverdir}/classes
%dir %{serverdir}/lib
%{serverdir}/lib/*.renametojar
%dir %{shareddir}
%dir %{shareddir}/classes
%dir %{shareddir}/lib
# Directories with special permissions
%attr(775,root,tomcat) %dir %{appdir}
%attr(775,root,tomcat) %dir %{confdir}
%attr(770,root,tomcat) %dir %{tempdir}
%attr(770,root,tomcat) %dir %{workdir}
%attr(755,tomcat,tomcat) %dir %{logdir}
%attr(644,tomcat,tomcat) %{logdir}/catalina.out
%attr(775,root,tomcat) %dir %{confdir}/Catalina
%attr(775,root,tomcat) %dir %{confdir}/Catalina/localhost
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{bindir}/relink
%attr(644,root,root) %{bindir}/*.jar
%attr(644,root,root) %{bindir}/*.xml
%attr(755,root,root) %{_initrddir}/%{name}
%attr(644,root,tomcat) %config(noreplace) %{confdir}/catalina.policy
%attr(644,root,tomcat) %config(noreplace) %{confdir}/catalina.properties
%attr(660,root,tomcat) %config(noreplace) %{confdir}/logging.properties
%attr(660,root,tomcat) %config(noreplace) %{confdir}/tomcat-users.xml
%config(noreplace) %{confdir}/%{name}.conf
%config(noreplace) %{confdir}/server-minimal.xml
%config(noreplace) %{confdir}/server.xml
%config(noreplace) %{confdir}/web.xml
%config(noreplace) %{confdir}/context.xml
%config(noreplace) %{confdir}/uriworkermap.properties
%config(noreplace) %{confdir}/workers.properties
%config(noreplace) %{confdir}/workers.properties.minimal
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%{commondir}/i18n/*
%{_mavendepmapfragdir}
%{_datadir}/maven2/poms
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/bootstrap*
%attr(-,root,root) %{_libdir}/gcj/%{name}/commons-daemon*
%attr(-,root,root) %{_libdir}/gcj/%{name}/commons-logging-api*
%attr(-,root,root) %{_libdir}/gcj/%{name}/tomcat-juli*
%attr(-,root,root) %{_libdir}/gcj/%{name}/tomcat-jkstatus-ant*
%endif

%files common-lib
%defattr(644,root,root,755)
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/naming*.jar
%{_mavendepmapfragdir}
%{_datadir}/maven2/poms
%if %{gcj_support}
%attr(-,root,root) %{_libdir}/gcj/%{name}/naming-*
%endif

%files server-lib
%defattr(644,root,root,755)
%{_javadir}/catalina*.jar
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/catalina-ant-jmx*.jar
%{_javadir}/%{name}/catalina-cluster*.jar
%{_javadir}/%{name}/catalina-deployer*.jar
%{_javadir}/%{name}/catalina.jar
%{_javadir}/%{name}/catalina-%{version}.jar
%{_javadir}/%{name}/catalina-optional*.jar
%{_javadir}/%{name}/catalina-storeconfig*.jar
%{_javadir}/%{name}/servlets*.jar
%{_javadir}/%{name}/tomcat*.jar
%{_mavendepmapfragdir}
%{_datadir}/maven2/poms
%if %{gcj_support}
%attr(-,root,root) %{_libdir}/gcj/%{name}/catalina-ant*
%attr(-,root,root) %{_libdir}/gcj/%{name}/catalina-cluster*
%attr(-,root,root) %{_libdir}/gcj/%{name}/catalina-optional*
%attr(-,root,root) %{_libdir}/gcj/%{name}/catalina-storeconfig*
%attr(-,root,root) %{_libdir}/gcj/%{name}/catalina-%{version}.jar*
%attr(-,root,root) %{_libdir}/gcj/%{name}/servlets-default*
%attr(-,root,root) %{_libdir}/gcj/%{name}/servlets-invoker*
%attr(-,root,root) %{_libdir}/gcj/%{name}/servlets-webdav*
%attr(-,root,root) %{_libdir}/gcj/%{name}/tomcat-ajp*
%attr(-,root,root) %{_libdir}/gcj/%{name}/tomcat-apr*
%attr(-,root,root) %{_libdir}/gcj/%{name}/tomcat-coyote*
%attr(-,root,root) %{_libdir}/gcj/%{name}/tomcat-http*
%attr(-,root,root) %{_libdir}/gcj/%{name}/tomcat-util*
%endif

%files webapps
%defattr(644,root,tomcat,775)
%dir %{appdir}/servlets-examples
%{appdir}/servlets-examples/*
%dir %{appdir}/jsp-examples
%{appdir}/jsp-examples/*
%dir %{appdir}/ROOT
%{appdir}/ROOT/*
%dir %{appdir}/tomcat-docs
%{appdir}/tomcat-docs/*
%dir %{appdir}/webdav
%{appdir}/webdav/*
%if %{gcj_support}
%ifnarch ppc64 s390x alpha
%attr(-,root,root) %{_libdir}/gcj/%{name}/catalina-root*
%endif
%endif

%files admin-webapps
%defattr(640,root,tomcat,750)
%attr(660,root,tomcat) %{confdir}/Catalina/localhost/manager.xml
%attr(660,root,tomcat) %{confdir}/Catalina/localhost/host-manager.xml
%{confdir}/Catalina/localhost/admin.xml
%dir %{appdir}/balancer
%{appdir}/balancer/*
%dir %{serverdir}/webapps
%{serverdir}/webapps/*
%attr(644,root,root) %{_javadir}/%{name}/catalina-admin*.jar
%attr(644,root,root) %{_javadir}/%{name}/catalina-manager*.jar
%attr(644,root,root) %{_javadir}/%{name}/catalina-host-manager*.jar
%if %{gcj_support}
%attr(-,root,root) %{_libdir}/gcj/%{name}/catalina-admin*
%attr(-,root,root) %{_libdir}/gcj/%{name}/catalina-balancer*
%attr(-,root,root) %{_libdir}/gcj/%{name}/catalina-host-manager*
%attr(-,root,root) %{_libdir}/gcj/%{name}/catalina-manager*
%endif

%files %{jname}
%defattr(644,root,root,755)
%doc ${RPM_BUILD_DIR}/%{name}-%{version}/%{packdname}/%{jname}/doc/jspc.html
%{_javadir}/%{jname}5-*.jar
%attr(755,root,root) %{_bindir}/%{jname}*.sh
%attr(755,root,root) %{_bindir}/jspc*.sh
%{_mavendepmapfragdir}
%{_datadir}/maven2/poms
%if %{gcj_support}
%attr(-,root,root) %{_libdir}/gcj/%{name}/%{jname}5-*
%endif

%files %{jname}-javadoc
%defattr(0644,root,root,0755)
%{_javadocdir}/%{jname}-%{version}
%ghost %doc %{_javadocdir}/%{jname}
%endif

%files servlet-%{servletspec}-api
%defattr(-,root,root)
%doc %{packdname}/build/LICENSE
%{_javadir}/%{name}-servlet-%{servletspec}-api*.jar
%{_javadir}/servletapi5.jar
%{_mavendepmapfragdir}
%{_datadir}/maven2/poms
%if %{gcj_support}
%attr(-,root,root) %{_libdir}/gcj/%{name}/%{name}-servlet-%{servletspec}-api*
%endif

%files servlet-%{servletspec}-api-javadoc
%defattr(-,root,root)
%doc %{_javadocdir}/%{name}-servlet-%{servletspec}-api-%{version}
%ghost %doc %{_javadocdir}/%{name}-servlet-%{servletspec}-api

%files jsp-%{jspspec}-api
%defattr(-,root,root)
%doc %{packdname}/build/LICENSE
%{_javadir}/%{name}-jsp-%{jspspec}-api*.jar
%{_javadir}/jspapi.jar
%{_mavendepmapfragdir}
%{_datadir}/maven2/poms
%if %{gcj_support}
%attr(-,root,root) %{_libdir}/gcj/%{name}/%{name}-jsp-%{jspspec}-api*
%endif

%files jsp-%{jspspec}-api-javadoc
%defattr(-,root,root)
%doc %{_javadocdir}/%{name}-jsp-%{jspspec}-api-%{version}
%ghost %doc %{_javadocdir}/%{name}-jsp-%{jspspec}-api

%if %{with_ecj}
%files jasper-eclipse
%defattr(-,root,root)
%dir %{_datadir}/eclipse
%dir %{_datadir}/eclipse/plugins
%{_datadir}/eclipse/plugins/org.apache.jasper_*
%endif
