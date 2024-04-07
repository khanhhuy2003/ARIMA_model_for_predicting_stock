import pandas as pd
import glob
all_files = glob.glob("/Users/mac/Desktop/untitled folder/7/*.xls")
output=pd.DataFrame()
for xlsfile in all_files: 
    df_sheet_index = pd.read_excel(xlsfile)
    # df_sheet_index = pd.read_excel('file1.xls', sheet_name=0)
    df=df_sheet_index.iloc[8:,2]
    df1=df_sheet_index.iloc[8:,3]
    data = pd.concat([df, df1], axis=1, join='inner')
    data = pd.concat([data, df_sheet_index.iloc[8:,8]], axis=1, join='inner')
    data = pd.concat([data, df_sheet_index.iloc[8:,11]], axis=1, join='inner')
    output = pd.concat([output,data])
# print(output)
output.to_csv('out.csv',index=False,header=False)



# df.to_csv('VPB.csv',index=False,header=False)
    


# df_sheet_index = pd.read_excel('file1.xls', sheet_name=0)
# df=df_sheet_index.iloc[15:,2]
# df1=df_sheet_index.iloc[15:,3]
# data = pd.concat([df, df1], axis=1, join='inner')
# data = pd.concat([data, df_sheet_index.iloc[15:,8]], axis=1, join='inner')
# data = pd.concat([data, df_sheet_index.iloc[15:,11]], axis=1, join='inner')
# data.to_csv('out.csv',index=False,header=False)

# df2=df_sheet_index.iloc[17:,4]
# df3=df_sheet_index.iloc[17:,3]

# data = pd.concat([df, df1], axis=1, join='inner')

# df3 = pd.concat([df, df1])
# print(df1)


# df_sheet_index = pd.read_excel('file1.xls', sheet_name=2)
# df=df_sheet_index.iloc[2:,0]
# df1=df_sheet_index.iloc[2:,1]
# df2 = pd.concat([df, df1], axis=1, join='inner')
# df3 = pd.concat([df, df1])


