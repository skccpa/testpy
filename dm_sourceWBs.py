
import pandas as pd
import numpy as np
from pathlib import Path

source_wb = (r'C:\Users\Kyle\CKC Advisors\CKC Sharept Dev - Documents\Sharepoint Project\Lists_Live\DataMap_Excel.xlsx')
df_datamap = pd.read_excel(source_wb,sheet_name = 'DM_PBI',skiprows=8) #where you want to replace values

df_dm_ws_pcs = pd.read_excel(source_wb,sheet_name = 'PCS') #where you want the source of the replacement to come from
df_dm_ws_qbo = pd.read_excel(source_wb,sheet_name = 'QBO') #where you want the source of the replacement to come from

output_wb = Path('DataMap_Excel_PythFINAL.xlsx')

external_sync_dir = (r'C:\Users\Kyle\CKC Advisors\CKC Sharept Dev - Documents\DevToolsTemplates\SyncFiles')

#QBO clients sync
qbo_client_wb = (r'C:\Users\Kyle\CKC Advisors\CKC Sharept Dev - Documents\DevToolsTemplates\SyncFiles\Customers_QBO_SalesExport.xlsx')
qbo_customer_wb = (r'C:\Users\Kyle\CKC Advisors\CKC Sharept Dev - Documents\DevToolsTemplates\SyncFiles\QBO_Clients_SalesExport.xlsx')

#Time DB
qbo_customer_wb = (r'C:\Users\Kyle\CKC Advisors\CKC Sharept Dev - Documents\DevToolsTemplates\SyncFiles\QBO_Clients_SalesExport.xlsx')

