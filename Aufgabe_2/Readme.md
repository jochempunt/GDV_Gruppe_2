# Task 2 Object counting
### Description
uses the modules *numpy* version 1.22.0 and *cv2* version 4.5.5.64 
the python version used is Python 3.8.5
##### Contents
the program contains **1** Python file: *"object_counting_code.py"*
### Instructions
Run the code file to showcase both the original image and the image with applied mask for each image.
To step to the next image, press *e* on your keyboard.
To exit the program, press *q* on your keyboard at any time.
### How it works
1. Sets hue, saturation and value and their respective ranges the fit the desired color.
2. Loads all "chewing_gum"-images from the image folder to iterate over them.
3. Applies a mask with the set color values and transforms the resulting image with erosion and dilatation.
4. Counts all connectedComponents for the same color that have a minimum size of 11x11.
5. Prints out the number of individual balls found.

### Authors
Nic Rubner, Marvin Fischer, Jochem Punt
