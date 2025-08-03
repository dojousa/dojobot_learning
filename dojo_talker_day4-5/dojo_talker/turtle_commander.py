# turtle_commander.py
import rclpy                              # ROS2 Python client
from rclpy.node import Node               # 节点基类
from geometry_msgs.msg import Twist       # 要发布的消息类型（控制速度）

class TurtleCommander(Node):              # 定义一个类，继承 Node
    def __init__(self):
        super().__init__('turtle_commander')          # 节点名字
        self.publisher_ = self.create_publisher(      # 创建 publisher 对象
            Twist,                                    # 要发什么类型的数据
            '/turtle1/cmd_vel',                       # 发给哪个话题
            10                                        # 队列大小（控制缓冲）
        )
        timer_period = 0.5                            # 发送频率（每0.5秒）
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.get_logger().info('Turtle Commander started.')

    def timer_callback(self):
        msg = Twist()
        msg.linear.x = 2.0      # 前进速度
        msg.angular.z = 1.0     # 旋转角速度
        self.publisher_.publish(msg)
        self.get_logger().info('发送移动指令')

def main(args=None):
    rclpy.init(args=args)
    node = TurtleCommander()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
