#!/usr/bin/env python3
from tkinter import*
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String
from std_msgs.msg import Int16

def fw():
    cmd = Twist()
    cmd.linear.x = 1
    cmd.angular.z= 0.0
    #publish
    pub.publish(cmd)
    pub_text.publish("Forward")
        
def bw():
    cmd = Twist()
    cmd.linear.x = -1
    cmd.angular.z= 0.0
    #publish
    pub.publish(cmd)
    pub_text.publish("Backward")
       
def tl():
    cmd = Twist()
    cmd.linear.x = 0
    cmd.angular.z= 1
    pub.publish(cmd)
    pub_text.publish("TurnLeft")
   
def tr():
    cmd = Twist()
    cmd.linear.x = 0
    cmd.angular.z= -1
    #publish
    pub.publish(cmd)
    pub_text.publish("TurnRight")

sensor1_value = 1
sensor2_value = 1
sensor3_value = 1
Togle = False

def sensor1(val):
    global sensor1_value
    sensor1_value = val.data
def sensor2(val):
    global sensor2_value
    sensor2_value = val.data
def sensor3(val):
    global sensor3_value
    sensor3_value = val.data

if __name__ == "__main__":
    rospy.init_node("Arduino_comand")
    pub = rospy.Publisher("turtle1/cmd_vel",Twist, queue_size=10)
    pub_text = rospy.Publisher("motion",String,queue_size=10)
    pub2 = rospy.Publisher("status",String, queue_size=10)

    sub1 = rospy.Subscriber("Topic_Sensor1",Int16,callback=sensor1)
    sub2 = rospy.Subscriber("Topic_Sensor2",Int16,callback=sensor2)
    sub3 = rospy.Subscriber("Topic_Sensor3",Int16,callback=sensor3)
    rate = rospy.Rate(1)

    while(not rospy.is_shutdown()):
    #   rospy.loginfo("node1: "+str(text))
        if sensor1_value == 0 and sensor2_value == 0 or sensor1_value == 0 and sensor3_value == 0 or sensor3_value == 0 and sensor2_value == 0:
            if Togle == False:
                fw()
            else:
                bw()
            pub2.publish("ARDUINO")
        elif sensor1_value == 0:
            tl()
            pub2.publish("ARDUINO")
        elif sensor3_value == 0:
            tr()
            pub2.publish("ARDUINO")
        elif sensor2_value == 0:
            Togle = ~Togle
            pub_text.publish("Togle")
            pub2.publish("ARDUINO")
        else:
            pub2.publish("GUI")
        rate.sleep()
    
    
    
