import pandas as pd
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split


student_data = {
    "study_hours": [2, 5, 7, 3, 6, 8, 4, 1, 9, 5],
    "attendance": [65, 78, 88, 70, 82, 90, 75, 60, 95, 80],
    "previous_mark": [55, 64, 75, 58, 70, 85, 62, 50, 92, 68],
    "final_marks": [58, 72, 84, 62, 78, 90, 68, 52, 95, 74],
}




# Question 1: Create and Inspect the DataFrame



df = pd.DataFrame(student_data)

print(df)

print("\nFirst Five Rows")
print(df.head())

print("\nShape of DataFrame")
print(df.shape)

print("\nDescriptive Statistics")
print(df.describe())




# Question 2: Select Features and Label

X = df[["study_hours", "attendance", "previous_mark"]]
y = df["final_marks"]

print("\nFirst Five Rows of X")
print(X.head())

print("\nFirst Five Rows of y")
print(y.head())
# X contains input features used for prediction.
# y contains the target value (label) that we want to predict.



# Question 3: Train a Linear Regression Model


model = LinearRegression()
model.fit(X, y)

print("\nLinear regression model trained")




# Question 4: Predict a New Student's Marks



new_student = pd.DataFrame({
    "study_hours": [6],
    "attendance": [82],
    "previous_mark": [70]
})

predicted_mark = model.predict(new_student)

print("\nPredicted Final Mark:")
print(round(predicted_mark[0], 1))




# Question 5: Inspect Model Coefficients


print("\nModel Coefficients")
print(model.coef_)




# Question 6: Pass/Fail Classification


df["result"] = (df["final_marks"] >= 70).astype(int)

y_class = df["result"]

log_model = LogisticRegression(max_iter=1000)
log_model.fit(X, y_class)

prediction = log_model.predict(new_student)

print("\nPass/Fail Prediction")
print("Prediction Number:", prediction[0])

if prediction[0] == 1:
    print("Meaning: Pass")
else:
    print("Meaning: Fail")


# Question 7: Train-Test Split


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42,
)

print("\nTraining Rows:", len(X_train))
print("Testing Rows:", len(X_test))


# Question 8: Evaluate Regression Model


test_model = LinearRegression()
test_model.fit(X_train, y_train)

y_pred = test_model.predict(X_test)

print("\nActual Test Values")
print(y_test.values)

print("\nPredicted Values")
print(y_pred)

mean = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nMAE:", round(mean, 2))
print("R2 Score:", round(r2, 2))
