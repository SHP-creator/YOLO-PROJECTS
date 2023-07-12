# YOLO Object Detection
YOLO (You Only Look Once) is a real-time object detection algorithm that can be used to detect objects in images and videos. YOLO is a single-stage detector, which means that it predicts bounding boxes and class probabilities in a single pass. This makes YOLO very fast, making it suitable for real-time applications.

## YOLOv4-tiny and YOLOv8n.pt
YOLOv4-tiny and YOLOv8n.pt are two different versions of the YOLO algorithm. YOLOv4-tiny is a smaller and faster version of YOLOv4, while YOLOv8n.pt is a larger and more accurate version.

Here is a table that summarizes the key differences between YOLOv4-tiny and YOLOv8n.pt:
|  Feature              |  YOLOV4-TINY |   YOLOV8n     |   
|-----------------------|--------------|---------------|
| Model Size            |   16MB       |   285MB       |   
|  Inference Speed      |   185 ms     |   150ms       |   
|  Number of Parameters | CSPDarknet53 |  CSPDarknet53 |   

## YOLOV4-tiny FPS and Inference :

Based on the system configuration and input size, the frames per second (fps) and inference will vary. This is my current fps and inference according to my input.

|  S.NO |  Resolution |  FPS |   INFERENCE|
|-------|-------------|------|------------|
| 1.    |  128*128    |  48 | 12-15 ms  |
| 2.    |  160*160    |  35 | 20-30 ms  |
| 3.    |  192*192    |  37 | 20-25ms|
| 4.    |  224*224    |  25 |  30-40 ms |
| 5.    | 256*256     |  27 |  32-45 ms |
| 6.    |  288*288    | 25  |  30-40 ms |
| 7.    |  320*320    | 19  |  42-53 ms  |
| 8.    |  352*352    | 16  | 50-65 ms  |
| 9.    |  384*384    | 15  |  50-65 ms |
| 10.   |  416*416    |  12 |  70-80 ms |
| 11.   |  448*448    |  11 | 70-85ms  |
| 12.   | 480*480     | 10  |  80-110ms |
| 13.   | 512*512     |  9 | 90-115 ms  |
| 14 .  |  544*544    |  8 |  95-120 ms |
| 15.   |  576*576    |  8 | 100-130 ms  |
| 16.   | 608*608     |  7 |  124-160 ms |
| 17.   |  640*640    | 6  |  130-150 ms |

## YOLOV4 FPS and Inference :

Based on the system configuration and input size, the frames per second (fps) and inference will vary. This is my current fps and inference according to my input.

|  S.NO |  Resolution |  FPS |   INFERENCE|
|-------|-------------|------|------------|
| 1.    |  128*128    |  9.47| 95-107 ms  |
| 2.    |  160*160    |  4.75|195-220 ms  |
| 3.    |  192*192    |  5.30| 173-200 ms|
| 4.    |  224*224    |  3.24 | 295-340 ms |
| 5.    | 256*256     |  3.24|  295-320 ms |
| 6.    |  288*288    |2.75 |  350-379ms|
| 7.    |  320*320    |2.15 |  450-480 ms |
| 8.    |  352*352    |1.65 | 580-600 ms |
| 9.    |  384*384    |1.75  | 550- 575 ms|
| 10.   |  416*416    |  1.25 | 790-820 ms|
| 11.   |  448*448    |  1.15 | 850-899 ms |
| 12.   | 480*480     |1.03|  935-1000 ms |
| 13.   | 512*512     |  0.93| 1065-1153ms |
| 14 .  |  544*544    |  0.84|  1180-1200 ms|
| 15.   |  576*576    | 0.80|1240-1275 ms|
| 16.   | 608*608     |  0.65 |  1511-1560 ms |
| 17.   |  640*640    |0.60|  1615-1690 ms |

# OBJECT DETECTION OF YOLOV8

![yolov8](https://github.com/SHP-creator/YOLO-PROJECTS/blob/main/YOLOV8/yolov8.png?raw=true)

