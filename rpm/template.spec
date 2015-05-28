Name:           ros-indigo-rotors-evaluation
Version:        1.1.4
Release:        0%{?dist}
Summary:        ROS rotors_evaluation package

Group:          Development/Libraries
License:        ASL 2.0
URL:            https://github.com/ethz-asl/rotors_simulator/wiki
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-rospy
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-rospy

%description
The dataset evaluation package for the RotorS simulator.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Thu May 28 2015 Fadri Furrer <fadri.furrer@mavt.ethz.ch> - 1.1.4-0
- Autogenerated by Bloom

* Thu May 28 2015 Fadri Furrer <fadri.furrer@mavt.ethz.ch> - 1.1.3-0
- Autogenerated by Bloom

* Wed May 27 2015 Fadri Furrer <fadri.furrer@mavt.ethz.ch> - 1.1.2-0
- Autogenerated by Bloom

* Fri Apr 24 2015 Fadri Furrer <fadri.furrer@mavt.ethz.ch> - 1.1.1-0
- Autogenerated by Bloom

