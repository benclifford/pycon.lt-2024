import pickle

high_scores = [("Sally", 107),
               ("Ben", 99),
               ("Philip", 78)]


with open("scores.pkl", "wb") as f:
    pickle.dump(high_scores, f)
