# Notes about particular interesting cases when evaluating the platform results.

## False Positive & False Negative
Storyline	SMART_CAMERA	Sophie's Blink Indoor Camera has a battery life of up to two years, so she doesn't have to worry about recharging it often.	Blink Indoor Camera	";('blink','SERVICE');"	(Blink Indoor Camera, Smart Camera)	0	1	0	1	0	1
> In this case, the model was trained to identify Blink as a Service, and it did, Except in this case blink is just part of the name of the Smart Camera

## False Positive, True Positive and False Negative
Storyline	SMART_CAMERA	The LG InstaView ThinQ's ability to monitor the contents of the fridge and provide expiration dates helped keep Jane's family's food fresh and safe to eat.	LG InstaView ThinQ	";('monitor','SERVICE');('eat','SERVICE');"	(LG InstaView ThinQ, On-Device Resource)	0	0	1	1	1	1

## Services are so subjective that parts of names of Actuators can be confused with Services, such as on the following example. Detecting reliably services, and making them a part of the system might be challenging due to the fuzzyness of their definition.
Functional Requirements	ACTUATOR	The system should use the ARO® EXP Series Diaphragm Pumps to use it's advanced analytics can optimize performance and reduce energy consumption	ARO® EXP Series Diaphragm Pumps	";('pumps','SERVICE');"	(ARO® EXP Series Diaphragm Pumps, Actuator)	0	1	0	0	1	0

## There is overlapping on entity names, what makes it harder for the model to categorize correctly
Functional Requirements	ON_DEVICE_RESOURCE	The system must incorporate an Arduino Uno microcontroller to enable versatile hardware interfacing and sensor integration, ensuring support for real-time data acquisition, processing, and control logic execution through user-defined programs.	Arduino Uno	";('arduino','ACTUATOR');('microcontroller','ACTUATOR');"	(Arduino Uno microcontroller, On-Device Resource)	0	1	0	1	2	0

Functional Requirements	TAG	The system must integrate the Acconeer XM132 Ultrasonic Sensor Tag to enable non-contact distance measurement and object detection, ensuring support for configurable sensing ranges, data accuracy, and real-time data retrieval for monitoring and control purposes.	Acconeer XM132 Ultrasonic Sensor Tag	";('xm132 ultrasonic sensor tag','SENSOR');"	(Acconeer XM132 Ultrasonic Sensor Tag, Tag)	0	1	0	0	1	0

## Display as a service X Display as an Actuator
User Stories	ACTUATOR	As a Hobbyist Electronics Enthusiast, I want to integrate the Adafruit 0.5 Mini AMOLED Display into my DIY project, so I can invite my friends to explore its interactive features and enjoy our electronics hobby together.	Adafruit 0.5 Mini AMOLED Display	";('adafruit 0','SENSOR');('display','SERVICE');"	(Adafruit 0.5 Mini AMOLED Display, On-Device Resource)	0	0	1	1	1	1

## Actuator x on-Device Resource
When a user activates a voice command, Arduino Uno processes the audio input, recognizes the intent, and performs the corresponding action within the IoT ecosystem.;39;50;Arduino Uno;ON_DEVICE_RESOURCE

Last year, I bought an arduino, a small computer about the size of a deck of cards.;23;30;arduino;ACTUATOR

## Sensors x Sensor Tags
User Stories	TAG	As a Tech Explorer, I want to organize a fun and educational scavenger hunt with my friends using the Acconeer XM132 Ultrasonic Sensor Tag, so we can explore the world of sensor technology together.	Acconeer XM132 Ultrasonic Sensor Tag	";('sensor','SENSOR');"	(Acconeer XM132 Ultrasonic Sensor Tag, Tag, Sensor)	0	1	0	0	1	0

# gps:sensor X GPS tracker:tag X GPS location:network resource X GPS Driver:on_device_resource

MediaTek GPS Driver ensures seamless communication between the wearable fitness tracker and the mobile app, enabling users to track their health and fitness goals.;0;19;MediaTek GPS Driver;ON_DEVICE_RESOURCE

The Piccolo ATMS GPS Tracker helped Jake recover his stolen bike by providing the location of the thief's hideout.;4;28;Piccolo ATMS GPS Tracker;TAG

# ChatGPT sometimes detects ICOs for which we have not discussed categorization, which leads to a careful consideration when evaluating the models performance
Storyline	SERVICE	The smart home security system accepts voice commands to arm or disarm the alarms based on the homeowner's voice recognition.	accepts	";('accepts','SERVICE');"	(Voice Recognition, On-Device Resource)	1	0	1	0	1	0


# Sometimes chatGPT finds stuff that are not even on the phrase:
Storyline	SERVICE	the heat to automatically adjust when people enter or exit a room	adjust	";('adjust','SERVICE');"	(Automated Heat Adjustment, Actuator)	1	0	1	0	1	0

# Sometiems chatPGT gets confused and bestows more than one label to the sample:
Functional Requirements	SENSOR	If applicable, the system should be able to act on the ADXRS620 Gyroscope Sensor Module's data by controlling actuators or triggering automated actions based on predefined rules.	ADXRS620 Gyroscope Sensor Module	";('adxrs620 gyroscope sensor module','SENSOR');"	 (ADXRS620 Gyroscope Sensor Module, Sensor, Actuator)	0	0	1	0	1	0

Functional Requirements	ACTUATOR	The system must seamlessly incorporate the Abus Bordo Smart 6000A Bike Lock, providing secure locking and unlocking functionality via a mobile app, real-time tamper alerts, and a user-friendly interface for managing bike access permissions.	Abus Bordo Smart 6000A Bike Lock	";"	 (Abus Bordo Smart 6000A Bike Lock, Actuator, On-Device Resource, Service)	0	0	1	1	0	0

# Sometimes chatGPT decides that the label is "Not Specified":
Functional Requirements	ACTUATOR	The B&C Speakers must blend seamlessly into the house's home decor.	B&C Speakers	";('b&c speakers','ACTUATOR');"	 (B&C Speakers, Not specified)	0	0	1	0	1	0

# Whats the difference between an on-device resource and an actuator ?
An actuator must provoke real world changes.
An on-device resource is a digital resource.

# chatGPT often categorizes fans as on_device_resource:
User Stories	ACTUATOR	As an Office Worker, I want to use the ARCTIC Breeze Mobile USB Fan at my workplace, so I can create a comfortable and refreshing environment for myself and my colleagues to enjoy together.	ARCTIC Breeze Mobile	";('usb','ON_DEVICE_RESOURCE');"	 (ARCTIC Breeze Mobile USB Fan, On-Device Resource)	0	0	1	1	1	0

# One contribution of this work is the dataset with subtypes.
Subcategorization is something hard to do, and the ready to use dataset can serve as a basis for further expansion of the data samples themselves as well as a guide to labelling new entities.

# It might really not make much sense to differentiate between on_device_resources and network_resources. The difference in terms of what can be captured intra text, principally in short texts, is too subtle.
User Stories	NETWORK_RESOURCE	As a Web Developer, I want to set up the Abyss Web Server on our hosting environment, so my colleagues and I can invite friends to collaborate on web development projects and showcase our work together.	Abyss Web Server	";('server','NETWORK_RESOURCE');"	(Abyss Web Server, On-Device Resource)	0	0	1	1	0	0  

How to categorize the entity above?

# ChatGPT categorized most network_resources as on_device_resource. 

# chatGPT gets pwned on services

# Sensor x Sensor Driver
ON_DEVICE_RESOURCE	The Texas Instruments Sensor Driver for the smart home security system shall integrate with door/window sensors and provide real-time intrusion alerts.	Texas Instruments Sensor Driver	";('sensor','SENSOR');"	Texas Instruments Sensor Driver, On-Device Resource)	0	1	0	1	0	1

# chatGPT Bogus answer
ACTUATOR	The system must seamlessly incorporate the Abus Bordo Smart 6000A Bike Lock, providing secure locking and unlocking functionality via a mobile app, real-time tamper alerts, and a user-friendly interface for managing bike access permissions.	Abus Bordo Smart 6000A Bike Lock	";"	 (Abus Bordo Smart 6000A Bike Lock, Actuator, On-Device Resource, Service)	0	0	1	1	0	0	

# Same entity connected to multiple categories
Bluetooth driver - on device resource
BLuetooth tag - tag

# The "System" as the Whole X The System as an "On Device Resource"
SERVICE	 The system must advise users on optimal IoT device configurations.	advise	";('advise','SERVICE');"	(System, Service)	1	0	1	0	1	0	

# Video as a Network Resource x On Device Resource

# Display Verb as a Service X Display as an Actuator

# 