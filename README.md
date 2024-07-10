# Project 4 Group 2

# Predicting Pet Adoption
Alexis Rojas

Katharina Sojka

Johanna Belmar

David Spir

https://www.kaggle.com/datasets/rabieelkharoua/predict-pet-adoption-status-dataset/data

Our goal is to determine the various factors that influence pet adoption in order to predict which 
pets are more likely to be adopted. This dataset is imperative in finding solutions focused on 
increasing pet adoption rates. Therefore, using machine learning to find predictions can be an 
important tool in finding these solutions.

## Dataset Description:
The Pet Adoption Dataset offers a thorough examination of the several variables that may affect a pet's chances of getting adopted from a shelter. This dataset contains comprehensive data on pets that are up for adoption, encompassing a range of traits and qualities.

## Questions:
1. How can we predict the adoption likelihood using Machine Learning?
    - We will create an analysis of existing data to make a classification.
2. How do certain factors affect the likelihood of a pet getting adopted?
    - Analyzing the impact of various factors on adoption rates.
    - Hypothesis: If the pet has no health conditions and have been vaccinated, we believe that the pet will most likely be adopted.

### We will be using:

Python Pandas

Matplotlib

ML - Neural Network Models/Scikit-learn

SQL

# Overview 
The repository contains:

- the images of charts used for the powerpoint
- jupyter notebooks
  - Project4Group2Clean.ipynb 

    This notebook includes the cleaned data, bar charts depicting each category, health condition vs adoption likelihood catplots, the predictions, logistic regression model, random forest model and the feature importance.
  - Project_4_Group_2_Spark_SQL.ipynb

    This notebook includes the information using Spark in order to generate some predictions of certain outcomes/scenarios.
- random forest model saved as pkl file
- powerpoint presentation
- python app utilizing radom forest model to predict adoption likelihood
- csv files (original and transformed)
    

# Conclusion
Perfoming certain tasks like the logistic regression model, creating bar graphs for comparisons, the features importance graph, and using spark, gave us an insight on what certain factors owners look for in adopting. We noticed that certain factors such as medium sized pets, age in months, vaccinated/health conditions, etc. do take part in a pet's adoption likelihood. 
Using logistic regression model and random forest model, we found that our prediction was 91% and 93% accurate respectively. The precision score predicting whether the pet would be adopted or not were very similar. 
