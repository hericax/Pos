import numpy as np
import pandas as pd

"""1: Circulatory | 2: Respiratory | 3: Digestive | 4: Diabetes | 5: Injury | 6: Musculoskeletal | 7: Genitourinary | 8: Neoplasms | 9: Other"""
                                    
def convertDiagnosis(data, col):
    for i in range(len(data[col])):
        
        if (np.floor(data[col][i]) <= 0): #V-E
            data[col][i] = 9
                                 
        elif (np.floor(data[col][i]) == 250): #250.xx
            data[col][i] = 4

        elif (np.floor(data[col][i]) == 785) or (np.floor(data[col][i]) >= 390 and np.floor(data[col][i]) <= 459): #390–459
            data[col][i] = 1
         
        elif (np.floor(data[col][i]) == 786) or (np.floor(data[col][i]) >= 460 and np.floor(data[col][i]) <= 519): #460–519
            data[col][i] = 2
         
        elif (np.floor(data[col][i]) == 787) or (np.floor(data[col][i]) >= 520 and np.floor(data[col][i]) <= 579): #520–579
            data[col][i] = 3
                   
        elif (np.floor(data[col][i]) == 788) or (np.floor(data[col][i]) >= 580 and np.floor(data[col][i]) <= 629): #580–629
            data[col][i] = 7
                                 
        elif (np.floor(data[col][i]) >= 710 and np.floor(data[col][i]) <= 739): #710–739
            data[col][i] = 6
            
        elif (np.floor(data[col][i]) >= 800 and np.floor(data[col][i]) <= 999): #800–999
            data[col][i] = 5
                 
        elif (np.floor(data[col][i]) == 780) or (np.floor(data[col][i]) >= 140 and np.floor(data[col][i]) <= 239): #140–239 780
            data[col][i] = 8
                             
        elif (np.floor(data[col][i]) >= 781 and np.floor(data[col][i]) <= 784): #781, 782, 784
            data[col][i] = 8
                             
        elif (np.floor(data[col][i]) >= 789 and np.floor(data[col][i]) <= 799): #789–799
            data[col][i] = 8
                                         
        elif (np.floor(data[col][i]) >= 240 and np.floor(data[col][i]) <= 279) and (np.floor(data[col][i]) != 250):#240–279 !250
            data[col][i] = 8
                                         
        elif (np.floor(data[col][i]) >= 680 and np.floor(data[col][i]) <= 709): #680–709
            data[col][i] = 8
                                                     
        elif (np.floor(data[col][i]) >= 1 and np.floor(data[col][i]) <= 139): #001–139
            data[col][i] = 8
        
        elif (np.floor(data[col][i]) >= 280 and np.floor(data[col][i]) <= 389):#280–289 290–319 320–359 360–389
                data[col][i] = 9
                        
        elif (np.floor(data[col][i]) >= 630 and np.floor(data[col][i]) <= 679):#630–679
                data[col][i] = 9
                                        
        elif (np.floor(data[col][i]) >= 740 and np.floor(data[col][i]) <= 759):#740–759
                data[col][i] = 9  
            
    return data