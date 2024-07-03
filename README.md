# 环境配置
## 实验24运行步骤
### 新建终端
`cd /home/mc/autodriver/24/pcl_test`
`catkin_make`
`source devel/setup.bash`
`roslaunch pcl_test pcl_test.launch`
### 再新建终端
`rosbag play --clock /home/mc/autodriver/24/pcl_test/src/test.bag/home/mc/autodriver/24/pcl_test/src/test.bag`
### 再新建终端
`rosrun rviz rviz`

## 实验3运行步骤
### 新建终端
`cd /home/mc/autodriver/3/ukf-code/build`

`make   使`

`./ukf ../data/data_synthetic.txt ../data/output.txt./ukf`

`cd ../data   cd . . /数据`

`conda activate base   Conda激活基地`

`python plot.py`
