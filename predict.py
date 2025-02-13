from ultralytics import YOLO

# Load model
model = YOLO("evaluation/model/train15.pt")

# Run model
model.predict(source = "data/final_polygons.yolov11/test", show=True, save=True)