import pandas as pd
import numpy as np
import array as arr

df = pd.read_excel('labeledDownRate.xlsx',sheet_name=0)
i=0
rate=0
ratestock=pd.DataFrame()
stock=pd.DataFrame()
last_index =0
tong=0.0 
avg=0.0
while (i <= 416):
    tong += df.Rate[i]
    print(tong)
    if(i==416):
        avg= tong/(i-last_index)
        last_index=i
        pd.concat(avg,ratestock)
        pd.concat(df.Sector[i],stock)
        break 
    if (df.Sector[i] != df.Sector[i+1]):
        avg= tong/(i-last_index)
        last_index=i
        pd.concat(avg,ratestock)
        pd.concat(df.Sector[i],stock)
        avg=0
        tong=0
    i = i+1 
output = pd.concat([stock,ratestock],axis=1, join='inner')

print(output)
# print(df)
# df.to_csv('VPB.csv',index=False,header=False)

# df = pd.read_csv('out.csv')
# df1 = df.iloc[::-1]

# print(df)
# df1.to_csv('out_reverse.csv',index=False,header=False)

