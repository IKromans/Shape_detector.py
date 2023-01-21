# Shape_detector.py

Hey! Welcome to my application which will process given image and output following data:

- `Amount of figures in scene`
- `Name of the figures shape`
- `Get measurements in mm:`
  - `Length of rectangle side`
  - `Circle radius`
  - `Value of any triangle angle`
  
Resourse folder contains following files:

- `camera_intrinsics.json` - camera intrinsics parameters
- `png_image.png` - target image in png format
- `raw_image.npy` - target image as npy array

Distance between the camera and the wall equals 380mm.

Code is in `Python` (using `OpenCV` and `Numpy` libraries).

To run application:

- clone repository `https://github.com/IKromans/Shape_detector.py.git`
- start terminal where `run.py` file is located and run command `python run.py`
- it should start the application and display calculated data like so:

![Screenshot 2023-01-22 003505](https://user-images.githubusercontent.com/66387211/213889698-bf0c8534-3cca-49ff-86e7-369345a2cd8a.jpg)

- as well as the picture with shape contours and data like so:

![Screenshot 2023-01-22 003534](https://user-images.githubusercontent.com/66387211/213889758-76fc87ea-dd1c-41f6-83c7-18f0ea5c1ef6.jpg)

Enjoy!
