<!-- Centered content -->
<div align="center">
  <!-- Image -->
  <img src="https://github.com/user-attachments/assets/aa697654-16be-4b74-9d79-e035dc95833d" alt="Image Description" width="300px">
  
  <!-- Title and Information -->
  <h1><strong>Artificial Intelligence (Lab)</strong></h1>
  <h2>Lab 04: Supervised Learning - Classification with k-NN and Decision Trees</h2>
  <p><strong>Hassaan Ali Bukhari</strong><br>2022654<br><strong>Cyber Security</strong></p>
  <br>
</div>

<!-- Separator -->

## Table of Contents
1. [Introduction](#introduction)
2. [Data Exploration and Preprocessing](#data-exploration-and-preprocessing)
3. [Implementing k-NN and Decision Trees](#implementing-knn-and-decision-trees)
4. [Model Evaluation](#model-evaluation)
5. [Visualization](#visualization)
6. [Source Code](#source-code)

## Introduction
In this lab, we aim to predict whether passengers survived the Titanic disaster using the k-Nearest Neighbors (k-NN) and Decision Tree algorithms. The model takes into account various factors such as age, gender, ticket class, and fare paid.

## Data Exploration and Preprocessing
### 1. Explore the Dataset
- Load the dataset and display the first few rows.
- Visualize the distribution of key features (like `Pclass`, `Age`, `Sex`, etc.).
- Check for any missing values or outliers.

### 2. Data Preprocessing
- Handle missing values by either filling them (e.g., with the median) or removing records with missing data.
- Encode categorical variables like `Sex` and `Embarked` into numerical values.
- Standardize or normalize the numerical features like `Age` and `Fare`.

## Implementing k-NN and Decision Trees
### 1. Model Training
- Split the dataset into training and testing sets (70% training, 30% testing).
- Implement the k-Nearest Neighbors (k-NN) algorithm and train the model using the training set.
- Implement a Decision Tree algorithm and train it using the same training set.

## Model Evaluation
### 1. Performance Metrics
- Use the test set to make predictions for both models.
- Evaluate the performance of each model using accuracy, precision, recall, and F1-score.
- Compare the results and discuss which model performed better.

## Visualization
### 1. Decision Boundaries
- Create visualizations to display the decision boundaries of both models (k-NN and Decision Tree) using two features from the dataset.
- Plot the data points along with the decision boundaries to show how each model classifies the data.

### 2. Performance Visualization
- Plot a bar chart showing the performance metrics (accuracy, precision, recall, F1-score) of both models for easy comparison.

## Source Code
The complete source code for this lab can be found in the following Jupyter Notebook:

[Hassaan_Ali_Bukhari_CS351L_Lab04.ipynb](https://github.com/B3TA-BLOCKER/CS-351L---AI-Lab-GitHub-Repository_2022654/blob/main/Lab%2004%3A%20Supervised%20Learning%20-%20Classification%20with%20k-NN%20and%20Decision%20Trees/Hassaan_Ali_Bukhari_CS351L_Lab04.ipynb)
