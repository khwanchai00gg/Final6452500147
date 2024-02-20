#!/usr/bin/env python3
from tkinter import*
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String
from std_msgs.msg import Int16
from subprocess import call

# Parameter for Defult Scale
#
#

frame = Tk()
frame.title("Turtle_Control")
frame.geometry("200x400")

# Initial ROS node and determine Publish or Subscribe action
#
#
#
rospy.init_node("Turtle_Control")
pub = rospy.Publisher("turtle1/cmd_vel",Twist, queue_size=10)
pub_text = rospy.Publisher("motion",String,queue_size=10)
pub_led = rospy.Publisher("Topic_LED",Int16,queue_size=10)

def status(val):
	status_text.config(text="Status: " + str(val.data))

sub = rospy.Subscriber("status",String,callback=status)

def fw():
    cmd = Twist()
    cmd.linear.x = LinearVel.get()
    cmd.angular.z= 0.0
    #publish
    pub.publish(cmd)
    pub_text.publish("Forward")
        
def bw():
    cmd = Twist()
    cmd.linear.x = -LinearVel.get()
    cmd.angular.z= 0.0
    #publish
    pub.publish(cmd)
    pub_text.publish("Backward")
       
def tl():
    cmd = Twist()
    cmd.linear.x = 0
    cmd.angular.z= AngularVel.get()
    #publish
    pub.publish(cmd)
    pub_text.publish("TurnLeft")
   
def tr():
    cmd = Twist()
    cmd.linear.x = 0
    cmd.angular.z= -AngularVel.get()
    #publish
    pub.publish(cmd)
    pub_text.publish("TurnRight")

def pn():
    #publish
    call(["rosservice", "call", "turtle1/set_pen", "{r: 200, g: 200, b: 200, width: 3,'off': 0}" ])
    pub_text.publish("PenOn")
    pub_led.publish(1)

def po():
    #publish
    call(["rosservice", "call", "turtle1/set_pen", "{'off': 1}" ])
    pub_text.publish("PenOff")
    pub_led.publish(0)

status_text = Label(frame,font=('Arial',10),text="Status: GUI")
status_text.pack()

LinearVel = Scale(frame, from_=0, to=2, orient=HORIZONTAL)
LinearVel.set(1) # 1 is defult value for scale
LinearVel.pack()

AngularVel = Scale(frame, from_=0, to=2, orient=HORIZONTAL)
AngularVel.set(1) # 1 is defult value for scale
AngularVel.pack()

B1 = Button(text = "FW", command=fw)
B1.place(x=73, y=120)

B2 = Button(text = "BW", command=bw)
B2.place(x=73, y=230)

B3 = Button(text = "TL", command=tl)
B3.place(x=20, y=180)

B4 = Button(text = "TR", command=tr)
B4.place(x=128, y=180)

B5 = Button(text = "PenOn", command=pn)
B5.place(x=63, y=280)

B6 = Button(text = "PenOff", command=po)
B6.place(x=62, y=330)

frame.mainloop()    
    
    
    
