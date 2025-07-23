from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess    

def generate_launch_description():

    turtle1 = 'turtle1'

    turtle = Node(
        package = 'turtlesim',
        executable = 'turtlesim_node',
        namespace = turtle1,
        output = 'screen'
    )

    spawn_turtle = ExecuteProcess(
        cmd=[[
            'ros2 service call ',
            turtle1,
            '/spawn ',
            'turtlesim/srv/Spawn ',
            '"{x: 2, y: 2, theta: 0.2}"'
        ]],
        shell=True
    )

    # draw_circle = Node(package = 'launch_ex', executable = 'draw_circle.py', name='draw_circle', output = 'screen')

    
    return LaunchDescription([
        turtle,
        spawn_turtle,
        # draw_circle
    ])
   

