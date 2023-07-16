from flask import Flask, request
from pymongo import MongoClient
from flask import jsonify

app = Flask(__name__)

# root route
@app.route('/')
def hello_world():
	return 'Hello, World!'

# Set up MongoDB connection and collection
client = MongoClient('mongodb://localhost:27017/')

# Create database named demo if it doesn't exist already
db = client['data_types']

# Create collection named data if it doesn't exist already
collection = db['int']
collection2 = db['float']
collection3 = db['string']
# Add data to MongoDB route
@app.route('/add_data', methods=['POST'])
def add_data():
	# Get data from request
	fromdata = request.json
	

	# Insert data into MongoDB
	collection.insert_one(fromdata)
	collection2.insert_one(fromdata)
	collection3.insert_one(fromdata)
	return 'Data are added to MongoDB'

# Another API route
@app.route('/get_data', methods=['GET'])
def get_data():
	# Retrieve data from MongoDB
	data = collection.find()
		

	# Prepare a response
	response = []
	for item in data:
		if '_id' in item:
			item['_id'] = str(item['_id'])
		response.append(item)
	print(response)

	return response


# Yet another API route
@app.route('/delete_data', methods=['DELETE'])
def delete_data():
	# Delete all data from MongoDB collection
	result = collection.delete_many({})

	return f'Deleted {result.deleted_count} documents'

if __name__ == '__main__':
	app.run()
    

'''from flask import Flask, request
from pymongo import MongoClient
from flask import jsonify

app = Flask(__name__)

# root route
@app.route('/')
def hello_world():
	return 'Hello, World!'

# Set up MongoDB connection and collection
client = MongoClient('mongodb://localhost:27017/')

# Create database named demo if it doesn't exist already
db = client['data_types_trial']

# Create collection named data if it doesn't exist already
collection = db['int']
collection2 = db['float']
collection3 = db['string']
# Add data to MongoDB route
@app.route('/add_data1', methods=['POST'])

def add_data1():
	# Get data from request
	fromdata = request.json
	

	# Insert data into MongoDB
	collection.insert_one(fromdata)

	return 'Data are added to MongoDB'

@app.route('/add_data2', methods=['POST'])
def add_data2():
	# Get data from request
	fromdata = request.json
	

	# Insert data into MongoDB
	collection2.insert_one(fromdata)

	return 'Data are added to MongoDB'

# Another API route

@app.route('/add_data3', methods=['POST'])
def add_data3():
	# Get data from request
	fromdata = request.json
	

	# Insert data into MongoDB
	collection3.insert_one(fromdata)

	return 'Data are added to MongoDB'

@app.route('/get_data', methods=['GET'])
def get_data():
	# Retrieve data from MongoDB
	data = collection.find()
		

	# Prepare a response
	response = []
	for item in data:
		if '_id' in item:
			item['_id'] = str(item['_id'])
		response.append(item)
	print(response)

	return response


# Yet another API route
@app.route('/delete_data', methods=['DELETE'])
def delete_data():
	# Delete all data from MongoDB collection
	result = collection.delete_many({})

	return f'Deleted {result.deleted_count} documents'

if __name__ == '__main__':
	app.run()'''
