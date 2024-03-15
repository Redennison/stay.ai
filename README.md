# Customer Churn Prediction Model

## Overview

This TensorFlow-based neural network model predicts potential customer churn for a bank. It leverages customer data to forecast the likelihood of customers leaving the bank. The model utilizes preprocessing techniques like encoding and feature scaling, and constructs a simple artificial neural network (ANN) with two hidden layers.

## Data Preprocessing

- **Encoding Categorical Data**: Categorical variables such as "Gender" and "Geography" are encoded to numeric values to be fed into the model.
- **Feature Scaling**: StandardScaler is applied to ensure all features contribute equally to the model performance.

## Model Architecture

- The model is initialized as a sequential model in TensorFlow.
- Two hidden layers are added, each with 6 units and ReLU activation.
- The output layer uses a sigmoid activation function, suitable for binary classification tasks.

## Compilation and Training

- The model is compiled with the Adam optimizer and binary crossentropy loss function.
- It is trained on the training set for 100 epochs with a batch size of 32.

## Evaluation

- The model's performance is evaluated using the test set.
- A confusion matrix and accuracy score are computed to assess its prediction capability.

## Requirements

- numpy
- matplotlib
- pandas
- tensorflow
- scikit-learn

## Usage

1. Import the necessary libraries and the dataset.
2. Encode the categorical variables.
3. Split the dataset into training and test sets.
4. Apply feature scaling.
5. Initialize the ANN, add layers, and compile the model.
6. Train the model on the training set.
7. Predict test set results and evaluate the model.

## Dataset Variables

- Independent Variables: CreditScore, Geography, Gender, Age, Tenure, Balance, NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary.
- Dependent Variable: Customer churn indicator (binary).

## Note

The dataset `Churn_Modelling.csv` must be present in the working directory for the code to run successfully. Ensure all prerequisite libraries are installed.
