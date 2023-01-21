import json
import cv2
import numpy as np

with open("resources/camera_intrinsics.json", "r") as f:
    camera_intrinsics = json.load(f)

png_image = cv2.imread("resources/png_image.png")

raw_image = np.load("resources/raw_image.npy")

gray = cv2.cvtColor(png_image, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray, 150, 450)
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)