Name:           ros-indigo-aniso8601
Version:        0.8.3
Release:        3%{?dist}
Summary:        ROS aniso8601 package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  ros-indigo-catkin >= 0.6.18
BuildRequires:  ros-indigo-catkin-pip >= 0.1.15

%description
Another ISO 8601 parser for Python

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
* Wed Nov 16 2016 AlexV <asmodehn@gmail.com> - 0.8.3-3
- Autogenerated by Bloom

* Wed Nov 16 2016 AlexV <asmodehn@gmail.com> - 0.8.3-2
- Autogenerated by Bloom

* Wed Nov 16 2016 AlexV <asmodehn@gmail.com> - 0.8.3-1
- Autogenerated by Bloom

* Wed Nov 16 2016 AlexV <asmodehn@gmail.com> - 0.8.3-0
- Autogenerated by Bloom

