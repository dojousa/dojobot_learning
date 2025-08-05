import rclpy                               # 引入 ROS2 Python 客户端库
from rclpy.node import Node                # 引入 Node 基类（所有节点必须继承它）
from turtlesim.msg import Pose            # 引入 turtlesim 提供的 Pose 消息类型（位置 + 朝向）

# 🧠 创建一个自定义节点类，继承自 Node
class PoseListener(Node):
    def __init__(self):
        super().__init__('pose_listener')  # 节点名称为 pose_listener
        # 创建订阅者，监听 /turtle1/pose 话题，收到消息后调用 self.pose_callback()
        self.subscription = self.create_subscription(
            Pose,                         # 消息类型
            '/turtle1/pose',              # 订阅的 topic 名
            self.pose_callback,           # 回调函数（收到消息时执行）
            10                            # 队列大小（防止消息丢失）
        )

    # 📥 回调函数：每收到一条 Pose 消息就会被调用
    def pose_callback(self, msg: Pose):
        # 日志输出当前乌龟的位置
        self.get_logger().info(f"位置：x={msg.x:.2f}, y={msg.y:.2f}, θ={msg.theta:.2f}")

# 🚀 节点入口：ROS2 程序执行的主函数
def main(args=None):
    rclpy.init(args=args)               # 初始化 rclpy 系统
    node = PoseListener()               # 创建我们定义的 Node 实例
    rclpy.spin(node)                    # 进入 ROS2 循环，等待消息回调
    node.destroy_node()                 # 程序退出前销毁节点
    rclpy.shutdown()                    # 关闭 ROS2

# ✅ 只有当直接运行该文件时，才会执行 main()
if __name__ == '__main__':
    main()
