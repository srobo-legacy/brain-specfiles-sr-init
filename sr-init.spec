%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           sr-init
Version:        0.1
Release:        1%{?dist}
Summary:        Student Robotics init shim

License:        GPLv3+
URL:            https://www.studentrobotics.org/
Source0:        sr-init-%{version}.tar.xz

BuildArch:	noarch
Requires:       python, PyYAML

%description
Student Robotics init shim.  This runs prior to init, waits for a USB
key to be inserted with a robot.zip on it, and then applies any
filesystem overlays specified/provided by the robot.zip.

%prep
%autosetup

%build
%{__python} ./setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} ./setup.py install --root $RPM_BUILD_ROOT

%files
%{_bindir}/*
%{python_sitelib}/sr_init-*.egg-info/

%changelog
* Tue Sep 30 2014 Rob Spanton <rspanton@zepler.net>
- Initial packaging
