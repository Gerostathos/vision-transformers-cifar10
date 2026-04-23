# Vision Transformers on CIFAR-10

## Overview
This repository contains a PyTorch-based notebook project on Vision Transformers (ViTs) for image classification on the CIFAR-10 dataset.

The notebook combines:
- implementation of a custom Vision Transformer from core building blocks,
- training and validation on CIFAR-10,
- targeted hyperparameter experiments,
- attention-map visualization for interpretability,
- fine-tuning of pre-trained Vision Transformer models.

## Main Result
The best model reported in the notebook achieved **93.86% test accuracy** on CIFAR-10.

## What the Notebook Covers
The notebook includes the following stages:

1. **Data preparation and visualization**
   - loading CIFAR-10,
   - inspecting class distributions,
   - visualizing sample images.

2. **Custom Vision Transformer implementation**
   - patch embedding,
   - positional embeddings,
   - attention head,
   - multi-head self-attention,
   - MLP block,
   - transformer block and encoder,
   - end-to-end Vision Transformer model.

3. **Training and evaluation**
   - training loop and validation logic,
   - model evaluation on held-out data.

4. **Hyperparameter experiments**
   - learning rate,
   - patch size,
   - hidden size,
   - number of transformer layers,
   - number of attention heads.

5. **Model interpretability**
   - attention-map visualization.

6. **Transfer learning experiments**
   - fine-tuning a pre-trained ViT-Tiny model,
   - classifier-only fine-tuning variants,
   - final evaluation on the CIFAR-10 test set.

## Technologies Used
- Python
- PyTorch
- Torchvision
- NumPy
- Matplotlib
- tqdm
- timm

## Repository Structure
```text
vision-transformers-cifar10/
├── README.md
├── .gitignore
└── vision_transformers_cifar10.ipynb
```

## How to Run
1. Create a Python environment.
2. Install the required libraries:
   - `torch`
   - `torchvision`
   - `numpy`
   - `matplotlib`
   - `tqdm`
   - `timm`
3. Open the notebook in Jupyter Notebook or VS Code.
4. Run the cells in order.

## Notes
- CIFAR-10 is loaded through `torchvision.datasets`, so the dataset can be downloaded automatically when needed.
- Training time and final performance depend on hardware availability, especially GPU usage.
- The repository is currently presented as a clean notebook-based project; it can later be refactored into a multi-file package structure if needed.

## Future Improvements
- split notebook code into reusable Python modules,
- add a `requirements.txt` file,
- save trained model checkpoints and evaluation artifacts in dedicated folders,
- provide example figures directly in the repository README.
