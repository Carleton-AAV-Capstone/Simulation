#!/bin/bash

# Run ros-bridge container
docker run -it --network host carla-ros-bridge:foxy

# Start ROS bridge
ros2 launch carla_ros_bridge carla_ros_bridge.launch.py timeout:=10000 sychronous_mode:=false

# Spawn Objects (vehicles, sensors)
