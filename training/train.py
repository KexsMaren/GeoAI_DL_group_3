from ultralytics import YOLO

# Load model
model = YOLO("yolo11n.pt")


# Train model
model.train(data="train.yaml", imgsz=640, batch=8, epochs=250, workers=1, device="cpu")