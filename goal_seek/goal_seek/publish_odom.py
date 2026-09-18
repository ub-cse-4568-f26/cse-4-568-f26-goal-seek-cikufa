import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Quaternion
import math

class TurtlesimOdomPublisher(Node):
    def __init__(self):
        super().__init__('turtlesim_odom_publisher')
        self.pose_sub = self.create_subscription(Pose, '/turtle1/pose', self.pose_callback,10)
        self.odom_pub = self.create_publisher(Odometry, '/turtle1/odom', 10)
        self.x = None
        self.y = None
        self.theta = None

    def pose_callback(self, msg: Pose):
        odom = Odometry()
        odom.header.stamp = self.get_clock().now().to_msg()
        odom.header.frame_id = "turtle1/odom"
        odom.child_frame_id = "turtle1/base_link"


        if self.x is None:
            self.x = msg.x
            self.y = msg.y
            self.theta = msg.theta

        odom.pose.pose.position.x = msg.x - self.x
        odom.pose.pose.position.y = msg.y - self.y
        odom.pose.pose.position.z = 0.0
        theta = msg.theta - self.theta
        qz = math.sin(theta / 2.0)
        qw = math.cos(theta / 2.0)
        odom.pose.pose.orientation = Quaternion(x=0.0, y=0.0, z=qz, w=qw)

        odom.twist.twist.linear.x = msg.linear_velocity
        odom.twist.twist.angular.z = msg.angular_velocity

        self.odom_pub.publish(odom)

def main(args=None):
    rclpy.init(args=args)
    node = TurtlesimOdomPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
