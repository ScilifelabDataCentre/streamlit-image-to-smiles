from DECIMER import predict_SMILES

image_path = "test_predictions/example_structure.png"
SMILES = predict_SMILES(image_path)
print(f"🎉 Decoded SMILES: {SMILES}")