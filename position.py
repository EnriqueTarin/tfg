from nav_msgs.msg import Odometry
import rospy

class position:
  
  def __init__(self):  
    self.position_linear_x = 0
    self.current = 0
    self.level= 0
    self.battery_info_sub=rospy.Subscriber("/robot/robotnik_base_control/odom",Odometry,self.odometry_cb)

  def odometry_cb(self,msg):
    self.position_linear_x = msg.pose.pose.position.x
    self.position_linear_y = msg.pose.pose.position.y
    self.position_linear_z = msg.pose.pose.position.z  

    self.position_angular_x = msg.pose.pose.orientation.x
    self.position_angular_y = msg.pose.pose.orientation.y
    self.position_angular_z = msg.pose.pose.orientation.z 

  def __main__(self):
    rospy.spin()
    self.odometry_cb