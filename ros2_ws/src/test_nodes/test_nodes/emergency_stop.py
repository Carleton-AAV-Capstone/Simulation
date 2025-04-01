import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool 
from ackermann_msgs.msg import AckermannDrive

class EmergencyStop(Node):
    def __init__(self):
        super().__init__('emergency_stop')
        self.control_info_subscriber = self.create_subscription(
            Bool,
            '/e_stop',
            self.emergency_stop_response,
            10
        )
        self.ackermann_stop_publisher = self.create_publisher(AckermannDrive, '/carla/ego_vehicle/ackermann_cmd', 10)
        self.get_logger().info("Emergency Stop Node initialized")

    def emergency_stop_response(self, msg):
        try:
            if msg.data:
                self.get_logger().info("Emergency Stop is active")
                ackermann_msg = AckermannDrive()
                ackermann_msg.speed = 1.0
                ackermann_msg.acceleration = 0.0
                # Publish the AckermannDrive message
                self.ackermann_publisher.publish(ackermann_msg)
                self.get_logger().info(f"Published AckermannDrive: {ackermann_msg}")
            else:
                self.get_logger().info("Emergency Stop is NOT ACTIVE")
        except Exception as e:
            self.get_logger().error(f"Error processing control_info message: {str(e)}")

def main(args=None):
    rclpy.init(args=args)
    emergency_stop = EmergencyStop()
    rclpy.spin(emergency_stop)
    emergency_stop.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
