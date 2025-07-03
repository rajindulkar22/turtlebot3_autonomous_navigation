#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from nav2_msgs.action import NavigateToPose
from geometry_msgs.msg import PoseStamped
import time

class TurtleBotNavigator(Node):
    def __init__(self):
        super().__init__('turtlebot3_navigator_action')
        self._client = ActionClient(self, NavigateToPose, 'navigate_to_pose')
        self.get_logger().info("Action client created")

    def send_goal(self, x, y, w=1.0):
        while not self._client.wait_for_server(timeout_sec=5.0):
            self.get_logger().info('Waiting for "navigate_to_pose" action server...')

        goal_msg = NavigateToPose.Goal()
        goal_msg.pose.header.frame_id = 'map'
        goal_msg.pose.header.stamp = self.get_clock().now().to_msg()
        goal_msg.pose.pose.position.x = x
        goal_msg.pose.pose.position.y = y
        goal_msg.pose.pose.orientation.w = w  # Facing forward

        self.get_logger().info(f"Sending goal: x={x}, y={y}")
        send_goal_future = self._client.send_goal_async(goal_msg)
        rclpy.spin_until_future_complete(self, send_goal_future)

        goal_handle = send_goal_future.result()
        if not goal_handle.accepted:
            self.get_logger().error('Goal rejected!')
            return

        self.get_logger().info('Goal accepted.')
        result_future = goal_handle.get_result_async()
        rclpy.spin_until_future_complete(self, result_future)

        result = result_future.result().result
        self.get_logger().info(f'Goal finished with result: {result}')

def main(args=None):
    rclpy.init(args=args)
    navigator = TurtleBotNavigator()

    point_a = (0.2, 0.0)
    point_b = (1.5, 1.5)

    navigator.send_goal(*point_b)
    navigator.send_goal(*point_a)

    navigator.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

