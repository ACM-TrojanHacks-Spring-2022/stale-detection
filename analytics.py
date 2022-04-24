import json

f = open('analytics_data.json','r')
data = json.load(f)
f.close()

# get the classification based on prediction
classification = 'Spoiled'

data['pie_counts'][classification]+=1

with open('analytics_data.json', 'w') as outfile:
    json.dump(data, outfile)

