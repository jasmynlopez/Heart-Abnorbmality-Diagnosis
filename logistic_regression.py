import math
import numpy as np 
import pandas as pd

# Load files with option of including or excluding demographics 
def load(filename, include_demographics=True):
    df_x = pd.read_csv(f"{filename}")
    df_x.insert(0, "bias", 1)

    if not include_demographics:
       df_x = df_x.drop(columns=["Demographic"])
    
    df_y = df_x[df_x.columns[-1]]
    df_x = df_x.drop(columns = [df_x.columns[-1]])
    
    return [df_x, df_y]

# Helper function that calculates sigmoid of a value x
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


# Train
def train(df_x, df_y): 
    size = df_x.shape[1] 
    step_size = .00625
    theta_arr = np.zeros(size) 

    for i in range(100):  # Step size 1000
        gradient = np.zeros(size)
        
        for index, row in df_x.iterrows():
            for j in range(len(gradient)): # Iterating through the columns(features)
                dot = np.dot(theta_arr, row)
                gradient[j] += (row[j] * (df_y[index] - sigmoid(dot)))
        for j in range(len(gradient)): 
            theta_arr[j] += (step_size * gradient[j])
    return theta_arr 

# Make a prediction based on the weights and features
def predict(weight, features): 
    dot = np.dot(features, weight)
    sig = sigmoid(dot)
    prediction = np.zeros(len(features))

    for i in range(1, (len(features) + 1)): 
        val = sig[i - 1: i]
        if (val >= 0.5): 
            prediction[i - 1] = 1
        else: 
            prediction[i - 1] = 0
    return prediction

# Compute accuracy by comparing prediction to true value
def compute_accuracy(df_y, prediction): 
    correct = 0 
    total = len(prediction)
    for i in range(total): 
        if (prediction[i] == df_y[i]): 
            correct += 1
    return (correct / total)
        

def main(): 
    df_train = load("heart-train.csv", False)
    theta = train(df_train[0], df_train[1]) # Training

# Calculating log likelihood 
    df_x = df_train[0]
    df_y = df_train[1]
    ll = 0
    ll0 = 0
    theta0 = np.zeros(df_x.shape[1]) 
    print(theta)
    for index, row in df_x.iterrows(): 
        dot = np.dot(theta, row)
        dot0 = np.dot(theta0, row)
        sig = sigmoid(dot)
        sig0 = sigmoid(dot0)
        ll += ((df_y[index] * math.log(sig)) + ((1 - df_y[index]) * math.log(1 - sig)))
        ll0 += ((df_y[index] * math.log(sig0)) + ((1 - df_y[index]) * math.log(1 - sig0)))
    
    print("log likelihood before training" + str(ll0))
    print("log likelihood after training" + str(ll))

    train_prediction = predict(theta, df_train[0]) # Prediction Train
    compute_accuracy(df_train[1], train_prediction)
    train_accuracy = compute_accuracy(df_train[1], train_prediction) # Accuracy Train


    df_test = load("netflix-test.csv", False) # Load test
    test_prediction = predict(theta, df_test[0]) # Prediction Test
    compute_accuracy(df_test[1], test_prediction)
    test_accuracy = compute_accuracy(df_test[1], test_prediction) # Accuracy Test

    print("Training Accuracy : " + str(train_accuracy))
    print("Testing Accuracy : " + str(test_accuracy))

if __name__  == "__main__": 
    main()
