Name:           ros-indigo-rotors-gazebo-plugins
Version:        2.1.0
Release:        1%{?dist}
Summary:        ROS rotors_gazebo_plugins package

Group:          Development/Libraries
License:        ASL 2.0
URL:            https://github.com/ethz-asl/rotors_simulator
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-cv-bridge
Requires:       ros-indigo-gazebo-ros
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-mav-msgs
Requires:       ros-indigo-octomap
Requires:       ros-indigo-octomap-msgs
Requires:       ros-indigo-octomap-ros
Requires:       ros-indigo-rosbag
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-rotors-comm
Requires:       ros-indigo-rotors-control
Requires:       ros-indigo-std-srvs
Requires:       ros-indigo-tf
Requires:       yaml-cpp-devel
BuildRequires:  gazebo-devel
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-cmake-modules
BuildRequires:  ros-indigo-cv-bridge
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-mav-msgs
BuildRequires:  ros-indigo-octomap
BuildRequires:  ros-indigo-octomap-msgs
BuildRequires:  ros-indigo-octomap-ros
BuildRequires:  ros-indigo-rosbag
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-rotors-comm
BuildRequires:  ros-indigo-rotors-control
BuildRequires:  ros-indigo-std-srvs
BuildRequires:  ros-indigo-tf
BuildRequires:  yaml-cpp-devel

%description
The rotors_gazebo_plugins package

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
        -DCMAKE_INSTALL_LIBDIR="lib" \
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
* Sun Apr 09 2017 Fadri Furrer <fadri.furrer@mavt.ethz.ch> - 2.1.0-1
- Autogenerated by Bloom

* Sun Apr 09 2017 Fadri Furrer <fadri.furrer@mavt.ethz.ch> - 2.1.0-0
- Autogenerated by Bloom

* Mon Aug 10 2015 Fadri Furrer <fadri.furrer@mavt.ethz.ch> - 2.0.1-0
- Autogenerated by Bloom

* Sun Aug 09 2015 Fadri Furrer <fadri.furrer@mavt.ethz.ch> - 2.0.0-0
- Autogenerated by Bloom

* Thu Jun 11 2015 Fadri Furrer <fadri.furrer@mavt.ethz.ch> - 1.1.6-0
- Autogenerated by Bloom

* Tue Jun 09 2015 Fadri Furrer <fadri.furrer@mavt.ethz.ch> - 1.1.5-0
- Autogenerated by Bloom

* Thu May 28 2015 Fadri Furrer <fadri.furrer@mavt.ethz.ch> - 1.1.4-0
- Autogenerated by Bloom

* Thu May 28 2015 Fadri Furrer <fadri.furrer@mavt.ethz.ch> - 1.1.3-0
- Autogenerated by Bloom

* Wed May 27 2015 Fadri Furrer <fadri.furrer@mavt.ethz.ch> - 1.1.2-0
- Autogenerated by Bloom

* Fri Apr 24 2015 Fadri Furrer <fadri.furrer@mavt.ethz.ch> - 1.1.1-0
- Autogenerated by Bloom

