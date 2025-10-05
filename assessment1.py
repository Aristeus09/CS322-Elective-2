import numpy as np
from share.lecture1 import plot_regression_line, estimate_coef

#define given values
x = np.array([1.7, 1.5, 2.8, 5, 1.3, 2.2, 1.3])
y = np.array([368, 340, 665, 954, 331, 556, 376])

#get the estimated coefficient of x and y
ec = estimate_coef(x, y)

#get the y prediction
y_pred = ec[0] + ec[1] * x

#print estimated coeffiecients
print("Estimated Coefficients:\na = {:.2f}\nb = {:.2f}\n".format(ec[0], ec[1]))
print("Plot regression line (x, y):{}{}".format(x, y_pred))
#plotting of regression line
plot_regression_line(x, y, ec)