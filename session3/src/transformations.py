<<<<<<< HEAD
import numpy as np

def normalize(data, min_val = 0, max_val=1):
    # step1
    data_normed = np.array([data])-np.array([data]).min()
    data_normed = data_normed/np.array([data_normed]).max()

    data_normed = data_normed * (max_val-min_val) + min_val
=======
def normalize(data, min_val=0, max_val=1):

    # step 1: normalize between 0 and 1
    data_nomred = data - data.min()
    data_normed = data_nomred / data_nomred.max()

    data_normed = data_normed * (max_val - min_val) + min_val
>>>>>>> 29d6b737cf17a6350afacd52193357c2c364229f
    return data_normed