
import pandas as pd 
employee_attrition_data = pd.read_csv('Employee Attrition.csv')
employee_attrition_data.head()

employee_attrition_data.hist(figsize=(15,15)) 
plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt
import seaborn as sns
sns.kdeplot(employee_attrition_data.loc[employee_attrition_data['Attrition']== 'No', 'Age'],label = 'Active Employee')
sns.kdeplot(employee_attrition_data.loc[employee_attrition_data['Attrition'] == 'Yes', 'Age'], label = 'Ex-Employees')
plt.legend()
plt.show()

sns.boxplot(y=employee_attrition_data["MonthlyIncome"], x= employee_attrition_data["JobRole"])
plt.grid(True, alpha=1)
plt.tight_layout()
plt.show()

sns.catplot(x='JobRole', hue='Attrition', data=employee_attrition_data, kind ="count", height = 7, aspect=2, legend = False)
plt.legend(loc='upper right', title='Attrition') 
plt.tight_layout()
plt.show()

sns.catplot(x='JobRole', hue='OverTime', data=employee_attrition_data, kind ="count", height = 7, aspect=2, legend = False)
plt.legend(loc='upper right', title='Over Time') 
plt.tight_layout()
plt.show()

employee_attrition_data['Attrition'].value_counts().plot(kind='bar',color = '#ADD8E6')
plt.show()
employee_attrition_data.dtypes


for col in employee_attrition_data.columns:
	if employee_attrition_data[col].dtype =='object':
		employee_attrition_data[col]= employee_attrition_data[col].astype('category')
		employee_attrition_data[col] = employee_attrition_data[col].cat.codes



sns.heatmap(corr, vmax=.5, mask=mask, linewidths=.2, cmap="YlGnBu")

from sklearn.linear_model import LogisticRegression 
from plot_metric.functions import BinaryClassification as BC

employee_attrition_data = employee_attrition_data[(employee_attrition_data['Attrition']!=0)|(np.random.rand(len(employee_attrition_data))<.33)]
X = employee_attrition_data.drop('Attrition',axis=1) 
y = employee_attrition_data['Attrition']
# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, random_state=42, stratify=y)
# Data Normalization
scaler = MinMaxScaler(feature_range = (0,1))
scaler.fit(X_train)

X_train = scaler.transform(X_train) 
X_test = scaler.transform(X_test)


params = { 
		'solver': ['newton-cg', 'liblinear'],
		'penalty': ['l2'],
		'C': np.logspace(-4.5,4.5,50),
		'class_weight':['balanced'],
		'tol':[0.0001, 0.001, 0.01, 0.1],
		'fit_intercept':[True, False], 
		'intercept_scaling':[1, 2, 3]
}

# Initializing Grid Search with Logistic Regression and keeping roc_auc as the performance metric
grid_search = GridSearchCV(estimator = LogisticRegression(),
							param_grid=params, 
							cv = 5, n_jobs=-1, 
							verbose=0, scoring="roc_auc",
							return_train_score=True)

grid_search.fit(X_train, y_train)
 
print('='*20) 
print("best params: " + str(grid_search.best_estimator_)) 
print("best params: " + str(grid_search.best_params_)) 
print('best score:', grid_search.best_score_)
print('='*20)

from plot_metric.functions import BinaryClassification as BC 
y_pred = best_model.predict(X_test) 
bc = BC(y_test, y_pred)
# Plotting AUC_ROC Curve 
plt.figure(figsize=(8,6)) 
bc.plot_roc_curve()
plt.show()

print("The accuracy is {:.2f}".format(accuracy_score(y_test, y_pred)))
print("The balanced accuracy is {:.2f}".format(balanced_accuracy_score(y_test, y_pred)))
print("The recall is {:.2f}".format(recall_score(y_test, y_pred))) 
print("The precision is {:.2f}".format(precision_score(y_test, y_pred)))
print("The F1 Score is {:.2f}".format(f1_score(y_test, y_pred))) print("The AUC ROC Score is {:.2f}".format(roc_auc_score(y_test, y_pred)))


cm = confusion_matrix(y_test,best_model.predict(X_test))
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=classes)
fig, ax = plt.subplots(figsize=(7,7)) 
plt.title("Confusion Matrix") 
disp = disp.plot(ax=ax) 
plt.grid(None)
plt.show()