<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://img.freepik.com/free-vector/robot-arm-concept-illustration_114360-8436.jpg?t=st=1656519056~exp=1656519656~hmac=72a1bfa23b9fb27258f7614a4a378c813cf75a67f002c39cb10ed8537110442c&w=740" alt="Project logo">
 </a>
</p>

<h1 align="center">IWB ROS PACKAGE</h1>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/kylelobo/The-Documentation-Compendium.svg)](https://gitlab.lrz.de/00000000014A6C01/sa_bblab/-/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/kylelobo/The-Documentation-Compendium.svg)](https://github.com/kylelobo/The-Documentation-Compendium/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> ros packages to support iwb robot modeling
    <br> 
</p>

## 📝 Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Development](#development)
- [Built Using](#built_using)
- [TODO](../TODO.md)
- [Contributing](../CONTRIBUTING.md)
- [Authors](#authors)
- [Acknowledgments](#acknowledgement)

## 🧐 About <a name = "about"></a>

There are the ros packages for iwb milling robot simulation, relying on ROS Noetic distribution. The packages perform robot modeling, visualization, path planning, controlling, simulation with physic simulator, and many other functionalities.

You can simply run each package seperately with terminal command line, which helps you to get to know how it works. Besides, with IWB_ROBOT class in iwb_ros python package, you can also run these ros functionalites in a few python lines and make them cooperate with you own programm.

## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [development](#development) for notes for developers.

The contents you need to walk through are:
- System Environment
- Prerequisites
  - ROS Noetic
  - Moveit!
  - Others
- Installation


### System Environment
The packages work with ROS Noetic, which is primarily targeted at:

- Ubuntu 20.04.4 LTS 

Other systems are supported to varying degrees. (--- [**ROS Noetics**](http://wiki.ros.org/noetic))

Besides, if you are running everything on a virtual machine, the following configurations are recommended:

- 30 GB storage.
- TODO...

You can follow the [**Tutorial Here**](https://ubuntu.tutorials24x7.com/blog/how-to-install-ubuntu-20-04-lts-on-windows-using-vmware-workstation-player) to setup a virtual machine.

### Prerequisites
###### Install ROS Noetic
The packages based on ROS Noetic distribution. You may install the desktop version of ROS Noetic [**Here**](http://wiki.ros.org/noetic/Installation/Ubuntu). Please choose Desktop-Full install, which is also recommanded in the page.


Every time you want to run the packages with terminal, use the following command to setup the ROS environment.

```console
$ source /opt/ros/noetic/setup.bash
```

if you want to source a different version of ROS, this line would be:

```console
$ source /opt/ros/ROS-DISTRO/setup.bash
# for example ROS 2 foxy:
$ source /opt/ros/foxy/setup.bash
```

You may have noticed that it's possible to avoid doing this every time opening a terminal by adding this line into your system "~/.bashrc". If you do so, please check if you append the line for the ROS version that of your use. (Remember this when transplant the project to a new ROS version, for example ROS 2 foxy)

Don't forget to try the turtle example provided in ROS tutorial to validate your installation.
###### Install Moveit

The path & motion planning parts of the packages are realized by moveit, which is the most widely used for robot manipulation. And it cooperates well with ROS.

You can install moveit ROS (binary) packages by execute the following line in your terminal:

```console
# here for ros noetic
$ sudo apt install ros-noetic-moveit 
```

_tips: You could always install lacking ros packages using command line like:_

```console
$ sudo apt update
$ sudo apt install ros-ROS_DISTRO-ros_package_name
# for example
$ sudo apt install ros-noetic-ros-control
```
The [Moveit tutorial](https://ros-planning.github.io/moveit_tutorials/) can help you to understand its planning functionalities. The Python interfaces of Moveit are explained [Here](https://ros-planning.github.io/moveit_tutorials/doc/move_group_python_interface/move_group_python_interface_tutorial.html), which is quite helpful. And the process to set up a robot for Moveit is shown [Here](https://ros-planning.github.io/moveit_tutorials/doc/setup_assistant/setup_assistant_tutorial.html).

Besides, for transplanting project to ROS 2, you may need Moveit 2 instead of Moveit.


###### Others

TODO

### Installing

After fulfilling the prerequisites, you can now install the packages to your device.

Open a terminal (ctrl+T) and run the lines below to make new directory for the project.

```console
$ cd
$ mkdir -p sa_ws/src
$ cd sa_ws/src
```
Then run git command to clone the packages into your new directory (You may need permission for that, e.g. add you as a maintainer.):

```console
# Do not ignore the point at last!
$ git clone https://gitlab.lrz.de/00000000014A6C01/sa_bblab.git .
```
Now check the packages you cloned. You should build the packages first before using:

_tips: Do not forget to source your ROS setup before using any functionality of ROS (especially when build a ROS package)._

```console
$ source /opt/ros/noetic/setup.bash
$ cd ~/sa_ws
$ catkin_make
```
Here the build tool catkin is used, which should be installed within ROS-Noetic. Install it manually if not so.

If no error message appear, the installation is then successful. You should also run some test command in terminal to validate the installation.



## 🔧 Running the tests <a name = "tests"></a>

There are some test commands to be run for testing the installation and functionalies of our packages. Firstly, the visualization of the robot, and secondly, a "fake control" to move the robot link.

The command below depends on rivz, which should be included in ROS installation. Set it manually if some errors appear.

Open a new terminal and run the commands below:

```console
# source the ROS setup first
$ source /opt/ros/noetic/setup.bash
# then source the setup of our packages
$ source ~/sa_ws/devel/setup.bash
# to visualize the robot with rivz
$ roslaunch robot_model view_robot.launch
```
This should open rivz and you may see our milling robot in it like this:

![The visualization of the robot](/readme_src/view_robot.png "view_robot")

Close it with keyboard interruption (ctrl+c) in the same terminal. Then run another command:

```console
$ roslaunch robot_model 
$ robot_visualization_setup_v2.launch
```
The rviz should be opened again and you should be able to see the last link rotating around a horizonal axis. Close everything if no error appears.

The test part ends here.
## 🎈 Usage <a name="usage"></a>

TODO

## 🚀 Development <a name = "development"></a>

TODO structure of the project

## ⛏️ Built Using <a name = "built_using"></a>

- [ROS Noeitcs](https://www.mongodb.com/) - Robot operation system
- [Pykdl](https://expressjs.com/) - Robot kinematics

## ✍️ Authors <a name = "authors"></a>

- [@BBlab](https://github.com/kylelobo) - Student in mechanical engineering
- And ... more contributers in the future.
<!-- See also the list of [contributors](https://github.com/kylelobo/The-Documentation-Compendium/contributors) who participated in this project. -->

## 🎉 Acknowledgements <a name = "acknowledgement"></a>

- TODO: citing and inspiration mabe
- Thanks for your contribution to the project!
- ...
