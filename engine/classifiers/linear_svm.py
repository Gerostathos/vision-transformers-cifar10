from builtins import range
import numpy as np
from random import shuffle
from past.builtins import xrange


def svm_loss_naive(W, X, y, reg):
    """
    Structured SVM loss function, naive implementation (with loops).

    Inputs have dimension D, there are C classes, and we operate on minibatches
    of N examples.

    Inputs:
    - W: A numpy array of shape (D, C) containing weights.
    - X: A numpy array of shape (N, D) containing a minibatch of data.
    - y: A numpy array of shape (N,) containing training labels; y[i] = c means
      that X[i] has label c, where 0 <= c < C.
    - reg: (float) regularization strength

    Returns a tuple of:
    - loss as single float
    - gradient with respect to weights W; an array of same shape as W
    """
    # Initialize the loss and gradient as zero
    loss = 0.0
    dW = np.zeros(W.shape)  # gradient of the weights, initialize to zero

    # Dimensions
    num_classes = W.shape[1]
    num_train = X.shape[0]

    
    for i in range(num_train):
      scores = X[i].dot(W)
      correct_class_score = scores[y[i]]
      for j in range(num_classes):
        if j == y[i]:
          continue
        margin = scores[j] - correct_class_score + 1
        if margin > 0:
          loss += margin
         
          dW[:, j] += X[i]
          dW[:, y[i]] -= X[i]
          
    loss /= num_train  
    dW /= num_train
    
    loss += 0.5 * reg * np.sum(W * W)
    dW += reg * W
    
    return loss, dW


def svm_loss_vectorized(W, X, y, reg):
    """
    Structured SVM loss function, vectorized implementation.

    Inputs and outputs are the same as svm_loss_naive.
    """
    loss = 0.0
    dW = np.zeros(W.shape)  # initialize the gradient as zero
    num_classes = W.shape[1]
    num_train = X.shape[0]

    scores = X.dot(W)  
    correct_class_scores = scores[np.arange(num_train), y].reshape(-1, 1) 
    margins = np.maximum(0, scores - correct_class_scores + 1)  
    margins[np.arange(num_train), y] = 0
    loss = np.sum(margins) / num_train  
    loss += reg * np.sum(W * W)
    
    binary = margins > 0
    binary = binary.astype(int)
    row_sum = np.sum(binary, axis=1)
    binary[np.arange(num_train), y] = -row_sum
    dW = X.T.dot(binary) / num_train
    dW += 2 * reg * W
    
    return loss, dW
