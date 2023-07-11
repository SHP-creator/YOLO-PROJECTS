import torch
import numpy as np
import cv2
from time import time
from ultralytics import YOLO
import supervision as sv


class ObjectDetection:

    def __init__(self, capture_index, model_name):
        self.capture_index = capture_index
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        print("Using Device: ", self.device)

        self.model = self.load_model(model_name)
        self.CLASS_NAMES_DICT = self.model.model.names
        self.box_annotator = sv.BoxAnnotator(sv.ColorPalette.default(), thickness=1, text_thickness=1, text_scale=0.4)

    def load_model(self, model_name):
        model = YOLO(model_name)  # load a pretrained YOLOv8n model
        model.fuse()
        return model

    def predict(self, frame):
        results = self.model(frame)
        return results

    def plot_bboxes(self, results, frame):
        xyxys = []
        confidences = []
        class_ids = []

        # Extract detections for person class
        for result in results:
            boxes = result.boxes.cpu().numpy()
            class_id = boxes.cls[0]
            conf = boxes.conf[0]
            xyxy = boxes.xyxy[0]

            if class_id == 0.0:
                xyxys.append(result.boxes.xyxy.cpu().numpy())
                confidences.append(result.boxes.conf.cpu().numpy())
                class_ids.append(result.boxes.cls.cpu().numpy().astype(int))

        # Setup detections for visualization
        detections = sv.Detections(
            xyxy=results[0].boxes.xyxy.cpu().numpy(),
            confidence=results[0].boxes.conf.cpu().numpy(),
            class_id=results[0].boxes.cls.cpu().numpy().astype(int),
        )

        # Format custom labels
        self.labels = [
            f"{self.CLASS_NAMES_DICT[class_id]} {confidence:0.2f}"
            for _, confidence, class_id, tracker_id
            in detections
        ]

        # Annotate and display frame
        frame = self.box_annotator.annotate(scene=frame, detections=detections, labels=self.labels)

        return frame

    def __call__(self):
        cap = cv2.VideoCapture("sample.mp4")
        assert cap.isOpened()

        # Get the video's original width and height
        original_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        original_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

        # Define the output video path
        output_path = "/home/secura/Documents/Yolo work/output.mp4"

        # Get the video properties
        fps = cap.get(cv2.CAP_PROP_FPS)
        frame_width = int(original_width)
        frame_height = int(original_height)

        # Create a VideoWriter object to save the output video
        output_video = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (frame_width, frame_height))

        # Create a named window and resize it
        cv2.namedWindow('YOLOv8 Detection', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('YOLOv8 Detection', frame_width, frame_height)

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            start_time = time()

            # Perform object detection
            results = self.predict(frame)
            frame = self.plot_bboxes(results, frame)

            end_time = time()
            fps = 1 / np.round(end_time - start_time, 2)

            cv2.putText(frame, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 2)

            # Write the frame to the output video file
            output_video.write(frame)

            cv2.imshow('YOLOv8 Detection', frame)

            key = cv2.waitKey(1)
            if key == ord('q') or key == ord('Q'):
                break

        # Release the resources
        cap.release()
        output_video.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    detector = ObjectDetection(capture_index=0, model_name="yolov8n.pt")
    detector()
