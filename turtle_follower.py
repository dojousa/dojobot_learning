import math
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist

class TurtleFollower(Node):
    def __init__(self):
        super().__init__('turtle_follower')
        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.subscription = self.create_subscription(Pose, '/turtle1/pose', self.pose_callback, 10)
        self.target_x = 8.0
        self.target_y = 5.0

    def pose_callback(self, pose: Pose):
        dx = self.target_x - pose.x
        dy = self.target_y - pose.y

        distance = math.sqrt(dx**2 + dy**2)
        angle_to_target = math.atan2(dy, dx)
        angle_diff = angle_to_target - pose.theta

        msg = Twist()

        # 🧠 闭环控制逻辑
        if abs(angle_diff) > 0.1:
            msg.angular.z = 2.0 * angle_diff
        else:
            msg.linear.x = 1.5 * distance

        self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = TurtleFollower()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
