# CIFAR-10 Computer Vision: From Basics to Transformers

This repository contains a notebook-based computer vision workflow on the CIFAR-10 image classification dataset. The project progresses from classical machine learning baselines to deep learning models and transformer-based architectures.

The work is organized as a sequence of labs covering k-Nearest Neighbors, linear classifiers, fully connected neural networks, convolutional neural networks, ResNet-18, and Vision Transformers.

---

## Project Overview

The project includes the following stages:

1. **k-Nearest Neighbor classification**
   - Loads and preprocesses CIFAR-10.
   - Implements k-NN classification.
   - Compares two-loop, one-loop, and no-loop distance computation.
   - Performs k-fold cross-validation for selecting `k`.

2. **Multiclass SVM**
   - Implements naive and vectorized SVM loss.
   - Performs gradient checking.
   - Trains a linear SVM with stochastic gradient descent.
   - Runs hyperparameter search over learning rate and regularization strength.
   - Visualizes learned class weights.

3. **Softmax classifier**
   - Implements naive and vectorized Softmax loss.
   - Performs gradient checking.
   - Trains a Softmax classifier on raw CIFAR-10 pixels.
   - Runs hyperparameter search and visualizes learned weights.

4. **Two-layer neural network with NumPy**
   - Implements affine layers, ReLU activation, forward passes, and backward passes.
   - Uses numerical gradient checks to validate implementations.
   - Trains a two-layer fully connected network with a custom solver.

5. **Two-layer neural network with PyTorch**
   - Introduces PyTorch tensors, modules, optimizers, and training loops.
   - Trains two-layer networks using barebone PyTorch, the Module API, and Sequential API.
   - Experiments with optimizers, activation functions, hidden layer sizes, dropout, and learning-rate schedulers.

6. **Custom CNNs and ResNet-18**
   - Trains three-layer convolutional networks using barebone PyTorch, Module API, and Sequential API.
   - Compares optimizer, activation, and channel/filter settings.
   - Trains ResNet-18 from scratch.
   - Fine-tunes pretrained ResNet-18 models for CIFAR-10.

7. **Vision Transformers**
   - Implements a custom Vision Transformer from PyTorch modules.
   - Builds patch embedding, positional embeddings, attention heads, multi-head attention, MLP blocks, encoder blocks, and a ViT classifier.
   - Performs experiments with learning rate, patch size, hidden size, number of layers, and attention heads.
   - Fine-tunes pretrained ViT-Tiny and ViT-Base models using `timm`.

---

## Repository Structure

```text
cifar10-computer-vision-from-basics-to-transformers/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
│   └── README.md
│
├── engine/
│   ├── __init__.py
│   ├── data_utils.py
│   ├── gradient_check.py
│   ├── layer_utils.py
│   ├── layers.py
│   ├── optim.py
│   ├── solver.py
│   ├── vis_utils.py
│   │
│   └── classifiers/
│       ├── __init__.py
│       ├── k_nearest_neighbor.py
│       ├── linear_classifier.py
│       ├── linear_svm.py
│       ├── softmax.py
│       └── two_layer_net.py
│
└── notebooks/
    ├── 01_knn.ipynb
    ├── 02_svm.ipynb
    ├── 03_softmax.ipynb
    ├── 04_numpy_two_layer_net.ipynb
    ├── 05_pytorch_two_layer_net.ipynb
    ├── 06_custom_cnns_vs_resnet.ipynb
    └── 07_custom_vision_transformer_vs_vit.ipynb
```

---

## Notebooks

The notebooks are intended to be read in numerical order.

| Notebook | Main topic |
|---|---|
| `01_knn.ipynb` | k-Nearest Neighbor classification on CIFAR-10 |
| `02_svm.ipynb` | Multiclass SVM loss, gradient checking, SGD, and tuning |
| `03_softmax.ipynb` | Softmax classifier implementation and tuning |
| `04_numpy_two_layer_net.ipynb` | Fully connected neural network from scratch with NumPy |
| `05_pytorch_two_layer_net.ipynb` | Two-layer neural networks with PyTorch |
| `06_custom_cnns_vs_resnet.ipynb` | Custom CNNs, ResNet-18 training, and ResNet-18 fine-tuning |
| `07_custom_vision_transformer_vs_vit.ipynb` | Custom Vision Transformer and pretrained ViT fine-tuning |

---

## Data

This project uses the CIFAR-10 dataset.

The dataset files are **not committed to GitHub**. Some notebooks use the raw CIFAR-10 Python batch format, while later notebooks use `torchvision.datasets.CIFAR10`, which can download the dataset automatically when `download=True`.

See `data/README.md` for local dataset placement instructions.

---

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/Gerostathos/cifar10-computer-vision-from-basics-to-transformers.git
cd cifar10-computer-vision-from-basics-to-transformers
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

macOS / Linux:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Prepare the dataset

Follow the instructions in:

```text
data/README.md
```

For the NumPy-based notebooks, place the CIFAR-10 Python batch folder locally as:

```text
data/cifar-10-batches-py/
```

For the PyTorch-based notebooks, the dataset can also be downloaded through `torchvision.datasets.CIFAR10`.

### 5. Open the notebooks

```bash
jupyter notebook
```

Then open the notebooks from the `notebooks/` folder and run them in order.

---

## Path Notes

The notebooks were originally developed in Google Colab / Google Drive and local notebook environments. Some cells may contain environment-specific paths such as:

```text
/content/drive/MyDrive/...
/mnt/data/datasets/...
```

When running locally, update dataset paths to point to the local CIFAR-10 location described in `data/README.md`.

If the notebook is executed from inside the `notebooks/` folder, use paths such as:

```python
../data/cifar-10-batches-py/
```

If the notebook is executed from the repository root, use paths such as:

```python
data/cifar-10-batches-py/
```

If local imports from `engine/` fail after moving the notebooks into the `notebooks/` folder, add the repository root to `sys.path` at the top of the notebook:

```python
import sys
from pathlib import Path

PROJECT_ROOT = Path.cwd()
if PROJECT_ROOT.name == "notebooks":
    PROJECT_ROOT = PROJECT_ROOT.parent

sys.path.insert(0, str(PROJECT_ROOT))
```

---

## Results Mentioned in the Notebooks

The notebooks include reported experimental results from the performed runs. Examples include:

| Model / experiment | Reported result |
|---|---:|
| k-NN on a small CIFAR-10 test subset | about 29% accuracy |
| Linear SVM on raw pixels | about 36.81% test accuracy |
| Softmax classifier on raw pixels | about 33.55% test accuracy |
| NumPy two-layer network | about 51.54% test accuracy |
| PyTorch two-layer network | about 53.91% test accuracy |
| Custom ConvNet | about 62.14% test accuracy |
| ResNet-18 trained from scratch | about 73.53% test accuracy |
| ResNet-18 full fine-tuning | about 78.94% test accuracy |
| ViT-Base classifier fine-tuning | about 93.86% test accuracy |

These values come from the saved notebook outputs and may vary with random seeds, hardware, runtime environment, dataset path settings, and training configuration.

---

## Main Libraries Used

- NumPy
- Matplotlib
- scikit-learn
- PyTorch
- Torchvision
- timm
- tqdm
- Pillow
- imageio

---

## Notes

- The repository contains both notebook experiments and reusable Python helper modules.
- The `engine/` folder contains implementation code for classical classifiers, neural-network layers, optimizers, gradient checking, solver logic, and visualization utilities.
- The CIFAR-10 dataset and generated model checkpoints are intentionally excluded from GitHub.
- Some notebooks contain saved outputs from previous runs. Re-running the notebooks may produce slightly different results.

---

## Possible Future Improvements

Possible extensions include:

- standardizing all notebooks to use repository-relative paths,
- adding a small configuration file for dataset paths and training settings,
- moving repeated PyTorch training utilities into reusable scripts,
- adding seed control for more reproducible experiments,
- saving selected result tables in a lightweight `results/` folder,
- adding a short project report summarizing the progression from classical methods to transformers.
