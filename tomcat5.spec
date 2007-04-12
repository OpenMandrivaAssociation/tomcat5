# Copyright (c) 2000-2005, JPackage Project
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

# If you want only apis to be built,
# give rpmbuild option '--with apisonly'

%define gcj_support 1
%define _localstatedir %{_var}

%define with_apisonly %{?_with_apisonly:1}%{!?_with_apisonly:0}
%define without_apisonly %{!?_with_apisonly:1}%{?_with_apisonly:0}

# If you don't want direct ecj support to be built in,
# while eclipse-ecj isn't available,
# give rpmbuild option '--without ecj'

%define without_ecj %{?_without_ecj:1}%{!?_without_ecj:0}
%define with_ecj %{!?_without_ecj:1}%{?_without_ecj:0}

%define full_name jakarta-%{name}
%define full_jname jasper5
%define jname jasper
%define majversion 5.5
%define servletspec 2.4
%define jspspec 2.0
%define section devel

%define tcuid 91

%define packdname apache-tomcat-%{version}-src

# FHS 2.2 compliant tree structure
# see http://www.pathname.com/fhs/2.2/
%define confdir %{_sysconfdir}/%{name}
%define logdir %{_localstatedir}/log/%{name}
%define homedir %{_datadir}/%{name}
%define bindir %{_datadir}/%{name}/bin
%define tempdir %{_localstatedir}/cache/%{name}/temp
%define workdir %{_localstatedir}/cache/%{name}/work
%define appdir %{_localstatedir}/lib/%{name}/webapps
%define serverdir %{_localstatedir}/lib/%{name}/server
%define commondir %{_localstatedir}/lib/%{name}/common
%define shareddir %{_localstatedir}/lib/%{name}/shared

Summary: Apache Servlet/JSP Engine, RI for Servlet 2.4/JSP 2.0 API
Name: tomcat5
Version: 5.5.17
Release: %mkrel 6.2.4
Epoch: 0
License: Apache Software License
#Vendor: JPackage Project
#Distribution: JPackage
Group: Development/Java
URL: http://tomcat.apache.org/
Source0: http://www.apache.org/dist/tomcat/tomcat-5/v%{version}/src/%{packdname}.tar.bz2
Source1: %{name}-%{majversion}.init
Source2: %{name}-%{majversion}.conf
Source3: %{name}-%{majversion}.wrapper
Source4: %{name}-%{majversion}.logrotate
Source5: %{name}-%{majversion}.relink
Patch0: %{name}-%{majversion}.link_admin_jar.patch
Patch1: %{name}-%{majversion}-skip-build-on-install.patch
Patch2: %{name}-%{majversion}-jt5-build.patch
Patch3: %{name}-%{majversion}-jtc-build.patch
Patch4: %{name}-%{majversion}-jtj-build.patch
Patch5: %{name}-%{majversion}-javaxssl.patch
#Patch6: %{name}-%{majversion}-bootstrap.MF.patch
Patch7: %{name}-%{majversion}-catalina.sh.patch
Patch8: %{name}-%{majversion}-jasper.sh.patch
Patch9: %{name}-%{majversion}-jspc.sh.patch
Patch10: %{name}-%{majversion}-setclasspath.sh.patch
Patch12: %{name}-%{majversion}-util-build.patch
Patch13: %{name}-%{majversion}-http11-build.patch
Patch14: %{name}-%{majversion}-jk-build.patch
Patch15: %{name}-%{majversion}-skip-native.patch
Patch16: %{name}-%{majversion}-jspc-classpath.patch
Patch17: %{name}-%{majversion}-gcj-class-init-workaround.patch
#FIXME Disable JSP pre-compilation on ppc64 and x390x
Patch18: %{name}-%{majversion}-skip-jsp-precompile.patch

Patch100: %{name}-%{majversion}-java-functions.patch

BuildRoot: %{_tmppath}/%{name}-%{epoch}-%{version}-%{release}-root

Requires: jpackage-utils >= 0:1.6.0
# xml parsing packages
Requires: xerces-j2 >= 0:2.7.1
Requires: xml-commons-apis >= 0:1.3
# jakarta-commons packages
Requires: jakarta-commons-daemon >= 0:1.0.1
Requires: jakarta-commons-launcher >= 0:0.9
# alternatives
Requires: jndi-ldap
# And it needs its own API subpackages for running
Requires: %{name}-common-lib = %{epoch}:%{version}-%{release}
Requires: %{name}-server-lib = %{epoch}:%{version}-%{release}
# And it needs its own API subpackages before being installed
Requires(post): %{name}-common-lib = %{epoch}:%{version}-%{release}
Requires(post): %{name}-server-lib = %{epoch}:%{version}-%{release}

Buildrequires: jpackage-utils >= 0:1.6.0
BuildRequires: ant >= 0:1.6.2
%if %{with_apisonly}
BuildRequires: java-devel >= 0:1.4.2
%endif
%if %{without_apisonly}
%if %{with_ecj}
BuildRequires: eclipse-ecj >= 0:3.1.1
%endif
BuildRequires: ant-trax
BuildRequires: xalan-j2
BuildRequires: jakarta-commons-beanutils >= 1.7
BuildRequires: jakarta-commons-collections >= 0:3.1
#BuildRequires: jakarta-commons-daemon >= 1.0.1
BuildRequires: jakarta-commons-daemon >= 1.0
BuildRequires: jakarta-commons-dbcp >= 0:1.2.1
BuildRequires: jakarta-commons-digester >= 0:1.7
BuildRequires: jakarta-commons-logging >= 0:1.0.4
BuildRequires: jakarta-commons-fileupload >= 0:1.0
BuildRequires: jakarta-commons-modeler >= 1.1
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
# xml-commons-apis is needed by Xerces-J2
BuildRequires: xml-commons-apis >= 1.3
# FIXME taglibs-standard is not listed in the Tomcat build.properties.default
BuildRequires: jakarta-taglibs-standard >= 0:1.1.0
# formerly non-free stuff
# geronimo-specs replaces non-free jta
#BuildRequires: geronimo-jta-1.0.1B-api
BuildRequires: jta >= 0:1.0.1
# jaf can be provided by classpathx-jaf
#BuildRequires: jaf >= 0:1.0.2
BuildRequires: jaf >= 0:1.0.1
# javamail can be provided by classpathx-mail
#BuildRequires: javamail >= 0:1.3.3
BuildRequires: javamail >= 0:1.3.1
%if %{gcj_support}
# libgcj aot-compiled native libraries
BuildRequires:    	java-gcj-compat-devel >= 0:1.0.43
Requires(post):   	java-gcj-compat >= 0:1.0.31
Requires(postun): 	java-gcj-compat >= 0:1.0.31
%endif
%endif

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
Requires(post): %{name} = %{epoch}:%{version}-%{release}
Requires: jakarta-taglibs-standard >= 0:1.1.0
Summary: Web applications for Jakarta Tomcat

%description webapps
Web applications for Jakarta Tomcat

%package admin-webapps
Group: Development/Java
Requires(post): %{name} = %{epoch}:%{version}-%{release}
Requires: struts >= 0:1.1
Summary: The administrative web applications for Jakarta Tomcat

%description admin-webapps
The administrative web applications (admin and manager) for Jakarta Tomcat
%endif

%package servlet-%{servletspec}-api
Group: Development/Java
Requires: /usr/sbin/update-alternatives
Summary: Jakarta Tomcat Servlet implementation classes
Obsoletes: servletapi5
Provides: servlet
Provides: servlet5
Provides: servlet24
Provides: servletapi5
%if %{gcj_support}
# libgcj aot-compiled native libraries
Requires(post):   	java-gcj-compat >= 0:1.0.31
Requires(postun): 	java-gcj-compat >= 0:1.0.31
%endif

%description servlet-%{servletspec}-api
Contains the implementation classes
of the Jakarta Tomcat Servlet API (packages javax.servlet).

%package servlet-%{servletspec}-api-javadoc
Group: Development/Java
Summary: Javadoc generated documentation for %{name}-servlet-%{servletspec}-api
Obsoletes: servletapi5-javadoc
Provides: servletapi5-javadoc
%if %{gcj_support}
# libgcj aot-compiled native libraries
Requires(post):   	java-gcj-compat >= 0:1.0.31
Requires(postun): 	java-gcj-compat >= 0:1.0.31
%endif
Requires(post): coreutils
Requires(postun): coreutils

%description servlet-%{servletspec}-api-javadoc
Contains the javadoc generated documentation for the implementation classes
of the Jakarta Tomcat Servlet and JSP APIs (packages javax.servlet).

%package jsp-%{jspspec}-api
Group: Development/Java
Requires: /usr/sbin/update-alternatives
Requires: servlet24
# We need this to indirectly get rid of legacy jsp included in old
# servlet packages (one day we will be able to remove this)
Requires(post): %{name}-servlet-%{servletspec}-api = %{epoch}:%{version}-%{release}
Summary: Jakarta Tomcat Servlet and JSP implementation classes
Provides: jsp
%if %{gcj_support}
# libgcj aot-compiled native libraries
Requires(post):   	java-gcj-compat >= 0:1.0.31
Requires(postun): 	java-gcj-compat >= 0:1.0.31
%endif

%description jsp-%{jspspec}-api
Contains the implementation classes
of the Jakarta Tomcat JSP API (packages javax.servlet.jsp).

%package jsp-%{jspspec}-api-javadoc
Group: Development/Java
Summary: Javadoc generated documentation for %{name}-jsp-%{jspspec}-api
%if %{gcj_support}
# libgcj aot-compiled native libraries
Requires(post):   	java-gcj-compat >= 0:1.0.31
Requires(postun): 	java-gcj-compat >= 0:1.0.31
%endif
Requires(post): coreutils
Requires(postun): coreutils

%description jsp-%{jspspec}-api-javadoc
Contains the javadoc generated documentation for the implementation classes
of the Jakarta Tomcat JSP API (packages javax.servlet.jsp).

%if %{without_apisonly}
%package common-lib
Group: Development/Java
Summary: Libraries needed to run the Tomcat Web container (part)
Requires: java >= 0:1.4.2
Requires(post): jpackage-utils >= 0:1.6.0
Requires: ant >= 0:1.6
Requires(post): ant >= 0:1.6
Requires: jakarta-commons-collections >= 0:3.1
Requires(post): jakarta-commons-collections >= 0:3.1
Requires: jakarta-commons-dbcp >= 0:1.2.1
Requires(post): jakarta-commons-dbcp >= 0:1.2.1
Requires: jakarta-commons-el >= 0:1.0
Requires(post): jakarta-commons-el >= 0:1.0
Requires: jakarta-commons-logging >= 0:1.0.4
Requires(post): jakarta-commons-logging >= 0:1.0.4
# FIXME commons-pool is not listed in the Tomcat build.properties.default
Requires: jakarta-commons-pool >= 0:1.2
Requires(post): jakarta-commons-pool >= 0:1.2
# jaf can be provided by classpathx-jaf
Requires: jaf >= 0:1.0.1
Requires(post): jaf >= 0:1.0.1
# javamail can be provided by classpathx-mail
Requires: javamail >= 0:1.3.1
Requires(post): javamail >= 0:1.3.1
Requires: jdbc-stdext
Requires(post): jdbc-stdext
Requires: jndi
Requires(post): jndi
# geronimo-specs replaces non-free jta
#Requires: geronimo-jta-1.0.1B-api
Requires: jta >= 0:1.0.1
#Requires(post): geronimo-jta-1.0.1B-api
Requires(post): jta >= 0:1.0.1
Requires: mx4j >= 0:3.0.1
Requires(post): mx4j >= 0:3.0.1
%if %{with_ecj}
Requires: eclipse-ecj >= 0:3.1.1
Requires(post): eclipse-ecj >= 0:3.1.1
%endif
# Other subpackages must go in first
Requires(post): %{name}-servlet-%{servletspec}-api = %{epoch}:%{version}-%{release}
Requires(post): %{name}-jsp-%{jspspec}-api = %{epoch}:%{version}-%{release}
Requires(post): %{name}-%{jname} = %{epoch}:%{version}-%{release}
Requires: %{name}-servlet-%{servletspec}-api = %{epoch}:%{version}-%{release}
Requires: %{name}-jsp-%{jspspec}-api = %{epoch}:%{version}-%{release}
Requires: %{name}-%{jname} = %{epoch}:%{version}-%{release}
%if %{gcj_support}
# libgcj aot-compiled native libraries
Requires(post):   	java-gcj-compat >= 0:1.0.31
Requires(postun): 	java-gcj-compat >= 0:1.0.31
%endif

%description common-lib
Libraries needed to run the Tomcat Web container (part)

%package server-lib
Group: Development/Java
Summary: Libraries needed to run the Tomcat Web container (part)
Requires(post): jpackage-utils >= 0:1.6.0
Requires: jakarta-commons-beanutils >= 0:1.7.0
Requires(post): jakarta-commons-beanutils >= 0:1.7.0
Requires: jakarta-commons-digester >= 0:1.6
Requires(post): jakarta-commons-digester >= 0:1.6
Requires: jakarta-commons-el >= 0:1.0
Requires(post): jakarta-commons-el >= 0:1.0
Requires: jakarta-commons-fileupload >= 0:1.0-1jpp
Requires(post): jakarta-commons-fileupload >= 0:1.0-1jpp
Requires: jakarta-commons-logging >= 0:1.0.4
Requires(post): jakarta-commons-logging >= 0:1.0.4
Requires: jakarta-commons-modeler >= 1.1
Requires(post): jakarta-commons-modeler >= 1.1
Requires: jaas
Requires(post): jaas
Requires: mx4j >= 0:3.0.1
Requires(post): mx4j >= 0:3.0.1
Requires: regexp >= 0:1.3
Requires(post): regexp >= 0:1.3
# Other subpackages must go in first
Requires: %{name}-%{jname} = %{epoch}:%{version}-%{release}
Requires(post): %{name}-%{jname} = %{epoch}:%{version}-%{release}
%if %{gcj_support}
# libgcj aot-compiled native libraries
Requires(post):   	java-gcj-compat >= 0:1.0.31
Requires(postun): 	java-gcj-compat >= 0:1.0.31
%endif

%description server-lib
Libraries needed to run the Tomcat Web container (part)

%package %{jname}
Group: Development/Java
Requires: %{name}-servlet-%{servletspec}-api = %{epoch}:%{version}-%{release}
Summary: Compiler JARs and associated scripts for %{name}
Obsoletes: jasper5
Provides: jasper5
%if %{gcj_support}
# libgcj aot-compiled native libraries
Requires(post):   	java-gcj-compat >= 0:1.0.31
Requires(postun): 	java-gcj-compat >= 0:1.0.31
%endif

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

%prep
%if 0
cat <<EOT

                If you want only apis to be built,
                give rpmbuild option '--with apisonly'

		If you don''t want direct ecj support to be built in,
		while eclipse-ecj isn''t available,
		give rpmbuild option '--without ecj'


EOT
%endif

rm -rf $RPM_BUILD_DIR/%{name}-%{version}

%setup -q -c -T -a 0

cd %{packdname}
%patch0 -b .p0
%patch1 -b .p1
%patch2 -b .p2
%patch3 -b .p3
%patch4 -b .p4
%patch5 -b .p5
#%patch6 -p1
%patch7 -b .p7
%patch8 -b .p8
%patch9 -b .p9
%patch10 -b .p10
# omit jdtcompilerpatch for eclipse-ecj >= 3.1
#%patch11 -b .p11
%patch12 -b .p12
%patch13 -b .p13
%patch14 -b .p14
#%patch15 -b .p15
%patch16 -b .p16
#%patch17 -b .p17
%ifarch ppc64 s390x
%patch18 -b .p18
%endif

%patch100 -b .p100

%if %{without_ecj}
rm %{jname}/src/share/org/apache/jasper/compiler/JDTCompiler.java
%endif

%build
#clp#export CLASSPATH=$(build-classpath xml-commons-apis xalan-j2 xalan-j2-serializer)

# Remove pre-built jars
for dir in $RPM_BUILD_DIR/%{name}-%{version}/%{packdname} ; do
    find $dir -name "*.jar" | xargs -t rm -f
done

# Remove garbled class files
pushd $RPM_BUILD_DIR/%{name}-%{version}/%{packdname}
    rm -rf connectors/jk/jkstatus/build
popd

pushd $RPM_BUILD_DIR/%{name}-%{version}/%{packdname}
    cp build/LICENSE .
popd 

# build jspapi and servletapi as ant dist will require them later
pushd $RPM_BUILD_DIR/%{name}-%{version}/%{packdname}/servletapi
    pushd jsr154
        %ant -Dservletapi.build=build \
            -Dservletapi.dist=dist \
            -Dbuild.compiler=modern dist
    popd
    pushd jsr152
        %ant -Dservletapi.build=build \
            -Dservletapi.dist=dist \
            -Dbuild.compiler=modern dist
    popd
popd

%if %{without_apisonly}
# build jasper subpackage
#clp#CLASSPATH=$(build-classpath xml-commons-apis xalan-j2 xalan-j2-serializer)
#clp#export CLASSPATH=$CLASSPATH:$RPM_BUILD_DIR/%{name}-%{version}/%{packdname}/jakarta-servletapi-5/jsr154/dist/lib/servlet-api.jar
pushd $RPM_BUILD_DIR/%{name}-%{version}/%{packdname}/%{jname}
    cat > build.properties <<EOBP
ant.jar=$(build-classpath ant)
servlet-api.jar=$RPM_BUILD_DIR/%{name}-%{version}/%{packdname}/servletapi/jsr154/dist/lib/servlet-api.jar
jsp-api.jar=$RPM_BUILD_DIR/%{name}-%{version}/%{packdname}/servletapi/jsr152/dist/lib/jsp-api.jar
tools.jar=%{java.home}/lib/tools.jar
xerces.jar=$(build-classpath xerces-j2)
xercesImpl.jar=$(build-classpath jaxp_parser_impl)
xmlParserAPIs.jar=$(build-classpath xml-commons-apis)
commons-el.jar=$(build-classpath commons-el)
commons-collections.jar=$(build-classpath commons-collections)
commons-logging.jar=$(build-classpath commons-logging)
commons-daemon.jar=$(build-classpath commons-daemon)
junit.jar=$(build-classpath junit)
jasper-compiler-jdt.jar=$(build-classpath jdtcore)
EOBP
    # can't use jikes to build tomcat4 (strange)
    %ant -Djava.home=%{java_home} -Dbuild.compiler=modern javadoc
popd

# build tomcat 5
pushd $RPM_BUILD_DIR/%{name}-%{version}/%{packdname}/build
    cat >> build.properties << EOBP
ant.jar=%{_javadir}/ant.jar
ant-launcher.jar=%{_javadir}/ant.jar
jtc.home=$RPM_BUILD_DIR/%{name}-%{version}/%{packdname}/connectors/
%{jname}.home=$RPM_BUILD_DIR/%{name}-%{version}/%{packdname}/%{jname}
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
servlet-api.jar=$RPM_BUILD_DIR/%{name}-%{version}/%{packdname}/servletapi/jsr154/dist/lib/servlet-api.jar
jsp-api.jar=$RPM_BUILD_DIR/%{name}-%{version}/%{packdname}/servletapi/jsr152/dist/lib/jsp-api.jar
servlet.doc=$RPM_BUILD_DIR/%{name}-%{version}/%{packdname}/servletapi/jsr154/dist/docs/api
xercesImpl.jar=$(build-classpath jaxp_parser_impl)
xml-apis.jar=$(build-classpath xml-commons-apis)
struts.jar=$(build-classpath struts)
struts.lib=%{_datadir}/struts
activation.jar=$(build-classpath jaf)
mail.jar=$(build-classpath javamail/mailapi)
jta.jar=$(build-classpath jta)
jaas.jar=$(build-classpath jaas)
jndi.jar=$(build-classpath jndi)
jdbc20ext.jar=$(build-classpath jdbc-stdext)
jcert.jar=$(build-classpath jsse/jcert)
jnet.jar=$(build-classpath jsse/jnet)
jsse.jar=$(build-classpath jsse/jsse)
servletapi.build.notrequired=true
jspapi.build.notrequired=true
EOBP
export CLASSPATH=$RPM_BUILD_DIR/%{name}-%{version}/%{packdname}/servletapi/jsr154/dist/lib/servlet-api.jar
# can't use jikes to build tomcat4 (strange)
    %ant -Dbuild.compiler=modern -Djava.home=%{java_home} build
popd

# build the connectors
pushd $RPM_BUILD_DIR/%{name}-%{version}/%{packdname}/connectors
# use the JARs created above to build
export CLASSPATH=$RPM_BUILD_DIR/%{name}-%{version}/%{packdname}/servletapi/jsr154/dist/lib/servlet-api.jar:$RPM_BUILD_DIR/%{name}-%{version}/%{packdname}/jakarta-tomcat-5/build/server/lib/catalina.jar
    cat > build.properties << EOBP
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
mail.jar=$(build-classpath javamail/mailapi)
#jta.jar=$(build-classpath geronimo-jta-1.0.1B-api)
jta.jar=$(build-classpath jta)
jaas.jar=$(build-classpath jaas)
jndi.jar=$(build-classpath jndi)
jdbc20ext.jar=$(build-classpath jdbc-stdext)
jcert.jar=$(build-classpath jsse/jcert)
jnet.jar=$(build-classpath jsse/jnet)
jsse.jar=$(build-classpath jsse/jsse)
tomcat5.home=../../build/build
EOBP
    %ant -Dbuild.compiler=modern -Djava.home=%{java_home} build
popd
%endif

%install
rm -rf $RPM_BUILD_ROOT

install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
%if %{without_apisonly}
CLASSPATH=$(build-classpath xalan-j2 xalan-j2-serializer xml-commons-apis jakarta-taglibs-core jakarta-taglibs-standard mx4j/mx4j-jmx struts)
export CLASSPATH=$CLASSPATH:$RPM_BUILD_DIR/%{name}-%{version}/%{packdname}/servletapi/jsr152/dist/lib/jsp-api.jar:$RPM_BUILD_DIR/%{name}-%{version}/%{packdname}/servletapi/jsr154/dist/lib/servlet-api.jar
# build initial path structure
install -d -m 755 $RPM_BUILD_ROOT{%{confdir},%{logdir},%{homedir},%{bindir}}
install -d -m 755 $RPM_BUILD_ROOT{%{serverdir},%{tempdir},%{workdir}}
install -d -m 755 $RPM_BUILD_ROOT{%{appdir},%{commondir},%{shareddir}}
install -d -m 755 $RPM_BUILD_ROOT%{_sysconfdir}/{init.d,logrotate.d}
install -d -m 755 $RPM_BUILD_ROOT%{_bindir}
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -m 755 %{SOURCE5} $RPM_BUILD_ROOT/%{bindir}/relink
# SysV init and configuration
install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/init.d/%{name}
install %{SOURCE2} $RPM_BUILD_ROOT%{confdir}/%{name}.conf
pushd $RPM_BUILD_DIR/%{name}-%{version}/%{packdname}/build
    export usejikes=false
    export OPT_JAR_LIST="ant/ant-trax xalan-j2 xalan-j2-serializer"
    %ant -Dbuild.compiler=modern -Djava.home=%{java_home} dist
    pushd dist
        mv bin/* $RPM_BUILD_ROOT%{bindir}
        mv common/* $RPM_BUILD_ROOT%{commondir}
        mv conf/* $RPM_BUILD_ROOT%{confdir}
        mv server/* $RPM_BUILD_ROOT%{serverdir}
        mv shared/* $RPM_BUILD_ROOT%{shareddir}
        mv webapps/* $RPM_BUILD_ROOT%{appdir}
    popd
    pushd build/conf
	mv jk2.properties jk2.manifest jkconf.ant.xml jkconfig.manifest \
           shm.manifest tomcat-jk2.manifest uriworkermap.properties \
           workers.properties workers.properties.minimal workers2.properties \
           workers2.properties.minimal \
             $RPM_BUILD_ROOT%{confdir}
    popd
popd
# create reloctomcat5 (is this really necessary anymore?)
cat >> $RPM_BUILD_ROOT%{bindir}/reloctomcat5 << EORLTC
#!/bin/sh
#

echo "relocating http & ajp ports to 81xx"

sed -e 's;8080;8180;' \
    -e 's;8081;8181;' \
    -e 's;8082;8182;' \
    -e 's;8443;8543;' \
    -e 's;8009;8109;' \
    %{confdir}/server.xml > %{confdir}/server.xml.reloc

mv %{confdir}/server.xml %{confdir}/server.xml.bak
cp %{confdir}/server.xml.reloc %{confdir}/server.xml

EORLTC
# rename catalina.sh into dtomcat5 to let wrapper take precedence
install $RPM_BUILD_ROOT%{bindir}/catalina.sh \
    $RPM_BUILD_ROOT%{_bindir}/d%{name}
rm -f $RPM_BUILD_ROOT%{bindir}/catalina.sh.*
# Remove leftover files
rm -f $RPM_BUILD_ROOT%{bindir}/*.orig
# install wrapper as tomcat5
install %{SOURCE3} $RPM_BUILD_ROOT%{_bindir}/%{name}
# install logrotate support
install %{SOURCE4} ${RPM_BUILD_ROOT}%{_sysconfdir}/logrotate.d/%{name}
# remove / reorder non-usefull stuff
rm -rf $RPM_BUILD_ROOT%{homedir}/src/
rm -f  $RPM_BUILD_ROOT%{bindir}/*.sh $RPM_BUILD_ROOT%{bindir}/*.bat
# FHS compliance patches, not easy to track them all boys :)
for i in $RPM_BUILD_ROOT%{confdir}/%{name}.conf \
         $RPM_BUILD_ROOT%{_bindir}/d%{name} \
         $RPM_BUILD_ROOT%{_bindir}/%{name} \
         $RPM_BUILD_ROOT%{_sysconfdir}/init.d/%{name} \
         $RPM_BUILD_ROOT%{bindir}/relink \
         $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/%{name}; do
    perl -pi -e "s|\@\@\@TCCONF\@\@\@|%{confdir}|g;" $i
    perl -pi -e "s|\@\@\@TCHOME\@\@\@|%{homedir}|g;" $i
    perl -pi -e "s|\@\@\@TCBIN\@\@\@|%{bindir}|g;" $i
    perl -pi -e "s|\@\@\@TCCOMMON\@\@\@|%{commondir}|g;" $i
    perl -pi -e "s|\@\@\@TCSERVER\@\@\@|%{serverdir}|g;" $i
    perl -pi -e "s|\@\@\@TCSHARED\@\@\@|%{shareddir}|g;" $i
    perl -pi -e "s|\@\@\@TCAPP\@\@\@|%{appdir}|g;" $i
    perl -pi -e "s|\@\@\@TCLOG\@\@\@|%{logdir}|g;" $i
done
# Remove local JARs (to be replaced with jpp links in post)
pushd $RPM_BUILD_ROOT%{serverdir}/lib
    find . -name "*.jar" -not -name "catalina*" \
                         -not -name "servlets-*" \
                         -not -name "tomcat-*" | xargs -t rm -f
    # catalina-ant will be installed in a public repository
    mv catalina-ant.jar $RPM_BUILD_ROOT%{_javadir}/catalina-ant-%{version}.jar
    pushd $RPM_BUILD_ROOT%{_javadir}
        ln -fs catalina-ant-%{version}.jar catalina-ant5.jar
    popd
    # catalina* jars will be installed in a public repository
    for i in catalina*.jar; do
        j=`echo $i | sed 's:\.jar$::'`
        mv $j.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/$j-%{version}.jar
        pushd $RPM_BUILD_ROOT%{_javadir}/%{name}
            ln -sf $j-%{version}.jar $j.jar
        popd
        ln -sf %{_javadir}/%{name}/$j.jar $j.jar
    done
    # servlets* jars will be installed in a public repository
    for i in servlets-*.jar; do
        j=`echo $i | sed 's:\.jar$::'`
        mv $j.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/$j-%{version}.jar
        pushd $RPM_BUILD_ROOT%{_javadir}/%{name}
            ln -sf $j-%{version}.jar $j.jar
        popd
        ln -sf %{_javadir}/%{name}/$j.jar $j.jar
    done
    # tomcat* jars will be installed in a public repository
    for i in tomcat-*.jar; do
        j=`echo $i | sed 's:\.jar$::'`
        mv $j.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/$j-%{version}.jar
        pushd $RPM_BUILD_ROOT%{_javadir}/%{name}
            ln -sf $j-%{version}.jar $j.jar
        popd
        ln -sf %{_javadir}/%{name}/$j.jar $j.jar
    done
popd
# Process admin webapp server/webapps/admin
pushd $RPM_BUILD_ROOT%{serverdir}/webapps/admin/WEB-INF/lib
    find . -name "*.jar" -not -name 'catalina-admin*' | xargs -t rm -f
    for i in catalina-admin; do
        cp $i.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/$i-%{version}.jar
        pushd $RPM_BUILD_ROOT%{_javadir}/%{name}
            ln -sf $i-%{version}.jar $i.jar
        popd
    done
popd
# Process manager webapp server/webapps/manager
pushd $RPM_BUILD_ROOT%{serverdir}/webapps/manager/WEB-INF/lib
    for i in catalina-manager; do
        cp $i.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/$i-%{version}.jar
        pushd $RPM_BUILD_ROOT%{_javadir}/%{name}
            ln -sf $i-%{version}.jar $i.jar
        popd
    done
popd
# Process host-manager webapp server/webapps/host-manager
pushd $RPM_BUILD_ROOT%{serverdir}/webapps/host-manager/WEB-INF/lib
    for i in catalina-host-manager; do
        cp $i.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/$i-%{version}.jar
        pushd $RPM_BUILD_ROOT%{_javadir}/%{name}
            ln -sf $i-%{version}.jar $i.jar
        popd
    done
popd
# Process common/lib
pushd $RPM_BUILD_ROOT%{commondir}/lib
    find . -name "*.jar" -not -name "%{jname}*" \
                         -not -name "naming*" | xargs -t rm -f
    # jasper's jars will be installed in a public repository
    for i in %{jname}-compiler %{jname}-runtime; do
        j=`echo $i | sed 's:%{jname}-:%{jname}5-:'`
        mv $i.jar $RPM_BUILD_ROOT%{_javadir}/$j-%{version}.jar
        pushd $RPM_BUILD_ROOT%{_javadir}
            ln -sf $j-%{version}.jar $j.jar
        popd
    done
    # naming* jars will be installed in a public repository
    for i in naming-*.jar; do
        j=`echo $i | sed 's:\.jar$::'`
        mv $j.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/$j-%{version}.jar
        pushd $RPM_BUILD_ROOT%{_javadir}/%{name}
            ln -sf $j-%{version}.jar $j.jar
        popd
        ln -sf %{_javadir}/%{name}/$j.jar $j.jar
    done
popd
# Process common/endorsed
pushd $RPM_BUILD_ROOT%{commondir}/endorsed
    find . -name "*.jar" | xargs -t rm -f
popd
# avoid duplicate servlet.jar
rm -f $RPM_BUILD_ROOT%{commondir}/lib/servlet.jar
# Perform FHS translation
# (final links)
pushd $RPM_BUILD_ROOT%{homedir}
    [ -d bin ] || ln -fs %{bindir} bin
    [ -d common ] || ln -fs %{commondir} common
    [ -d conf ] || ln -fs %{confdir} conf
    [ -d logs ] || ln -fs %{logdir} logs
    [ -d server ] || ln -fs %{serverdir} server
    [ -d shared ] || ln -fs %{shareddir} shared
    [ -d webapps ] || ln -fs %{appdir} webapps
    [ -d work ] || ln -fs %{workdir} work
    [ -d temp ] || ln -fs %{tempdir} temp
popd
cd $RPM_BUILD_DIR/%{name}-%{version}/%{packdname}
find $RPM_BUILD_ROOT%{homedir} -type l -maxdepth 1 | \
    sed s+$RPM_BUILD_ROOT++g > homelinks
%endif
# begin servlet api subpackage install
pushd $RPM_BUILD_DIR/%{name}-%{version}/%{packdname}/servletapi
    install -m 644 jsr154/dist/lib/servlet-api.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}-servlet-%{servletspec}-api-%{version}.jar
    pushd $RPM_BUILD_ROOT%{_javadir}
        ln -sf %{name}-servlet-%{servletspec}-api-%{version}.jar \
            %{name}-servlet-%{servletspec}-api.jar
        # For backward compatibility with old JPP packages
        ln -sf %{name}-servlet-%{servletspec}-api-%{version}.jar \
            servletapi5.jar
    popd
    # javadoc servlet
    install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-servlet-%{servletspec}-api-%{version}
    cp -pr jsr154/build/docs/api/* \
        $RPM_BUILD_ROOT%{_javadocdir}/%{name}-servlet-%{servletspec}-api-%{version}
    # ghost symlink
    ln -s %{name}-servlet-%{servletspec}-api-%{version} \
        $RPM_BUILD_ROOT%{_javadocdir}/%{name}-servlet-%{servletspec}-api
popd
# begin jsp api subpackage install
pushd $RPM_BUILD_DIR/%{name}-%{version}/%{packdname}/servletapi
    install -m 644 jsr152/dist/lib/jsp-api.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}-jsp-%{jspspec}-api-%{version}.jar
    pushd $RPM_BUILD_ROOT%{_javadir}
        ln -sf %{name}-jsp-%{jspspec}-api-%{version}.jar \
            %{name}-jsp-%{jspspec}-api.jar
        # For backward compatibility with old JPP packages
        ln -sf %{name}-jsp-%{jspspec}-api-%{version}.jar \
            jspapi.jar
    popd
    # javadoc jsp
    install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-jsp-%{jspspec}-api-%{version}
    cp -pr jsr152/build/docs/api/* \
        $RPM_BUILD_ROOT%{_javadocdir}/%{name}-jsp-%{jspspec}-api-%{version}
    # ghost symlink
    ln -s %{name}-jsp-%{jspspec}-api-%{version} \
        $RPM_BUILD_ROOT%{_javadocdir}/%{name}-jsp-%{jspspec}-api
popd
%if %{without_apisonly}
# begin jasper subpackage install
pushd $RPM_BUILD_DIR/%{name}-%{version}/%{packdname}/%{jname}
    install -m755 src/bin/jspc.sh \
        $RPM_BUILD_ROOT%{_bindir}/jspc5.sh
    install -m755 src/bin/%{jname}.sh \
        $RPM_BUILD_ROOT%{_bindir}/%{full_jname}.sh
popd
pushd $RPM_BUILD_DIR/%{name}-%{version}/%{packdname}/container
    install -m755 catalina/src/bin/setclasspath.sh \
        $RPM_BUILD_ROOT%{_bindir}/%{full_jname}-setclasspath.sh
popd
# javadoc
install -d -m755 $RPM_BUILD_ROOT%{_javadocdir}/%{jname}-%{version}
pushd $RPM_BUILD_DIR/%{name}-%{version}/%{packdname}/%{jname}
    cp -pr build/javadoc/* \
        $RPM_BUILD_ROOT%{_javadocdir}/%{jname}-%{version}
    # ghost symlink
    ln -s %{jname}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{jname}
popd

# disable the juli log manager until the classpath
# java.util.logging.LogManager is fixed
rm -f $RPM_BUILD_ROOT%{bindir}/tomcat-juli.jar

%endif

# sample.war is a malformed zip file
%if %{gcj_support}
#aot-compile-rpm --exclude /var/lib/tomcat5/webapps/tomcat-docs/appdev/sample/sample.war
%{_bindir}/aot-compile-rpm
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{without_apisonly}
%post
# install tomcat5 (but don't activate)
/sbin/chkconfig --add %{name}
# Create automated links - since all needed extensions may not have been
# installed for this jvm output is muted
# Try to set a sensible jvm
unset JAVA_HOME
[ -r %{confdir}/tomcat5.conf ] && . %{confdir}/tomcat5.conf
[ -z "$JAVA_HOME" ] && [ -r %{_sysconfdir}/java/java.conf ] && \
    . %{_sysconfdir}/java/java.conf
[ -z "$JAVA_HOME" ] && JAVA_HOME=%{_jvmdir}/java
# Remove old automated symlinks
for repository in %{commondir}/endorsed ; do
    find $repository -name '\[*\]*.jar' -not -type d | xargs rm -f
done
build-jar-repository %{commondir}/endorsed jaxp_parser_impl \
                                           xml-commons-apis 2>&1
build-jar-repository %{bindir} mx4j/mx4j 2>&1
%{update_gcjdb}

%postun
%{clean_gcjdb}

%post common-lib
# Create automated links - since all needed extensions may not have been
# installed for this jvm output is muted
# Try to set a sensible jvm
unset JAVA_HOME
[ -r %{confdir}/tomcat5.conf ] && . %{confdir}/tomcat5.conf
[ -z "$JAVA_HOME" ] && [ -r %{_sysconfdir}/java/java.conf ] && \
    . %{_sysconfdir}/java/java.conf
[ -z "$JAVA_HOME" ] && JAVA_HOME=%{_jvmdir}/java
# Remove old automated symlinks
for repository in %{commondir}/lib ; do
    find $repository -name '\[*\]*.jar' -not -type d | xargs rm -f
done
build-jar-repository %{commondir}/lib ant commons-collections commons-dbcp \
                                      commons-el commons-logging-api \
                                      commons-pool jaf javamail jdbc-stdext \
                                      jndi jsp \
                                      mx4j/mx4j \
                                      servlet %{jname}5-compiler \
                                      %{jname}5-runtime 2>&1
#build-jar-repository %{commondir}/lib geronimo-jta-1.0.1B-api 2>&1
build-jar-repository %{commondir}/lib jta 2>&1
%if %{with_ecj}
pushd %{commondir}/lib > /dev/null
ln -sf %{_javadir}/jdtcore.jar .
popd > /dev/null
%endif
%{update_gcjdb}

%postun common-lib
%{clean_gcjdb}

%post server-lib
# Create automated links - since all needed extensions may not have been
# installed for this jvm output is muted
# Try to set a sensible jvm
unset JAVA_HOME
[ -r %{confdir}/tomcat5.conf ] && . %{confdir}/tomcat5.conf
[ -z "$JAVA_HOME" ] && [ -r %{_sysconfdir}/java/java.conf ] && \
    . %{_sysconfdir}/java/java.conf
[ -z "$JAVA_HOME" ] && JAVA_HOME=%{_jvmdir}/java
# Remove old automated symlinks
for repository in %{serverdir}/lib ; do
    find $repository -name '\[*\]*.jar' -not -type d | xargs rm -f
done
build-jar-repository %{serverdir}/lib catalina-ant5 commons-beanutils \
                                      commons-digester commons-el \
                                      commons-fileupload commons-logging \
                                      commons-modeler jaas mx4j/mx4j \
                                      regexp 2>&1
%if %{with_ecj}
pushd %{serverdir}/lib > /dev/null
ln -sf %{_javadir}/jdtcore.jar .
popd > /dev/null
%endif
%{update_gcjdb}

%postun server-lib
%{clean_gcjdb}

%post webapps 
# Create automated links - since all needed extensions may not have been
# installed for this jvm output is muted
# Try to set a sensible jvm
unset JAVA_HOME
[ -r %{confdir}/tomcat5.conf ] && . %{confdir}/tomcat5.conf
[ -z "$JAVA_HOME" ] && [ -r %{_sysconfdir}/java/java.conf ] && \
    . %{_sysconfdir}/java/java.conf
[ -z "$JAVA_HOME" ] && JAVA_HOME=%{_jvmdir}/java
build-jar-repository %{appdir}/jsp-examples/WEB-INF/lib \
      jakarta-taglibs-core jakarta-taglibs-standard 2>&1
%{update_gcjdb}

%postun webapps
%{clean_gcjdb}

%post admin-webapps
# Create automated links - since all needed extensions may not have been
# installed for this jvm output is muted
# Try to set a sensible jvm
unset JAVA_HOME
[ -r %{confdir}/tomcat5.conf ] && . %{confdir}/tomcat5.conf
[ -z "$JAVA_HOME" ] && [ -r %{_sysconfdir}/java/java.conf ] && \
    . %{_sysconfdir}/java/java.conf
[ -z "$JAVA_HOME" ] && JAVA_HOME=%{_jvmdir}/java
# Remove old automated symlinks
find %{serverdir}/webapps/admin/WEB-INF/lib -name '\[*\]*.jar' \
     -not -name 'catalina-admin*' -not -type d | xargs rm -f
build-jar-repository %{serverdir}/webapps/admin/WEB-INF/lib struts 2>&1
%{update_gcjdb}

%postun admin-webapps
%{clean_gcjdb}
%endif

%post servlet-%{servletspec}-api
update-alternatives --install %{_javadir}/servlet.jar servlet \
    %{_javadir}/%{name}-servlet-%{servletspec}-api.jar 20400
%{update_gcjdb}

%post servlet-%{servletspec}-api-javadoc
rm -f %{_javadocdir}/servletapi # legacy symlink
rm -f %{_javadocdir}/%{name}-servlet-%{servletspec}-api
ln -s %{name}-servlet-%{servletspec}-api-%{version} \
    %{_javadocdir}/%{name}-servlet-%{servletspec}-api
%{update_gcjdb}

%postun servlet-%{servletspec}-api
if [ "$1" = "0" ]; then
    update-alternatives --remove servlet \
        %{_javadir}/%{name}-servlet-%{servletspec}-api.jar
fi
%{clean_gcjdb}

%post jsp-%{jspspec}-api
update-alternatives --install %{_javadir}/jsp.jar jsp \
    %{_javadir}/%{name}-jsp-%{jspspec}-api.jar 20000
%{update_gcjdb}

%post jsp-%{jspspec}-api-javadoc
rm -f %{_javadocdir}/jsp-api # legacy symlink
rm -f %{_javadocdir}/%{name}-jsp-%{jspspec}-api
ln -s %{name}-jsp-%{jspspec}-api-%{version} \
    %{_javadocdir}/%{name}-jsp-%{jspspec}-api

%postun jsp-%{jspspec}-api
if [ "$1" = "0" ]; then
    update-alternatives --remove jsp \
        %{_javadir}/%{name}-jsp-%{jspspec}-api.jar
fi
%{clean_gcjdb}

%if %{without_apisonly}
%preun
# Always clean up workdir and tempdir on upgrade/removal
rm -fr %{workdir}/* %{tempdir}/*
if [ $1 = 0 ]; then
    [ -f /var/lock/subsys/%{name} ] && %{_sysconfdir}/init.d/%{name} stop
    [ -f %{_sysconfdir}/init.d/%{name} ] && /sbin/chkconfig --del %{name}
    # Remove automated symlinks
    for repository in %{commondir}/endorsed ; do
        find $repository -name '\[*\]*.jar' -not -type d | xargs rm -f
    done
fi

%preun server-lib
if [ $1 = 0 ]; then
    # Remove automated symlinks
    for repository in %{serverdir}/lib ; do
        find $repository -name '\[*\]*.jar' -not -type d | xargs rm -f
    done
fi

%preun common-lib
if [ $1 = 0 ]; then
    # Remove automated symlinks
    for repository in %{commondir}/lib ; do
        find $repository -name '\[*\]*.jar' -not -type d | xargs rm -f
    done
fi

%preun admin-webapps
if [ $1 = 0 ]; then
    find %{serverdir}/webapps/admin/WEB-INF/lib  \
         -name '\[*\]*.jar' \
         -not -name 'catalina-admin*' -not -type d | xargs rm -f
fi

%preun webapps
if [ $1 = 0 ]; then
    find %{appdir}/jsp-examples/WEB-INF/lib  \
         -name '\[*\]*.jar' \
         -not -type d | xargs rm -f
fi

%pre
# Add the "tomcat" user and group
# we need a shell to be able to use su - later
%{_sbindir}/groupadd -g %{tcuid} -r tomcat 2> /dev/null || :
%{_sbindir}/useradd -c "Tomcat" -u %{tcuid} -g tomcat \
    -s /bin/sh -r -d %{homedir} tomcat 2> /dev/null || :
%endif

%if %{without_apisonly}
%files -f %{packdname}/homelinks
%defattr(644,root,root,755)
%doc %{packdname}/build/{LICENSE,RELE*,RUNNING.txt,BENCHMARKS.txt}
# Normal directories
%dir %{homedir}
%dir %{bindir}
%dir %{_localstatedir}/lib/%{name}
%dir %{_localstatedir}/cache/%{name}
%dir %{commondir}
%dir %{commondir}/classes
%dir %{commondir}/lib
%dir %{commondir}/endorsed
%dir %{commondir}/i18n
%dir %{serverdir}/
%dir %{serverdir}/classes
%dir %{serverdir}/lib
%dir %{shareddir}
%dir %{shareddir}/classes
%dir %{shareddir}/lib
# Directories with special permissions
%attr(775,root,tomcat) %dir %{appdir}
%attr(775,root,tomcat) %dir %{confdir}
%attr(775,root,tomcat) %dir %{tempdir}
%attr(775,root,tomcat) %dir %{workdir}
%attr(755,tomcat,tomcat) %dir %{logdir}
%attr(775,root,tomcat) %dir %{confdir}/Catalina
%attr(775,root,tomcat) %dir %{confdir}/Catalina/localhost
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{bindir}/*
%attr(755,root,root) %{_sysconfdir}/init.d/%{name}
%attr(644,root,tomcat) %config(noreplace) %{confdir}/catalina.policy
%attr(644,root,tomcat) %config(noreplace) %{confdir}/catalina.properties
%attr(660,root,tomcat) %config(noreplace) %{confdir}/jk2.properties
%attr(660,root,tomcat) %config(noreplace) %{confdir}/logging.properties
%attr(660,root,tomcat) %config(noreplace) %{confdir}/tomcat-users.xml
%config(noreplace) %{confdir}/tomcat5.conf
%config(noreplace) %{confdir}/server-minimal.xml
%config(noreplace) %{confdir}/server.xml
%config(noreplace) %{confdir}/web.xml
%config(noreplace) %{confdir}/context.xml
%config(noreplace) %{confdir}/jk2.manifest
%config(noreplace) %{confdir}/jkconf.ant.xml
%config(noreplace) %{confdir}/jkconfig.manifest
%config(noreplace) %{confdir}/shm.manifest
%config(noreplace) %{confdir}/tomcat-jk2.manifest
%config(noreplace) %{confdir}/uriworkermap.properties
%config(noreplace) %{confdir}/workers.properties
%config(noreplace) %{confdir}/workers.properties.minimal
%config(noreplace) %{confdir}/workers2.properties
%config(noreplace) %{confdir}/workers2.properties.minimal
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%{commondir}/i18n/*
%if %{gcj_support}
%attr(-,root,root) %{_libdir}/gcj/%{name}/bootstrap*
%attr(-,root,root) %{_libdir}/gcj/%{name}/commons-daemon*
%attr(-,root,root) %{_libdir}/gcj/%{name}/commons-logging-api*
#%attr(-,root,root) %{_libdir}/gcj/%{name}/tomcat-juli*
%attr(-,root,root) %{_libdir}/gcj/%{name}/tomcat-jkstatus-ant*
%endif

%files common-lib
%defattr(644,root,root,755)
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/naming*.jar
%{commondir}/lib/*
%if %{gcj_support}
%attr(-,root,root) %{_libdir}/gcj/%{name}/naming-*
%endif

%files server-lib
%defattr(644,root,root,755)
%{_javadir}/catalina*.jar
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/catalina-ant-jmx*.jar
%{_javadir}/%{name}/catalina-cluster*.jar
%{_javadir}/%{name}/catalina.jar
%{_javadir}/%{name}/catalina-%{version}.jar
%{_javadir}/%{name}/catalina-optional*.jar
%{_javadir}/%{name}/catalina-storeconfig*.jar
%{_javadir}/%{name}/servlets*.jar
%{_javadir}/%{name}/tomcat*.jar
%{serverdir}/lib/*
%if %{gcj_support}
%attr(-,root,root) %{_libdir}/gcj/%{name}/catalina-ant*
%attr(-,root,root) %{_libdir}/gcj/%{name}/catalina-cluster*
%attr(-,root,root) %{_libdir}/gcj/%{name}/catalina-optional*
%attr(-,root,root) %{_libdir}/gcj/%{name}/catalina-storeconfig*
%attr(-,root,root) %{_libdir}/gcj/%{name}/catalina-%{version}.jar*
%attr(-,root,root) %{_libdir}/gcj/%{name}/servlets-cgi*
%attr(-,root,root) %{_libdir}/gcj/%{name}/servlets-default*
%attr(-,root,root) %{_libdir}/gcj/%{name}/servlets-invoker*
%attr(-,root,root) %{_libdir}/gcj/%{name}/servlets-ssi*
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
%attr(-,root,root) %{_libdir}/gcj/%{name}/applet*
%attr(-,root,root) %{_libdir}/gcj/%{name}/catalina-root*
%attr(-,root,root) %{_libdir}/gcj/%{name}/jsp-examples*
%attr(-,root,root) %{_libdir}/gcj/%{name}/sample*
%attr(-,root,root) %{_libdir}/gcj/%{name}/servlets-examples*
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
%attr(-,root,root) %{_libdir}/gcj/%{name}/commons-fileupload*
%endif

%files %{jname}
%defattr(644,root,root,755)
%doc $RPM_BUILD_DIR/%{name}-%{version}/%{packdname}/%{jname}/doc/jspc.html
%{_javadir}/%{jname}5-*.jar
%attr(755,root,root) %{_bindir}/%{jname}*.sh
%attr(755,root,root) %{_bindir}/jspc*.sh
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
%if %{gcj_support}
%attr(-,root,root) %{_libdir}/gcj/%{name}/%{name}-jsp-%{jspspec}-api*
%endif

%files jsp-%{jspspec}-api-javadoc
%defattr(-,root,root)
%doc %{_javadocdir}/%{name}-jsp-%{jspspec}-api-%{version}
%ghost %doc %{_javadocdir}/%{name}-jsp-%{jspspec}-api


