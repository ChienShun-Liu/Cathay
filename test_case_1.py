import numpy as np
import os
import pandas as pd
import requests

#%% Import the test.json
response = requests.get("https://raw.githubusercontent.com/ChienShun-Liu/Cathay/main/input_json/test_1.json")
test_data = response.json()

#%% Separate the test.json
country      = test_data["鄉鎮市區"]
trans_target = test_data["交易標的"]
trans_date   = test_data["交易年月日"]

page         = test_data["頁數"]
every_page   = test_data["每頁筆數"]

#%% Import all data
os.chdir('data')
Column = pd.read_csv("a_lvr_land_a.csv")
Column = pd.DataFrame(Column).columns

tmp  = pd.read_excel("All_data.xlsx")
data = pd.DataFrame(tmp).values

os.chdir('..')
#%% Search the target data
word_input  = [country,trans_target,trans_date]
index_input = np.array([0,1,7])

tar_ind = np.array(range(len(data)))
data = data.T
for k in range(len(index_input)):
    if word_input[k] == "":
        continue
    test = data[index_input[k]][tar_ind]
    tmp_ind = np.array([i for i, e in enumerate(test) if e == word_input[k] ])
    tar_ind = tar_ind[tmp_ind]

data = data.T
tar_data = data[tar_ind]
tar_data = pd.DataFrame(tar_data, columns=Column)
#%% Save the target data as .csv
tar_data.to_csv('test_1.csv',index=False, header=True,encoding='utf-8-sig') 
