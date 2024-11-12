import streamlit as st
from streamlit_ketcher import st_ketcher
from DECIMER import predict_SMILES
from PIL import Image

st.header("Predict SMILES encodings of chemical structure depictions in an image file")

st.markdown("Here you can upload your image of a chemical structure depiction (for example, picture of a hand drawing) "
         "and get a prediction of what structure it is in SMILES notation from [DECIMER Image Transformer](https://github.com/Kohulan/DECIMER-Image_Transformer). "
         "Allowed image formats: .jpg, .jpeg, .png. "
         "Note that it may take a few minutes after you upload your file before you see the result. "
         "You will then be able to see and edit the predicted structure in [Ketcher](https://github.com/epam/ketcher).")

st.write("The image files are only stored in RAM memory and are removed as soon as you close or reload the page.")

with open("./test_predictions/example_structure_2.jpg", "rb") as file:
    btn = st.download_button(
        label="Download an example image",
        data=file,
        file_name="example_structure.jpg",
        mime="image/jpg",
    )

st.subheader("Step 1. Upload a file", divider="gray")

# Input widget for users to upload image files from their computer
uploaded_file = st.file_uploader("Select an image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    container = st.container(border=True)
    container.image(image, caption="Uploaded image")

    # Run SMILES prediction
    SMILES = predict_SMILES(uploaded_file)
    
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
    st.write("Please upload an image to predict SMILES.")