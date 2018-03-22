# Converted from MATLAB, Author: tblaha
# 12.03.2018
# 
# Inputs:
#       model : a model function that takes 2 arguments and outputs a column of the results
#           1. a column vector of n parameters to be ajusted using least square regression
#           2. a column vector for the variables x
#       n     : the number of parameters in the model function, so the length of the parameter vector mentioned above in 1.
#       beta  : a column vector containing the initial guesses for the parameters of the model function
#       data  : a mx2 matrix with 2 colums for the x-y data to be fitting using lsq regression
#       h     : objective function step size at which the algorithm is assumed to have converged (default 1e-4) don't go below 1e-6 otherwise rounding messes it up (see NA reader)
#
# Outputs:
#       gamma : the parameter vector minimizing the least square error
#       pval  : the p-value of the chi squared statistical significance test of the model fitted to the data at the x values in the data matrix
#       itern : number of iteration needed to converge 

import numpy as np
import numpy.linalg as la
import scipy.stats as chi2

def model(beta, x):
    return 1./3 *beta[0]/beta[1] * (x/beta[1])**(beta[0]-1) * np.exp(-1*(x/beta[1])**beta[0]) + 1./3 *beta[2]/beta[3] * (x/beta[3])**(beta[2]-1) * np.exp(-1*(x/beta[3]**beta[2]) + 1./3 *beta[4]/beta[5] * (x/beta[5])**(beta[4]-1) * np.exp(-1*(x/beta[5]**beta[4])))

def lstsquares(model, n, beta, data, h):
        
    ## Computations
    def r(beta,x,y): return y - model(beta,x); # parametric error function, y and x must be same length vectors. beta is vector too, of course
    
    beta = np.transpose(np.array([2,1,6,6,10,11])); # must be a column vector
    
    itern = 1
    conti = True;
    while conti:
        # main loop, here the Newton Gauss is facilitated
        J = jacobian(r,datax,beta,h) # O(length(datax)*length(beta))
        betanew = beta - la.pinv(J)*r(beta,datax,datay) # O(2n*m+m^3+n^2*m) pseudoinverse, like in Least Square in LinAlg
        itern += 1
        if la.norm(betanew-beta) < h:
            conti = False
            gamma = beta
    
    
    ## Chi squared test
    
    modely = model(beta,data[:,0])
    
    Xsquare = sum((datay - modely)**2/modely)
    
    probnull = chi2.cdf(Xsquared) # how likely is obtained X square value if all is independant (ie null hypothesis)
    pval = 1-probnull
    
    
    
    
    
    return (gamma, pval, itern)
    
    
    ## helper functions
    
    def jacobian(fun,x,beta,h):
        # computes the jacobian for the Newton Gau? Method
        # works in a loop and computes every partial derivative with the finite
        # difference method, which probably is slower than it could be, but I 
        # couldn't come up with something better
    
        n = len(beta) # dimensions of the Jacobian, m rows, n columns
        m = len(x)
        
        J = np.zeros([n,n])
        for i in range(m):
            for j in range(n):
                helper    = np.matrix(np.zeros([n,1]));
                helper[j] = 1; # helper helps to change only the entry in the beta vector that must be considered
                zeta1     = beta + 0.5* h*helper; # finite difference method with central differences
                zeta2     = beta - 0.5* h*helper;
                J[i,j]    = (fun(zeta1,x(i),1)-fun(zeta2,x(i),1))/h;