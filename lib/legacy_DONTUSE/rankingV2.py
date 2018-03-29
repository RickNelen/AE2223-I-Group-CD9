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

top_x_choice = int(raw_input("Type in the number of items you want to see in your ranking list:     "))
column_choice = int(raw_input("Please indicate which column you want to rank by ( 0 = serial number, 1 = type of aircraft, 2 = date, 3 = delay time, 4 = number of cancellations, 5 = ATA number):  "))

#==============================================================================
"""SAMPLE DATA""" 
#
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
#"""Still have to work on it. Kind of fucked up"""            
        
        
    return final_ranked_list

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
    
    
rankme(dataset, top_x_choice, column_choice)
    