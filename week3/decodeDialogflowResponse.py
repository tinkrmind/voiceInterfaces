import json
response = json.load(open('sampleResponse.json'))

print(response["result"]["parameters"]["BandColor1"].lower())
print(response["result"]["parameters"]["BandColor2"].lower())
print(response["result"]["parameters"]["BandColor3"].lower())
print(response["result"]["parameters"]["ToleranceColor"].lower())