^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package ros2_numpy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

2.0.13 (2026-10-11)
-------------------
* Fixes tostring() deprecation in numpy (`#13 <https://github.com/Box-Robotics/ros2_numpy/pull/13>`_)
* Contributors: hello-robot-shehab

2.0.12 (2024-11-11)
-------------------
* Adds support for LaserScan messages (`#12 <https://github.com/Box-Robotics/ros2_numpy/pull/12>`_)
* Contributors: Aniketh Seelam

2.0.11 (2024-06-25)
------------------
* Removed dependency on nose
* Contributors: Tom Panzarella

2.0.9 (2023-01-03)
------------------
* Fix for numpy 1.24.0
* Contributors: Florian Vahl

2.0.8 (2022-06-12)
------------------
* Update for ROS2 Humble (`#5 <https://github.com/Box-Robotics/ros2_numpy/pull/5>`_)
* Contributors: Sean Kelly

2.0.7 (2022-05-16)
------------------
* Remove unneeded array and handle bigendian (`#4 <https://github.com/Box-Robotics/ros2_numpy/pull/4>`_)
* Contributors: Florian Vahl

2.0.6 (2022-04-15)
------------------
* Improve speed of msgify(point_cloud_2_np) by 115x (`#3 <https://github.com/Box-Robotics/ros2_numpy/pull/3>`_)
* Contributors: Alex Thiel

2.0.5 (2022-02-24)
------------------
* Ported to `tf_transformations <https://github.com/DLu/tf_transformations>`_
* Contributors: Tom Panzarella

2.0.4 (2021-11-02)
------------------
* Modified transformations.py for quaternion convention (`#2 <https://github.com/Box-Robotics/ros2_numpy/pull/2>`_)
* Added a test case for the quaternion convention
* Fixed rosdep dependencies in package.xml
* Contributors: Asil Orgen, Tom Panzarella

2.0.3 (2020-07-12)
------------------
* Renamed fork to ``ros2_numpy``
* Start tracking changes in CHANGELOG at 2.0.3
* Contributors: Tom Panzarella
