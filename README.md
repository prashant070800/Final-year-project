

# ***Real time surveillance and analysis of a classroom using Faster R-CNN***


**Table of Content**

1. [Introduction]()
2. [Roadmap]()
3. [Estimation]()
5. [Demonstration]()
6. [Members]()

**1. Introduction**


* It is necessary to make use of automatic video analysis technologies for developing smart surveillance system which can aid the human operator in both detecting and reacting to potential threats.
* This project is based on the state of the art object detection network, faster-Region convolutional neural network.  Faster R-CNN, is composed of two modules. The first module is a deep fully convolutional network that proposes regions, and the second module is the Fast R-CNN detector that uses the proposed regions.  
* The entire system is a single, unified network for object detection.

**2. Roadmap**

*  The whole system can be modeled as the figure below. There are four stages, namely image preprocessing, person detection, face recognition, and database management.
 
![image](https://github.com/prashant070800/Final-year-project/blob/main/images/Algo%20description.jpg)

*  These four blocks are in the order of size in the direction from input to output. We take video as input from camera and then extract image frames. 

*  These images get preprocessed and feed to object detection neural network model. If in this image a person is detected then face will be classify.

*  Finally the database will be maintain according to visitor frequency.





