# 环境配置
## 实验24运行步骤
### 新建终端
`cd /home/mc/autodriver/24/pcl_test`
`catkin_make`
`source devel/setup.bash`
`roslaunch pcl_test pcl_test.launch`
### 再新建终端
`rosbag play --clock /home/mc/autodriver/24/pcl_test/src/test.bag`
### 再新建终端
`rosrun rviz rviz`
