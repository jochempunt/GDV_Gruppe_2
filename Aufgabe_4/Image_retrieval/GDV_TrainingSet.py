import cv2
import numpy as np
from pathlib import Path
import glob
from enum import Enum


class Descriptor(Enum):
    ''' Define available descriptors '''
    TINY_GRAY4, TINY_GRAY8, TINY_COLOR4, TINY_COLOR8 , TINY_COLOR16 = range(5)

    ''' Compute the descriptor vector '''
    def compute(self, img):
        if (self is Descriptor.TINY_GRAY4):
            img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            return np.ravel(cv2.resize(img_gray, (4, 4)))

        if (self is Descriptor.TINY_GRAY8):
            img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            return np.ravel(cv2.resize(img_gray, (8, 8)))

        if (self is Descriptor.TINY_COLOR4):
            return np.ravel(cv2.resize(img, (4, 4)))

        if (self is Descriptor.TINY_COLOR8):
            return np.ravel(cv2.resize(img, (8, 8)))
        if (self is Descriptor.TINY_COLOR16):
            return np.ravel(cv2.resize(img, (16, 16)))

        

    ''' Get the length of the descriptor vector '''
    def getSize(self):
        if (self is Descriptor.TINY_GRAY4):
            return 4*4

        if (self is Descriptor.TINY_GRAY8):
            return 8*8

        if (self is Descriptor.TINY_COLOR4):
            return 4*4*3

        if (self is Descriptor.TINY_COLOR8):
            return 8*8*3
        
        if (self is Descriptor.TINY_COLOR16):
            return 16*16*3


class TrainingSet:
    ''' Create and manage the image data set used as training data'''
    def __init__(self, root_path) -> None:
        self.root_path = root_path

    # compute a descriptor for all images and store the data
    def createTrainingData(self, descriptor=Descriptor.TINY_COLOR16):
        print('Start creating the training data:')
        if (isinstance(descriptor, Descriptor)):
            print('Used descriptor: ', descriptor.name)
            self.descriptor = descriptor
        else:
            print('ERROR: No correct descriptor set. Pick one:')
            for d in Descriptor:
                print(d.name)
            return

        self.categories = []
        self.img_files = []
        self.responses = []
        self.num_training_images = 0
        tempData = []
        tempResponses = []
        category_index = 0.0
        # read all available categories
        print('Found categories:')
        for path in Path(self.root_path).iterdir():
            if path.is_dir():
                self.categories.append(path.name)
                category_index += 1.0
                # for each category
            num_files_in_category = 0
            for file in glob.glob(str(path) + '/*.jpg'):
                # print(file)
                # create response array
                tempResponses.append([category_index])
                # load image
                img = cv2.imread(file, cv2.IMREAD_COLOR)
                # compute image descriptors and store them
                tempData.append(self.descriptor.compute(img))
                self.num_training_images += 1
                num_files_in_category += 1
                self.img_files.append(file)
            print('Found %d files in %s' % (num_files_in_category, path.name))

        self.trainData = np.ndarray(shape=(self.num_training_images, self.descriptor.getSize()),
                                    buffer=np.float32(np.array(np.ravel(tempData))),
                                    dtype=np.float32)
        self.responses = np.ndarray(shape=(self.num_training_images, 1),
                                    buffer=np.float32(np.ravel(tempResponses)),
                                    dtype=np.float32)
        print('Training succeeded: computed descriptors for %d images' % self.num_training_images)

    # save the training data to a file
    def saveTrainingData(self, file_name):
        self.file_name = file_name
        np.savez(file_name, categories=self.categories,
                 num_images=self.num_training_images,
                 responses=self.responses,
                 trainData=self.trainData,
                 img_files=self.img_files,
                 descriptor=self.descriptor.name)
        print('Saved training data to file:', self.file_name)
        print('Number of images: ', self.num_training_images)
        print('Used descriptor:', self.descriptor)

    # load the training data from a file
    def loadTrainingData(self, file_name):
        data = np.load(file_name, allow_pickle=True)
        self.responses = data['responses']
        self.trainData = data['trainData']
        self.categories = data['categories']
        self.img_files = data['img_files']
        self.num_training_images = data['num_images']
        descriptor_name = data['descriptor']
        if str(descriptor_name) == 'TINY_GRAY4':
            self.descriptor = Descriptor.TINY_GRAY4
        elif str(descriptor_name) == 'TINY_GRAY8':
            self.descriptor = Descriptor.TINY_GRAY8
        elif str(descriptor_name) == 'TINY_COLOR4':
            self.descriptor = Descriptor.TINY_COLOR4
        elif str(descriptor_name) == 'TINY_COLOR8':
            self.descriptor = Descriptor.TINY_COLOR8
        elif str(descriptor_name) == 'TINY_COLOR16':
                self.descriptor = Descriptor.TINY_COLOR16
        else:
            print('ERROR: Unknown descriptor')
        print('Loaded training data:')
        print('Number of images: ', self.num_training_images)
        print('Used descriptor:', self.descriptor)

    def getFilenameFromIndex(self, index):
        return self.img_files[index]