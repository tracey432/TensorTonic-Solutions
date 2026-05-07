import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """ 
    # Write code here
    nparr = np.array(x)
    return 1 / (1 + np.exp(-nparr))
    
   