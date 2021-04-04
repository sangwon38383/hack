from selenium import webdriver
from selenium.webdriver.common.by import By 
import pandas as pd
import numpy as np  
import csv 
import torch 
import torch.nn as nn 
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader
import FinanceDataReader as fdr  
import time
#from .text_analysis import *

spr = fdr.StockListing('S&P500')
spr_key = spr['Symbol'].drop([0])


finance_data = pd.Series([])
rating_data = pd.Series([])


for s in spr_key:    
    url = 'https://finviz.com/'
    driver = webdriver.Chrome('/Users/sangwon/Downloads/chromedriver') 
    driver.get(url) 
    time.sleep(5)
    driver.find_element_by_xpath("//input[@placeholder='Search ticker, company or profile']").send_keys(s)   
    driver.find_element_by_xpath("//span[@class='fa fa-search']").click()
    time.sleep(5)
    tbl = driver.find_element(By.CLASS_NAME, 'snapshot-table2').text
    cand = tbl.split()
    
    if cand[cand.index('ROE')+1] != 'ROI':
        roe = cand[cand.index('ROE')+1]
        roe = roe.split('%')
        roe = roe[0]
    else:
        fin = pd.Series(['Nan'])
        finance_data = finance_data.append(fin)
        continue 

    if cand[cand.index('ROA')+1] != 'ROE':
        roa = cand[cand.index('ROA')+1]
        roa = roa.split('%')
        roa = roa[0]
    else:
        fin = pd.Series(['Nan'])
        finance_data = finance_data.append(fin)
        continue

    if cand[cand.index('Debt/Eq')+1] != 'LT':
        debt_eq = cand[cand.index('Debt/Eq')+1]
        
    else:
        fin = pd.Series(['Nan'])
        finance_data = finance_data.append(fin)
        continue

    if cand[cand.index('LT')+2] != 'SMA20':
        lt_debt_eq = cand[cand.index('LT')+2]
        
    else:
        fin = pd.Series(['Nan'])
        finance_data = finance_data.append(fin)
        continue

    fin = [roe, roa, debt_eq, lt_debt_eq]

    print(fin)
    fin = pd.Series([fin]) 
    finance_data = finance_data.append(fin)
    print(finance_data)

finance_data.to_csv("./findata_micro, header=False, index=False")

#신용평가 - S&P에서 수집

for s in spr_key:
    try:     
        url = 'https://www.standardandpoors.com/en_US/web/guest/home'
        driver = webdriver.Chrome('/Users/sangwon/Downloads/chromedriver')
        driver.get(url)
        time.sleep(5)
        driver.find_element(By.ID, "searchTerm").send_keys(s)
        driver.find_element(By.ID, "findEntities").click()
        time.sleep(5)
        driver.find_element(By.ID, '_oamloginportlet_WAR_rdsmregistrationportlet_email').send_keys('sangwon38383@snu.ac.kr')
        driver.find_element(By.ID, '_oamloginportlet_WAR_rdsmregistrationportlet_password').send_keys('Tkddnjs95!')
        driver.find_element(By.ID, 'submitForm').click()
        rate = driver.find_element(By.CLASS_NAME, 'rating').text.split('\n')[0]
        rate = pd.Series([rate])
        rating_data = rating_data.append(rate)
    except:
        rate = pd.Series(['Nan'])
        rating_data = rating_data.append(rate)


fin_data = pd.Series([])
rat_data = pd.Series([])


for i in range(len(spr_key)):
    if finance_data[i] != 'Nan' and rating_data[i] != 'Nan':
        fin_data = fin_data.append(pd.Series([finance_data[i]]))
        rat_data = rat_data.append(pd.Series([rating_data[i]])) 


#rate을 수치로 바꾸어 줌
rat_data[(rating_data == 'AAA')] = 21
rat_data[(rating_data == 'AA+')] = 20
rat_data[(rating_data == 'AA')] = 19
rat_data[(rating_data == 'AA-')] = 18
rat_data[(rating_data == 'A+')] = 17
rat_data[(rating_data == 'A')] = 16
rat_data[(rating_data == 'A-')] = 15
rat_data[(rating_data == 'BBB+')] = 14
rat_data[(rating_data == 'BBB')] = 13
rat_data[(rating_data == 'BBB-')] = 12
rat_data[(rating_data == 'BB+')] = 11
rat_data[(rating_data == 'BB')] = 10
rat_data[(rating_data == 'BB-')] = 9
rat_data[(rating_data == 'B+')] = 8
rat_data[(rating_data == 'B')] = 7
rat_data[(rating_data == 'B-')] = 6
rat_data[(rating_data == 'CCC+')] = 5
rat_data[(rating_data == 'CCC')] = 4
rat_data[(rating_data == 'CCC-')] = 3
rat_data[(rating_data == 'CC')] = 2
rat_data[(rating_data == 'C')] = 1
rat_data[(rating_data == 'D')] = 0


data = torch.Tensor(fin_data)
labels = torch.Tensor(rat_data) 


len_comp_list = len(fin_data) 


#임시로 2019년 데이터만 사용  
macro_data = pd.read_excel('./macro_data.xlsx') 
macro_data = macro_data['Unnamed: 11'].drop([0, 9])
for m in macro_data:
    data = torch.cat((data, torch.Tensor([m]*len_comp_list)), dim=1)
data_dim = macro_data = macro_data['Unnamed: 11'].drop([0, 9]) 




class MsDataset(Dataset):
    def __init__(self, data, labels):
        self.data = data
        self.labels = labels

    def __len__(self):
        return len(self.data) 

    def __getitem__(self, i):
        return (self.data[i], self.labels[i])


dataset = MsDataset(data, labels)
dataloader = DataLoader(dataset = dataset, batch_size = 32)


class DataModel(nn.Module):
    def __init__(self):
        super(DataModel, self).__init__()
        self.fc1 = nn.Linear()
        self.fc2 = nn.Linear()

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = self.fc2(x)


model = DataModel()
model.train().cuda()


epoch = 3

criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr = 0.001, momentum = 0.9)

for e in range(epoch):
    for data, labels in dataloader:
        optimizer.zero_grad()
        data = data.cuda()
        labels = labels.cuda()

        logit = model.forward(data)
        loss = criterion(logit, labels)
        loss.backward()
        optimizer.step()


torch.save({'model':model}, './save_model')


