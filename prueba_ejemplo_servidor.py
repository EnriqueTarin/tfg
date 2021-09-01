#!/usr/bin/env python
# -*- coding: utf-8 -*-
from prometheus_client import start_http_server, Summary, Gauge
import random
import time
import rospy
from battery import Battery
from position import position

rate = rospy.Rate(2)
rospy.init_node('robot_monitor')
# Objetos tipoc clase
bateria=Battery()
posicion=position()

REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')
# Decorate function with metric.
@REQUEST_TIME.time()
def process_request(t):
    """A dummy function that takes some time."""
    time.sleep(t)

def battery_fuc():
    # Gauges 
    voltaje=Gauge('robot_voltaje','voltaje de la bateria')
    capacidad=Gauge('robot_capacidad_bateria','capacidad de la bateria')
    capacidad_ruido=Gauge('robot_cacidad_bateria_ruido','capacidad de la bateria con ruido generado por factores externos')
    nivel=Gauge('robot_nivel_bateria','Nivel de la bateria')
    # Metiendo datos a las variables para enviarlas a prometheus
    voltaje.set(bateria.voltage)
    nivel.set(bateria.level) 
    capacidad.set(bateria.capacity)
    capacidad_ruido.set(bateria.noisy_capacity)

def position_func():
#Gauges
    #Odom
        #Lineal
    odom_linear_x=Gauge('robot_lienal_odom_x','odometria lineal del eje x')
    odom_linear_y=Gauge('robot_lineal_odom_y','odometria lineal del eje y')
    odom_linear_z=Gauge('robot_lienal_odom_z','odometria lineal del eje z')
        #Angular
    odom_angular_x=Gauge('robot_odom_angular_x','odometria angular del eje x')
    odom_angular_y=Gauge('robot_odom_angular_y','odometria angular del eje y')
    odom_angular_z=Gauge('robot_odom_angular_z','odometria angular del eje z')
    #Imu
    imu_linear_acc_x = Gauge('robot_imu_linear_acc_x','informacion de la imu acceleracion eje x')
    imu_linear_acc_y = Gauge('robot_imu_linear_acc_y','informacion de la imu acceleracion eje y')
    imu_linear_acc_z = Gauge('robot_imu_linear_acc_z','informacion de la imu acceleracion eje z')

    imu_angular_vel_x = Gauge('robot_imu_angular_vel_x','informacion de la velocidad angular del eje x')
    imu_angular_vel_y = Gauge('robot_imu_angular_vel_y','informacion de la velocidad angular del eje y')
    imu_angular_vel_z = Gauge('robot_imu_angular_vel_z','informacion de la velocidad angular del eje z')

    odom_linear_x.set(posicion.position_linear_x)
    odom_linear_y.set(posicion.position_linear_y)
    odom_linear_z.set(posicion.position_linear_z)

    odom_angular_x.set(posicion.position_angular_x)
    odom_angular_y.set(posicion.position_angular_y)
    odom_angular_z.set(posicion.position_angular_z)

    imu_linear_acc_x.set(posicion.imu_linear_acc_x)
    imu_linear_acc_y.set(posicion.imu_linear_acc_y)
    imu_linear_acc_z.set(posicion.imu_linear_acc_z)

    imu_angular_vel_x.set(posicion.imu_angular_vel_X)
    imu_angular_vel_y.set(posicion.imu_angular_vel_y)   
    imu_angular_vel_z.set(posicion.imu_angular_vel_z)


if __name__ == '__main__':
    # Start up the server to expose the metrics.
        start_http_server(9091)

while not rospy.is_shutdown(): 
    rate.sleep()
    # Generate some requests.
    while True:  
        process_request(random.random())
        # Llamadas a funciones
        battery_fuc()
        position_func
