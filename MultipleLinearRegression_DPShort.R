# Data Preprocessing

#-- Importing the dataset
dataset = read.csv('Data.csv')
#dataset = dataset[, 2:3] subset of it


#-- Taking care of missing data


#-- Encoding categorical data
                    #will use factor function 


#-- Splitting the dataset into the Training set and Test set

# install.packages('caTools') comment it just download it once
library(caTools)  #use the library by code or check it from packages tab 
set.seed(123)     #use seed to get same result, like we used random_state in python

split = sample.split( dataset$Purchased, SplitRatio = 0.8) #put only y in python we had to put X and y
                                                  #we hve to be careful in python we put the % of test set but here
                                                  #we have to put it for the train set
                                                  #will return true or false for each observation so each one will have true or false
                                                  #True observation goes to train set and False goes to test set

training_set = subset(dataset, split == TRUE)  #subset of Our dataset, who's values are TRUE
test_set = subset(dataset, split == FALSE)     #subset of Our dataset who's values are FALSE



#-- Feature Scaling                       #scale is already programmed function
{
training_set[, 2:3] = scale(training_set[,2:3])        #country and purschased are not numiric by default so we hve to specify the age and salary to scale them
test_set[, 2:3] = scale(test_set[, 2:3])
}


