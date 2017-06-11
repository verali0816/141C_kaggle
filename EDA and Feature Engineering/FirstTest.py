#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon May 22 17:54:23 2017

@author: wenqian
"""

import pandas as pd

train = pd.read_csv("/Users/wenqian/141C_kaggle/train.csv")

train.describe() #only for numerical, 38 columns
#get the dtypes of each column
train.dtypes
#get the dtype of each column
[train.iloc[:,i].apply(type).value_counts() for i in range(train.shape[1])]

#get the number of NAs in each column
train.isnull().sum()
#There are several columns with a lot of NAs, we can drop them.

p = len(train.columns)

#get the column names of NAs > 500
for i in range(p):
    if train.iloc[:,i].isnull().sum() > 500:
        print train.columns[i]
        
##Alley
##FireplaceQu
##PoolQC
##Fence
##MiscFeature

#Get the number of unique values of object columns
for i in range(p):
    if train.iloc[:,i].dtype == "object":
        print i, train.columns[i]
        print train.iloc[:,i].value_counts(dropna = False)