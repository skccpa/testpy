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
look_through_wb = (r'C:\Users\Kyle\CKC Advisors\CKC Sharept Dev - Documents\Sharepoint Project\Lists_SQLdb\SalesInv_DB_Excel.xlsx')
B = look_through_wb
Output_WB = (r'C:\Users\Kyle\CKC Advisors\CKC Sharept Dev - Documents\Sharepoint Project\PythonApps\Output.xlsx')

df_initial = pd.read_excel(B,sheet_name = 'All_TimeDB')
df_info = pd.read_excel(A,sheet_name = 'DM_PBI', skiprows=8)

#print(df_initial.columns)
#print(df_info.columns)
 
#change col name - This step ONLY NEEDED if col headings don't match
#df_initial.rename(columns={1:'CKC_ID'}, inplace=True)
#print(df_info.columns)

#Key/match_col = the col with the match in the search WB
match_col = 'PCS_ClientID'
#target/ret_value_col = the col whos value we are getting back when a match is found
ret_value_col = 'CKC_ClientID'
#on is a REQUIRED keyword, the on/merge field is the field that matches so that is why we can merge it
#merge_col = lookup Wb col and search Wb col with the matching values
merge_col = "PCS_ClientID"
df_3 = pd.merge(df_initial, df_info[[match_col,ret_value_col]],on=merge_col,how='left')
#print(df_3[[match_col,ret_value_col + '_y',merge_col]])

#rename col heading
df_3.rename(columns={ret_value_col + '_y':ret_value_col},inplace = True)

#replace nan values
df_3 = df_3.replace(np.nan,'', regex = True)

#print new values
print(df_3[[match_col,ret_value_col]])

df_print = df_3[[match_col,ret_value_col]]

from datetime import datetime
# datetime object containing current date and time
now = datetime.now()
#print("now =", now)
# dd/mm/YY H:M:S
dt_string = now.strftime("%d%m%Y_%H:%M:%S")
print("date and time =", dt_string)

#newoutput File name
file_out = Output_WB
print(file_out)

#output file execution
df_print.to_excel(file_out, index=False)

