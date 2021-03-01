import json
with open("predictions.json") as f:
    data = json.load(f)
n = open("bandwidth.json", "w")
reqBand = {}
for k,v in data.items():
    bandGood = 0
    bandBad = 0
    bandAvg = 0
    for i,j in v.items():
        if i == "Watching Television" or i == "Video on a Computer" or i == "Video on Smartphone":
            bandGood += j*5
            bandAvg += j*3
            bandBad += j*.5
        elif i == "Internet Device on TV" or i == "Internet on Computer (excluding video)":
            bandGood += j*4
            bandAvg += j*2
            bandBad += j
        elif i == "Gaming":
            bandGood += j*3
            bandAvg += j*2
            bandBad += j
        elif i == "Streaming Audio on Smartphone":
            bandGood += 2*j
            bandAvg += 1.5*j
            bandBad += j
    reqBand[k] = [bandBad, bandAvg, bandGood]
n.write(json.dumps(reqBand))
n.close()
