

# 🏠 Real Estate Price Predictor

A machine learning project that predicts real estate prices based on property features using multiple regression models. This project compares the performance of **Linear Regression**, **Decision Tree Regressor**, and **Random Forest Regressor** using **MSE** and **RMSE** as evaluation metrics.

---

## 📌 Overview

The aim of this project is to build a price prediction engine for real estate properties using regression techniques. The models are trained on features like area, number of bedrooms, and location to estimate prices.

---

## 🧰 Tech Stack

- Python 3
- Pandas & NumPy
- Scikit-learn
- Matplotlib / Seaborn
- Jupyter Notebook

---

## 🧪 Dataset Features

 Attribute Information:

    1. CRIM      per capita crime rate by town
    2. ZN        proportion of residential land zoned for lots over 
                 25,000 sq.ft.
    3. INDUS     proportion of non-retail business acres per town
    4. CHAS      Charles River dummy variable (= 1 if tract bounds 
                 river; 0 otherwise)
    5. NOX       nitric oxides concentration (parts per 10 million)
    6. RM        average number of rooms per dwelling
    7. AGE       proportion of owner-occupied units built prior to 1940
    8. DIS       weighted distances to five Boston employment centres
    9. RAD       index of accessibility to radial highways
    10. TAX      full-value property-tax rate per $10,000
    11. PTRATIO  pupil-teacher ratio by town
    12. B        1000(Bk - 0.63)^2 where Bk is the proportion of blacks 
                 by town
    13. LSTAT    % lower status of the population
    14. MEDV     Median value of owner-occupied homes in $1000's

## 📊 Model Evaluation

The models are evaluated using:

- **MSE** (Mean Squared Error)
- **RMSE** (Root Mean Squared Error)

| Model              | Mean        | Standard.d   |
|-------------------|-------------|------------|
| Linear Regression |4.915287939  |  1.054306689  |
| Decision Tree     | 4.206183972 | 0.9184593664  |
| Random Forest     |  3.20410072|0.87125164162 |


-
##Add Frontend Part
This UI lets you input features like crime rate, number of rooms, tax rate, and more — and instantly predict the price of a home using a trained machine learning model.
--![Screenshot 2025-05-04 212414](https://github.com/user-attachments/assets/2706f6d4-2683-4fa8-99ce-a7c57910e86e)


## 🧱 Project Structure
![_- visual selection (1)](https://github.com/user-attachments/assets/1b5bb4bb-4c89-48da-8bb0-4bb2a80ecd87)

