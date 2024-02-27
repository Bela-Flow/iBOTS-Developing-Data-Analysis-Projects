import numpy as np
from tqdm import tqdm
from scipy.io import loadmat

def merge_pupil_data(all_mat_files,pupil_variable):
    
    pupil_area_data = []
    for filename in tqdm(all_mat_files, desc=f"Merging the {pupil_variable} data"):
        pupil_area_data_per_trial = loadmat(filename)[pupil_variable].squeeze()
        pupil_area_data.append(pupil_area_data_per_trial)

    pupil_area_data = np.stack(pupil_area_data)
    return pupil_area_data

def merge_data(all_npy_files, desc = "Merging the data"):
    data = []
    for filename in tqdm(all_npy_files, desc=desc):
        data_per_trial = np.load(filename)
        data.append(data_per_trial)

    data = np.stack(data)
    return data