"""
Created on Mon Sep 25 00:32:40 2017
@author: mahmoud
"""


import numpy as np  #mathematical tools"""
import matplotlib.pyplot as plt  #sub library of matplotlib, help us plot nice charts"""
import pandas as pd 

#-- Importing the dataset

dataset = pd.read_csv('50_Startups.csv')

                                            # R&D Spend, Adminstration, Marking spend, State
X = dataset.iloc[:, :-1].values             # [ Lines , Columns ] of data set ':' means all , ':-1' means all columns except last one

                                            # Profit
y = dataset.iloc[:, 4].values               # 4 is the number of the column with R&D Spend being no. 0



#-- Encoding categorical data (words -> nums)
                                            #encode words like france,germany,spain in country column and yes,no in purschased column 
                                            #1st- encode countries turn them into 0  , 1, 2
                                            #2nd- it might consider it as 0 < 1 < 2 so we have to make another good way
                                            #3rd- will use Dummy variables, will turn country column into table for each country (3 tables) with 0 and 1 / 0 if its not this country, 1 if its this country
                                            
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelEncoder_X = LabelEncoder() #create object
X[:,3] = labelEncoder_X.fit_transform(X[:,3]) #apply this method on X all the lines and on its first column only then make all this = to our main X[:,0]

        # create X dummy variables, first France, 2nd Germany, 3rd Spain

onehotencoder = OneHotEncoder(categorical_features = [3]) #which column we would like to OneHotEncode
X = onehotencoder.fit_transform(X).toarray()


#-- Avoiding the Dummy Variable Trap [some librarys already takes care of it, put it to reminds you in future]
X = X[ :, 1:]  #removed the first column of X, 1: means take all columns of X start from index 1 which is the 2nd column



#-- Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split

                                             #test size is 20% of X and y
                                             #random_state we will have random results if we dont put it
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)


"""                    
#-- Feature Scaling
                    #we are scaling the age and salary becase they are not in the same level
                    #and sometimes we will need to do it for decreasing the run time like in decission tress it will run for a long time if we didn't do it
                    #we don't need to apply feature scaling to y for now bec. they are only 0 and 1

from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()                  #sc for scale, object of the class
X_train = sc_X.fit_transform(X_train)    #when applying scalling to your training set you have to fit the scalling set and then transform it
X_test = sc_X.transform(X_test)          #dont need to fit it bec. its alreay fit in train set
                        #All the Varibales will be from -1 to +1
"""

# Fitting Multiple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()      #create our object
regressor.fit(X_train, y_train)


# Predicting the Test set results
y_pred = regressor.predict(X_test)



