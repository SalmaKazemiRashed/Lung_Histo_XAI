
![](docs/_static/Summary.png)
# From Pixels to Pathology: Explainable CNNs in Lung Tissue Analysis

This repository accompanies the manuscript **_“From Pixels to Pathology: Explainable CNNs in Lung Tissue Analysis.”_**

This work is a continuation of our previous manuscript [(Here)](https://www.biorxiv.org/content/10.1101/2023.05.12.540340v1.abstract) and [code](https://github.com/Aitslab/lunghisto), focusing on:

- **Numerical analysis** of deep learning models for lung tissue classification  
- **Explainable AI (XAI) algorithms** to connect pathology-driven features with model-driven representations  

The goal of this study is to enhance interpretability and transparency in CNN-based lung pathology analysis by bridging computational features with domain-specific pathology insights.


The raw data is from [(data)](https://www.ebi.ac.uk/biostudies/bioimages/studies/S-BIAD419). 

In our previous publication, we employed CNN architectures, including VGG16 and EfficientNet, combined with various image augmentation techniques, to classify the extent of damage in histology slides.


In this work, we explored post hoc explainability algorithms applied to our best-performing models from previous studies. These analyses included [clustering and pattern discovery](https://github.com/Aitslab/Histology_XAI/tree/main/Unsupervised)  in feature vectors, generating [Grad-CAM](https://github.com/Aitslab/Histology_XAI/tree/main/GradCAM) activation maps for image tiles, and computing and visualizing [SHAP](https://github.com/Aitslab/Histology_XAI/tree/main/SHAP) values for the trained models. In subsequent steps, we trained new models with [deeper architectures](https://github.com/Aitslab/Histology_XAI/tree/main/Train_more_layers) and incorporated [attention layers](https://github.com/Aitslab/Histology_XAI/tree/main/Attention) for improved performance. All experiments were conducted using both the previously optimized models and the newly developed ones, along with the same dataset.




![](docs/_static/unsup.png)

# Discovering Structure in Latent Representations via Unsupervised Clustering
The latent representations of the tiles, extracted from the final layer of the three-class classifier, were processed using unsupervised dimensionality reduction algorithms such as UMAP and t-SNE. The first two components were then visualized in three ways:

1- Colored by treatment group (Control, ECMO, ECMO+LPS, MV, MV+LPS),

2 -Colored by the model’s predicted classes (low, medium, high), and

3 -Colored by the gold standard labels (low, medium, high) for direct comparison between predicted and true classifications.


The [first](./Unsupervised/Histo_unsupervised_featurespace_VGG16.ipynb) notebook documents the complete workflow for VGG16-based models, and the [second](./Unsupervised/Histo_unsupervised_featurespace_EffnetB4.ipynb) outlines the corresponding process for EfficientNet-based models.


![](docs/_static/Grad_CAM.png)

# Gradient-weighted Class Activation Mapping (Grad-CAM) 


The Gradient-weighted Class Activation Mapping (Grad-CAM) algorithm computes the gradients of each target class (e.g., ‘low’, ‘medium’, and ‘high’) with respect to the model’s last convolutional layer, identifying regions of the image that most influence the final prediction for that class. The resulting map is a coarse-grained activation map, which must be resized to accurately overlay and highlight the activated areas on the original input image.

The [first](./GradCAM/Visualize_Grad_Cam_initial_relu.ipynb) file illustrates the workflow using the initial ReLU activation function. The [second](./GradCAM/Visualize_GradCam_different_Activation_function.ipynb) notebook presents the analysis after replacing the activation function with ELU and Leaky ReLU, and so on. The [final](./GradCAM/Visualize_GradCam_train_more_layers.ipynb) notebook displays the activation maps for models with [deeper](./Train_more_layers/) layers trained.

![](docs/_static/shap.png)

# SHAP (SHapley Additive exPlanations) 