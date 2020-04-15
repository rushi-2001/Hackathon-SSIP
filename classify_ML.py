# USAGE
# python classify.py --model ssip3.model --labelbin ssip3_le.pickle --image test_ssip/1.jpg --output img1.jpg

# import the necessary packages
from keras.preprocessing.image import img_to_array
from keras.models import load_model
import numpy as np
import argparse
import imutils
import pickle
import cv2
import os
import pathlib

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-m", "--model", required=True,
	help="path to trained model model")
ap.add_argument("-l", "--labelbin", required=True,
	help="path to label binarizer")
#ap.add_argument("-i", "--image", required=True,
	#help="path to input image")
#ap.add_argument("-o", "--output", required=True,
	#help="name of output image")
args = vars(ap.parse_args())

valid=0
invalid=0

PATH_TO_TEST_IMAGES_DIR = pathlib.Path('./test_ssip/')
TEST_IMAGE_PATHS = sorted(list(PATH_TO_TEST_IMAGES_DIR.glob("*.jpg")))
print(TEST_IMAGE_PATHS)

for i in TEST_IMAGE_PATHS:
	a=i.split('/')
    print(a)
	
'''
	# load the image
image = cv2.imread(i)
output = image.copy()
 
# pre-process the image for classification
image = cv2.resize(image, (96, 96))
image = image.astype("float") / 255.0
image = img_to_array(image)
image = np.expand_dims(image, axis=0)

# load the trained convolutional neural network and the label
# binarizer
print("[INFO] loading network...")
model = load_model(args["model"])
lb = pickle.loads(open(args["labelbin"], "rb").read())

# classify the input image
print("[INFO] classifying image...")
proba = model.predict(image)[0]
idx = np.argmax(proba)
label = lb.classes_[idx]

# we'll mark our prediction as "correct" of the input image filename
# contains the predicted label text (obviously this makes the
# assumption that you have named your testing image files this way)
filename = args["image"][args["image"].rfind(os.path.sep) + 1:]
correct = "correct" if filename.rfind(label) != -1 else "incorrect"

if(label == 'a is not garbage' or proba[idx] * 100 < 60.0):
	print(image_path,"is invalid")
	invalid=invalid+1
# build the label and draw the label on the image
label = "{}: {:.2f}%".format(label, proba[idx] * 100)
output = imutils.resize(output, width=400)
cv2.putText(output, label, (7, 25),  cv2.FONT_HERSHEY_SIMPLEX,
	0.75, (0, 255, 0), 2)

valid = len(TEST_IMAGE_PATHS)-invalid
print("\n\n")
print("Total Invalid Images = ",invalid,"\nTotal Valid Images = ",valid)
'''