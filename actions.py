import image_file_loader_and_transformator as iflt
import variables as v
import cv2
import numpy as np

for contour in iflt.contours:
    approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)

    if len(approx) == 3:
        v.num_of_figures += 1
        v.figure_names.append("triangle")
        side1 = np.sqrt((approx[0][0][0] - approx[1][0][0]) ** 2 + (approx[0][0][1] - approx[1][0][1]) ** 2)
        side2 = np.sqrt((approx[1][0][0] - approx[2][0][0]) ** 2 + (approx[1][0][1] - approx[2][0][1]) ** 2)
        side3 = np.sqrt((approx[2][0][0] - approx[0][0][0]) ** 2 + (approx[2][0][1] - approx[0][0][1]) ** 2)
        angle = np.arccos((side2 ** 2 + side3 ** 2 - side1 ** 2) / (2 * side2 * side3))
        triangle_angle = round(angle * 180 / np.pi, 0)
        text_size = cv2.getTextSize("Triangle", v.font, 0.5, 2)[0]
        triangle_points = [approx[0][0], approx[1][0], approx[2][0]]
        x_points = [point[0] for point in triangle_points]
        y_points = [point[1] for point in triangle_points]
        textX = int(sum(x_points) / len(x_points) - text_size[0] / 2.5)
        textY = int(sum(y_points) / len(y_points))
        pt1 = (approx[0][0][0], approx[0][0][1])
        pt2 = (approx[1][0][0], approx[1][0][1])
        pt3 = (approx[2][0][0], approx[2][0][1])
        cv2.line(iflt.png_image, pt1, pt2, (0, 0, 255), 2)
        cv2.putText(iflt.png_image, f"{triangle_angle} degrees", (pt1[0], pt1[1] - 5), v.font, 0.5, (255, 255, 255), 1)
        cv2.putText(iflt.png_image, "Triangle", (textX, textY), v.font, 0.5, (0, 255, 0), 1)

    elif len(approx) == 4:
        (x, y, w, h) = cv2.boundingRect(approx)
        aspectRatio = float(w) / h
        if 0.95 <= aspectRatio <= 1.05:
            v.num_of_figures += 1
            v.figure_names.append("rectangle")
            fx = iflt.camera_intrinsics["ffx"]
            length_pixels = w
            length_mm = round(((380 * length_pixels) / fx), 0)
            rect_side_length = length_mm
            text_size = cv2.getTextSize("Rectangle", v.font, 0.5, 2)[0]
            textX = x + w / 2 - text_size[0] / 2
            textY = y + h / 2
            cv2.putText(iflt.png_image, f"{int(length_mm)}mm", (x + 120, y + 110), v.font, 0.5, (255, 255, 255), 1)
            cv2.putText(iflt.png_image, "Rectangle", (int(textX), int(textY)), v.font, 0.5, (0, 255, 0), 1)

    elif len(approx) > 15:
        v.num_of_figures += 1
        v.figure_names.append("circle")
        (x, y), radius = cv2.minEnclosingCircle(approx)
        center = (int(x), int(y))
        radius_pixels = int(radius)
        fx = iflt.camera_intrinsics["ffx"]
        radius_mm = round(((380 * radius_pixels) / fx), 0)
        circle_radius = radius_mm
        radius = int(radius_mm)
        cv2.line(iflt.png_image, center, (center[0], center[1] + radius_pixels), (0, 255, 0), 2)
        pt1 = (center[0], center[1])
        pt2 = (center[0], center[1] + radius * 2)
        cv2.putText(iflt.png_image, f"{radius}mm", (pt1[0] + 5, pt1[1] + 15), v.font, 0.5, (255, 255, 255), 1)
        text_size = cv2.getTextSize("Circle", v.font, 0.5, 2)[0]
        textX = int(x - text_size[0] / 2)
        textY = int(y)
        cv2.putText(iflt.png_image, "Circle", (textX, textY), v.font, 0.5, (0, 255, 0), 1)
