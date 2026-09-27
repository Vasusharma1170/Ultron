from picamera2 import Picamera2
from ultralytics import YOLO
import cv2

model = YOLO("yolo11n.pt")
CONFIDENCE_THRESHOLD = 0.60

camera = Picamera2()

camera.configure(
    camera.create_preview_configuration(
        main={"size": (640, 480), "format": "RGB888"}
    )
)

camera.start()

print("YOLO camera started")
print("Press Q to exit")

while True:
    frame = camera.capture_array()

    results = model(frame, imgsz=320, verbose=False)

    result = results[0]

    for box in result.boxes:
        class_id = int(box.cls[0])
        object_name = model.names[class_id]
        confidence = float(box.conf[0])

        if confidence < CONFIDENCE_THRESHOLD:
            continue

        x1, y1, x2, y2 = map(int, box.xyxy[0])

        x_center = (x1 + x2) // 2
        y_center = (y1 + y2) // 2

        print(
    f"Object: {object_name} | "
    f"Confidence: {confidence:.2f} | "
    f"Box: ({x1}, {y1}, {x2}, {y2}) | "
    f"Center: ({x_center}, {y_center})"
)
    annotated_frame = result.plot()
    cv2.imshow("YOLO - Raspberry Pi Camera", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.stop()
cv2.destroyAllWindows()
