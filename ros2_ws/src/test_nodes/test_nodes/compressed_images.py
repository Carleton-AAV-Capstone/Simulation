import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class CompressedCamera(Node):
    def __init__(self):
        super().__init__('compressed_camera')
        self.bridge = CvBridge()
        self.camera_topics =  [
            '/carla/ego_vehicle/rgb_front_right/image'
            '/carla/ego_vehicle/rgb_front_left/image'
            '/carla/ego_vehicle/rgb_side_right/image'
            '/carla/ego_vehicle/rgb_side_left/image'
        ]
        self.compressed_publisher = {}
        for topic in self.camera_topics:
            self.create_subscription(
                Image,
                topic,
                lambda msg, topic=topic: self.image_callback(msg, topic),
                10
            )
            compressed_topic = f"{topic}/compressed"
            self.compressed_publishers[topic] = self.create_publisher(Image, compressed_topic, 10)
            self.get_logger().info(f"Set up subscription and publishing for: {topic}")

    def timer_callback(self):
        cv_image = self.bridge.imgmsg_to_cv2(msg, 'bgr8')
        success, encoded_image = cv2.imencode('.jpg', cv_image)
        if not success:
            self.get_logger().error(f"Failed to encode image for topic {topic}")
            return
        compressed_msg = self.bridge.cv2_to_imgmsg(encoded_image, encoding='bgr8')
        compressed_msg.header = msg.header
        self.compressed_publishers[topic].publish(compressed_msg)
        self.get_logger().info(f"Published compressed image for topic: {topic}")

def main(args=None):
    rclpy.init(args=args)
    compressed_camera = CompressedCamera()
    rclpy.spin(compresed_camera)
    compressed_camera.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
