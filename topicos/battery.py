from robotnik_msgs.msg import BatteryStatus
import rospy

class Battery:
  
  def __init__(self):  
    self.voltage = 0
    self.current = 0
    self.level= 0
    self.battery_info_sub=rospy.Subscriber("/robot/battery_estimator/data",BatteryStatus,self.battery_info_cb)

  def battery_info_cb(self,msg):
    self.voltage = msg.voltage
    self.current = msg.current
    self.level = msg.level  

  def __main__(self):
    rospy.spin()


#if __name__ == '__main__':
#    rospy.init_node('nodo_monitor_bateria', anonymous=True)
#    nodo_bateria = Battery()
#    try:
#        nodo_bateria.__main__()
#    except rospy.ROSInterruptException:
#        pass
