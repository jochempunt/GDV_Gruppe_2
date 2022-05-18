# Task 3 Hybrid Imaging
### Description
uses the modules *numpy* version 1.22.0 and *cv2* version 4.5.5.64 
the python version used is Python 3.8.5
##### Contents
the program contains **1** Python file: *"object_counting_code.py"*
the folder also contains two hybrid images: *"hybrid_image1.png"* & *"hybrid_image2.png"*
### Instructions
Run the code file to showcase both the images undedited. 
Now select 3 points on both images (the selection should be made in the same order).
The resulting image is the combination of the first image with an applied high-pass filter and the second image with the applied low pass filter/gaussian filter.
To reset the selected points, press *r* on your keyboard.
To save the result, press *s* on your keyboard.
To exit the program, press *q* on your keyboard at any time.
### How it works
1. Loads two images and resizes them to 400x400
2. Applies high-pass filter to first image and gaussian filter to the second image.
3. Transforms the high-pass image to the selected points.
4. Combines the low-pass image with the transformed image using cv2.addWeighted.

### Authors
Nic Rubner, Marvin Fischer, Jochem Punt
