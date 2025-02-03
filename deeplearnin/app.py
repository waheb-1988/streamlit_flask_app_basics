import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Load the model
@st.cache_resource
def load_model():
    return tf.keras.models.load_model("alzheimer_model.h5")

model = load_model()

# Function to preprocess the image
def preprocess_image(image):
    image = image.resize((224, 224))  # Adjust size based on model input
    image = np.array(image) / 255.0   # Normalize
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image

# Streamlit UI
st.title("Alzheimer's Detection App")
st.write("Upload an MRI scan to check for Alzheimer's disease.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    st.write("Processing image...")
    processed_image = preprocess_image(image)
    
    prediction = model.predict(processed_image)
    
    # Modify this based on how your model outputs results
    class_names = ["No Alzheimer's", "Alzheimer's Detected"]
    result = class_names[int(prediction[0][0] > 0.5)]
    
    st.write(f"Prediction: **{result}**")
