import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

class CenterFollower(Node):
    def __init__(self):
        super().__init__('center_follower')

        # 🧭 订阅乌龟的位置（就像眼睛）
        self.subscription = self.create_subscription(
            Pose,
            '/turtle1/pose',
            self.pose_callback,
            10
        )

        # 🦶 发布移动指令（就像脚步控制）
        self.publisher = self.create_publisher(
            Twist,
            '/turtle1/cmd_vel',
            10
        )

    def pose_callback(self, msg):
        # 目标点：屏幕中心 (5.5, 5.5)
        target_x = 5.5
        target_y = 5.5

        dx = target_x - msg.x
        dy = target_y - msg.y

        # 简单的P控制，让它朝向目标走
        cmd = Twist()
        cmd.linear.x = 0.5 * (dx**2 + dy**2)**0.5     # 朝目标点前进
        cmd.angular.z = 2.0 * (msg.theta - self.compute_angle(dx, dy))  # 转向

        self.publisher.publish(cmd)
        self.get_logger().info(f'位置：x={msg.x:.2f}, y={msg.y:.2f}，目标指令已发出')

    def compute_angle(self, dx, dy):
        # 根据坐标差计算目标角度（单位：弧度）
        import math
        return math.atan2(dy, dx)

def main(args=None):
    rclpy.init(args=args)
    node = CenterFollower()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
