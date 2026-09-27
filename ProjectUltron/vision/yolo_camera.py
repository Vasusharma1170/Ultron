from picamera2 import Picamera2
from ultralytics import YOLO
import cv2

# Load YOLO model
model = YOLO("yolo11n.pt")

# Start camera
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
    # Capture frame
    frame = camera.capture_array()

    # Run YOLO
    results = model(frame, imgsz=320, verbose=False)

    # Draw detections
    annotated_frame = results[0].plot()

    # Display
    cv2.imshow("YOLO - Raspberry Pi Camera", annotated_frame)

    # Exit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.stop()
cv2.destroyAllWindows()

