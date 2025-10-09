
# From Pixels to Pathology: Explainable CNNs in Lung Tissue Analysis

This repository accompanies the manuscript **_“From Pixels to Pathology: Explainable CNNs in Lung Tissue Analysis.”_**

This work is a continuation of our previous manuscript [(Here)](https://www.biorxiv.org/content/10.1101/2023.05.12.540340v1.abstract) and [code](https://github.com/Aitslab/lunghisto), focusing on:

- **Numerical analysis** of deep learning models for lung tissue classification  
- **Explainable AI (XAI) algorithms** to connect pathology-driven features with model-driven representations  

The goal of this study is to enhance interpretability and transparency in CNN-based lung pathology analysis by bridging computational features with domain-specific pathology insights.


The raw data is from [(data)](https://www.ebi.ac.uk/biostudies/bioimages/studies/S-BIAD419). 

In our previous publication, we employed CNN architectures, including VGG16 and EfficientNet, combined with various image augmentation techniques, to classify the extent of damage in histology slides.


In this work, we explored post hoc explainability algorithms applied to our best-performing models from previous studies. These analyses included [clustering and pattern discovery](https://github.com/Aitslab/Histology_XAI/tree/main/Unsupervised)  in feature vectors, generating [Grad-CAM](https://github.com/Aitslab/Histology_XAI/tree/main/GradCAM) activation maps for image tiles, and computing and visualizing [SHAP](https://github.com/Aitslab/Histology_XAI/tree/main/SHAP) values for the trained models. In subsequent steps, we trained new models with [deeper architectures](https://github.com/Aitslab/Histology_XAI/tree/main/Train_more_layers) and incorporated [attention layers](https://github.com/Aitslab/Histology_XAI/tree/main/Attention) for improved performance. All experiments were conducted using both the previously optimized models and the newly developed ones, along with the same dataset.

