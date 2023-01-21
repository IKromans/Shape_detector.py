import cv2

import image_file_loader_and_transformator as iflt
import variables as v
import actions as s

cv2.drawContours(iflt.png_image, iflt.contours, -1, (0, 255, 0), 2)
cv2.putText(iflt.png_image, 'Amount of figures in scene: {}'
            .format(v.num_of_figures), (10, 30), v.font, 1, (0, 255, 0), 2)
output = "\n".join([
    "Amount of figures in scene: {}".format(v.num_of_figures),
    "Name of the figures shape: {}".format(v.figure_names),
    "Length of rectangle side (mm): {}".format(s.rect_side_length),
    "Circle radius (mm): {}".format(s.circle_radius),
    "Value of any triangle angle (degrees): {}".format(f"{s.triangle_angle}°")
])
print(output)
cv2.imshow("Shapes", iflt.png_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
