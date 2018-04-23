# --- Ranking, Author: Tony --- #

"""Make a function that takes 3 parameters, the dataset, the top X number, and 
the column you want to rank by. Then it will return a matrix with all the available
data for those top x number"""

"""NOTE to whoever is looking at this: the functions "by-x" are all basically the 
same code, this was initially to make it so that it's easier to edit each individual functions.
"""

#Note to myself: Just be careful, because you're using Python 2.7 instead of 3.x
#int/int doesn't give you float. print is not a function.



#Data
#[[serial][type][date][delay][cancelled][ATA0][ATA1][ATA2][ATA3][ATA4][ATA5]]


#==============================================================================
# --- Example ---
"""SAMPLE DATA""" 
#
"""
top_x_choice = 5 # number of items in the list, in this case the top 5 will be found
column_choice = 2 # ( 0 = serial number, 1 = type of aircraft, 2 = date, 3 = delay time, 4 = number of cancellations, 5 = ATA number):  "))

dataset = [[1,1,4,100,17,'T'],
            [2,2,5,120,6,'F'],
            [3,1,6,140,40,'T'],
            [4,2,7,160,34,1],
            [7,3,8,180,56,2],
            [2,1,9,100,18,2],
            [5,2,10,130,29,1],
            [6,3,11,150,38,2],
            [7,2,12,170,45,1],
            [10,3,13,190,33,1],
            [200,3,14,200,31,2],
            [122,2,15,200,37,1]]
            
rankme(dataset, top_x_choice, column_choice)
            
"""
#==============================================================================

#==============================================================================
#==============================================================================
#   Pre-requisite functions
#==============================================================================
#==============================================================================
def find_max(dataset, top_x, column): #Used for simple floats
    if dataset == None:
        print "Done"
    else:
        current_max_in_loop = 0
        i = 0
        while i < len(dataset):
            if dataset[i][column] > current_max_in_loop:
                current_max_in_loop = dataset[i][column]
                idx = i
            i += 1
            
        return idx
#Basically here, I took i less than the length of the dataset and then found the 
#biggest one I can find. and it returns the index. 

"""int(datetime.datetime.fromtimestamp(b[i][2]).strftime('%D'))"""

def byserial(dataset, top_x):
    #Takes in dataset and top_x number and sorts it by serial number.
    number_found = 0
    ranked_list = []
#    item_in_list = []
    while number_found < top_x:
        idx = find_max(dataset, top_x, column_choice) #Here, I take the index
        #Then I append the ranked_list with the entry and then delete it from the
        #datset. 
        ranked_list.append(dataset[idx])
        dataset.remove(dataset[idx])
        number_found  += 1    
    return ranked_list
        
#==============================================================================
def bytype(dataset, top_x):
    #and then rank by serial. 
    number_found = 0
    counter_unique = 0
    ranked_list = []
    final_ranked_list = []
    while number_found < top_x:
        idx = find_max(dataset, top_x, column_choice)
        if dataset[idx][1] not in ranked_list:
            counter_unique += 1
        ranked_list.append(dataset[idx])
        dataset.remove(dataset[idx])
        number_found += 1
    counter = 0
    while counter < counter_unique:    
        starting_type = ranked_list[counter][1]
        intermediate = []
        for i in range(len(ranked_list)):
            if ranked_list[i][1] == starting_type:
                intermediate.append(ranked_list[i])
        byserial(intermediate, len(intermediate), 0)
        final_ranked_list.append(intermediate)
        counter += 1
    return final_ranked_list
"""Still have to work on it. Kind of fucked up"""

def bydate(dataset, top_x):
    #Note that this takes the unix values. therefore, it's not readable. 
    number_found = 0
    ranked_list = []
    while number_found < top_x:
        idx = find_max(dataset, top_x, column_choice)
        ranked_list.append(dataset[idx])
        dataset.remove(dataset[idx])
        number_found += 1
    return ranked_list

def bydelaytime(dataset,top_x):
    number_found = 0
    ranked_list = []
    while number_found < top_x:
        idx = find_max(dataset, top_x, column_choice)
        ranked_list.append(dataset[idx])
        dataset.remove(dataset[idx])
        number_found += 1
    return ranked_list
    
"""def bydelaytime(dataset, top_x):
    number_found = 
"""

#==============================================================================
#==============================================================================
def rankme(dataset, top_x, column):
    if column == 0:
        serial_sorted_list = byserial(dataset, top_x)
        print serial_sorted_list
    elif column == 1:
        type_sorted_list = bytype(dataset, top_x)
        print type_sorted_list
    elif column == 2:
        date_sorted_list = bydate(dataset, top_x)
        print date_sorted_list
    elif column == 3:
        delaytime_sorted_list = bydelaytime(dataset, top_x)
        print delaytime_sorted_list
#==============================================================================
#==============================================================================
# 
# This function should take in 3 parameters, dataset, top_x number, and a column index.
# Then it will output a list with top_x number of components ranked by the column index
# given previously. 
#==============================================================================
    
    
    
# --- least squares ---

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

"""
example model function (this is a tri-modal weibull with 6 parameters in total):
def model(beta, x):
    return 1./3 *beta[0]/beta[1] * (x/beta[1])**(beta[0]-1) * np.exp(-1*(x/beta[1])**beta[0]) + 1./3 *beta[2]/beta[3] * (x/beta[3])**(beta[2]-1) * np.exp(-1*(x/beta[3]**beta[2]) + 1./3 *beta[4]/beta[5] * (x/beta[5])**(beta[4]-1) * np.exp(-1*(x/beta[5]**beta[4])))
"""



def lstsquares(model, n, beta, data, h=1e-4): # obsolete, cause I am now using a built-in
    
    ## load modules
    import numpy as np
    import numpy.linalg as la
    import scipy.stats as stats
    
    #print data.size
    
    if np.isnan(data[0,1]): # is the data array empty?
        raise TypeError("Data array passed is empty")
        
    
    datax = data[:,0]
    datay = data[:,1]
    
    
    ## Computations
    def r(beta,x,y):
        return y - model(beta,x); # parametric error function, y and x must be same length vectors. beta is vector too, of course
        
    def jacobian(fun,x,beta,h):
        # computes the jacobian for the Newton Gau? Method
        # works in a loop and computes every partial derivative with the finite
        # difference method, which probably is slower than it could be, but I 
        # couldn't come up with something better
    
        n = len(beta) # dimensions of the Jacobian, m rows, n columns
        m = len(x)
        
        J = np.zeros([m,n])
        for i in range(m):
            for j in range(n):
                helper    = np.matrix(np.zeros([n,1]));
                helper[j] = 1; # helper helps to change only the entry in the beta vector that must be considered
                zeta1     = beta + 0.5* h*helper; # finite difference method with central differences
                zeta2     = beta - 0.5* h*helper;
                J[i,j]    = (fun(zeta1,x[i],1)-fun(zeta2,x[i],1))/h;
        
        return np.transpose([J]) # don't remember why I have to take the transpose, but this works reliably
    
    itern = 1
    conti = True;
    while conti:
        
        # main loop, here the Newton Gauss is facilitated
        J = jacobian(r,datax,beta,h) # O(length(datax)*length(beta))
        betanew = beta - np.array(np.matrix(la.pinv(J)) * np.matrix(r(beta,datax,datay))) # O(2n*m+m^3+n^2*m) pseudoinverse, like in Least Square in LinAlg
        itern += 1
        
        #print betanew, beta
        #print la.norm(betanew-beta)
        if la.norm(betanew-beta) < h:
            conti = False
            gamma = beta
        if itern > 10:
            print "max itern"
            conti = False
            gamma = np.array([0,0])
        beta = betanew
    
    print "done"
    
    ## Chi squared test
    
    modely = model(beta,data[:,0])
    
    Xsquare = sum(np.array((datay - modely))**2/np.array(modely))
    
    probnull = stats.chi2.cdf(Xsquare,len(datax)-1) # how likely is obtained X square value if all is independant (ie null hypothesis)
    pval = 1-probnull
    
     
    
    return (gamma, pval, itern)





def fitweibull(histo, plot = 0):
    # takes _one_ normalized histogram from np.histogram and fits a weibull to it using init guess k=1.5, lambda = 20.
    # now uses scipy builtin function for the fitting
    
    import numpy as np
    import scipy.special as sp # import the special functions for gamma
    import matplotlib.pyplot as plt
    from scipy.optimize import curve_fit
    
    # model function: weibull
    #def weibull(beta, x):
     #   return beta[0]/beta[1] * np.multiply(np.power((np.array(x)/beta[1]),(beta[0]-1)), np.exp(-1* np.power((np.array(x)/beta[1]),beta[0])))
    
    def weibull(x, k, lamb): # parametric model for the scipi implementation of lstsquares
        return k/lamb * (x/lamb)**(k-1) * np.exp(-(x/lamb)**k)
    
    
    fitbeta = []
    mean    = []
    var     = []
#    pval    = []
#    iternum = []
    
    i = 0
    # idea for faster runtime/better convergence --> make weibull initial
    # guess beta[1] = index of max of histo instead of constant [1,20]
    #(fb, p, it) = lstsquares(weibull, 2, np.transpose([np.array([1.,20.])]), np.concatenate((np.matrix(histo[1][1][1:]).T, np.matrix(histo[1][0]).T), axis = 1) )
   
    try:
        fb, cov = curve_fit(weibull, histo[1][1][1:], histo[1][0], [1.5, 20.]) # I ditched my own implementation and used this one
    except RuntimeError:
        fb = np.array([0,0])
    except ValueError:
        fb = np.array([0,0])
    
    if not fb[0]: # if fitting failed:
        
        fitbeta.append(np.array([0,0]))
        mean.append(0)
        var.append(0)
#        pval.append(0)
#        iternum.append(0)
        
    else:
        # calculate mean
        m = fb[1]*sp.gamma(1+1/fb[0]) # wikipedia: weibull distribution
    
        # calculate variance in the weibull fit data
        v = fb[1]**2 * ( sp.gamma(1+2./fb[0]) - sp.gamma(1+1./fb[0])**2 ) # wikipedia: Weibull distribution
        
        
        fitbeta.append(fb)
        mean.append(m)
        var.append(v)
    
        #optional plotting
        if plot:
            xplot = np.arange(0,400,1)
            yfit = weibull(xplot,fb[0], fb[1])
            
            plt.close()
            plt.title("ATA Component 324 -- Year 2008 -- Stdev: %.1f min" % np.sqrt(v))
            plt.xlabel("Delay Time [min]")
            plt.ylabel("Density")
            plt.plot(xplot,yfit)
            plt.plot( histo[1][1][1:], histo[1][0] )
            plt.xlim([0,400])
            plt.savefig("ATA324_Fit.eps")
            plt.show()
        
        i += 1
        
    
    return (fitbeta, mean, var)
    
    
    
    
    
    
    
    
    