from PIL import Image
import numpy as np 
from fastai.tabular.learner import load_learner
from fastai import *
from fastai.vision import *
import torch
import sys
import warnings
import json


def predict(img,model):
    # load the pre trained model
    learn_inf = load_learner(model)
    learn_inf.dls.vocab
    pred_class,pred_idx,probs = learn_inf.predict(img)
    # create a dictionary with relevant values
    if pred_class=='1':
        pred_class='meta'
    if pred_class=='0':
        pred_class='non_meta'
    deep_dict = {
        "class": pred_class,
        "prob" : float(probs[pred_idx])
    }
    fname=model.split('.')[0]
    # create json object and write to a file
    deep_json = json.dumps(deep_dict, indent=2)
    with open(fname + ".json", "w") as outfile:
        outfile.write(deep_json)


    # print('predicted Class: {} '.format(pred_class) )
    # print('Predicted Probability:{:.3} '.format(float(probs[pred_idx])))

def load_image(img):
    im = Image.open(img).convert('RGB')
    image = np.array(im)
    return image

# Uploading the File to the Page


args = sys.argv[1:] # read the first argument

# Checking the Format of the page
# if args[0] == '-s':        
    # Load a single image for prediction
img = load_image(args[0])    
print("Image Uploaded Successfully")
predict(img,args[1])
# else:
#     print('Use {python <filename.py> s followed by the filename} to run single test image\n \
#            Use {python <filename.py> b followed by the filename} to run batch of test images')



