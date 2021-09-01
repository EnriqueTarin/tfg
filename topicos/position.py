from nav_msgs.msg import Odometry
import rospy
from sensor_msgs.msg import Imu

class position:
  
  def __init__(self):  
    self.position_linear_x = 0
    self.curposition_linear_y = 0
    self.position_linear_z= 0
    self.position_angular_x = 0
    self.position_angular_y = 0
    self.position_angular_z = 0
    self.battery_info_sub=rospy.Subscriber("/robot/robotnik_base_control/odom",Odometry,self.odometry_cb)
    self.battery_info_sub=rospy.Subscriber("/robot/imu/data",Imu,self.imu_cb)

  def odometry_cb(self,msg):
    self.position_linear_x = msg.pose.pose.position.x
    self.position_linear_y = msg.pose.pose.position.y
    self.position_linear_z = msg.pose.pose.position.z  

    self.position_angular_x = msg.pose.pose.orientation.x
    self.position_angular_y = msg.pose.pose.orientation.y
    self.position_angular_z = msg.pose.pose.orientation.z 

  def imu_cb(self,msg):
    self.imu_angular_vel_X = msg.angular_velocity.x
    self.imu_angular_vel_y = msg.angular_velocity.y
    self.imu_angular_vel_z = msg.angular_velocity.z

    self.imu_linear_acc_x = msg.linear_acceleration.x
    self.imu_linear_acc_y = msg.linear_acceleration.y
    self.imu_linear_acc_z = msg.linear_acceleration.z


  def __main__(self):
    rospy.spin()
    self.odometry_cb
    self.imu_cb