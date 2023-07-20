import configparser
import json
from flask import Flask, request,jsonify
from pymongo import MongoClient

client = MongoClient('mongodb+srv://himani124:himani%40123@cluster0.2myvnw5.mongodb.net/')
db = client['config_db']
collection = db['items']

app=Flask(__name__)

def config_file(file_path):
    config = configparser.ConfigParser()
    try:
        config.read(file_path)
    except Exception as e:
        print(f"Error reading configuration file: {str(e)}")
        return None

    result = {}
    for section in config.sections():
        result[section] = {}
        for key, value in config.items(section):
            result[section][key] = value

    return result

@app.route('/item', methods=['POST'])
def postItemRoute():
    item = request.json
    collection.insert_one(item)
    return jsonify({'message': 'Added Successfully'})

def save_to_database(data):
    json_data = json.dumps(data, indent=4)
    print(f"Saving to database:\n{json_data}")

if __name__ == '__main__':
    file_path = 'config_data.txt'  # Set the path to your configuration file
    app.run(port=3000)

    config_data = config_file(file_path)
    if config_data is not None:
        print("Configuration File Parser Results:")
        for section, values in config_data.items():
            print(f"\n{section}:")
            for key, value in values.items():
                print(f"- {key}: {value}")
        
        save_to_database(config_data)