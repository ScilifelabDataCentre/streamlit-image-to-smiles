import streamlit as st

st.title("Predict SMILES encodings of chemical structure depictions in images")

intro = '''This application allows users to either upload an image file or take a picture using their webcam
and get a prediction the chemical structure depicted in the image in SMILES notation. You can navigate using 
__links in the sidebar to the left__. The chemical structure depiction can be machine or hand drawn. Note that
loading the pages or getting a prediction may sometimes take a while.

This application is using the [DECIMER Image Transformer](https://github.com/Kohulan/DECIMER-Image_Transformer) (MIT license)
model to make predictions (as implemented in the [DECIMER Python package](https://pypi.org/project/decimer/)). The DECIMER (Deep lEarning for Chemical ImagE Recognition) addresses the Optical Chemical Structure 
Recognition (OCSR) with the latest computational intelligence methods to provide an automated open-source software solution.

In addition, the application allows to edit the predicted SMILES using the web-based 
molecule sketcher [Ketcher](https://github.com/epam/ketcher) (Apache 2.0 license).

'''
st.markdown(intro)

st.subheader("Model behind the app", divider=None)
st.markdown("The DECIMER Image Transformer model was developed by the [Cheminformatics and Computational Metabolomics research group](https://cheminf.uni-jena.de/) "
         "at Friedrich Schiller University Jena, Germany. You can find out more about the model in these publications:")
citations = '''
1. Rajan K, et al. "DECIMER.ai - An open platform for automated optical chemical structure identification, segmentation and recognition in scientific publications." *Nat. Commun.* 14, 5045 (2023).
2. Rajan, K., et al. "DECIMER 1.0: deep learning for chemical image recognition using transformers." *J Cheminform* 13, 61 (2021).
3. Rajan, K., et al. "Advancements in hand-drawn chemical structure recognition through an enhanced DECIMER architecture," *J Cheminform* 16, 78 (2024).
'''
st.markdown(citations)

st.subheader("App source code", divider=None)
app_info = '''
The source code of this web application 
[can be found on GitHub](https://github.com/ScilifelabDataCentre/streamlit-image-to-smiles) with an 
open source license so feel free to use it to build your own apps. The app was built using the
 [Streamlit](https://github.com/streamlit/streamlit) framework (Apache 2.0 license).

We welcome suggestions and contributions to this web application. If you found a mistake or would like to make 
a suggestion, please create an issue in the app's GitHub repository. Those who wish are also welcome to submit 
pull requests.
'''
st.markdown(app_info)