import streamlit as st
from streamlit_ketcher import st_ketcher
from DECIMER import predict_SMILES
from PIL import Image

st.header("Predict SMILES encodings of chemical structure depictions in a webcam photo")

st.write("Here you can take a picture of a chemical structure depiction using your webcam "
         "and get a prediction of what structure it is in SMILES notation from [DECIMER Image Transformer](https://github.com/Kohulan/DECIMER-Image_Transformer). "
         "You have to allow webcam access to this page in your browser to be able to take a picture. "
         "Note that it may take a few minutes after you upload your file before you see the result. "
         "You will then be able to see and edit the predicted structure in [Ketcher](https://github.com/epam/ketcher).")

st.write("The pictures you take are only stored in RAM memory and are removed as soon as you close or reload the page.")

st.subheader("Step 1. Take a picture", divider="gray")

# Input widget to take a photo with the user's webcam
webcam_photo = st.camera_input("Take a picture")

if webcam_photo is not None:
    # Display the photo that was taken
    image = Image.open(webcam_photo)
    container = st.container(border=True)
    container.image(image, caption="Uploaded image")

    # Run SMILES prediction
    SMILES = predict_SMILES(webcam_photo)
    
    # Display the prediction
    st.subheader("Step 2. See the prediction", divider="gray")
    st.html(f"<h5>Predicted SMILES:</h5><p><span style='font-size: 1.25em; color: red;'>{SMILES}</span></p>")
    #st.markdown(f"Predicted SMILES: ``{SMILES}``")

    # Tool to edit the prediction
    st.subheader("Step 3. Edit/fine-tune the prediction", divider="gray")
    edited_SMILES = st_ketcher(SMILES)
    st.html(f"<h5>SMILES from the Ketcher drawing:</h5><p><span style='font-size: 1.25em; color: green;'>{edited_SMILES}</span></p>")
    #st.markdown(f"SMILES from the Ketcher drawing: ``{edited_SMILES}``")

else:
    st.write("Please take a photo to predict SMILES.")