import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32, Header
from gpiozero import DistanceSensor

TRIG = 18
ECHO = 21
MAX_DIST = 3.0
DT = 0.05

class UltrasonicPublisher(Node):
    def __init__(self):
        super().__init__('ultrasonic_publisher')
        self.header_pub_ = self.create_publisher(Header, 'distance_header', 10)
        self.dist_pub_ = self.create_publisher(Float32, 'distance', 10)
        # https://gpiozero.readthedocs.io/en/stable/api_input.html#distancesensor-hc-sr04
        self.sensor = DistanceSensor(echo=ECHO, trigger=TRIG, max_distance=MAX_DIST)
        self.timer = self.create_timer(DT, self.publish_distance)

    def publish_distance(self):
        msg_header = Header()
        msg_header.stamp = self.get_clock().now().to_msg()
        
        distance_m = self.sensor.distance  # distance in meters
        msg = Float32()
        msg.data = distance_m
        
        self.header_pub_.publish(msg_header)
        self.dist_pub_.publish(msg)
        self.get_logger().info(f"Distance: {distance_m:.3f} m")

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

