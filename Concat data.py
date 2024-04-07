import pandas as pd
import glob
all_files = glob.glob("C:\\Users\\Admin\\Desktop\\Sem 221\\Discrete structures for computing\\Data\\*.xls")
output=pd.DataFrame()
for xlsfile in all_files: 
    df_sheet_index = pd.read_excel(xlsfile)
    # df_sheet_index = pd.read_excel('file1.xls', sheet_name=0)
    df=df_sheet_index.iloc[15:,2]
    df1=df_sheet_index.iloc[15:,3]
    data = pd.concat([df, df1], axis=1, join='inner')
    data = pd.concat([data, df_sheet_index.iloc[15:,8]], axis=1, join='inner')
    data = pd.concat([data, df_sheet_index.iloc[15:,11]], axis=1, join='inner')
    output = pd.concat([output,data])
# print(output)
# output.to_csv('out.csv',index=False,header=False)