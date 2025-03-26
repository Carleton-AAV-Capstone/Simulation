import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class CompressedCamera(Node):
    def __init__(self):
        super().__init__('compressed_camera')
        self.bridge = CvBridge()
        self.front_right_camera_publisher = self.create_publisher(Image, '/compressed/rgb_front_right/image', 15)
        self.front_right_camera_subscriber = self.create_subscription(
                Image,
                '/carla/ego_vehicle/rgb_front_right/image',
                self.publish_compressed_image,
                10)
        self.get_logger().info("Compressed camera node initialized and ready")

    def publish_compressed_image(self, img_msg):
        try:
            # Convert ROS Image message to OpenCV format
            cv_img = self.bridge.imgmsg_to_cv2(img_msg, 'bgr8')

            # Encode the OpenCV image to JPEG
            success, encoded_img = cv2.imencode('.jpg', cv_img)
            if not success:
                self.get_logger().error("Failed to encode image to JPEG format")
                return

            # Manually create a compressed ROS Image message
            compressed_msg = Image()
            compressed_msg.header = img_msg.header
            compressed_msg.data = encoded_img.tobytes()  # Convert to raw bytes
            compressed_msg.encoding = 'jpeg'

            # Publish the compressed image
            self.front_right_camera_publisher.publish(compressed_msg)
            self.get_logger().info("Published compressed image successfully")

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
