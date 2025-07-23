import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():

    pkg_name='my_bot'
    world_file='/home/ultra/world21.world'

    rsp_launch = IncludeLaunchDescription(PythonLaunchDescriptionSource([os.path.join(get_package_share_directory(pkg_name), 'launch', 'rsp.launch.py')]), launch_arguments={'use_sim_time' : 'true'}.items())
    
    gazebo = IncludeLaunchDescription(PythonLaunchDescriptionSource([os.path.join(
        get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py'
    )]),launch_arguments={'world': world_file}.items()
    )

    spawn = Node(package='gazebo_ros', executable='spawn_entity.py', 
                 arguments=['-topic', 'robot_description', '-entity', 'my_bot'], output='screen')
    

    return LaunchDescription([
        rsp_launch,
        gazebo,
        spawn
    ])