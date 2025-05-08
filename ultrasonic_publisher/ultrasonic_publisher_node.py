import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
from gpiozero import DistanceSensor
from signal import pause

TRIG = 18 # 트리거
ECHO = 21 # 에코

class UltrasonicPublisher(Node):
    def __init__(self):
        super().__init__('ultrasonic_publisher')
        self.publisher_ = self.create_publisher(Float32, 'distance', 10)
        self.sensor = DistanceSensor(echo=ECHO, trigger=TRIG, max_distance=3.0)
        self.timer = self.create_timer(0.05, self.publish_distance)

    def publish_distance(self):
        distance_m = self.sensor.distance  # distance in meters (0.0 to 1.0)
        distance_cm = distance_m * 100.0
        msg = Float32()
        # msg.data = distance_cm
        msg.data = distance_m
        self.publisher_.publish(msg)
        self.get_logger().info(f"Distance: {distance_cm:.2f} cm")

def main(args=None):
    rclpy.init(args=args)
    node = UltrasonicPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()

