import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError('List must contain nine numbers.')
    a = np.array(list).reshape(3, 3)
    calculations = {
        'mean' : [np.mean(a, axis = 0).tolist()[0], np.mean(np.transpose(a), axis = 0).tolist()[0], np.mean(a)],
        'variance' : [np.var(a, axis = 0).tolist()[0], np.var(np.transpose(a), axis = 0).tolist()[0], np.var(a)],
        'standard deviation' : [np.std(a, axis = 0).tolist()[0], np.std(np.transpose(a), axis = 0).tolist()[0], np.std(a)],
        'max' : [np.max(a, axis = 0).tolist()[0], np.max(np.transpose(a), axis = 0).tolist()[0], np.max(a)],
        'mix' : [np.min(a, axis = 0).tolist()[0], np.min(np.transpose(a), axis = 0).tolist()[0], np.min(a)],
        'sum' : [np.sum(a, axis = 0).tolist()[0], np.sum(np.transpose(a), axis = 0).tolist()[0], np.sum(a)]
    }
    return calculations