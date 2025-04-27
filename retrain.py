import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV, StratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import (accuracy_score, precision_score, 
                            recall_score, f1_score, roc_auc_score,
                            confusion_matrix, ConfusionMatrixDisplay)
from sklearn.feature_selection import SelectKBest, f_classif
import matplotlib.pyplot as plt
import joblib
import os

# --------------------------------------------
# 1. dataset
df = pd.read_csv("data/fake_news_dataset_modified.csv") 
# --------------------------------------------
# PREPROCESSING
# --------------------------------------------
#elimino los NaN
df = df.dropna()

#creamos x y a y
y = df["label"]
X = df.drop(["id",  "label","title","author","text","state","date_published","source","category","political_bias","fact_check_rating"], axis=1)

#verifico valores nulos
print("\nValores nulos en x")
print(X.isnull().sum())

print("Tipos de datos en X:")
print(X.dtypes)

print("\nPrimeras filas de X:")
print(X.head())

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#20% datos para prueba
# --------------------------------------------
# PIPELINE, normaliza los datos y utilizamos modelo de regresión logística
# --------------------------------------------
pipeline = Pipeline(steps=[
    ('scaler', StandardScaler()),
    ('classifier', LogisticRegression())
])

# --------------------------------------------
# HYPERPARAMETER OPTIMIZATION
# --------------------------------------------
param_grid_logreg = {
    'classifier__C': [0.1, 1, 10, 100]
}

# --------------------------------------------
# TRAINING
# --------------------------------------------
grid_search_log_reg = GridSearchCV(pipeline, param_grid_logreg, cv=5, n_jobs=-1,error_score='raise')
grid_search_log_reg.fit(X_train, y_train)

# --------------------------------------------
# BEST MODEL SELECTION
# --------------------------------------------
best_params = grid_search_log_reg.best_params_
best_model = grid_search_log_reg.best_estimator_
coefficients = best_model.named_steps['classifier'].coef_[0]
feature_names = X_train.columns

plt.figure(figsize=(10, 6))
plt.barh(feature_names, coefficients, color='skyblue')
plt.xlabel('Coeficiente')
plt.title('Importancia de las características en el modelo de regresión logística')
plt.savefig("feature_importance.png", dpi=120)
plt.close()

# --------------------------------------------
# METRICS
# --------------------------------------------
y_pred = best_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

with open("metrics.txt", 'w') as outfile:
    outfile.write("Training accuracy: %2.1f%%\n" % accuracy)

# --------------------------------------------
# SERIALIZING
# --------------------------------------------
os.makedirs('model', exist_ok=True)
model_filename = 'model/logistic_regression_model.pkl'
joblib.dump(best_model, model_filename)

print("----- The train process finished -----")


