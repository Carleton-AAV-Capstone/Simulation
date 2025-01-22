FROM carla-ros-bridge:foxy

RUN /bin/bash -c "python3 -m pip install --force-reinstall 'simple-pid==1.0.1'"
RUN /bin/bash -c "python3 -m pip install --force-reinstall 'matplotlib'"

RUN mkdir -p /opt/simulation
WORKDIR /opt/simulation

COPY ./ros2_ws /opt/simulation

RUN /bin/bash -c "source /opt/ros/foxy/setup.bash && \
    colcon build --symlink-install"

COPY ./ros_entrypoint.sh /

CMD /bin/bash -c "sleep 5 && bash ./run.sh"
