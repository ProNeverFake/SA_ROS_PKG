#include <string>
#include <ros/ros.h>
#include <sensor_msgs/JointState.h>
#include <tf/transform_broadcaster.h>

int main(int argc, char** argv) {
    ros::init(argc, argv, "iwb_state_publisher");
    ros::NodeHandle n;
    ros::Publisher joint_pub = n.advertise<sensor_msgs::JointState>("joint_states", 1);
    // tf::TransformBroadcaster broadcaster;
    ros::Rate loop_rate(30);

    const double degree = M_PI/180;

    // robot state
    double joint_6_x = 0, joint_6_y = 0, joint_6_z = 0;

    // message declarations
    // geometry_msgs::TransformStamped odom_trans;
    sensor_msgs::JointState joint_state;
    // odom_trans.header.frame_id = "odom";
    // odom_trans.child_frame_id = "axis";

    while (ros::ok()) {
        //update joint_state
        joint_state.header.stamp = ros::Time::now();
        joint_state.name.resize(18);
        joint_state.name[15] = "joint_6_x";
        joint_state.position.resize(18);
        joint_state.position[15] = joint_6_x;
        joint_state.position[16] = joint_6_y;
        joint_state.position[17] = joint_6_z;


        // update transform
        // (moving in a circle with radius=2)
        // odom_trans.header.stamp = ros::Time::now();
        // odom_trans.transform.translation.x = cos(angle)*2;
        // odom_trans.transform.translation.y = sin(angle)*2;
        // odom_trans.transform.translation.z = .7;
        // odom_trans.transform.rotation = tf::createQuaternionMsgFromYaw(angle+M_PI/2);

        //send the joint state and transform
        joint_pub.publish(joint_state);
        // broadcaster.sendTransform(odom_trans);

        // Create new robot state
        joint_6_x = joint_6_x + 0.01;
        if(joint_6_x > 3.14)
        {
            joint_6_x = joint_6_x - 6.28;
        }

        // This will adjust as needed per iteration
        loop_rate.sleep();
    }


    return 0;
}
