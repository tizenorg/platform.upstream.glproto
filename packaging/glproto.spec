Name:       glproto
Summary:    X.Org X11 Protocol glproto
Version:    1.4.16
Release:    1 
Group:      Development/System
License:    MIT
URL:        http://www.x.org
Source0:    http://xorg.freedesktop.org/releases/individual/proto/glproto-%{version}.tar.bz2


%description
glproto is the protocol for the client to send 3D rendering commands to the X server.


%prep
%setup -q 

%build

%configure --libdir=%{_datadir}

make %{?jobs:-j%jobs}

%install
%make_install

%files
%defattr(-,root,root,-)
%{_datadir}/pkgconfig/glproto.pc
%{_includedir}/GL/glxmd.h
%{_includedir}/GL/glxtokens.h
%{_includedir}/GL/glxproto.h
%{_includedir}/GL/internal
%{_includedir}/GL/internal/glcore.h
%{_includedir}/GL/glxint.h

