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
- [Deployment](#deployment)
- [Built Using](#built_using)
- [TODO](../TODO.md)
- [Contributing](../CONTRIBUTING.md)
- [Authors](#authors)
- [Acknowledgments](#acknowledgement)

## 🧐 About <a name = "about"></a>

There are the ros packages for iwb milling robot simulation, relying on ROS Noetic distribution. The packages perform robot modeling, visualization, path planning, controlling, simulation with physic simulator, and many other functionalities.

You can simply run each package seperately with terminal command line, which helps you get to know how it works. Besides, with IWB_ROBOT class in iwb_ros python package, you can also run these ros functionalites in a few lines and make them cooperate with you own programm.

## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

### System Requirements
The packages work in ROS Noetics, which is primarily targeted at:

- Ubuntu 20.04.4 LTS 

Other systems are supported to varying degrees. (--- [**ROS Noetics**](http://wiki.ros.org/noetic))

Besides, if you are running everything on a virtual machine, the following configurations are recommended:

- 30 GB storage.
- TODO...

You can follow the [**Tutorial Here**](https://ubuntu.tutorials24x7.com/blog/how-to-install-ubuntu-20-04-lts-on-windows-using-vmware-workstation-player) to setup a virtual machine.

### Prerequisites
#### Install ROS Noetic
The packages based on ROS Noetic distribution. You may install the desktop version of ROS Noetic [**Here**](http://wiki.ros.org/noetic/Installation/Ubuntu). Please choose Desktop-Full install, which is also recommanded in the page.


Every time you want to run the packages with terminal, use the following command to setup the ROS environment.

```console
source /opt/ros/noetic/setup.bash
```

if you want to source a different version of ROS, this line would be:

```console
source /opt/ros/ROS-DISTRO/setup.bash
#

```


You may have noticed that it's possible to avoid doing this every time opening a terminal by adding this line into your system "~/.bashrc". If you do so, please check if you append the line for the ROS version that of your use. (Remember this when transplant the project to a new ROS version, for example ROS 2 foxy)


### Installing

A step by step series of examples that tell you how to get a development env running.

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo.

## 🔧 Running the tests <a name = "tests"></a>

Explain how to run the automated tests for this system.

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## 🎈 Usage <a name="usage"></a>

Add notes about how to use the system.

## 🚀 Deployment <a name = "deployment"></a>

Add additional notes about how to deploy this on a live system.

## ⛏️ Built Using <a name = "built_using"></a>

- [ROS Noeitcs](https://www.mongodb.com/) - Robot operation system
- [Express](https://expressjs.com/) - Server Framework

## ✍️ Authors <a name = "authors"></a>

- [@BBlab](https://github.com/kylelobo) - Student in mechanical engineering
- And ... more contributers in the future.
<!-- See also the list of [contributors](https://github.com/kylelobo/The-Documentation-Compendium/contributors) who participated in this project. -->

## 🎉 Acknowledgements <a name = "acknowledgement"></a>

- TODO: citing and inspiration mabe
- Thanks for your contribution to the project!
- ...
