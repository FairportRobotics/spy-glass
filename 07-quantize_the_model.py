from ultralytics import YOLO
#import torch

pytorch_model_file  = "best.py"

model = YOLO(pytorch_model_file)
#metrics = model.val()
#print(metrics)

model.export(format='onnx')

import numpy as np
from onnxruntime.quantization import quantize_static, CalibrationMethod, CalibrationDataReader, QuantType, QuantFormat

# loading the ONNX model
onnx_model_input_path = pytorch_model_file.replace(".pt", ".onnx")
onnx_model_output_path = "quantized.onnx"

# calibration dataset (dummy data for calibration)
class DummyDataReader(CalibrationDataReader):
    def __init__(self, num_samples):
        self.num_samples = num_samples
        self.current_sample = 0

    def get_next(self):
        if self.current_sample < self.num_samples:
            input_data = self.generate_random_input()
            self.current_sample += 1
            return {'images': input_data}
        else:
            return None

    def generate_random_input(self):
        input_data = np.random.uniform(-1, 1, size=input_shape).astype(np.float32)
        return input_data

num_calibration_samples = 100
input_shape = (1, 3, 640, 640)

calibration_data_reader = DummyDataReader(num_samples=num_calibration_samples)


# Quantize the model to int8
quantized_model = quantize_static(
    model_input=onnx_model_input_path,
    model_output=onnx_model_output_path,
    calibration_data_reader=calibration_data_reader,
    activation_type=QuantType.QInt8,
    weight_type=QuantType.QInt8,
    quant_format=QuantFormat.QDQ,
    per_channel=False,
    calibrate_method=CalibrationMethod.MinMax
)