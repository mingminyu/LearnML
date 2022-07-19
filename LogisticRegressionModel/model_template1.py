# coding: utf8

import logging
import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
from pathlib import Path
from sklearn.model_selection import train_test_split
from statsmodels.stats.outliers_influence import variance_inflation_factor

"""使用逻辑回归构建分类预测模型
- 建模工具使用 statsmodels 搭建 LR
- 模型评价
"""






if __name__ == '__main__':

    df_it = pd.read_csv("../data/train2.csv")