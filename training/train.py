from ultralytics import YOLO

# Load model
model = YOLO("yolo11n.pt")

# Train model

# model.train(data="dataset_custom.yaml", imgsz=640, batch=8, epochs=100, workers=1, device="cpu") # leads to overfitting
model.train(data="dataset_custom.yaml", imgsz=640, batch=8, epochs=50, workers=1, device="cpu") # adjusted because of overfitting