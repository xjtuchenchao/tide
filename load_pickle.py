import pickle

with open('lr_0.01_result.pkl', 'rb') as f:
    data = pickle.load(f)
print(data)