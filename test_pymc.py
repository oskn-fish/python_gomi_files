#%%
import arviz as az
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#%config InlineBackend.figure_format = 'retina'
RANDOM_SEED = 8927
rng = np.random.default_rng(RANDOM_SEED)
az.style.use("arviz-darkgrid")

# true parameters
# alpha = intercept
# sigma = variance
alpha, sigma = 1, 1
beta = [1, 2.5]

# size of dataset
size = 100

# predictor variable
X1 = np.random.randn(size)
X2 = np.random.randn(size)*0.2

# 重回帰．X1とX2の二変数の線形+ノイズのデータ
Y = alpha+beta[0]*X1+beta[1]*X2+rng.normal(size=size)*sigma

# sharexでxの値の範囲を共有してる
# alphaは不透明度
fig, axes = plt.subplots(1, 2, sharex=True, figsize=(10, 4)) 
axes[0].scatter(X1, Y, alpha=0.6)
axes[1].scatter(X2, Y, alpha=0.6)
axes[0].set_ylabel("Y")
axes[0].set_xlabel("X1")
axes[1].set_xlabel("X2")

# %%
import pymc as pm

basic_model = pm.Model()
with basic_model:
    # define prior distoributions
    alpha = pm.Normal("alpha", mu=0, sigma=10)
    beta = pm.Normal("beta", mu=0, sigma=10, shape=2)
    sigma = pm.HalfNormal("sigma", sigma=1)
    
    # 線形変換
    mu = alpha+beta[0]*X1+beta[1]*X2
    
    # define model(Likelihood)
    Y_obs = pm.Normal("Y_obs", mu=mu, sigma=sigma, observed=Y)
    
with basic_model:
    idata = pm.sample(cores=1)
    
#%%
idata
    
# %%
import arviz as az
az.plot_trace(idata, combined=True)
# %%
