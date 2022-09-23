import numpy as np

def divided_diff(x, y):
    '''
    function to calculate the divided
    differences table
    '''
    n = len(y)
    coef = np.zeros([n, n])

    #for i in range(n):
     #   coef = [0][y]

    #the first column is y
    coef[:,0] = y
    
    for j in range(1,n):
        for i in range(n-j):
            coef[i][j] = (coef[i+1][j-1] - coef[i][j-1]) / (x[i+j]-x[i])            
    
    return coef

def newton_poly(coef, x_data, x):
    '''
    evaluate the newton polynomial 
    at x
    '''
    n = len(x_data) - 1 
    p = coef[n]
    for k in range(1,n+1):
        p = coef[n-k] + (x -x_data[n-k])*p
    return p

# tutaj wpisać f(x) x
x = np.array([0.5,1.0,1.25,1.75,2.0])
#x = [1,3,2,5,7]

# tutaj wpisać = y
y = np.array([0.48, 0.84, 0.95, 0.98, 0.91])
#y = [1, 2, 3, 4, 6]

# get the divided difference coef

#wspolczynniki
a_s = divided_diff(x, y)[0, :]
print(a_s)

#wartosc funkcji w pkt x_new
x_new = 1.5

y_new = newton_poly(a_s, x, x_new)
print(y_new)
