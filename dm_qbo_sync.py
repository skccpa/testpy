import pandas as pd
import numpy as np
from pathlib import Path

from dm_sourceWBs import df_dm_ws_pcs, df_dm_ws_qbo, df_datamap

#combine data map and QBO df
df1 = df_datamap
df2 = df_dm_ws_qbo 

df_initial = df1 #replace values here
df_info = df2 #lookup values here

print(df_initial.columns)
print(df_info.columns)
dm_replace_col = 'QBO_CustomerFullName'
replace_with_col = 'Customer FullName'

#change col name - This step ONLY NEEDED if col headings don't match
df_initial.rename(columns={dm_replace_col:replace_with_col}, inplace=True)

#Key/match_col = the col with the match in the search WB
match_col = 'Individual Client Name'
df_initial.rename(columns={'CKC_ClientLegalName':match_col}, inplace=True)
#target/ret_value_col = the col whos value we are getting back when a match is found
ret_value_col = 'Customer FullName'
#on is a REQUIRED keyword, the on/merge field is the field that matches so that is why we can merge it
#merge_col = lookup Wb col and search Wb col with the matching values
merge_col = "Individual Client Name"
df_3 = pd.merge(df_initial, df_info[[match_col,ret_value_col]],on=merge_col,how='left')
#print(df_3[[match_col,ret_value_col + '_y',merge_col]])

#rename col heading
#df_3.rename(columns={ret_value_col + '_y':ret_value_col},inplace = True)

#replace nan values
#df_3 = df_3.replace(np.nan,'', regex = True)

#print new values


