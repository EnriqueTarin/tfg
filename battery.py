#from _typeshed import Self
#from robot_monitor.prueba_ejemplo_servidor import battery_fuc
from robotnik_msgs.msg import BatteryStatus
import rospy
from std_msgs.msg import Float32

class Battery:
  
  def __init__(self):  
    self.voltage = 0
    self.current = 0
    self.level= 0
    self.capacity = 0
    self.noisy_capacity = 0
    self.battery_info_sub=rospy.Subscriber("/robot/battery_estimator/data",BatteryStatus,self.battery_info_cb)
    self.battery_capacity_sub =rospy.Subscriber('/robot/battery_estimator/debug/present_capacity',Float32,self.capacity_cb)
    self.battery_noisy_capacity_sub= rospy.Subscriber('/robot/battery_estimator/debug/noisy_present_capacity',Float32,self.noisy_capacity_cb)

  def battery_info_cb(self,msg):
    self.voltage = msg.voltage
    self.current = msg.current
    self.level = msg.level 

  def capacity_cb(self,msg):
    self.capacity = msg.data
  def noisy_capacity_cb(self,msg):
    self.noisy_capacity = msg.data


  def __main__(self):
    rospy.spin()
    self.battery_info_cb
    self.capacity_cb