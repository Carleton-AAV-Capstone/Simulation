#!/bin/bash
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

ros2 launch carla_ros_bridge carla_ros_bridge.launch.py synchronous_mode:=false town:=town01 register_all_sensors:=false timeout:=3000 &
ros2 launch carla_waypoint_publisher carla_waypoint_publisher.launch.py &
ros2 launch ./launch/basic_launch.py &
/bin/bash
