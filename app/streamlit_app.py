import os

import keras
from keras.datasets import mnist     # MNIST dataset is included in Keras
import numpy as np
import pandas as pd
import streamlit as st
import random

st.title("Streamlit <-> Heroku Template App")

# load mnist dataset, test set
(_, _), (x_test, y_test) = mnist.load_data()

# load model from file
model = keras.models.load_model(os.path.join("mlmodels", "mnist_model1"))

# if button clicked, classify
if st.button("Get Next Random Digit"):
    # get random image from the test set
    random_idx = random.randint(0, x_test.shape[0]-1)
    digit_img = x_test[random_idx, :,:]
    
    # show the image
    st.image(digit_img)

    # classify
    prediction = model.predict(digit_img.reshape([1, 28,28,1]))[0]
    st.text("Predicted to be  : {}".format(np.argmax(prediction)))
    st.text("And the truth is : {}".format(y_test[random_idx]))
