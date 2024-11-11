# Predict SMILES encodings of chemical structure depictions in images

This repository contains code for a web app that allows users to either upload an image file or take a picture using their webcam and get a prediction the chemical structure depicted in the image in SMILES notation. 

This application was built using the [Streamlit](https://github.com/streamlit/streamlit) framework (Apache 2.0 license). It is using the [DECIMER Image Transformer](https://github.com/Kohulan/DECIMER-Image_Transformer) (MIT license) model to make predictions (as implemented in the [DECIMER Python package](https://pypi.org/project/decimer/)). In addition, the application allows to edit the predicted SMILES using the web-based 
molecule sketcher [Ketcher](https://github.com/epam/ketcher) (Apache 2.0 license).


The live app can be found here: [image-to-smiles.serve.scilifelab.se](https://image-to-smiles.serve.scilifelab.se/).

## Model behind the app

The DECIMER Image Transformer model was developed by the [Cheminformatics and Computational Metabolomics research group](https://cheminf.uni-jena.de/) at Friedrich Schiller University Jena, Germany. You can find out more about the model in these publications:

- Rajan K, et al. "DECIMER.ai - An open platform for automated optical chemical structure identification, segmentation and recognition in scientific publications." *Nat. Commun.* 14, 5045 (2023).
- Rajan, K., et al. "DECIMER 1.0: deep learning for chemical image recognition using transformers." *J Cheminform* 13, 61 (2021).
- Rajan, K., et al. "Advancements in hand-drawn chemical structure recognition through an enhanced DECIMER architecture," *J Cheminform* 16, 78 (2024).

## Contributing

We welcome suggestions and contributions. If you found a mistake or would like to make a suggestion, please create an issue in this repository. Those who wish are also welcome to submit pull requests.

## Contact

This web app was built by [SciLifeLab Data Centre](https://github.com/ScilifelabDataCentre) team members.
