
#Data
#[[serial][type][date][ata][delay][cancelled]]
dataset = [['a',1,4,100,17,'T'],
           ['b',2,5,120,6,'F'],
           ['c',3,6,140,40,'T'],
           ['d',4,7,160,34,1],
           ['e',5,8,180,56,2],
           ['f',6,9,100,18,2],
           ['g',7,10,130,29,1],
           ['h',8,11,150,38,2],
           ['i',9,12,170,45,1],
           ['j',10,13,190,33,1],
           ['k',11,14,200,31,2],
           ['l',12,15,200,37,1]]



#print(isinstance(dataset, list))

#print(len(dataset))

no_of_entry = len(dataset)

serial = []
t1pye = []
date = []
delay = []
cancelled = []
#if the ATA number is already there, check if delay is bigger, if not, replace that entry.

#might be better to just store every data so that we can use it later on.
data_entry = []


###############################################################################
#Assuming other people have organized everything by ATA number already, we will 
#continue the code.
def find_max_delay(no_of_entry, data):
    if data == None:
        print("done")
    else:
        max_delay = 0
        i = 0
        while i < no_of_entry:
            #print(data, i,  "i")
            #print(max_delay, "MAX_DELA")
            if data[i][4] > max_delay:
                
                max_delay = data[i][4]
                idx = i
                ATA_number = data[i][3]
            i += 1
        
        return max_delay, ATA_number, idx


top_ten = []
ATA = []  


#new_dataset = dataset
max_delay, ATA_number, idx = find_max_delay(no_of_entry, dataset)
top_ten.append(max_delay)
ATA.append(ATA_number)
print(dataset[idx], "this is old")
dataset.remove(dataset[idx])
print(idx, "INDEX")
print(dataset, "this is the new dataset")
no_of_entry -= 1
j = False
k = 0
while not j:
    if dataset == None:
        print("done this time")
        break
    else:    
        max_delay, ATA_number, idx = find_max_delay(no_of_entry, dataset)
        if ATA_number not in ATA:
            top_ten.append(max_delay)
            print(top_ten, "TOP TEN")
            ATA.append(ATA_number)
            print(ATA, "ATAAAAAA")
            dataset.remove(dataset[idx])
            print(dataset, "this is dataset within while")
            k += 1
            print(k, "K")
            no_of_entry -= 1
            #print(idx, "CHECKING")
            if k > 8:
                j= True
        else:
            dataset.remove(dataset[idx])
            no_of_entry -= 1
            

        
    
print(top_ten)
    
    
    
    
    

# =============================================================================
#     if data[i][3] not in ATA:
#         #serial.append(data[i][0])
#         #t1ype.append(data[i][1])
#         #date.append(data[i][2])
#         ATA.append(data[i][3])
#         delay.append(data[i][4])
#         #cancelled.append(data[i][5])
#     else:
#         idx = ATA.index(data[i][3])
#         if delay[idx] < data[i][4]:
#             delay[idx] = 
#             
# =============================================================================
            

"""TODO

--> Get the other delays of the same components and categorize them into ranges
and then graph them. 
-->     
    """
    
    
    
    
