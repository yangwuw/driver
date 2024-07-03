# 环境配置
1、安装cmake
sudo apt install cmake   安装cmake   安装cmake
查看是否安装成功：
cmake --version   cmake——版本   cmake——版本
2、安装c++环境
sudo apt install g++   Sudo apt install   Sudo apt install
查看c++环境：
gcc --version   gcc -版本   gcc -版本
3、安装pcl sudo apt-get install libpcl-dev
查看pcl版本：
apt-cache show libpcl-devApt-cache show libpcl-devApt-cache show libpcl-dev
4、安装numdifftools
pip install numdifftools   PIP安装numdifftools   PIP安装numdifftools
5、安装依赖
sudo apt install python3-roslaunch安装python3-roslaunch安装python3-roslaunch
sudo apt-get install libboost-all-dev安装libboost-all-dev安装libboost-all-dev
sudo apt-get install libboost-dev安装libboost-dev安装libboost-dev
sudo apt-get update   Sudo apt-get update   Sudo apt-get update
sudo apt-get install vscode安装vscode安装vscode
chmod +x ./Anaconda3-2024.02-1-Linux-x86_64.shchmod x ./Anaconda3-2024.02-1-Linux-x86_64.shchmod x ./Anaconda3-2024.02-1-Linux-x86_64.sh
bash ./Anaconda3-2024.02-1-Linux-x86_64.shbash。/ anaconda3 - 2024.02 - 1 - linux - x86_64.shbash。/ anaconda3 - 2024.02 - 1 - linux - x86_64.sh
6、安装tensorflow，keras版本 2.12.0
pip install tensorflow==2.12.0PIP安装tensorflow==2.12.0PIP安装tensorflow==2.12.0
pip install FuzzyTM>=0.4.0pip安装FuzzyTM>=0.4.0pip安装FuzzyTM>=0.4.0
7、安装ros
sudo sh -c '. /etc/lsb-release && echo "deb http://mirrors.ustc.edu.cn/ros/ubuntu/ $DISTRIB_CODENAME main" > /etc/apt/sources.list.d/ros-latest.list'Sudo sh -c '。/etc/ lbs -release && echo "deb http://mirrors.ustc.edu.cn/ros/ubuntu/ $DISTRIB_CODENAME main" > /etc/apt/sources.list.d/ros-latest.list'Sudo sh -c '。/etc/ lbs -release && echo "deb http://mirrors.ustc.edu.cn/ros/ubuntu/ $DISTRIB_CODENAME main" > /etc/apt/sources.list.d/ros-latest.list'
sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654sudo apt-key adv——keyserver 'hkp://keyserver.ubuntu.com:80'——recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
sudo apt update   Sudo apt更新
（15）问题：Resource not found: husky_gazebo(15)问题:未找到资源:husky_gazebo
sudo apt-get install ros-noetic-husky-gazeboSudo apt-get install ros-noetic-husky-gazebo
25、
Could not find a package configuration file provided by "jsk_recognition_msgs" with any of the following names:找不到由“jsk_recognition_msgs”提供的具有以下名称的包配置文件:
解决：
sudo apt-get install ros-noetic-jsk-recognition-msgs执行命令apt-get install ros-noetic-jsk-recognition- messages
sudo apt-get install ros-noetic-jsk-rviz-plugins安装ros-noetic-jsk-rviz-plugins
26、
No module PIL   无模块PIL
python3 -m pip install Pillowpython3 -m pip安装枕头
[ERROR] [1712393598.959944751]: PluginlibFactory:[错误][1712393598.959944751]:PluginlibFactory:
sudo apt-get install ros-noetic-rviz-visual-toolsSudo apt-get install ros- nonote -rviz-visual-tools

