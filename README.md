# driver   #司机   司机
data   数据
环境准备
安装vscode 
安装anaconda 
python3.8

代码7就是cv_lane_detect
1、打开vscode 

打开文件夹：autodriver/1

运行

2、vscode 里运行

3、

打开终端

cd /home/mc/autodriver/3/ukf-code/build

make

./ukf ../data/data_synthetic.txt ../data/output.txt

cd ../data

conda activate base

python plot.py

5、vscode里运行

6、vscode里运行

切换python3.8

7、vscode里运行

切换python3.11（base）

9、vscode里运行

切换python3.11

11、vscode里运行

切换python3.11

13、

打开终端

cd /home/mc/autodriver/13/build

./normal_distributions_transform cloud1.pcd cloud2.pcd

14、

打开终端

roscore

cd /home/mc/autodriver/14/husky_ws1

source devel/setup.bash   源猛击/ setup.bash

roslaunch husky_gazebo empty_world.launch

rostopic pub -r 10  /husky_velocity_controller/cmd_vel geometry_msgs/Twist '{linear: {x: 4, y: 0, z: 0}, angular: {x: 0, y: 0, z: 0.5}}’

16、vscode里运行

18、vscode里运行

切换python3.8

19、vscode里运行

切换python3.11

20、vscode里运行

python3.11

21、vscode里运行

切换python3.11

24、

新建终端

cd /home/mc/autodriver/24/pcl_test

catkin_make

source devel/setup.bash

roslaunch pcl_test pcl_test.launch

再新建终端

rosbag play --clock /home/mc/autodriver/24/pcl_test/src/test.bag

再新建终端

rosrun rviz rviz

![2024-04-06 10-07-46 的屏幕截图.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/b86377b3-b8e3-4b4e-9116-da261e44cdc5/8c896af7-21d8-4064-9ce8-9d3b88fba689/2024-04-06_10-07-46_%E7%9A%84%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE.png)

左下角 点击Add 

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/b86377b3-b8e3-4b4e-9116-da261e44cdc5/b6e14b26-981a-41d8-85c3-ef169dfd7bf4/Untitled.png)! (Untitled) (https://prod -文件- secure.s3.us -西方- 2. - amazonaws.com/b86377b3 b8e3 - 4 - b4e - 9116 da261e44cdc5/b6e14b26 - 981 - 85 - 41 - d8 - - c3 - ef169dfd7bf4/untitled.png)

25、

新建终端

roscore

再新建终端

cd /home/mc/autodriver/25/euclidean_cluster

source devel/setup.bash   源猛击/ setup.bash

rosbag play --clock /home/mc/autodriver/25/euclidean_cluster/src/test.bag

再新建终端

cd /home/mc/autodriver/24/pcl_test

source devel/setup.bash

roslaunch pcl_test  pcl_test.launch

再新建终端

cd /home/mc/autodriver/25/euclidean_cluster

source devel/setup.bash   源猛击/ setup.bash

roslaunch euclidean_cluster euclidean_cluster.launchrolaunch euclidean_cluster.launchrolaunch euclidean_cluster。launchrolaunch euclidean_cluster.launch

再新建终端

rosrun rviz rviz

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/b86377b3-b8e3-4b4e-9116-da261e44cdc5/2b2fa4a1-6c7e-4de9-865a-a4630afa442e/Untitled.png)! (Untitled) (https://prod -文件- secure.s3.us -西方- 2. - amazonaws.com/b86377b3 b8e3 - 4 - b4e - 9116 - da261e44cdc5/2b2fa4a1 - 6 - c7e 4 - de9 - 865 a - a4630afa442e/untitled.png)

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/b86377b3-b8e3-4b4e-9116-da261e44cdc5/0bb82b38-e5c9-452d-a9a3-93f556a0afb9/Untitled.png)! (Untitled) (https://prod -文件- secure.s3.us -西方- 2. - amazonaws.com/b86377b3 b8e3 - 4 - b4e - 9116 da261e44cdc5/0bb82b38 e5c9 - 452 d - a9a3 - 93 f556a0afb9/untitled.png)![无题]（https://prod-files-secure.s3.us-west-2.amazonaws.com/b86377b3-b8e3-4b4e-9116-da261e44cdc5/0bb82b38-e5c9-452d-a9a3-93f556a0afb9/Untitled.png）！（无题）（https://prod - 文件 - secure.s3.us - 西 - 2. - amazonaws.com/b86377b3 B8E3 - 4 - B4E - 9116 DA261E44CDC5/0BB82B38 E5C9 - 452 D - A9A3 - 93 F556A0AFB9/untitled.png）

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/b86377b3-b8e3-4b4e-9116-da261e44cdc5/f5ac08a0-c505-43d0-8d65-ccc08f22e642/Untitled.png)! (Untitled) (https://prod -文件- secure.s3.us -西方- 2. - amazonaws.com/b86377b3 b8e3 - 4 - b4e - 9116 - da261e44cdc5/f5ac08a0 c505 - 43 - d0 - 8 d65 ccc08f22e642/untitled.png)![无题]（https://prod-files-secure.s3.us-west-2.amazonaws.com/b86377b3-b8e3-4b4e-9116-da261e44cdc5/f5ac08a0-c505-43d0-8d65-ccc08f22e642/Untitled.png）！（无题）（https://prod -Document-secure.s3.us -西- 2. - amazonaws.com/b86377b3 B8E3 - 4 - B4E - 9116 - DA261E44CDC5/F5AC08A0 C505 - 43 - D0 - 8 D65 CCC08F22E642/untitled.png）![无题]（https://prod-files-secure.s3.us-west-2.amazonaws.com/b86377b3-b8e3-4b4e-9116-da261e44cdc5/f5ac08a0-c505-43d0-8d65-ccc08f22e642/Untitled.png）！（无题）（https://prod - 文件 - secure.s3.us - 西 - 2. - amazonaws.com/b86377b3 b8e3 - 4 - b4e - 9116 - da261e44cdc5/f5ac08a0 c505 - 43 - d0 - 8 d65 ccc08f22e642/untitled.png）！[无题]（https://prod-files-secure.s3.us-west-2.amazonaws.com/b86377b3-b8e3-4b4e-9116-da261e44cdc5/f5ac08a0-c505-43d0-8d65-ccc08f22e642/Untitled.png）！（无题）（https://prod -Document-secure.s3.us -西- 2.- amazonaws.com/b86377b3 B8E3 - 4 - B4E - 9116 - DA261E44CDC5/F5AC08A0 C505 - 43 - D0 - 8 D65 CCC08F22E642/untitled.png）

26、

新建终端

roscore

新建终端

cd /home/mc/autodriver/26/SqueezeSeg_Ros-master/

source devel/setup.bash   源猛击/ setup.bash

roslaunch squeezeseg_ros squeeze_seg_ros.launchRoslaunch squeezeseg_ros squeeze_seg_ros.launchRoslaunch squeezeseg_ros squeeze_seg_roslaunchRoslaunch squeezeseg_ros squeeze_seg_ros

再新建终端

cd /home/mc/autodriver/26/SqueezeSeg_Ros-master/src/scriptcd /home/mc/autodriver/26/SqueezeSeg_Ros-master / src /脚本cd /home/mc/autodriver/26/ squeezeseg_ros -master/src/脚本

conda activate py36   激活py36

python squeezeseg_ros_node.py

再新建终端

rviz   RVIZ

使用add添加上述主题，类型为PointCloud2，固定坐标（Fixed Frame）设置为velodyne_link，channel name 设置为label  。size 设置为0.06 即可得到识别分割图像。

27

新建终端

roscore

新建终端

cd /home/mc/autodriver/27/plane_fit_ground_filter-master/plane_fit_ground_filter-master/src

rosbag play --clock test.bag 罗斯巴格比赛——计时测试

新建终端

cd /home/mc/autodriver/27/plane_fit_ground_filter-master/plane_fit_ground_filter-master

source devel/setup.bash    源猛击/ setup.bash

roslaunch plane_ground_filter plane_ground_filter.launch plane_ground_filter.launch

新建终端

rviz   RVIZ   RVIZ RVIZ

add 点云，输入velodyne

28

新建终端

roscore

新建终端

conda activate py36   激活py36

cd /home/mc/autodriver/28/vo/

source devel/setup.bash   源猛击/ setup.bash

roscd voxelnet_ros/script/

python3 voxelnet_ros.py & python3 pub_kitti_point_cloud.py Python3 voxelnet_ros.py & Python3 pub_kitti_point_cloud.pypython3 voxelnet_ros.py & python3 pub_kitti_point_cloud.py python3 voxelnet_ros.py & python3 pub_kitti_point_cloud.pypython3 voxelnet_ros.py & python3 pub_kitti_point_cloud.py python3 voxelnet_ros.py & python3 pub_kitti_point_cloud.py。Pypython3 voxelnet_ros.py & python3 pub_kitti_point_cloud.py python3 voxelnet_ros.py & python3 pub_kitti_point_cloud.pypython3 voxelnet_ros.py & python3 pub_kitti_point_cloud.py python3 voxelnet_ros.py & python3 pub_kitti_point_cloud.py。Pypython3 voxelnet_ros.py & python3 pub_kitti_point_cloud. Pypython3 voxelnet_ros.py & python3 pub_kitti_point_cloud.py。Pypython3 voxelnet_ros.py & python3 pub_kitti_point_cloud.py python3 voxelnet_ros.py & python3 pub_kitti_point_cloud.py。Pypython3 voxelnet_ros.py & python3 pub_kitti_point_cloud.py python3 voxelnet_ros.py & python3 pub_kitti_point_cloud.pypython3 voxelnet_ros.py & python3 pub_kitti_point_cloud.py Python3 voxelnet_ros.py & Python3 pub_kitti_point_cloud.pypython3 voxelnet_ros.py & python3 pub_kitti_point_cloud.py python3 voxelnet_ros.py & python3 pub_kitti_point_cloud.pypython3 voxelnet_ros.py & python3 pub_kitti_point_cloud.py python3 voxelnet_ros.py & python3 pub_kitti_point_cloud.py。Pypython3 voxelnet_ros.py & python3 pub_kitti_point_cloud.py python3 voxelnet_ros.py & python3 pub_kitti_point_cloud.pypython3 voxelnet_ros.py & python3 pub_kitti_point_cloud.py python3 voxelnet_ros.py & python3 pub_kitti_point_cloud.py。Pypython3 voxelnet_ros.py 和 python3 pub_kitti_point_cloud。Pypython3 voxelnet_ros.py & python3 pub_kitti_point_cloud.py。Pypython3 voxelnet_ros.py & python3 pub_kitti_point_cloud.py python3 voxelnet_ros.py & python3 pub_kitti_point_cloud.py。Pypython3 voxelnet_ros.py 和 python3 pub_kitti_point_cloud.py python3 voxelnet_ros.py 和 python3 pub_kitti_point_cloud.py

新建终端 

rviz   RVIZ   RVIZ RVIZ

修改map为velodyne   点击add，添加点云
