#!/usr/bin/python

# Needs:
# Python-opencv should be installed

# cropFaces.py
# Based on :
# http://creatingwithcode.com/howto/face-detection-in-static-images-with-python/

# Usage: python cropFaces.py <image_file>

import sys, os
import Image
from opencv.cv import *
from opencv.highgui import *

typeCascade= [
    "types/haarcascade_frontalface_default.xml",
    "types/haarcascade_frontalface_alt2.xml",
    "types/haarcascade_frontalface_alt_tree.xml",
    "types/haarcascade_frontalface_alt.xml",
    "types/haarcascade_profileface.xml",
    "types/lbpcascade_frontalface.xml"
    ]

def detectObjects(image):
  """Converts an image to grayscale and prints the locations of any 
     faces found"""
  grayscale = cvCreateImage(cvSize(image.width, image.height), 8, 1)
  cvCvtColor(image, grayscale, CV_BGR2GRAY)

  storage = cvCreateMemStorage(0)
  cvClearMemStorage(storage)
  cvEqualizeHist(grayscale, grayscale)
          
  # cvHaarDetectObjects
  # For faster face detection use the following parameters :
  #  (scale_factor=1.2, min_neighbors=2, flags=CV_HAAR_DO_CANNY_PRUNING).
  # For acurate face detection yet slow  use the following parameters:
  # (scale_factor=1.1, min_neighbors=3, flags=0)
  nFaces = i = 0
  while(nFaces==0 and i<5):
      cascade = cvLoadHaarClassifierCascade(
          typeCascade[i],
          cvSize(1,1))
      faces = cvHaarDetectObjects(grayscale, cascade, storage, 1.2, 2,
                                  CV_HAAR_DO_CANNY_PRUNING, cvSize(50,50))
      if faces:
          for f in faces:
              cropFace(nFaces,f)
              nFaces=nFaces+1
      # If i didn't found an image I try other cascade
      i=i+1


# Input:
#    Coordinates of a face 
#    Number of a face
# Output:
#    Face croped
def cropFace(n,f):
    im = Image.open(sys.argv[1])
    im=im.crop( (f.x, f.y, f.x+f.width, f.y+f.height))
    im.save (str(n)+sys.argv[1])

def main():
    # open Image
    image = cvLoadImage(sys.argv[1]);
    # If there is a face in the object we will crop the face!
    detectObjects(image)


if __name__ == "__main__":
  main()
