import streamlit as st
from PIL import Image
import numpy as np 
from fastai.tabular.learner import load_learner
from fastai import *
from fastai.vision import *
import torch

st.title("Histopathological Image Classification with PyTorch")
st.header("TIL Metastasis/Non-Metastasis prediction Example")
st.text("Upload a histopathological images for classifying as Metastasis or Non-Metastasis")

def predict():
    # load the pre trained model
    learn_inf = load_learner('export.pkl')
    learn_inf.dls.vocab
    pred_class,pred_idx,probs = learn_inf.predict(img)
    st.write('predicted Class: {} '.format(pred_class) )
    st.write('Predicted Probability:{:.3} '.format(float(probs[pred_idx])))
def load_image(img):
    im = Image.open(img).convert('RGB')
    image = np.array(im)
    # st.write(image.shape)
    return image

# Uploading the File to the Page


uploadFile = st.file_uploader(label="Upload image")
# Checking the Format of the page
if uploadFile is not None:
    global img
    # Perform your Manupilations (In my Case applying Filters)
    img = load_image(uploadFile)
    st.image(img)
    st.write("Image Uploaded Successfully")
else:
    st.write("Make sure you image is in JPG/PNG Format.")

if st.button('predict'):
    predict()
