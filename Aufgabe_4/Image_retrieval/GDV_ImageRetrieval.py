from GDV_TrainingSet import Descriptor, TrainingSet
import cv2
import numpy as np


def findBestMatch(trainData, sample):
    FLANN_INDEX_KDTREE = 1
    index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
    search_params = dict(checks=50)
    flann = cv2.FlannBasedMatcher(index_params, search_params)
    matches = flann.knnMatch(trainData.trainData, sample, k=1)
    matches = sorted(matches, key=lambda x: x[0].distance)
    bestMatch = matches[0][0]
    return bestMatch.queryIdx


def getMosaicImage(img_to_mosaic, n_rows, n_cols):
    imgX = int(img_to_mosaic.shape[1] / n_cols) * n_cols
    imgY = int(img_to_mosaic.shape[0] / n_rows) * n_rows 
    img_to_mosaic = cv2.resize(img_to_mosaic, (imgX, imgY)) #resize the image to make calculations work properly and avoid rounding errors
    img_result = img_to_mosaic.copy()
    for idx1 in range (0, n_rows):
        for idx2 in range (0, n_cols):
            divided_Section = img_to_mosaic[int(idx1 * (imgY / n_rows)): int((idx1 * imgY / n_rows + imgY / n_rows)),
                                  int(idx2 * (imgX / n_cols)): int((idx2 * imgX / n_cols + imgX / n_cols))]
            assert(isinstance(trainData.descriptor, Descriptor)) #start matching algorithm to find the best match for the divided_section
            descr = trainData.descriptor
            newcomer = np.ndarray(shape=(1, descr.getSize()),
                                buffer=np.float32(descr.compute(divided_Section)),
                                dtype=np.float32)
            match = findBestMatch(trainData, newcomer)
            matching_img = cv2.imread(trainData.getFilenameFromIndex(match), cv2.IMREAD_COLOR)
            matching_img = cv2.resize(matching_img, (int(imgX / n_cols), int(imgY / n_rows)))
            img_result[int(idx1 * (imgY / n_rows)): int((idx1 * imgY / n_rows + imgY / n_rows)),
                       int(idx2 * (imgX / n_cols)): int((idx2 * imgX / n_cols + imgX / n_cols))] = matching_img
    img_result = cv2.resize(img_result, (img_to_mosaic.shape[1], img_to_mosaic.shape[0])) #revert the resize made before to keep the original image ratio
    cv2.imwrite("Mosaic_Img.jpeg",img_result) 
    cv2.imshow("Mosaic creation", img_result)

    
root_path = 'Aufgabe_4/image_retrieval/data/101_ObjectCategories/'
file_name = 'Aufgabe_4/image_retrieval/data/data.npz'

trainData = TrainingSet(root_path)
trainData.createTrainingData(Descriptor.TINY_COLOR16)
trainData.saveTrainingData(file_name)
#trainData.loadTrainingData(file_name)

img_to_compute = cv2.imread('Aufgabe_4/image_retrieval/rundown.jpg')
cv2.imshow('original image', img_to_compute)
desired_rows = 90
desired_cols = 90
getMosaicImage(img_to_compute, desired_rows, desired_cols)
cv2.waitKey(0)