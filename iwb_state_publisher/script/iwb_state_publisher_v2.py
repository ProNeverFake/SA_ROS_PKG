#!/usr/bin/env python



# the python pkg for ros functionalities
import rospy
# import the msg type
from sensor_msgs.msg import JointState
from std_msgs.msg import Header

# the function to publish the msg
def publishit():
    # create the publisher with topic "joint_states" with msg-type JointState
    pub = rospy.Publisher('iwb_joint_state', JointState, queue_size=10)

    rospy.init_node('iwb_state_publisher_v2')
    rate = rospy.Rate(10) # the publishing rate is 10hz
    joint_msg = JointState()

    i = 0
    n = 0.01

    # while ros is ready
    while not rospy.is_shutdown():

        # the message:
        joint_msg.header = Header()
        joint_msg.header.stamp = rospy.Time.now()
        joint_msg.name = ['joint_1_x', 'joint_1_y', 'joint_1_z', 'joint_2_x', 'joint_2_y', 'joint_2_z',
            'joint_3_x', 'joint_3_y', 'joint_3_z', 'joint_4_x', 'joint_4_y', 'joint_4_z',
            'joint_5_x', 'joint_5_y', 'joint_5_z', 'joint_6_x', 'joint_6_y', 'joint_6_z']
        joint_msg.position = [0]*18
        joint_msg.position[17] = i
        joint_msg.velocity = []
        joint_msg.effort = []

        # publish the msg to the topic
        pub.publish(joint_msg)

        # msg iteration (rotation)
        i = i + n 
        if i > 3.14:
            i = -3.14


        # "ros.spin", sleep according to the rospy.Rate (10hz)
        rate.sleep()



if __name__ == '__main__':
    try:
        publishit()
    except rospy.ROSInterruptException:
        pass