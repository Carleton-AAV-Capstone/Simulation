# Simulation

Simulation system to test autonomous control of ECOLO vehicle.

## Installation

### Install Docker 
1. [Install Docker using the repository](https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository)
2. [Allow non-root users to use Docker](https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user)
### Set up CARLA 
1. Pull CARLA image from docker hub.
```
docker pull carlasim/carla:0.9.13
```
2. If issues arise allow Docker to use the current X server.
```
xhost local:docker
```
3. (Optional) Run CARLA in Docker to test.
```
docker run --privileged --gpus all --net=host -e DISPLAY=$DISPLAY carlasim/carla:0.9.13 ./CarlaUE4.sh
```
### Set up ROS bridge
1. Clone the ROS bridge repository
```
git clone --recurse-submodules https://github.com/carla-simulator/ros-bridge.git src/ros-bridge
```
2. Build the ROS bridge image inside the docker folder
```
cd ros-bridge/docker
./build.sh
```
3. (Optional) Run ROS bridge with the run script or generate your own dockerfile using the ROS bridge docker image.
```
./run.sh
```
## Usage
1. Build and run the CARLA and ROS bridge docker containers with Docker compose.
```
docker compose up --build
```
2. Bash to interact with ROS bridge
```
docker exec -it simulation-main-1 bash
```
3. Prepare the ROS2 environment inside the ROS bridge container
```
source ./install/setup.bash/
```

