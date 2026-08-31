🌱 Dry Bean Classification
--

Machine Learning-Based Classification of Dry Bean Varieties Using Geometric Measurement

A machine learning project that classifies 7 varieties of dry beans using 16 geometric measurements extracted from bean images. Multiple feature selection and dimensionality reduction techniques are evaluated and compared with a Support Vector Machine (SVM) classifier.

🚀 Live Demo
--

🌱 Try the Application

[Open the Live Streamlit Application](https://dry-bean-classification123.streamlit.app/)

The deployed application allows users to enter the geometric measurements of a dry bean and receive a predicted bean variety.

📌 Table of Contents
--

Project Overview

Objectives

Dataset

Bean Classes

Features

Methodology

Machine Learning Model

Experimental Results

Classification Report

Error Analysis

Streamlit Application

Project Structure

Technologies Used

Installation

Run the Application Locally

How to Use

Future Improvements

Conclusion

Author

📖 Project Overview
--

Dry beans are an important agricultural crop with several varieties that can have similar physical characteristics. Manual classification can be time-consuming and may be affected by human judgment.

This project develops an automated dry bean variety classification system using machine learning.

The system uses geometric measurements of bean samples as input and predicts one of seven bean varieties.

The project also investigates whether reducing the number of input features can maintain or improve classification performance.

🎯 Objectives
--

The main objectives of this project are:

Load and preprocess the Dry Bean dataset.

Perform exploratory data analysis.

Analyze the relationships between geometric features.

Train a baseline Support Vector Machine classifier using all features.

Apply different feature selection techniques.

Apply Principal Component Analysis (PCA).

Compare classification performance across different approaches.

Analyze classification errors using a confusion matrix.

Save the trained model and feature scaler.

Develop and deploy an interactive Streamlit application.

📊 Dataset
--

The project uses the Dry Bean Dataset from the UCI Machine Learning Repository.

Dataset: Dry Bean Dataset
Repository: UCI Machine Learning Repository
Number of instances: 13,611
Number of input features: 16
Number of classes: 7

Dataset Link

https://archive.ics.uci.edu/dataset/602/dry+bean+dataset

The dataset contains geometric measurements extracted from images of dry bean grains.

🌱 Bean Classes
--

The dataset contains seven different bean varieties:

Class

Description

BARBUNYA

Dry bean variety

BOMBAY

Dry bean variety

CALI

Dry bean variety

DERMASON

Dry bean variety

HOROZ

Dry bean variety

SEKER

Dry bean variety

SIRA

Dry bean variety

📐 Features
--

The classification system uses the following 16 geometric features:

No.

Feature

1

Area

2

Perimeter

3

Major Axis Length

4

Minor Axis Length

5

Aspect Ratio

6

Eccentricity

7

Convex Area

8

Equivalent Diameter

9

Extent

10

Solidity

11

Roundness

12

Compactness

13

Shape Factor 1

14

Shape Factor 2

15

Shape Factor 3

16

Shape Factor 4

🔬 Methodology

The overall workflow of the project is:

                 Dry Bean Dataset
                        │
                        ▼
              Data Loading & Cleaning
                        │
                        ▼
            Exploratory Data Analysis
                        │
                        ▼
                Train/Test Split
                        │
                        ▼
                 Feature Scaling
                        │
          ┌─────────────┼─────────────┐
          ▼             ▼             ▼
      All Features   Feature       PCA
                     Selection
          │             │             │
          │       ┌─────┼─────┐       │
          │       ▼     ▼     ▼       │
          │     ANOVA  MI    RF       │
          │       │     │     │       │
          └───────┴─────┴─────┴───────┘
                        │
                        ▼
                   SVM Classifier
                        │
                        ▼
              Performance Evaluation
                        │
                        ▼
                Error / Confusion
                    Analysis
                        │
                        ▼
                Model Serialization
                        │
                        ▼
                 Streamlit Web App
                        │
                        ▼
                    Deployment

🤖 Machine Learning Model
--

The final classifier is a Support Vector Machine (SVM).

The selected model configuration is:

SVC(C=10, gamma=0.1)

Before classification, the input features are standardized using:

StandardScaler()

The trained model and scaler are saved using joblib.

📈 Experimental Results
--

Baseline — All 16 Features

Metric

Score

Number of Features

16

Accuracy

92.73%

Precision

92.72%

Recall

92.73%

F1 Score

92.72%

Training Time

0.444 sec

ANOVA Feature Selection

Metric

Score

Number of Features

10

Accuracy

90.75%

Precision

90.85%

Recall

90.75%

F1 Score

90.76%

Training Time

0.4074 sec

Mutual Information

Metric

Score

Number of Features

10

Accuracy

90.64%

Precision

90.74%

Recall

90.64%

F1 Score

90.64%

Training Time

0.4029 sec

Random Forest Feature Selection

Metric

Score

Number of Features

10

Accuracy

90.78%

Precision

90.90%

Recall

90.78%

F1 Score

90.80%

Training Time

0.3699 sec

PCA

Metric

Score

Number of Components

10

Accuracy

92.73%

Precision

92.72%

Recall

92.73%

F1 Score

92.72%

Training Time

0.5045 sec

📊 Overall Comparison
--

Method

Features / Components

Accuracy

F1 Score

Training Time

All Features

16

92.73%

92.72%

0.444 s

ANOVA

10

90.75%

90.76%

0.4074 s

Mutual Information

10

90.64%

90.64%

0.4029 s

Random Forest Selection

10

90.78%

90.80%

0.3699 s

PCA

10

92.73%

92.72%

0.5045 s

🏆 Best Result
--

The All Features SVM and PCA-based SVM achieved the highest accuracy of:

92.73%

The baseline model using all 16 original features was selected as the final model because it provides excellent performance while retaining the original feature representation.

📋 Classification Report
--

The final SVM model achieved an overall accuracy of approximately 93% on the test set.

Class

Precision

Recall

F1-Score

Support

BARBUNYA

0.93

0.91

0.92

265

BOMBAY

1.00

1.00

1.00

104

CALI

0.94

0.94

0.94

326

DERMASON

0.91

0.93

0.92

709

HOROZ

0.96

0.95

0.96

386

SEKER

0.94

0.96

0.95

406

SIRA

0.88

0.87

0.87

527

Overall Accuracy





0.93

2723

🔎 Error Analysis
--

The confusion matrix was analyzed to identify the most common classification error.

Most Frequent Misclassification

Actual Class     : SIRA
Predicted Class  : DERMASON
Number of Cases  : 51

This indicates that SIRA and DERMASON have relatively similar geometric characteristics, making them more difficult for the classifier to distinguish.

Error analysis can help identify areas where additional features or more advanced models could improve performance.

🖥️ Streamlit Application
--

An interactive web application was developed using Streamlit.

Application Features
--

🌱 User-friendly interface

📏 Input fields for all 16 geometric measurements

🤖 Trained SVM model

📊 Model performance information

🔍 Real-time bean variety prediction

📐 Feature information

📱 Browser-based interface

☁️ Cloud deployment

📁 Project Structure
--

Dry_Bean_Classification/
│
├── data/
│   └── Dry_Bean_Dataset.xlsx
│
├── models/
│   ├── dry_bean_model.pkl
│   └── scaler.pkl
│
├── notebooks/
│   ├── dry_bean_analysis.ipynb
│   ├── confusion_matrix.png
│   ├── feature_importance.png
│   └── feature_selection_results.csv
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore

🛠️ Technologies Used

Programming Language

Python

Data Processing

Pandas

NumPy

Data Visualization

Matplotlib

Seaborn

Machine Learning

Scikit-learn

Support Vector Machine (SVM)

StandardScaler

ANOVA

Mutual Information

Random Forest Feature Selection

Principal Component Analysis (PCA)

Model Deployment

Streamlit

Streamlit Community Cloud

Model Serialization

Joblib

Development Environment

Visual Studio Code

Jupyter Notebook

Git

GitHub

⚙️ Installation
--
1. Clone the Repository

git clone https://github.com/rahulnongmeikapam/dry-bean-classification.git
cd dry-bean-classification

2. Create a Virtual Environment

python -m venv .venv

3. Activate the Virtual Environment

Windows PowerShell

.venv\Scripts\Activate.ps1

4. Install Dependencies

pip install -r requirements.txt

▶️ Run the Application Locally

Start the Streamlit application using:

python -m streamlit run app.py

The application will open in your browser.

🧪 How to Use
--

Open the Streamlit application.

Enter the 16 geometric measurements of a dry bean.

Click "Predict Bean Variety".

The trained SVM model processes the input.

The application displays the predicted bean variety.

📌 Example Prediction
--
The model accepts measurements such as:

Area
Perimeter
Major Axis Length
Minor Axis Length
Aspect Ratio
Eccentricity
Convex Area
Equivalent Diameter
Extent
Solidity
Roundness
Compactness
Shape Factor 1
Shape Factor 2
Shape Factor 3
Shape Factor 4

The output is one of the seven bean varieties:

BARBUNYA
BOMBAY
CALI
DERMASON
HOROZ
SEKER
SIRA

🔮 Future Improvements
--
Possible future improvements include:

Hyperparameter optimization using GridSearchCV or RandomizedSearchCV

Testing additional classifiers such as Random Forest, XGBoost and MLP

Improving SIRA vs DERMASON classification

Adding probability/confidence estimates

Adding interactive visualizations to the Streamlit dashboard

Implementing automated data validation

Adding model explainability using SHAP

Improving UI/UX of the web application

Adding automated testing

Containerizing the application with Docker

✅ Conclusion
--
This project demonstrates how statistical pattern recognition and machine learning can be applied to classify dry bean varieties using geometric measurements.

The final SVM classifier achieved 92.73% accuracy using all 16 features. PCA achieved the same accuracy with 10 components, while the feature-selection techniques reduced accuracy slightly.

The trained model was integrated into an interactive Streamlit application and deployed online, allowing users to perform real-time dry bean variety classification.

👨‍💻 Author
--
Rahul Nongmeikapam

Computer Science Engineering — Artificial Intelligence

Project

Dry Bean Classification using Machine Learning

⭐ Acknowledgements
--
UCI Machine Learning Repository for providing the Dry Bean Dataset.

Scikit-learn for machine learning algorithms and evaluation tools.

Streamlit for application development and deployment.

📄 License

This project is intended for educational and academic purposes.
