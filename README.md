# 🩺 Diabetes Analysis & Prediction

## 📌 Project Overview
This project analyzes the **Pima Indians Diabetes dataset** to explore risk factors for diabetes, perform data quality checks, and build predictive models.  
The best model (**Random Forest**) achieves **86% accuracy** and **0.90 AUC**, deployed via a **Streamlit app** for real-time prediction.

---

## 📂 Project Contents
- **Data Quality Report** – Detect hidden missing values (fake zeros), outliers, and skewness.  
- **Exploratory Data Analysis (EDA)** – Visualizations of glucose, BMI, age, and genetic predisposition.  
- **Modeling** – Comparison of Logistic Regression, Random Forest, SVM, KNN, and CART.  
- **Hyperparameter Tuning** – Optimized Random Forest as best-performing model.  
- **Deployment** – Streamlit app for interactive diabetes risk prediction.  

---

## 🔑 Key Insights
- **Glucose** is the strongest predictor of diabetes.  
- **BMI + Glucose** define a high-risk population.  
- **Age & Genetics (Pedigree Function)** are significant contributors.  
- **SMOTE** improved performance by addressing class imbalance.  

---


## 🖼️ Visualizations

* Outcome distribution (class imbalance)
* Glucose distribution by outcome
* BMI vs Age scatter (colored by outcome)
* Correlation heatmap
* Joint Glucose & BMI density

---

## 📊 Model Performance (After SMOTE)

| Model         | Accuracy |
| ------------- | -------- |
| Logistic Reg. | 0.755    |
| Random Forest | **0.86** |
| SVM           | 0.84     |
| KNN           | 0.786    |
| CART          | 0.774    |
✅ **Random Forest chosen as final model**.

---

## 📎 Dataset Reference

* **Pima Indians Diabetes Database** – [UCI Repository](https://archive.ics.uci.edu/ml/datasets/pima+indians+diabetes)

---

## 👨‍💻 Author

* **Ahmed Hamed**

 
