
#%matplotlib inline
import matplotlib
import numpy as np
import matplotlib.pyplot as plt

# Make sure that caffe is on the python path:
caffe_root = '../'  # this file is expected to be in {caffe_root}/examples
import os
import sys
sys.path.insert(0, caffe_root + 'python')
import caffe

# Set the right path to your model definition file, pretrained model weights,
# and the image you would like to classify.
MODEL_FILE = '../models/age_pred/deploy.prototxt'
PRETRAINED = '../models/age_pred/age_pred1k.caffemodel'
TEST_FILE = '../data/age_pred/test.txt'
caffe.set_mode_cpu()
net = caffe.Classifier(MODEL_FILE, PRETRAINED)
net.set_raw_scale('data',255)
net.set_channel_swap('data',(2,1,0))
net.set_mean('data',np.load(caffe_root+'python/caffe/imagenet/ilsvrc_2012_mean.npy'))
absError = 0
cnt = 0
with open(TEST_FILE, "r") as ins:
    for line in ins:
	parsed = line.split()
	IMAGE_FILE = parsed[0]
	real_age = int(parsed[1])
	input_image = caffe.io.load_image(IMAGE_FILE)
	#plt.imshow(input_image)
	#plt.show()
	prediction = net.predict([input_image])  # predict takes any number of images, and formats them for the Caffe net automatically
	predicted_age = prediction[0][0]
	absError += abs(real_age - predicted_age)
	cnt +=1
	#plt.show()
absError /= cnt
print 'ABS_ERROR:', absError














