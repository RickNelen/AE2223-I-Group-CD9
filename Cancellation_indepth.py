import lib.core as core
import matplotlib.pyplot as plt


k = core.unpickle("./Data.txt")                                                 #getting the data ready
k = core.sortata(k, 2)

#getbyata for a certain ata

""" JUST MAKE SURE THE ATA NUMBERS YOU INPUT ACTUALLY HAVE CANCELLATIONS
WITHIN THE TIME PERIOD"""

def graphthis(year, ata, actype, data):
    k = core.getbyType(data,actype)
    canc_freq = []
    labels = []
    
    
    for m in range(len(ata)):
        canc_freq.append([0])
    
    print canc_freq, "initial"
    yearlst = []
    no_of_yrs = year[1]-year[0] + 1
    
    for p in range(no_of_yrs):
        yearlst.append(int(year[0]+p))
    
    
    for i in range(len(ata)):
        int_canc_freq = []
        labels.append(ata[i])
        
        delay, date = core.getdelaylist([year[0],year[1]], 12, k)
        
        for j in range(no_of_yrs):
            #if j not in yearlst:
            #    yearlst.append(year[0]+j)
            
            for n in range(len(delay[j])):
                if delay[j][n][0] == ata[i]:
                    int_canc_freq.append(delay[j][n][3])
            print int_canc_freq, "intermediate, per ata"
        canc_freq[i] = int_canc_freq
    """
        plt.xlabel('Year')
        plt.ylabel('Cancellation Frequency')
        plt.plot(yearlst, canc_freq[i])
        plt.legend()
        plt.show()"""
    print canc_freq, "cancel frequency"
    print yearlst, "yearlist"
    
    
    plt.xlabel('Year')
    plt.ylabel('Cancellation Frequency')
    for q, label in zip(range(len(ata)),labels):
        plt.plot(yearlst, canc_freq[q], marker = 'o', label = label)
        plt.xticks(yearlst)
    plt.legend()
    plt.savefig('Results/hopefullyitworks.png', dpi = 200)
    plt.show()



graphthis([1998,2003],[32,34, 27,22],1,k)















    
    





















