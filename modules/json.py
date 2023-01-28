import json

def write(data, filename):
	with open(filename, encoding='utf-8') as file:
		f = json.load(file)
		for key in list(data.keys()):
			f[key] = data[key]

		with open(filename, 'w', encoding='utf-8') as outfile:
			json.dump(f, outfile, indent=4)

def read(filename):
	with open(filename, 'r', encoding='utf-8') as file:
		return json.load(file)