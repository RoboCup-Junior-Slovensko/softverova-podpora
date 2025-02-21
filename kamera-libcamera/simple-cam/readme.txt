Simple example to use camera on new RPI4 system using libcamera.
Retrieves frames from the camera in 24-bit RGB format and prints the pixel values to the standard output.

requirements:

meson
cmake
libcamera


building:

$ meson setup build
$ cd build
$ ninja


running:

$ ./simple_cam > pixels.txt


Based on example from here: https://github.com/kbingham/simple-cam/blob/master/simple-cam.cpp
