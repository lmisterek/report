import json;

data = [];

f = open("March2024.tsv", "r")

properties = f.readline().split('\t');
secondLine = f.readline().split('\t');

a = 0;

for x in f:
	newLine = x.split('\t');
	element = {
		properties[3]: newLine[3],
		properties[4]: newLine[4],
		properties[5]: newLine[5],
		properties[6]: newLine[6],
		properties[7]: newLine[7],
		properties[8]: newLine[8],
		properties[9]: newLine[9],
		properties[10]: newLine[10],
		properties[11]: newLine[11],
		properties[12]: newLine[12]
	}
	data.append(element)

f.close();

json_array = json.dumps(data)
print(json_array)
	
with open("data.json", "w") as f:
    json.dump(data, f)