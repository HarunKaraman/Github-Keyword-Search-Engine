# -*- coding: utf-8 -*-
ACCESS_TOKEN = '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'
"""
Github Repo Search Engine

August 2021

@project manager : Seha Solakoğlu
@author          : Harun Karaman

"""
from pandas import DataFrame as df
from github import Github
import pyexcel_xlsx as excel
import datetime
import os
import time

TIMESTAMP = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

RESULTS = []

g = Github(ACCESS_TOKEN)

#print(g.get_user().get_repos())

def getwdandcwd():
    scriptcurrentdirectory = os.path.dirname(os.path.realpath(__file__))
    os.chdir(scriptcurrentdirectory)

def iteration():
    #try:
    x = 0
    y = 0
    for i in datakeywords['keywords']:
        x +=1
        print(x)
        if x > 10:
            #print('kural calisti')
            print(x)
            x=0
            time.sleep(63)
            search_github(i)
            y +=1
        else:
            #print('kural calismiyor')
            search_github(i)
            y +=1
        saving_results()
        print(y)
    #except:
    #    print("Error in iteration")

def search_github(keywords):
    query = '+'.join(keywords)
    result = g.search_repositories(query, 'stars', 'desc')
    print(f'Toplam {result.totalCount} REPO bulundu.')
    for repo in result:
        #print(repo.clone_url)
        RESULTS.append([TIMESTAMP,str.join(" - ", keywords),repo.clone_url])

def read_keywords(excelfilename):
    global datakeywords
    global totalcount
    datakeywords = excel.get_data(excelfilename)    
    totalcount = 0
    for value in datakeywords:
        value_list = datakeywords[value]
        count = len(value_list)
        totalcount += count
    print(totalcount)
    
def saving_results():
    try:
        print('Sonuçlar excel dosyasına aktarıldı.')
        final_data = df(RESULTS, columns=['TIMESTAMP','KEYWORD', 'REPO URL'])
        final_data.to_excel("results.xlsx",sheet_name='RESULTS')  
    except:
        print('File Saving Error!')

def start():
    print("Aranacak Keywordler excel dosyasından okunuyor.")
    read_keywords("keywords.xlsx")
    getwdandcwd()
    iteration()

if __name__ == "__main__":
    print("Github keyword arama scripti çalıştırıldı!")
    start()
