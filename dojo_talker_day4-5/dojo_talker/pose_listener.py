# pose_listener.py
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose   # 注意导入 turtlesim 自带的 Pose 消息类型

class PoseListener(Node):
    def __init__(self):
        super().__init__('pose_listener')  # 节点名称
        self.subscription = self.create_subscription(
            Pose,                        # 接收的消息类型
            '/turtle1/pose',            # 订阅哪个话题
            self.pose_callback,         # 回调函数（消息一来就执行它）
            10                          # 消息队列大小
        )
        self.subscription  # 防止 Python 垃圾回收把它回收掉

    def pose_callback(self, msg):
        # 回调函数会自动收到消息对象 msg，我们打印位置信息
        self.get_logger().info(f'乌龟位置：x={msg.x:.2f}, y={msg.y:.2f}, theta={msg.theta:.2f}')

def main(args=None):
    rclpy.init(args=args)
    node = PoseListener()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
