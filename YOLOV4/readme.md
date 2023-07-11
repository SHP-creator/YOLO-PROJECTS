# YOLOV4 OBJECT DETECTION using OPENCV 
This repository contains code for performing real-time object detection using YOLOv4 with Darknet Framework. The YOLOv4 algorithm is a state-of-the-art object detection model known for its high accuracy and speed.
## DESCRIPTION
The code in this repository demonstrates real-time object detection using YOLOv4 with Darknet Framework. It takes input from a video file and performs object detection on each frame, drawing bounding boxes and labels around the detected objects. 
    The YOLOv4 model used in this code is based on the yolov4-tiny and yolov4 configuration, which is a lightweight version of YOLOv4 and highweight version of YOLOV4 optimized for faster inference.
## Prerequisites
To run the code, you need the following:

-Python 3.7 or higher installed on your system.

-OpenCV version 4.5.1 or higher. You can install it using pip install opencv-python.

-Pre-trained YOLOv4 weights (yolov4-tiny.weights) and configuration (yolov4-tiny.cfg) files. These files can be obtained from the official darknet repository.

-Pre-trained YOLOv4 weights (yolov4.weights) and configuration (yolov4.cfg) files. These files can be obtained from the official darknet repository.

-A file named classes.txt containing a list of class names that the YOLOv4 model can detect.

## Usage
To use the object detection code:

1.Clone this repository to your local machine.

     git clone https://github.com/SHP-creator/YOLO-PROJECTS.git
     cd YOLO-PROJECTS

2.Place the yolov4-tiny.weights, yolov4-tiny.cfg, and classes.txt  or yolov4.weights ,yolov4.cfg and classes.text  files in the project directory

3.Modify the sample.mp4 file in the project directory or replace it with your own video file on which you want to perform object detection.

4.Run the object detection script:

      python yolov4_project.py

The script will open a window displaying the real-time object detection results. Bounding boxes will be drawn around the detected objects, and labels will indicate the class and confidence score for each detection. Additionally, the output video with the detections will be saved as output.mp4 in user provided path.

## PERFORMANCE

The YOLOv4 object detection algorithm is known for its efficiency and real-time inference capabilities. The code provided here achieves high frame rates, especially with the default resolution of 416x416 pixels. The average frame rate achieved on the tested hardware is around 14 frames per second (FPS). However, the actual performance may vary depending on your system's hardware specifications.

## Customization

The code provides several customization options:

You can adjust the Conf_threshold and NMS_threshold variables to control the confidence and non-maximum suppression thresholds for object detection. Higher thresholds result in stricter filtering of detections.

The COLORS list contains the RGB values for different classes, allowing you to modify the colors used for drawing bounding boxes.

The class_name list in the classes.txt file can be modified to include or exclude specific classes based on your needs.

You can modify the target_width and target_height variables to change the target resolution for object detection. Higher resolutions may improve detection accuracy at the cost of decreased frame rates.

## REFRENCES

YOLOv4: Optimal Speed and Accuracy of Object Detection by Alexey Bochkovskiy, Chien-Yao Wang, and Hong-Yuan Mark Liao.

YOLO: Real-Time Object Detection by Joseph Redmon and Ali Farhadi.

OpenCV

## AUTHOR

G.R.SRI HARI PRIYA
