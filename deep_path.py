from PIL import Image
import numpy as np 
from fastai.tabular.learner import load_learner
from fastai import *
from fastai.vision.all import *
import torch
import sys
import warnings
import json
import glob
import os


def predict(imfile,fname):
    # load the pre trained model
    img = load_image(imfile)
    model=fname+'.pkl'
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
        "im_id" : imfile.split('/')[-1].split('.')[0]
    }
    # create json object and write to a file
    deep_json = json.dumps(deep_dict, indent=2)
    return deep_json
   


    # print('predicted Class: {} '.format(pred_class) )
    # print('Predicted Probability:{:.3} '.format(float(probs[pred_idx])))

def load_image(img):
    im = Image.open(img).convert('RGB')
    image = np.array(im)
    return image

# Uploading the File to the Page


args = sys.argv[1:] # read the first argument

# Checking the Format of the page
if args[0] == '-s':        
    # Load a single image for prediction
    lst=args[1].split('/')
    lst.pop()
    lst.pop()
    s='/'
    lst=s.join(lst)
    try:
        os.remove(lst + '/' + args[2] + '.json')
    except:
        print("json file is updated")
    else:
        print("json file is newly updated")   
    print("Image Uploaded Successfully")
    deep_json=predict(args[1],args[2])
    
    with open(lst + '/' + args[2] + ".json", "a") as outfile:
        outfile.write(deep_json)
elif(args[0] == '-d'):
    try:
        os.remove(args[1] +'/'+args[2]+'.json')
    except:
        print("json file is updated")
    else:
        print("json file is newly updated")
    model=args[2]
    # path= os.getcwd() +'/'+ args[1] 
    path= args[1]
    for im in glob.glob(path +'/**/*.*'):
        deep_json=predict(im,model)
        with open(args[1]+ '/' + args[2] + ".json", "a") as outfile:
            outfile.write(deep_json)


    