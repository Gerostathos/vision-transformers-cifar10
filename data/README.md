# Dataset Instructions

This folder is reserved for the CIFAR-10 dataset files used by this project.

The dataset files are **not committed to GitHub**. To run the notebooks locally, download or place CIFAR-10 under this folder using the structure described below.

## Dataset Source

The project uses the CIFAR-10 image classification dataset. CIFAR-10 contains 60,000 color images of size 32 × 32 from 10 classes:

```text
airplane, automobile, bird, cat, deer, dog, frog, horse, ship, truck
```

The official dataset page is:

```text
https://www.cs.toronto.edu/~kriz/cifar.html
```

The PyTorch notebooks can also use `torchvision.datasets.CIFAR10`, which downloads the dataset automatically when `download=True`.

## Expected Local Structure

For the NumPy-based notebooks that use the raw CIFAR-10 Python batch files, place the extracted CIFAR-10 folder here:

```text
data/
├── README.md
└── cifar-10-batches-py/
    ├── data_batch_1
    ├── data_batch_2
    ├── data_batch_3
    ├── data_batch_4
    ├── data_batch_5
    ├── test_batch
    ├── batches.meta
    └── readme.html
```

Only this `README.md` file should be committed to GitHub. The actual CIFAR-10 files should remain local.

## How the Dataset Is Used

The earlier notebooks use the raw CIFAR-10 Python batch format through the helper function `load_CIFAR10` from `engine/data_utils.py`.

The later PyTorch notebooks use:

```python
torchvision.datasets.CIFAR10
```

with `train=True` or `train=False`, and may download the dataset automatically depending on the value of `download`.

## Path Notes

The notebooks were originally developed in Google Colab / Google Drive and local notebook environments. Some cells may contain environment-specific paths such as:

```text
/content/drive/MyDrive/...
/mnt/data/datasets/...
```

When running the project locally, update dataset paths to point to the local CIFAR-10 folder.

If a notebook is executed from inside the `notebooks/` folder, use:

```python
../data/cifar-10-batches-py/
```

If code is executed from the repository root, use:

```python
data/cifar-10-batches-py/
```

For PyTorch notebooks, a local dataset root such as the following is also appropriate:

```python
../data/
```

or, from the repository root:

```python
data/
```

## GitHub Policy

The CIFAR-10 dataset files are intentionally excluded from this repository to keep the GitHub project lightweight and to avoid redistributing external data.

Do not commit:

```text
cifar-10-batches-py/
cifar-10-python.tar.gz
*.pkl
model checkpoints
training outputs
```

Commit only this `README.md` file inside the `data/` folder.
