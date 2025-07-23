#!/usr/bin/env python3
import rclpy
from rclpy.node import Node 
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
import math
import random

class turtlechase(Node):
    def __init__(self):
        self.t1pose = None
        self.t2pose = None
        super().__init__("turtlechase")
        self.pose_sub = self.create_subscription(Pose, '/turtle1/turtle2/pose', self.turtle2_pose, 10)
        self.pose2_sub = self.create_subscription(Pose, '/turtle1/turtle1/pose', self.turtle1_pose, 10)
        self.msg_pub = self.create_publisher(Twist, '/turtle1/turtle1/cmd_vel', 10)
        self.msg2_pub = self.create_publisher(Twist, '/turtle1/turtle2/cmd_vel', 10)
        self.timer1 = self.create_timer(0.5, self.tur1)

    def turtle2_pose(self, msg: Pose):
        self.t2pose = msg

    def turtle1_pose(self, msg: Pose):
        self.t1pose = msg

    def go_to_goal(self, x1, y1, x2, y2, x1_theta,pub):
        msg = Twist()
        dx = x2 - x1
        dy = y2 - y1

        distance = math.sqrt(dx**2 + dy**2)
        angle = math.atan2(dy, dx)
        angle_diff = angle - x1_theta
        distance_tolerance = 0.6

        while(distance >= distance_tolerance):
            msg.linear.x = 1.5 * distance
            msg.linear.y = 0.0
            msg.linear.z = 0.0

            msg.angular.x = 0.0
            msg.angular.y = 0.0
            msg.angular.z = 4.0 * angle_diff
            self.msg_pub.publish(msg)
        
        msg.linear.x = 0.0
        msg.angular.z = 0.0

        self.msg_pub.publish(msg)


    def tur1(self):
        self.get_logger().info("func called!")
        self.go_to_goal(self.t1pose.x, self.t1pose.y, self.t2pose.x, self.t2pose.y, self.t1pose.theta, 0)
        
        

def main(args = None):
    rclpy.init(args = args)
    mynode = turtlechase()
    rclpy.spin(mynode)
    rclpy.shutdown()

if __name__ == '__main__':
    main()