# Employee Attrition Prediction

## Description
A predictive analytics project for **TechNova Solutions**, designed to identify employees at risk of leaving using HR operational and survey data. It combines exploratory analysis, feature engineering, and machine learning (Logistic Regression with SMOTE) to support proactive retention strategies.

## Table of Contents
- [Built With](#built-with)
- [Getting Started](#getting-started)
- [Dataset](#dataset)
- [Features & Methods](#features--methods)
- [Modeling & Evaluation](#modeling--evaluation)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [Contact](#contact)

## Built With
- Python 3.9+
- pandas, numpy, scikit-learn, imbalanced-learn
- xgboost (for model comparison)
- matplotlib, seaborn for visualizations
- Jupyter Notebook for development

## Getting Started

### Prerequisites
```bash
pip install -r requirements.txt
```

## Dataset
The dataset includes **10,000 employee records** with 22 key attributes (Demographics, Performance, Workload, Engagement) and a binary target `Churn` (0 = Stayed, 1 = Left).  
Detailed description of each feature is available in the notebook.

## Features & Methods
- Exploratory analysis to understand attrition drivers
- Feature engineering including:
  - `Overtime_Ratio`, `Projects_Per_Year`, `Training_Intensity`, `Absenteeism_Rate`
  - Engagement metrics: `Engagement_Score`, `Promotion_Frequency`, `Workload_Balance`, `Training_x_Perf`
- Categorical encoding (`OneHotEncoder`), scaling (`StandardScaler`), and train/test split with stratification
- Imbalance handling using **SMOTE** and final model selection using **Logistic Regression (L1 regularized)**

## Modeling & Evaluation
**Final model:** Logistic Regression + SMOTE  
- Recall: ~54% (captures more than half of actual churners)  
- Precision: ~21%  
- Accuracy: ~49% (acceptable given class imbalance)  
- ROC-AUC: ~0.52  

**Key drivers of attrition:**  
- Workload imbalance, high project count, long commute  

**Key retention factors:**  
- Remote work, manager feedback, balanced training  

## Project Structure
```
├── data/
│   └── employee_churn_dataset.csv
│   └── employee_churn_data_dictionary.csv
├── notebooks/
│   └── TechNova_Attrition_Prediction_<your_id>.ipynb
├── README.md
└── requirements.txt
```