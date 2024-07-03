环境配置
1、安装cmake
sudo apt install cmake
查看是否安装成功：
cmake --version
2、安装c++环境
sudo apt install g++
查看c++环境：
gcc --version
3、安装pcl sudo apt-get install libpcl-dev
查看pcl版本：
apt-cache show libpcl-dev
4、安装numdifftools
pip install numdifftools
5、安装依赖
sudo apt install python3-roslaunch
sudo apt-get install libboost-all-dev
sudo apt-get install libboost-dev
sudo apt-get update
sudo apt-get install vscode
chmod +x ./Anaconda3-2024.02-1-Linux-x86_64.sh
bash ./Anaconda3-2024.02-1-Linux-x86_64.sh
6、安装tensorflow，keras版本 2.12.0
pip install tensorflow==2.12.0
pip install FuzzyTM>=0.4.0
7、安装ros
sudo sh -c '. /etc/lsb-release && echo "deb http://mirrors.ustc.edu.cn/ros/ubuntu/ $DISTRIB_CODENAME main" > /etc/apt/sources.list.d/ros-latest.list'
sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
sudo apt update
（15）问题：Resource not found: husky_gazebo
sudo apt-get install ros-noetic-husky-gazebo
25、
Could not find a package configuration file provided by "jsk_recognition_msgs" with any of the following names:
解决：
sudo apt-get install ros-noetic-jsk-recognition-msgs
sudo apt-get install ros-noetic-jsk-rviz-plugins
26、
No module PIL
python3 -m pip install Pillow
[ERROR] [1712393598.959944751]: PluginlibFactory:
sudo apt-get install ros-noetic-rviz-visual-tools

