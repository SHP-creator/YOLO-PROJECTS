#  Real-Time Object Detection with YOLOv8 and OpenCV
This repository contains code for real-time object detection using the YOLOv8 model with OpenCV. YOLOv8 is a powerful object detection algorithm known for its high accuracy and efficiency.

## DESCRIPTION
The code provided in this repository demonstrates real-time object detection using YOLOv8 with OpenCV. It takes input from a video file and performs object detection on each frame, drawing bounding boxes and labels around the detected objects. 
The YOLOv8 model used in this code is loaded from the "yolov8n.pt" file.

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

2.Place the "yolov8n.pt" file in the project directory.

3.Modify the "sample.mp4" file in the project directory or replace it with your own video file for object detection.

4.Run the object detection script:

      python yolov4_project.py

The script will open a window displaying the real-time object detection results. Bounding boxes will be drawn around the detected objects, and labels will indicate the class and confidence score for each detection. Additionally, the output video with the detections will be saved as output.mp4 in user provided path.

## PERFORMANCE

The YOLOv8 object detection algorithm is known for its efficiency and real-time inference capabilities. The code provided achieves high frame rates, thanks to the optimized implementation of YOLOv8. The actual performance may vary depending on your system's hardware specifications and the complexity of the input video.

## Customization

The code provides some customization options:

You can modify the model_name parameter in the ObjectDetection class constructor to specify a different model file if needed.

Adjust the values of thickness, text_thickness, and text_scale in the ObjectDetection class constructor to change the visualization properties of the bounding boxes and labels.

Modify the output video path by changing the output_path variable in the script.

Customize the window name and resizing by modifying the cv2.namedWindow and cv2.resizeWindow function calls.

## OUTPUT

![yolov8](https://github.com/SHP-creator/YOLO-PROJECTS/blob/main/YOLOV8/yolov8.png?raw=true)

## References
YOLOv8: An Improved Version of the YOLO Object Detection Algorithm

Ultralytics YOLO

OpenCV

## AUTHOR

G.R.SRI HARI PRIYA

