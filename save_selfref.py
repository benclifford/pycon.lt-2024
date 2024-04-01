import pickle

a = []
a.append(a)

print(a)

with open("a_selfref.pkl", "wb") as f:
    pickle.dump(a, f)

