import time
import pandas as pd
import numpy as np

def solar_pv():

    v_pow_pv = A_pv * n_pv * ghi * (1 - (293 - (273+temp_PV(h))) * gamma)
