from prometheus_client import start_http_server, Metric, REGISTRY, Gauge
import json
import requests
import sys
import time
import rospy 
from battery import Battery
from position import position

class JsonCollector(object):

  def __init__(self, endpoint):
    rospy.init_node('robot_monitor')
    self.bateria=Battery()
    self.posicion=position()

    self._endpoint = endpoint

  def collect(self):
    # Fetch the JSON
    response = json.loads(requests.get(self._endpoint).content.decode('UTF-8'))

    # Convert requests and duration to a summary in seconds
    metric = Metric('svc_requests_duration_seconds',
        'Requests time taken in seconds', 'summary')
    metric.add_sample('svc_requests_duration_seconds_count',
        value=response['requests_handled'], labels={})
    metric.add_sample('svc_requests_duration_seconds_sum',
        value=response['requests_duration_milliseconds'] / 1000.0, labels={})
    yield metric

    # Counter for the failures
    metric = Metric('svc_requests_failed_total',
       'Requests failed', 'summary')
    metric.add_sample('svc_requests_failed_total',
       value=response['request_failures'], labels={})
    yield metric

    # Metrics with labels for the documents loaded
    metric = Metric('svc_documents_loaded', 'Requests failed', 'gauge')
    for k, v in response['documents_loaded'].items():
      metric.add_sample('svc_documentes_loaded', value=v, labels={'repository': k})
    yield metric

    self.battery_fuc()
    self.position_func()

  def battery_fuc(self):
     # Gauges 
     voltaje=Gauge('robot_voltaje','voltaje de la bateria')
     capacidad=Gauge('robot_capacidad_bateria','capacidad de la bateria')
     capacidad_ruido=Gauge('robot_cacidad_bateria_ruido','capacidad de la bateria con ruido generado por factores externos')
     nivel=Gauge('robot_nivel_bateria','Nivel de la bateria')
     # Metiendo datos a las variables para enviarlas a prometheus
     voltaje.set(self.bateria.voltage)
     nivel.set(self.bateria.level) 
     capacidad.set(self.bateria.capacity)
     capacidad_ruido.set(self.bateria.noisy_capacity)


  def position_func(self):
    #Odom
        #Lineal
    odom_linear_x=Gauge('robot_lienal_odom_x','odometria lineal del eje x')
    odom_linear_y=Gauge('robot_lineal_odom_y','odometria lineal del eje y')
    odom_linear_z=Gauge('robot_lienal_odom_z','odometria lineal del eje z')
    odom_linear_x.set(self.posicion.position_linear_x)
    odom_linear_y.set(self.posicion.position_linear_y )
    odom_linear_z.set(self.posicion.position_linear_z)
        #Angular
    odom_angular_x=Gauge('robot_odom_angular_x','odometria angular del eje x')
    odom_angular_y=Gauge('robot_odom_angular_y','odometria angular del eje y')
    odom_angular_z=Gauge('robot_odom_angular_z','odometria angular del eje z')
    odom_angular_x.set(self.posicion.position_angular_x)
    odom_angular_y.set(self.posicion.position_angular_y)
    odom_angular_z.set(self.posicion.position_angular_z)
    #Imu
    imu_linear_acc_x = Gauge('robot_imu_linear_acc_x','informacion de la imu acceleracion eje x')
    imu_linear_acc_y = Gauge('robot_imu_linear_acc_y','informacion de la imu acceleracion eje y')
    imu_linear_acc_z = Gauge('robot_imu_linear_acc_z','informacion de la imu acceleracion eje z')

    imu_linear_acc_x.set(self.posicion.imu_linear_acc_x)
    imu_linear_acc_y.set(self.posicion.imu_linear_acc_y)
    imu_linear_acc_z.set(self.posicion.imu_linear_acc_z)
    
    imu_angular_vel_x = Gauge('robot_imu_angular_vel_x','informacion de la velocidad angular del eje x')
    imu_angular_vel_y = Gauge('robot_imu_angular_vel_y','informacion de la velocidad angular del eje y')
    imu_angular_vel_z = Gauge('robot_imu_angular_vel_z','informacion de la velocidad angular del eje z')
    imu_angular_vel_x.set(self.posicion.imu_angular_vel_X)
    imu_angular_vel_y.set(self.posicion.imu_angular_vel_y)   
    imu_angular_vel_z.set(self.posicion.imu_angular_vel_z)

if __name__ == '__main__':
  # Usage: json_exporter.py port endpoint
  start_http_server(int(sys.argv[1]))
  REGISTRY.register(JsonCollector(sys.argv[2]))
  while True: 
      time.sleep(1)
      rospy.spin()