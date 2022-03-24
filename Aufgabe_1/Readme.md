# Task 1 Optical-Illlusion
### Description
uses the *numpy* and *cv2* library
##### Contents
the program contains **1** Python file: *"Task_Code.py"*
and **1** video file :*"gradientIllusion.mp4"*
### Instructions
Run the code file.
To exit the animation, press *q* on your keyboard
### How it works
1. creates a blank image and fils it with a gradient using *for loops* (filling every 5 pixel-columns with a slightly different gray-value)
2. copies a 100x100 square from the middle of the gradient  to the top left and top right corner
3. creates an animation, using another copy of the square, by pasting it on coordinates of a sinus-wave-path every few milliseconds.
4. this results in an optical illusion: if the animated square reaches its original x-coordinates it seems to dissapear. The square seems to be darker on the right side  of the gradient

### Authors
Nic Rubner, Marvin Fischer, Jochem Punt
