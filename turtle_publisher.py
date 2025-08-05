import rclpy                              # ROS2 Python 客户端
from rclpy.node import Node               # 节点基类
from geometry_msgs.msg import Twist       # 控制速度的消息类型

class TurtlePublisher(Node):
    def __init__(self):
        super().__init__('turtle_publisher')   # 节点名称
        self.publisher = self.create_publisher(
            Twist,                          # 消息类型：速度控制
            '/turtle1/cmd_vel',             # 发布到这个 topic 上
            10                              # 队列大小
        )
        timer_period = 0.5                  # 每 0.5 秒发一次速度命令
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = Twist()
        msg.linear.x = 2.0                 # 前进速度
        msg.angular.z = 1.0                # 转弯速度
        self.publisher.publish(msg)       # 发送指令
        self.get_logger().info('发出速度指令：前进 2.0，转弯 1.0')

def main(args=None):
    rclpy.init(args=args)                 # 初始化 ROS2
    node = TurtlePublisher()              # 创建节点对象
    rclpy.spin(node)                      # 开始监听回调
    node.destroy_node()                   # 程序退出前清理资源
    rclpy.shutdown()                      # 关闭 ROS2 系统

# ✅ 直接运行才执行 main（防止模块导入时自动执行）
if __name__ == '__main__':
    main()
