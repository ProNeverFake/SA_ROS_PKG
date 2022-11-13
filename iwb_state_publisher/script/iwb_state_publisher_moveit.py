#!/usr/bin/env python
'''
    the python script run by the bash script to start iwb state publisher with
    motion plannning configs. Not in use yet.
    
'''
# the python pkg for ros functionalities
import sys
import copy
import rospy
import moveit_commander
from math import pi

# import the msg type
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list
import moveit_msgs.msg
import geometry_msgs.msg

# the function to publish the msg
def publishit():
    # initialize the node and the commander obj
    moveit_commander.roscpp_initialize(sys.argv)
    rospy.init_node('iwb_planner', anonymous=True)

    display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',
                                               moveit_msgs.msg.DisplayTrajectory,
                                               queue_size=20)
    # Instantiate a RobotCommander object
    moveit_robot = moveit_commander.RobotCommander()

    # Instantiate a PlanningSceneInterface object
    scene = moveit_commander.PlanningSceneInterface()

    # Instantiate a MoveGroupCommander object
    group_name = "robot_arm"
    group = moveit_commander.MoveGroupCommander(group_name)

    # create the topic for rviz visualize
    

    # We can get the name of the reference frame for this robot:
    planning_frame = group.get_planning_frame()
    print("============ Reference frame: %s" % planning_frame)

    # We can also print the name of the end-effector link for this group:
    eef_link = group.get_end_effector_link()
    print("============ End effector: %s" % eef_link)

    # We can get a list of all the groups in the robot:
    group_names = moveit_robot.get_group_names()
    print("============ Robot Groups:", moveit_robot.get_group_names())

    # print the entire state of the robot

    print("============ Printing robot state")
    print(robot.get_current_state())
    print("")

    print("============ check the function return")
    joint_goal = group.get_current_joint_values()
    print(joint_goal)

    # set the goal
    joint_goal[2] = -pi/4
    joint_goal[5] = -pi/4
    joint_goal[8] = -pi/4
    joint_goal[11] = -pi/4
    joint_goal[14] = -pi/4
    joint_goal[17] = -pi/4

    # plan
    # group.go(joint_goal, wait=True)
    print(group.go(joint_goal, wait=True))
    

    # Calling ``stop()`` ensures that there is no residual movement
    group.stop()
    # # clear the target (this is for pose only)
    # group.clear_pose_targets()


    # !plan is only used with pose planning

    # # display the trajectory
    # display_trajectory = moveit_msgs.msg.DisplayTrajectory()
    # display_trajectory.trajectory_start = robot.get_current_state()
    # display_trajectory.trajectory.append(plan)
    # # Publish
    # display_trajectory_publisher.publish(display_trajectory)

    # execuate the plan 
    # group.execute(plan, wait=True)

    # no param. when the goal was already set
    # group.execute(plan, wait=True)
    # group.move()



    
if __name__ == '__main__':
    try:
        publishit()
    except rospy.ROSInterruptException:
        pass