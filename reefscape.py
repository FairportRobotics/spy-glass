from ultralytics import YOLO

# Load the weights from our repository
model = YOLO("reefscape.pt")

image_path = 'images/processed/ff4220bed1c921176c4471f3ff97095a.jpg'

results = model(image_path, save_txt=True)
