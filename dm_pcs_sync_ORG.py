from datetime import datetime
# datetime object containing current date and time
now = datetime.now()
#print("now =", now)  dd/mm/YY H:M:S
dt_string = now.strftime("%d%m%Y_%H:%M:%S")

print(f'DM_PCS update initialized at {now}')

import pandas as pd
import numpy as np
from pathlib import Path

#Dev tools path
#Path(r"C:\Users\Kyle\CKC Advisors\CKC Sharept Dev - Documents\Sharepoint Project")
#print("dev tools path: " + devTools_path)

#Lookup from/source WB
source_wb = (r'C:\Users\Kyle\CKC Advisors\CKC Sharept Dev - Documents\Sharepoint Project\Lists_Live\DataMap_Excel.xlsx')
A = source_wb

#Lookup/write to workbook
look_through_wb = source_wb
B = look_through_wb
Output_WB = (r'C:\Users\Kyle\CKC Advisors\CKC Sharept Dev - Documents\Sharepoint Project\PythonApps\DataMap\OutputDM_PCS.xlsx')

#Initial is the sheet we are looking IN TO FIND something
df_initial = pd.read_excel(B,sheet_name = 'DM_PBI',skiprows=8) #where you want to replace values
#Info is our source wb with the key/dictionary value that we lookup against
df_info = pd.read_excel(A,sheet_name = 'PCS') #where you want the source of the replacement to come from

#print(df_initial.columns) #Data Map
#print(df_info.columns) #PCS sheet
 
#change col name - This step ONLY NEEDED if col headings don't match
#rename the column in the initia/ref workbook to match the col in the info WB
key_col = 'PCSID' #this is the columb being replaced
replace_col_name = 'PCS_ClientID' #this is the column with the key value we are looking up
df_initial.rename(columns={replace_col_name:key_col}, inplace=True)
#print(df_info.columns)

#Key/match_col = the col with the match in the search WB
match_col = key_col
#target/ret_value_col = the col whos value we are getting back when a match is found
ret_value_col = 'PCS Name'
#on is a REQUIRED keyword, the on/merge field is the field that matches so that is why we can merge it
#merge_col = lookup Wb col and search Wb col with the matching values
merge_col = key_col
df_3 = pd.merge(df_initial, df_info[[match_col,ret_value_col]],on=merge_col,how='left')
#print(df_3[[match_col,ret_value_col,merge_col]])

#rename col heading
#df_3.rename(columns={ret_value_col + '_y':ret_value_col},inplace = True)
#Back to original value
df_3.rename(columns={key_col:replace_col_name}, inplace=True)
#df_3.rename(columns={ret_value_col:'PCS_ClientName'}, inplace=True)
#ret_value_col = 'PCS_ClientName'
#copy_name = 'lookup_copy'
#df_3.rename(columns={replace_col_name:copy_name}, inplace=True)

#replace nan values
df_3 = df_3.replace(np.nan,'', regex = True)
#print(df_3.columns)

#print new values
#print(df_3[[replace_col_name,ret_value_col]])

df_print = df_3[[replace_col_name,ret_value_col]]

#newoutput File name
#file_out = Output_WB
print(df_print)

#output file execution
#df_print.to_excel(file_out, index=False)

