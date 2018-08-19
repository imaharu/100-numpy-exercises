import numpy as np
x = np.zeros(25).reshape(5,5)
def pad_with(vector, pad_width, iaxis, kwargs):
    pad_value = kwargs.get('padder', 10)
    vector[:pad_width[0]] = pad_value
    vector[-pad_width[1]:] = pad_value
    return vector
print(np.pad(x,1 ,pad_with, padder=1))