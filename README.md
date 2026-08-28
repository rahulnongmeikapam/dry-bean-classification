🌱 Dry Bean Classification System

A machine learning-based classification system that identifies seven
varieties of dry beans using 16 geometric measurements. The project
compares multiple feature selection and dimensionality reduction
techniques and deploys the final Support Vector Machine (SVM) model as
an interactive Streamlit web application.

🚀 Live Demo

Try the deployed application:
https://dry-bean-classification123.streamlit.app/

📌 Project Overview

The objective of this project is to develop an automated system capable
of classifying dry bean varieties based on geometric characteristics
extracted from bean images.

The project investigates whether feature selection and dimensionality
reduction techniques can improve or maintain classification performance
while reducing the number of input features.

The final model uses all 16 geometric features with a Support
Vector Classifier (SVC) and achieved an accuracy of 92.73% on the
test dataset.

🎯 Objectives

Classify dry beans into their respective varieties.

Perform data preprocessing and exploratory data analysis.

Train and compare multiple machine learning classifiers.

Evaluate different feature selection techniques.

Apply Principal Component Analysis (PCA) for dimensionality
reduction.

Compare model performance using accuracy, precision, recall,
F1-score, and training time.

Save the best-performing model and scaler.

Develop an interactive Streamlit application.

Deploy the application for public access.

📊 Dataset

The project uses the Dry Bean Dataset from the UCI Machine Learning
Repository.

The dataset contains 13,611 instances, 16 geometric features,
and 7 bean classes.

Bean varieties

BARBUNYA

BOMBAY

CALI

DERMASON

HOROZ

SEKER

SIRA

Features

The model uses the following geometric measurements:

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

Dataset source: UCI Machine Learning Repository --- Dry Bean Dataset.

🧠 Methodology

The overall workflow followed in the project is:

Dataset
   ↓
Data Loading
   ↓
Data Cleaning & Preprocessing
   ↓
Exploratory Data Analysis
   ↓
Train-Test Split
   ↓
Feature Scaling
   ↓
Baseline Classification
   ↓
Feature Selection
   ├── ANOVA
   ├── Mutual Information
   └── Random Forest Feature Selection
   ↓
Dimensionality Reduction
   └── PCA
   ↓
Model Evaluation
   ↓
Best Model Selection
   ↓
Model & Scaler Serialization
   ↓
Streamlit Application
   ↓
Cloud Deployment

🤖 Machine Learning Model

Several classification approaches were evaluated during the project.

The final deployed model is:

Support Vector Classifier (SVC)

Configuration:

SVC(C=10, gamma=0.1)

The model was trained using standardized feature values with
StandardScaler.

📈 Experimental Results

Baseline --- All 16 Features

Metric                     Result

Number of Features             16
Accuracy               92.73%
Precision              92.72%
Recall                 92.73%
F1 Score               92.72%
Training Time           0.444 sec

Feature Selection & PCA Comparison

Technique       Features /     Accuracy   Precision     Recall   F1 Score   Training
Components                                                      Time

All Features            16   92.73%      92.72%     92.73%     92.72%    0.444 s

ANOVA                   10       90.75%      90.85%     90.75%     90.76%    0.407 s

Mutual                  10       90.64%      90.74%     90.64%     90.64%    0.403 s
Information

Random Forest           10       90.78%      90.90%     90.78%     90.80%    0.370
s

PCA                     10   92.73%      92.72%     92.73%     92.72%    0.505 s

Key Finding

The baseline SVM using all 16 features achieved the highest overall
performance among the tested feature-selection approaches.

Interestingly, PCA reduced the representation to 10 components while
maintaining the same 92.73% accuracy.

🔍 Classification Performance

The final SVM achieved an overall accuracy of approximately 93% on
the test set.

Class-wise Performance

Bean Class     Precision   Recall   F1 Score

BARBUNYA            0.93     0.91       0.92
BOMBAY              1.00     1.00       1.00
CALI                0.94     0.94       0.94
DERMASON            0.91     0.93       0.92
HOROZ               0.96     0.95       0.96
SEKER               0.94     0.96       0.95
SIRA                0.88     0.87       0.87

The most frequent observed misclassification was:

SIRA → DERMASON: 51 cases

🖥️ Streamlit Application

The project includes an interactive web interface where users can enter
the 16 geometric measurements of a dry bean and receive a predicted bean
variety.

Application features

Interactive input fields

SVM-based prediction

Model information dashboard

Accuracy display

Predicted variety display

Feature information

Project description

Responsive two-column interface

Live Application

https://dry-bean-classification123.streamlit.app/

🛠️ Technologies Used

Programming Language

Python

Machine Learning

Scikit-learn

Support Vector Machine (SVM)

StandardScaler

PCA

ANOVA

Mutual Information

Random Forest

Data Processing

Pandas

NumPy

Visualization

Matplotlib

Seaborn

Deployment

Streamlit

Streamlit Community Cloud

Development Tools

Jupyter Notebook

Visual Studio Code

Git

GitHub

📁 Project Structure

dry-bean-classification/
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

⚙️ Installation & Local Setup

1. Clone the repository

git clone https://github.com/rahulnongmeikapam/dry-bean-classification.git
cd dry-bean-classification

2. Create a virtual environment

Windows:

python -m venv .venv

Activate it:

.venv\Scripts\activate

3. Install dependencies

pip install -r requirements.txt

4. Run the Streamlit application

python -m streamlit run app.py

The application will open in your browser.

📦 Model Files

The trained model and preprocessing scaler are stored using Joblib:

models/dry_bean_model.pkl
models/scaler.pkl

The Streamlit application loads these files and uses them to transform
user input and generate predictions.

📚 Research & Learning Outcomes

This project demonstrates practical implementation of:

Supervised machine learning

Multi-class classification

Feature scaling

Feature selection

Dimensionality reduction

Model evaluation

Confusion matrix analysis

Classification reports

Model serialization

Streamlit application development

Git/GitHub version control

Cloud deployment

🔮 Future Improvements

Possible future enhancements include:

Add probability/confidence scores for predictions.

Allow users to upload bean measurement files.

Add interactive charts to the Streamlit dashboard.

Compare additional classifiers such as Random Forest, KNN, MLP, and
Naïve Bayes.

Perform hyperparameter optimization using GridSearchCV or
RandomizedSearchCV.

Add automated model retraining.

Improve the UI with richer visualizations.

Add image-based dry bean classification using computer vision.

👨‍💻 Author

Rahul Nongmeikapam

Computer Science Engineering --- Artificial Intelligence

GitHub: https://github.com/rahulnongmeikapam

⭐ Acknowledgement

The project uses the Dry Bean Dataset provided by the UCI Machine
Learning Repository.

If you find this project useful, consider giving the repository a ⭐ on
GitHub.
