import pandas as pd
import numpy as np
import os


class GoogleDB:
    def __init__(self,inputName,path):
        self.inputName=inputName
        self.path=path

    def merage(self):
        dataGoogleApi=pd.read_csv(self.path+'GoogleApi/'+self.inputName+'.csv')
        dataGoogleInfo=pd.read_csv(self.path+'GoogleInfo/'+self.inputName+'.csv')
        dataGoogle=pd.merge(dataGoogleApi,dataGoogleInfo,on='placeid')
        if os.path.isdir(self.path+'merage/'):
            pass
        else:
            os.makedirs(self.path+'merage/')
        dataGoogle.to_csv(self.path+'merage/'+self.inputName+'.csv')
        dataGoogle.columns=['from', 'icon', 'id', 'lat', 'lon', 'name', 'placeid', 'price',
           'rating', 'type', 'user_ratings_total', 'vicinity', 'url',
           'googletype', 'imageUrl', 'opentime', 'phone', 'ray', 'review',
           'webUrl']
        return dataGoogle

    
class CheckFood:
    def __init__(self,foodTypes,notTypes,data):
        self.foodTypes=foodTypes
        self.notTypes=notTypes
        self.data=data
###   檢查是否存在上述的foodtypes， 如果存在於nottypes 將會去除  避免ㄧ些怪怪的
###   set like private to use 
    def _check(self,onetype,types):
        boFood=False
        for t in types:
            if(t in onetype):
                boFood=True
                break
        return boFood

##### 滿足 googletype  為上述的成分
#### 滿足 types 裡面有 food 的因子o
    def get_check(self):
        data=self.data
        boCheck=[]
        for i,j in zip(data['googletype'],data['type']):
            boTmp=False
            if('food' in str(j)):
                boTmp=True
            if(self._check(str(i),self.foodTypes)):
                boTmp=True
            if(self._check(str(i),self.notTypes)):
                boTmp=False
            boCheck.append(boTmp)
        return data[boCheck].reset_index(drop=True)
