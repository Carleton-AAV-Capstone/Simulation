import os
import launch
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    ld = launch.LaunchDescription([
        launch.actions.DeclareLaunchArgument(
            name='objects_definition_file',
            default_value=get_package_share_directory(
                'test_nodes') + '/config/objects.json'
        ),
        launch.actions.DeclareLaunchArgument(
            name='role_name',
            default_value='ego_vehicle'
        ),
        launch.actions.DeclareLaunchArgument(
            name='spawn_point_ego_vehicle',
            default_value='None'
        ),
        launch.actions.DeclareLaunchArgument(
            name='spawn_sensors_only',
            default_value='False'
        ),
        launch.actions.DeclareLaunchArgument(
            name='control_id',
            default_value='control'
        ),
        Node(
            package='test_nodes',
            namespace='test',
            executable='compressed_camera',
            name='compressed_camera'
        ),
        Node(
            package='test_nodes',
            namespace='test',
            executable='ackermann_control',
            name='ackermann_control'
        ),
        Node(
            package='test_nodes',
            namespace='test',
            executable='emergency_stop',
            name='emergency_stop'
        ),
        launch.actions.IncludeLaunchDescription(
            launch.launch_description_sources.PythonLaunchDescriptionSource(
                os.path.join(get_package_share_directory(
                    'carla_ackermann_control'), 'carla_ackermann_control.launch.py')
                ),
            launch_arguments={
                'role_name': launch.substitutions.LaunchConfiguration('role_name')
                }.items()
            ),
        launch.actions.IncludeLaunchDescription(
            launch.launch_description_sources.PythonLaunchDescriptionSource(
                os.path.join(get_package_share_directory(
                    'carla_spawn_objects'), 'carla_spawn_objects.launch.py')
            ),
            launch_arguments={
                'objects_definition_file': launch.substitutions.LaunchConfiguration('objects_definition_file'),
                'spawn_point_ego_vehicle': launch.substitutions.LaunchConfiguration('spawn_point_ego_vehicle'),
                'spawn_sensors_only': launch.substitutions.LaunchConfiguration('spawn_sensors_only')
            }.items()
        ),
        launch.actions.IncludeLaunchDescription(
            launch.launch_description_sources.PythonLaunchDescriptionSource(
                os.path.join(get_package_share_directory(
                    'carla_spawn_objects'), 'set_initial_pose.launch.py')
            ),
            launch_arguments={
                'role_name': launch.substitutions.LaunchConfiguration('role_name'),
                'control_id': launch.substitutions.LaunchConfiguration('control_id')
            }.items()
        )
    ])
    return ld


if __name__ == '__main__':
    generate_launch_description()
