import joblib


passenger_class = int(input("Enter your passenger class: "))
gender = int(input("Enter your gender: "))
age = int(input("Enter your age: "))
fare = int(input("Enter your fare: "))
family_size = int(input("Enter the size of your family (including you): "))
cabin = int(input("Do you have a cabin? "))

model = joblib.load('LR-model.pkl')

prediction = model.predict([[passenger_class, gender, age, fare, family_size, cabin]])

print(prediction)
