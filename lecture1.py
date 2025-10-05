import numpy as np
import matplotlib.pyplot as plt

def estimate_coef(x, y):
    #number of observation/sample size
    n = np.size(x)
    #mean of x and y
    m_x = np.mean(x)
    m_y = np.mean(y)
    #calculate cross - deviation (xy) and deviation about x (xx) x^2
    ss_xy = np.sum(x * y) - n * m_y * m_x
    ss_xx = np.sum(x * x) - n * m_x * m_x
    #caclulate coef of A and B
    a = ss_xy / ss_xx
    b = m_y - a * m_x
    return b, a

def plot_regression_line(x, y, ec):
    #plotting the actual points as scatter plot
    plt.scatter(x, y, color = "m", marker = "o", s = 30)
    #predicated vectors
    y_pred = ec[0] + ec[1] * x
    #plot regression line
    plt.plot(x, y_pred, color = "g")
    #labels
    plt.xlabel("X")
    plt.ylabel("Y")
    #show graph
    plt.show()

def main():
    #define given values
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([12, 19, 29, 37, 45])
    #get the estimated coefficient of x and y
    ec = estimate_coef(x, y)
    #get the y prediction
    y_pred = ec[0] + ec[1] * x
    #print estimated coeffiecients
    print("Estimated Coefficients:\na = {:.2f}\nb = {:.2f}\n".format(ec[0], ec[1]))
    print("Plot regression line (x, y):{}{}".format(x, y_pred))
    #plotting of regression line
    plot_regression_line(x, y, ec)
if __name__ == '__main__':
    main()