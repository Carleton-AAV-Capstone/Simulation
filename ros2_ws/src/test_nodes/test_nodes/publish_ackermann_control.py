import rclpy
from rclpy.node import Node
from ackermann_msgs.msg import AckermannDrive
from carla_ackermann_msgs.msg import EgoVehicleControlInfo

class AckermannControl(Node):
    def __init__(self):
        super().__init__('ackermann_control')
        self.control_info_subscriber = self.create_subscription(
                EgoVehicleControlInfo,
                '/carla/ego_vehicle/ackermann_control/control_info',
                self.control_info_callback,
                10
            )
        self.ackermann_publisher = self.create_publisher(AckermannDrive, '/ackermann_drive', 10)
        self.get_logger().info("Ackermann Publisher Node initialized")

    def control_info_callback(self, msg):
        try:
            # Extract data from EgoVehicleControlInfo
            ackermann_msg = AckermannDrive()
            ackermann_msg.steering_angle = msg.target.steering_angle
            ackermann_msg.speed = msg.target.speed
            ackermann_msg.acceleration = msg.target.accel
            ackermann_msg.jerk = msg.target.jerk
            
            # Publish the AckermannDrive message
            self.ackermann_publisher.publish(ackermann_msg)
            self.get_logger().info(f"Published AckermannDrive: {ackermann_msg}")
        
        except Exception as e:
            self.get_logger().error(f"Error processing control_info message: {str(e)}")

def main(args=None):
    rclpy.init(args=args)
    ackermann_control = AckermannControl()
    rclpy.spin(ackermann_control)
    ackermann_control.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
