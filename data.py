import random
import json 

pie_counts = {
    "Fresh Produce":random.randint(1,20),
    "Ripe Produce": random.randint(1,20),
    "Spoiled" : random.randint(1,20),
    "Rotten": random.randint(1,20)
}

current_goodie_score = random.randint(1,200)


data = {
    "pie_counts" : pie_counts,
    "current_goodie_score":current_goodie_score,
    "saved" : random.randint(1,20), #potential_loss
    
}

with open("analytics_data.json","w") as f:
    json.dump(data,f)

