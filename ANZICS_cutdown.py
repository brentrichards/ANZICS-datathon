import pandas as pd
data = pd.read_csv("Sydney_datathon_APD2006to2016.csv", skipinitialspace=True)

#can drop the first column here, or wait for the notebooks
#data.drop(data.columns[0], axis=1, inplace=True) # drop the first column

#ap3diagnosis = int(input("enter the AP3 diagnosis number \n"))
#use the line above if you want user input (and comment out the next line), else use
#ap3diagnosis = 401403
ap3diagnosis = 102

#use this line if you get user input
#data_ap3= data[(data.ap3diag==ap3diagnosis)]

#if you want multiple ap3's, enter them here
##mult_ap3=[401,403]
mult_ap3=[102]
#sub_code=[102.02] - doesn't work
data_ap3 = data[data.ap3diag.isin(mult_ap3)]
#data_ap3 = data[data.ap3diag.isin(mult_ap3)] & ~data[data.ap3_subcode.isin(sub_code)] doesn't work mixed types

# have worked out how to use more than 1 number (yeah!) - it is needed (e.g. all the sepsis diagnoses)

data_ap3.shape

#print out with file named from ap3diagnosis above

NewOutputFile="ap3subset"+str(ap3diagnosis)+".csv"
print (NewOutputFile)
data_ap3.to_csv(NewOutputFile.format(data_ap3.shape[0]), index=False)
#output is ap3subset401403.csv

#this excludes a sub-diag. Uses a number (seen as float)
sub_code=102_02
data_ap3sub = data_ap3[data_ap3.ap3_subcode !=102.02] 
NewOutputFile2="ap3subset"+str(ap3diagnosis)+"_" +str(sub_code)+".csv"
print (NewOutputFile2)
data_ap3sub.to_csv(NewOutputFile2.format(data_ap3sub.shape[0]), index=False)