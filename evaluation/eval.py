from ultralytics import YOLO

# Load model
model = YOLO("model/train12.pt")

# Start evaluation on test dataset
model.val(data="eval.yaml", imgsz=640, device="cpu", split="test")