import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from sensor_msgs.msg import CompressedImage
from cv_bridge import CvBridge
import cv2
import numpy as np

class CompressedCamera(Node):

    def __init__(self):
        super().__init__('compressed_camera')
        self.bridge = CvBridge()
        self.front_right_camera_publisher = self.create_publisher(Image, '/compressed/rgb_front_right/image', 10)
        self.front_right_camera_subscriber = self.create_subscription(
                Image,
                '/carla/ego_vehicle/rgb_front_right/image',
                self.publish_compressed_image,
                10)
        self.get_logger().info("Compressed camera node initialized and ready")

    def publish_compressed_image(self, msg):
        try:
            # Convert ROS Image message to OpenCV format
            cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
            
            # Compress the image using JPEG format
            _, compressed_image = cv2.imencode('.jpg', cv_image, [cv2.IMWRITE_JPEG_QUALITY, 90])

            # Decode the compressed image back to OpenCV format
            decompressed_image = cv2.imdecode(compressed_image, cv2.IMREAD_COLOR)

            # Convert the decompressed image back to a ROS Image message
            compressed_msg = self.bridge.cv2_to_imgmsg(decompressed_image, encoding='bgr8')

            # Publish the compressed image
            self.front_right_camera_publisher.publish(compressed_msg)

            self.get_logger().info('Compressed and published an image.')
        except Exception as e:
            self.get_logger().error(f"Error in image compression: {str(e)}")

def main(args=None):
    rclpy.init(args=args)
    compressed_camera = CompressedCamera()
    rclpy.spin(compressed_camera)
    compressed_camera.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
