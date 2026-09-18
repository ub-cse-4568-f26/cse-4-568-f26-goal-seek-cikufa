import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
import math
import tf_transformations
from ament_index_python.packages import get_package_share_directory
import os


class TurtleWaypointController(Node):
    def __init__(self):
        super().__init__('turtle_controller')

        self.waypoints = []
        self.read_waypoints('goals.txt')

        ###############################

        # Your code goes here

        ###############################

    def read_waypoints(self, filename):
        goals_filepath = os.path.join(get_package_share_directory('goal_seek'),"config", filename)
        ###############################
        # Code to read and parse the waypoints from the file

        ###############################

    ###############################

        # Your code goes here

    ###############################
    


def main(args=None):
    ###############################

        # Your code goes here

    ###############################
    pass


if __name__ == '__main__':
    main()
