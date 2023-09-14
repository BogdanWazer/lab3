import json
from pprint import pprint
from random import randint as rd, choice as ch

def write(data, filename):
	data = json.dumps(data)
	data = json.loads(str(data))
	with open(filename, 'w', encoding='utf-8') as file:
		json.dump(data, file, indent=4)

n_data = {
	"users": [1,2,3,4,5]
}

# write(n_data, 'config.json')
	
def read(filename): 
	with open(filename, 'r', encoding='utf-8') as file:
		return json.load(file)

class User: 
	def __init__(self):
		self.name = ch(['First','Second','Third'])
		self.age = rd(0,70)
		self.id = rd(0, 1000000)

datas = {
	"users" : []
}

for i in range(100):
	datas['users'].append(User().__dict__)

write(datas, 'data.json')
	
# pprint(read('config.json'))
# input()