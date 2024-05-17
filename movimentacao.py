#!/usr/bin/env python3

import time
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist


class Desenhador(Node):
    def __init__(self):
        super().__init__('desenhador') 
        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.twist_msg = Twist()
    def send_cmd_vel(self, vx, vy, vtheta, tempo_em_ms):
        self.twist_msg.linear.x = vx
        self.twist_msg.linear.y = vy
        self.twist_msg.angular = vtheta
        self.publisher_.publish(self.twist_msg)
        print(f"Velocidade em X: {vx}, Velocidade em Y: {vy}, Velocidade angular{vtheta}")

    def movimento():
        rclpy.init()
        node = Desenhador()
        vx = input("velocidade em x: ")
        vy = input("velocidade em y: ")
        vtheta = input("velocidade angular: ")

        node.send_cmd_vel(vx, vy, vtheta)


def main(args=None):
    rclpy.init(args=args)

    desenhador = Desenhador()

    rclpy.spin(desenhador)

    desenhador.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()