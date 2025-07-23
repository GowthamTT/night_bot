import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import os
from ultralytics import YOLO
import time

class ImageSubscriber(Node):
    def __init__(self):
        super().__init__('image_subscriber')
        self.subscription = self.create_subscription(
            Image,
            '/camera/image_raw',
            self.listener_callback,
            10)
        self.subscription
        self.bridge = CvBridge()

        self.model = YOLO("/home/ultra/yolo11n.pt") 

        self.save_directory = "/home/ultra/yolo_frames"
        if not os.path.exists(self.save_directory):
            os.makedirs(self.save_directory)

    def listener_callback(self, data):

        current_frame = self.bridge.imgmsg_to_cv2(data, desired_encoding='bgr8')

        results = self.model(current_frame)

        detections = results[0].boxes

        human_boxes = []
        human_detected = False  

        for detection in detections:
           
            if detection.cls == 0:  
                human_boxes.append(detection)
                human_detected = True  

        if human_detected:
        
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            filename = os.path.join(self.save_directory, f"frame_{timestamp}.png")

            cv2.imwrite(filename, current_frame)
            self.get_logger().info(f"Human detected! Frame saved as {filename}")

        annotated_frame = results[0].plot(boxes=human_boxes)

        cv2.imshow("Camera Feed - Human Detection", annotated_frame)
        cv2.waitKey(5)

def main(args=None):
    rclpy.init(args=args)
    image_subscriber = ImageSubscriber()
    rclpy.spin(image_subscriber)
    image_subscriber.destroy_node()
    rclpy.shutdown()
