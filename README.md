# 环境配置
## 实验24运行步骤
### 新建终端
`cd /home/mc/autodriver/24/pcl_test`
`catkin_make`
`source devel/setup.bash   源猛击/ setup.bash`
`roslaunch pcl_test pcl_test.launch启动pcl_test`
### 再新建终端
`rosbag play --clock /home/mc/autodriver/24/pcl_test/src/test.bag/home/mc/autodriver/24/pcl_test/src/test.bag`
### 再新建终端
`rosrun rviz rviz   Рсрпсние р`

## 实验3运行步骤
### 新建终端
`cd /home/mc/autodriver/3/ukf-code/build`

`make`

`./ukf ../data/data_synthetic.txt ../data/output.txt./ukf`

`cd ../data`

`conda activate base`

`python plot.py`
