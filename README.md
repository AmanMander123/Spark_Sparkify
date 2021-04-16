# Sparkify Web App

## Overview
The purpose of this app is to predict churn. A machine learning model is used to classify whether a user is at risk of churning. The dataset used to develop the machine learning model is provided by [Udacity](https://www.udacity.com/). The dataset is that of Sparkify - a music streaming service, similar to Spotify. The problem statement is similar to the one in [this article](https://addepto.com/machine-learning-predict-reduce-customer-churn/).

## Problem Statement
The problem that is being solved in this case is determining whether or not a particular user is at risk of churning. In order to accomplish this, the following tasks are performed:
1. Data Loading
2. Data Cleaning
3. Exploratory Data Analysis
4. Feature Engineering
5. Baseline Model Development
6. Hyperparameter tuning 
7. Model Evaluation

## Metrics
The evaluation metric used to measure model performance is the f1-score. This is because this is a classification problem and dataset is imbalanced, thus the f1-score would be the most appropriate metric in this scenario. 

## Running the App 
- Install the requirements using the requirements.txt file
- Navigate to the Spark_Sparkify directory and run 'flask run'
- Follow the instructions on the terminal to run the web app
