import statsmodels.api as sm

data = sm.datasets.spector.load_pandas()
y, x = data.endog, data.exog

reg = sm.OLS(y, x).fit()
# Print out regression summary
print reg.summary()
# Coefficients
print((reg.params))
# Residuals
print((reg.resid))


import numpy as np
import matplotlib.pyplot as plt

x = np.arange(100)
y = 150 + 3*x + 0.03*x**2 + 5*np.random.randn(len(x))

# Three ways to fit the regression model

# 1. Design Matrix + np.linalg.lstsq
M1 = np.vstack((np.ones_like(x), x)).T
M2 = np.vstack((np.ones_like(x), x, x**2)).T
M3 = np.vstack((np.ones_like(x), x, x**2, x**3)).T

p1 = np.linalg.lstsq(M1, y)
p2 = np.linalg.lstsq(M2, y)
p3 = np.linalg.lstsq(M3, y)

np.set_printoptions(precision=3) 

print('The coefficients from the linear fit: {0}'.format(p1[0]))
print('The coefficients from the quadratic fit: {0}'.format(p2[0]))
print('The coefficients from the cubic fit: {0}'.format(p3[0]))

import statsmodels.api as sm

# 2. Design Matrix + statsmodels.sm
Res1 = sm.OLS(y, M1).fit()
Res2 = sm.OLS(y, M2).fit()
Res3 = sm.OLS(y, M3).fit()

print(Res1.summary())
print(Res2.summary())
print(Res3.summary())

# 3. pandas + statsmodels.formula.sm
import pandas as pd 
import statsmodels.formula.api as smf
df = pd.DataFrame({'x':x, 'y':y})

Res1F = smf.ols('y ~ x', df).fit()
Res2F = smf.ols('y ~ x + I(x**2)', df).fit()
Res3F = smf.ols('y ~ x + I(x**2) + I(x**3)', df).fit()

print(Res1F.summary())
print(Res2F.summary())
print(Res3F.summary())