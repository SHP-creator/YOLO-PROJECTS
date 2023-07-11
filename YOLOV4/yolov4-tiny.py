import cv2
import time

Conf_threshold = 0.4
NMS_threshold = 0.7
COLORS = [(10, 255, 255), (90, 255, 65), (255, 255, 300),
          (0, 255, 0), (255, 255, 0), (0, 0, 255)]


class_name = []
with open('classes.txt', 'r') as f:
    class_name = [cname.strip() for cname in f.readlines()]

net = cv2.dnn.readNet('yolov4-tiny.weights', 'yolov4-tiny.cfg')

model = cv2.dnn_DetectionModel(net)
model.setInputParams(size=(416,416), scale=1/255, swapRB=True)

pre_timeframe=0
# vid = cv2.VideoCapture(0)
vid = cv2.VideoCapture('input.mp4')


frame_width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))

target_width = 640  # Specify the desired width
target_height = 480 



while True:
    ret, frame = vid.read()
    if not ret:
        break
    starting_time= time.time()
    # Resize the frame
    resized_frame = cv2.resize(frame, (target_width, target_height))
    
    classes, scores, boxes = model.detect(resized_frame, Conf_threshold, NMS_threshold)

    for (classid, score, box) in zip(classes, scores, boxes):
        color = COLORS[int(classid) % len(COLORS)]
        label = f"{class_name[classid]}:{score:.2f}"
        cv2.rectangle(resized_frame, box, color, 1)
        cv2.putText(resized_frame, label, (box[0], box[1] - 10),
                    cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, color, 1)

    ending_time = time.time()
    inference_time = ending_time - starting_time
    inference_time_ms = inference_time * 1000

    cv2.putText(resized_frame, f'inference_time: {inference_time_ms:.2f}ms', (20, 245),
                cv2.FONT_HERSHEY_DUPLEX, 0.6, (130, 70, 260), 2)

    fps = 1000/ inference_time
    cv2.putText(resized_frame, f'FPS: {fps:.2f}', (20, 225),
                cv2.FONT_HERSHEY_DUPLEX, 0.6, (125, 220, 3), 1)

    cv2.imshow('frame', resized_frame)
    key = cv2.waitKey(1)
    if key == ord('q') or key == ord('Q'):
        break

   

vid.release()
cv2.destroyAllWindows()
