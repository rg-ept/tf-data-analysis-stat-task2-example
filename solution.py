import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 42877418

def solution(p: float, x: np.array) -> tuple:
 
    alpha = 1 - p
    loc = np.max(x)
    left = loc
    right = (loc-0.053)/(alpha**(1/len(x)))+0.053
    return left, right
