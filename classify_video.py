# USAGE
# python classify_video.py --model ssip3.model --labelbin ssip3_le.pickle

# import the necessary packages
from keras.preprocessing.image import img_to_array
from keras.models import load_model
from imutils.video import FileVideoStream
import numpy as np
import argparse
import imutils
import time
import pickle
import cv2
import os

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-m", "--model", required=True,
	help="path to trained model model")
ap.add_argument("-l", "--labelbin", required=True,
	help="path to label binarizer")
#ap.add_argument("-i", "--image", required=True,
	#help="path to input image")
args = vars(ap.parse_args())

print("[INFO] starting video stream...")
vs = FileVideoStream('garbage.mp4').start()
time.sleep(2.0)

while True:
    # load the image
    image = vs.read()
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
    #filename = args["image"][args["image"].rfind(os.path.sep) + 1:]
    #correct = "correct" if filename.rfind(label) != -1 else "incorrect"

    # build the label and draw the label on the image
    label = "{}: {:.2f}%".format(label, proba[idx] * 100)
    output = imutils.resize(output, width=720)
    cv2.putText(output, label, (230, 60),  cv2.FONT_HERSHEY_SIMPLEX,
        0.7, (0, 255, 0), 2)

    # show the output image
    print("[INFO] {}".format(label))
    cv2.imshow("Output", output)
    key = cv2.waitKey(1) & 0xFF
     
        # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break

# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()