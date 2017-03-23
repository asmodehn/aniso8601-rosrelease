cmake_minimum_required(VERSION 2.8.3)
project(aniso8601)

# For ease of use, this CMakeLists allows to use this code from source, as if it were a normal catkin package.
# However no ROS/catkin debian package is provided for it.
# It is just a pip package that your packages should depend on (using rosdep pip dependency mechanism).
# We should follow closely https://github.com/gerkey/ros1_external_use

# Minimal Python module setup - catkin is assumed preinstalled along with ROS
# This assume catkin is installed along with a minimal ROS system.
find_package(catkin REQUIRED COMPONENTS
    catkin_pip
)

# defining current package as a package that should be managed by pip (not catkin - even though we make it usable with workspaces)
catkin_pip_package(aniso8601)

## Unit tests
if (CATKIN_ENABLE_TESTING)

    ############
    # NoseTests
    ############

    catkin_add_nosetests(python2/aniso8601 WORKING_DIRECTORY ${CMAKE_CURRENT_LIST_DIR}/python2)

endif()
