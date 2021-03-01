import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json

with open("data.json") as f:
    data = json.load(f)
n = open("predictions.json", "w")
predict = {}

for k,v in data.items():
    pushStuff = {}
    for i,j in v.items():
        pushStuff[i] = j[1]+j[0]
        pushStuff[i] /= 2
        pushStuff[i] = pushStuff[i] - pushStuff[i]%.001
    predict[k] = pushStuff
n.write(json.dumps(predict))
n.close()
