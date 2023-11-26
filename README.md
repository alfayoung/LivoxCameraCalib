如何标定？
- 首先对相机进行标定

注意到标定的内参矩阵不会受到棋盘大小的影响，这是显然的，因为所有相互平行的物平面都是相似的，因此任何相似的物体，呈的像都是一致的。
而标定的畸变矩阵会受到棋盘大小的影响。
现象是在尺度变大的时候，畸变矩阵参数会变大，意味着畸变变得更加明显。

- 获得了对相机的标定结果后
填入 calib.yaml 中

- 保持相机和激光雷达绝对位置不变，
获取一张相机的图片

在 livox viewer 中录制一段时间的点云，保存的文件为 .lvx。接下来使用 `roslaunch livox_ros_driver lvx_to_rosbag.launch lvx_file_path:="/path/to/lvx"`，即可转换为 .bag。最后使用 livox_camera_calib 中自带的 bag_to_pcd，即可把 bag 转换成 pcd 文件。

- 最后，准备初始的估计的外参，填入 config_outdoor.yaml 中，然后运行 `roslaunch livox_camera_calib calib.launch` 即可等待结果出现。


### Remarks：
目前项目存在的问题是点云在 rough calibration 之后完全匹配不上，怀疑需要使用更短的焦距的镜头进行标定。