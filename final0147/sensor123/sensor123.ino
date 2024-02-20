/* 
 * rosserial Subscriber Example
 * Blinks an LED on callback
 */

#include <ros.h>
#include <std_msgs/Int16.h>

ros::NodeHandle  nh;
std_msgs::Int16 sensorData1;
std_msgs::Int16 sensorData2;
std_msgs::Int16 sensorData3;
ros::Publisher pub1("Topic_Sensor1", &sensorData1 );
ros::Publisher pub2("Topic_Sensor2", &sensorData2 );
ros::Publisher pub3("Topic_Sensor3", &sensorData3 );

void control_LED( const std_msgs::Int16 & cmd_msg){
  int value = cmd_msg.data;
  digitalWrite(LED_BUILTIN, value);   // blink the led
}

ros::Subscriber<std_msgs::Int16> sub("Topic_LED", &control_LED );

void setup()
{ 
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(2,INPUT);
  pinMode(3,INPUT);
  pinMode(4,INPUT);
  digitalWrite(LED_BUILTIN, 1);
  nh.initNode();
  nh.advertise(pub1);
  nh.advertise(pub2);
  nh.advertise(pub3);
  nh.subscribe(sub);
}

void loop()
{  
  if(sensorData1.data != digitalRead(2)){
    sensorData1.data = digitalRead(2);
    pub1.publish(&sensorData1);
  }
  if(sensorData2.data != digitalRead(3)){
    sensorData2.data = digitalRead(3);
    pub2.publish(&sensorData2);
  }
  if(sensorData3.data != digitalRead(4)){
    sensorData3.data = digitalRead(4);
    pub3.publish(&sensorData3);
  }
  nh.spinOnce();
  delay(500);
}                                                                                                                                     
