import numpy as np

def mean_squared_error(y_pred, y_true):
    """
    Returns: float MSE
    """
    y_pred = np.asarray(y_pred)
    y_true = np.asarray(y_true)
    return 1 / len(y_pred) * np.sum((y_pred - y_true) ** 2)