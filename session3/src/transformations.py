import numpy as np

def normalize(data, min_val = 0, max_val=1):
    # step1
    data_normed = np.array([data])-np.array([data]).min()
    data_normed = data_normed/np.array([data_normed]).max()

    data_normed = data_normed * (max_val-min_val) + min_val
    return data_normed