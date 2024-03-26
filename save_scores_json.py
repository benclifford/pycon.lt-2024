import json

high_scores = [("Sally", 107),
               ("Ben", 99),
               ("Philip", 78)]


with open("scores.json", "w") as f:
    json.dump(high_scores, f)
