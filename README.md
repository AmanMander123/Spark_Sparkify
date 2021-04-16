# Sparkify Web App

## Project Definition

### Overview
The purpose of this app is to predict customer churn. A machine learning model is used to classify whether or not a user is at risk of churning. The dataset used to develop the machine learning model is provided by [Udacity](https://www.udacity.com/). The dataset is that of Sparkify - a music streaming service, similar to Spotify. The problem statement is similar to the one in [this article](https://addepto.com/machine-learning-predict-reduce-customer-churn/).

### Problem Statement
The problem that is being solved in this case is determining whether or not a particular user is at risk of churning. In order to accomplish this, the following tasks are performed:
1. Data Loading
2. Data Cleaning
3. Exploratory Data Analysis
4. Feature Engineering
5. Baseline Model Development
6. Hyperparameter tuning 
7. Model Evaluation

### Metrics
The evaluation metric used to measure model performance is the f1-score. This is because this is a classification problem and dataset is imbalanced, thus the f1-score would be the most appropriate metric in this scenario. 

## Analysis

### Data Exploration
The dataset that will be used to develop the model contains the following columns:
![image](https://user-images.githubusercontent.com/8799324/115024765-8773f400-9e8e-11eb-8cad-603aa9397fdd.png)
However, there are 8346 blank records for userId, thus those records are removed from the dataset. The number of males vs females seems to be fairly balanced (not confirmed through statistical significance) with the number of males being slightly larger than the number of females in the dataset. We also notice that California is the most popular state amongst the users in our dataset, followed by Texas and New York-New Jersey-Pennsylvania. The most common browser is Chrome, followed by Firefox, Safari and IE. The dataset also tells us that more users use Sparkify in the late-afternoon to evening hours as opposed to the morning hours. In the dataset used in this model, given that 173 users did not churn and only 52 churned, the dataset contains an (although not too extreme) imbalance. The churn rate in males is slightly higher (~26%) than in females (~19%), although it may or may not a statistically significant difference. The churn rate in the free level is slightly higher (~25%) than in the paid level (~17%), although it may or may not a statistically significant difference.

### Data Visualization
As mentioned above, the proportion of males vs females in this dataset is fairly similar, as demonstrated by the figure below:
![image](https://user-images.githubusercontent.com/8799324/115026143-24835c80-9e90-11eb-92b7-f071fa7946cd.png)
We can aslo see that users from California far outweigh the users from the other states:
![image](https://user-images.githubusercontent.com/8799324/115026265-4977cf80-9e90-11eb-80ae-7cd7d775e475.png)
From the plot below, we can see Sparkify's popularity based on the day of the week (more popular during the weekdays):
![image](https://user-images.githubusercontent.com/8799324/115026549-a07da480-9e90-11eb-8588-9a4092f5dea9.png)

## Conclusion

### Reflection
This project contained all of the aspects of a data science project. The process started from loading the data from a json file into a pyspark dataframe. Before the data can be used for any analysis, data cleansing was performed. During this step, the time column was converted into a more interpretable format by Python. The location was also split by city and state. It was interesting to see that these two fields were combined in the original dataset. An exploratory data analysis was then conducted in order to get a good understanding of the data before developing any models. From the exploratory data analysis, it was realized that there was a need for feature engineering. The purpose of the feature engineering step was to prepare the final features that would go into the model. After converting gender and latest level from categorical to numerical data, the modeling process begins. Three baseline models are created and one of them is selected for tuning (decision tree in this case). The tuning aspect was particularly challenging because of the long processing times.

### Improvement
There are several ways this analysis can be improved. Firstly, we can create more features to improve the performance of the model through more feature engineering. Also, during the hyperparameter tuning process, we can extend the range of the parameters with the trade off of longer processing times.

## Running the App 
- Install the requirements using the requirements.txt file
- Navigate to the Spark_Sparkify directory and run 'flask run'
- Follow the instructions on the terminal to run the web app

## Libraries Used
- Flask
- numpy
- pandas
- pyspark

## Files
- dtmodel/ - directory containing model binary files
- templates/index.html - landing page of the app
- templates/go.html - prediction page of the app
- Sparkify.ipynb - notebook containing data exploration and model development
- app.py - Flask app used to run the app
- requirements.txt - requirements file


## Acknowledgements
[Udacity](https://www.udacity.com/)  
[Pyspark Documentation](https://spark.apache.org/docs/0.9.0/index.html)  
[Flask Documentation](https://flask.palletsprojects.com/en/1.1.x/quickstart/)  


