#!/usr/bin/env python3
import rclpy
from rclpy.node import Node 
from geometry_msgs.msg import Twist

class turtle_func(Node):

    def __init__(self):
        super().__init__("draw_circle")
        self.turtle_vel = self.create_publisher(Twist, "/turtle1/turtle1/cmd_vel", 10)
        self.timer = self.create_timer(0.5, self.vel_pub)
        self.get_logger().info("node is also executing!!")

    def vel_pub(self):
        self.get_logger().info("Publishing velocity!")
        msg = Twist()
        msg.linear.x = 1.0
        msg.angular.z = 0.4
        self.turtle_vel.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = turtle_func()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()