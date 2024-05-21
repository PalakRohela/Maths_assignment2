import numpy as np

def rmse(predictions, targets):
    """
    Calculate the Root Mean Square Error (RMSE) between two arrays of predictions and targets.

    Args:
    predictions (array-like): Predicted values.
    targets (array-like): True target values.

    Returns:
    float: The RMSE between predictions and targets.
    """
    pred = np.array(predictions)
    tar = np.array(targets)
    rmse = np.sqrt(np.mean((pred - tar) ** 2))
    return rmse
