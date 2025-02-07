from ultralytics import YOLO

# Load the weights from our repository
model = YOLO("reefscape.pt")

image_path = 'images/processed/0a28280f126e3c6d2ba0addc0051f89b.jpg'

results = model(image_path, save_txt=True)
