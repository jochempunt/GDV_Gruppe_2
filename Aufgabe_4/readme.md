# Task 4 Image retrieval
### Description
uses the modules *numpy* version 1.22.0 and *cv2* version 4.6.0.66 
the python version used is Python 3.10.5
##### Contents
the program contains **2** Python files: *"GDV_ImageRetrieval.py"* & *"GDV_Training.py"*.
the *"GDV_Training.py"*-file contains a newly created Descriptor calles TINY_COLOR16
the taskfolder also contains two mosaic images: *"Mosaic_Img.jpeg"* & *"Mosaic_Img2.jpeg"*
note that the data set is empty since we put it into our .gitignore
### Instructions
Put the Caltech 101 image-set into the *"data"* folder for the program to work properly (https://data.caltech.edu/records/20086)
Choose an image and the desired rows and columns for the mosaic image creation by setting proper values.
Run the program to start the creation of the dataset. (When having done this already, the creation & save methods can be commented out and the load method can be commented in instead.
Depending on how many rows and columns were chosen, it will take a while to create the final image.
The program will display both the original image and the newly created mosaic image.
The mosaic image will also be saved automatically.
To exit the program, press *any key* on your keyboard.
### How it works
1. Loads the desired image into the getMosaicImage method.
2. The method separates the image into divided sections that have a size of (image_height * 1/rows) : (image_width * 1/cols). 
3. For each of the sections, the best matching image out of all the images from the dataset is found.
4. Creates a new image and pastes the match into the same coordinates as the corresponding divided section of the original image.
5. The final result is a mosaic version of the image thrown into the getMosaicImage method.

### Authors
Nic Rubner, Marvin Fischer, Jochem Punt
