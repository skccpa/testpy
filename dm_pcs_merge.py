from datetime import datetime
# datetime object containing current date and time
now = datetime.now()
#print("now =", now)  dd/mm/YY H:M:S
dt_string = now.strftime("%d%m%Y_%H:%M:%S")

print(f'DM_PCS merge update initialized at {now}')

import pandas as pd
from pathlib import Path

#Lookup from/source WB
#source_wb = (r'C:\Users\Kyle\CKC Advisors\CKC Sharept Dev - Documents\Sharepoint Project\Lists_Live\DataMap_Excel.xlsx')

#Merge in wb
output_wb = Path('DataMap_Excel_PythFINAL.xlsx')
from dm_pcs_sync import df_initial, replace_col_name, df_print, ret_value_col
#output_wb = A

df1 = df_initial
df2 = df_print #output file from previous step

merge_name = replace_col_name

#org name from data map
#df2.rename(columns={replace_col_name:merge_name}, inplace =True)

#print(df1.columns)
#print(df2.columns)

df_merge = pd.merge(df1, df2, on=merge_name)
print(df_merge.columns)

#df_merge.rename(columns={'PCS_ClientName','Remove'},inplace = True)
#df_merge.rename(columns={ret_value_col,'PCS_ClientName'},inplace = True)

replace_values_col = 'PCS_ClientName'
df_merge[replace_values_col] = df_merge[ret_value_col]

print(df_merge[[replace_values_col]])

#write to excel specific wb
df_write_col = df_merge[[replace_values_col]]
#df_write_col.to_excel(output_wb,index=False)

#write to sheet
shName = 'DM_PBI'

#to column/row
df_merge.to_excel(output_wb,shName,index=False)


#replace values column to merge2
#merge_name2 = 'PCS_ClientName'
#df2.rename(columns={ret_value_col:merge_name2}, inplace=True)
#(df2,axis=0)
#print(df2)
#merge_2 = pd.merge(merge_1, df2,on=merge_name2)



#print(merge[[replace_col_name,ret_value_col]])

#df_print



