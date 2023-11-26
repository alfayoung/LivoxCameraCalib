#include <ros/ros.h>
#include <sensor_msgs/PointCloud.h>
#include <sensor_msgs/point_cloud_conversion.h>
#include <laser_assembler/AssembleScans.h>

#include <pcl_conversions/pcl_conversions.h>
#include <pcl_ros/point_cloud.h>

int main(int argc, char *argv[]) {
    ros::init(argc, argv, "call_assembler_service");
    ros::NodeHandle nh("~");

    std::string path;
    if (!nh.getParam("save_path", path)) {
        ROS_ERROR("Failed to get param 'save_path'");
    }

    ros::service::waitForService("/assemble_scans");
    ros::ServiceClient client = nh.serviceClient<laser_assembler::AssembleScans>("/assemble_scans");
    laser_assembler::AssembleScans srv;
    srv.request.begin = ros::Time(0, 0);
    srv.request.end = ros::Time::now();

    if (client.call(srv)) {
        sensor_msgs::PointCloud2 cloud2;
        sensor_msgs::convertPointCloudToPointCloud2(srv.response.cloud, cloud2);
        pcl::PointCloud<pcl::PointXYZ>::Ptr cloud_assembled(new pcl::PointCloud<pcl::PointXYZ>());
        pcl::fromROSMsg(cloud2, *cloud_assembled);
        ROS_ERROR("Number of Cloud Points = %d \n", cloud_assembled->width);
        pcl::io::savePCDFileASCII(path, *cloud_assembled);
    } else {
        ROS_ERROR("Service call failed\n");
    }

    return 0;
}