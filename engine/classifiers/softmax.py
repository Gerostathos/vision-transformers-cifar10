from builtins import range
import numpy as np
from random import shuffle
from past.builtins import xrange


def softmax_loss_naive(W, X, y, reg):
    """
    Softmax loss function, naive implementation (with loops)

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
    # Initialize the loss and gradient to zero.
    loss = 0.0
    dW = np.zeros_like(W)

    num_train = X.shape[0]
    num_classes = W.shape[1]

    for i in range(num_train):
        # Compute the score for each class
        scores = X[i].dot(W)

        scores -= np.max(scores)
        sum_exp_scores = np.sum(np.exp(scores))
        softmax_probs = np.exp(scores) / sum_exp_scores

        correct_class_prob = softmax_probs[y[i]]
        loss += -np.log(correct_class_prob)


        for j in range(num_classes):
            # Softmax gradient computation
            if j == y[i]:
                dW[:, j] += (softmax_probs[j] - 1) * X[i]
            else:
                dW[:, j] += softmax_probs[j] * X[i]
    loss /= num_train

    dW /= num_train

    loss += reg * np.sum(W * W)

    dW += 2 * reg * W

    return loss, dW


def softmax_loss_vectorized(W, X, y, reg):
    """
    Softmax loss function, vectorized version.

    Inputs and outputs are the same as softmax_loss_naive.
    """
    # Initialize the loss and gradient to zero.
    loss = 0.0
    dW = np.zeros_like(W)

    num_train = X.shape[0]
    scores = X.dot(W)
    scores -= np.max(scores, axis=1, keepdims=True)
    exp_scores = np.exp(scores)
    softmax_probs = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)
    correct_class_probs = softmax_probs[np.arange(num_train), y]
    loss = -np.sum(np.log(correct_class_probs)) / num_train
    loss += reg * np.sum(W * W)
    softmax_probs[np.arange(num_train), y] -= 1
    dW = X.T.dot(softmax_probs) / num_train
    dW += 2 * reg * W

    return loss, dW
