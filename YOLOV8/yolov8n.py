import cv2
import argparse
import numpy as np
from ultralytics import  YOLO
import supervision as sv
import time



def main():
    pre_timeframe=0
    cap = cv2.VideoCapture("input.mp4")
    model = YOLO("yolov8n.pt")
    box_annotator = sv.BoxAnnotator(
        thickness=1,
        text_scale=0.35,
        text_padding=1
    )

    while True:
        ret, frame = cap.read()
       

        starting_time= time.time()
       

        resized_frame = cv2.resize(frame, (640,480))
        detections=model.predict(resized_frame,imgsz=(320,416))
        
        result = model(resized_frame, agnostic_nms=False)[0]
        detections = sv.Detections.from_yolov8(result)


        labels = [
            f"{model.model.names[class_id]} {confidence:0.2f}"
            for _, confidence, class_id, _
            in detections
        ]

        frame = box_annotator.annotate(
            scene=resized_frame,
            detections=detections,
            labels=labels
        )
        ending_time = time.time()
        inference_time = ending_time - starting_time
        inference_time_ms = inference_time * 1000

        fps =1/inference_time

        cv2.putText(frame, f'Inference_time: {inference_time_ms:.2f}ms', (20, 245),
                cv2.FONT_HERSHEY_DUPLEX, 0.6, (130, 195, 260), 1)
        
        cv2.putText(frame, f'FPS: {fps:.2f}', (20, 225),
                cv2.FONT_HERSHEY_DUPLEX, 0.6, (125, 220, 3), 1)
        cv2.imshow("yolov8", resized_frame)

        key = cv2.waitKey(1)
        if key == ord('q') or key == ord('Q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()

