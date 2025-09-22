
# Customer Churn Prediction

This project analyzes customer data to predict churn using various classification models, including Logistic Regression, SVM, and Random Forest.

---

## 📊 Data Preprocessing

- Loaded and cleaned the dataset.
- Handled missing and duplicated values .
- Encoded categorical variables (e.g., Gender, Geography).
- Split the dataset into training and testing sets.
- Applied feature scaling using `MinaMaxScaler`.

---

## 🔍 Exploratory Data Analysis (EDA)

- Investigated churn distribution across features like `Gender`, `Age`, `Balance`, and `IsActiveMember`.
- Visualized relationships using:
  - Count plots
  - Pie charts
  - Histograms
  - Correlation heatmap

---

## 🤖 Modeling

Trained the following classification models:

1. **Logistic Regression**
   - Used to model binary classification with a probabilistic output.

2. **Support Vector Machine (SVM)**
   - Implemented with `rbf` kernel.

3. **Random Forest Classifier**
   - Ensemble model with multiple decision trees.
   - Visualized one of the decision trees from the forest.

---


## 📈 Model Evaluation

- Used the following metrics:
  - Accuracy
  - Confusion Matrix

## Model Accuracy Comparison

| Model                     | Accuracy |
|---------------------------|----------|
| Logistic Regression       | 0.80     |
| Support Vector Machine    | 0.86     |
| Random Forest             | 0.864    |
---

## 💾 Save Model

- Saved trained models using `joblib` for deployment.
- Example:
  ```python
  import joblib
  joblib.dump(svm_model, 'rf_churn_model.pkl')
  ```

---

## 📁 File Structure

```
├── churn_data.csv
├── churn_analysis.ipynb
├── README.md
└── svm_churn_model.pkl
```


