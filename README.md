# turtlebot3_autonomous_navigation
#task 1
Launch the Turtlebot3 robot in gazebo simulation using ROS2
#used
#ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
#task 2
#control the robot by sending velocity command#
#ros2 topic pub /cmd_vel geometry_msgs/msg/Twist \
"{linear: {x: 0.2, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 0.3}}" -r 10
#task 3
#perform slam and create a map of the simulation
#used
ros2 launch turtlebot3_cartographer cartographer.launch.py use_sim_time:=True
ros2 run turtlebot3_teleop teleop_keyboard
#used to save the map
ros2 run nav2_map_server map_saver_cli -f maps/my_maps
#used to open the saved map
#ros2 launch turtlebot3_navigation2 navigation2.launch.py use_sim_time:=True map:=maps/my_maps.yaml
colcon build
source install/setup.bash
ros2 run turtlebot3_point_nav auto_navigator(to run the script)
![image](https://github.com/user-attachments/assets/5bc56c44-4530-442f-a2d4-185118720b6f)
![image](https://github.com/user-attachments/assets/72649ff9-3cc9-4778-9110-f08bfef1d8db)
![image](https://github.com/user-attachments/assets/5880823d-8f0f-4591-bd33-42575874d00b)
![image](https://github.com/user-attachments/assets/0e5218a8-a694-4c34-88d5-abab171aac8f)





