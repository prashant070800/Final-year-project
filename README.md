

# ***Intelligent security and information management system using video ananlysis.***


**Table of Content**

1. [Introduction](#1-introduction)
2. [Members](#2-members)
3. [Roadmap](#3-roadmap)
4. [Estimation](#4-estimation)
5. [Demonstration](#5-demonstration) 

## 1. Introduction


* It is necessary to make use of automatic video analysis technologies for development of smart surveillance system which can aid the human operator in both detection and reaction to potential threats.
* This project is based on the state of the art object detection network, faster-Region convolutional neural network.  Faster R-CNN, is composed of two modules, where the first module is a deep fully convolutional network that proposes regions, and the second module is the Fast R-CNN detector that uses the proposed regions.  
* The entire system is a single, unified network for object detection.

## 2. Members
* [Ajeet Kumar Yadav](https://github.com/Ajeet-kumar1) --*Responsible for algorithms, implement the Face Recognition stage*
* [Maneesh](https://github.com/maneesh06)-- *Generally Works on machine learning model and GUI*
* [Pranjal Mittal](https://github.com/PranjalM99) --*Documentation and GUI*
* [Prashant Singh](https://github.com/prashant070800) --*Database management and alert system*

## 3. Roadmap

*  The whole system can be modeled as the figure below. It consists of four stages, namely image preprocessing, person detection, face recognition, and database management.
 
![image](https://github.com/prashant070800/Final-year-project/blob/main/images/Algo%20description.jpg)

*  These four blocks are in the order of size in the direction from input to output. We take video as input from camera and then extract image frames. 

*  These images get preprocessed and fed to object detection neural network model. In this image if a person is detected then face will be classified.

*  Finally the database will be maintained according to visitor frequency.

## 4. Estimation

The collected data, divided it into three datasets, including training, validating, and testing. The face recognition accuracy and loss is schematically drawn in figure.
![image](https://github.com/prashant070800/Final-year-project/blob/main/images/Output%20graph.png)


## 5. Demonstration

**5.1 Face Recognition with Customized CNN**

![image](https://github.com/prashant070800/Final-year-project/blob/main/images/ppt%20gif.gif)




**5.2 Face Recogniton and data sharing at web page**

![image](https://github.com/prashant070800/Final-year-project/blob/main/images/ezgif.com-gif-maker%20(1).gif)

**5.3 Webpage**

![image](https://github.com/prashant070800/Final-year-project/blob/main/images/Picture2.jpg)



