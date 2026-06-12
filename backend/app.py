from flask import Flask, request,jsonify
from dotenv import load_dotenv
import os
import pymongo
load_dotenv()

MONGO_URI =os.getenv('MONGO_URI') 

client = pymongo.MongoClient(MONGO_URI )
db = client.test
collection = db['flask-tutorial']

app = Flask(__name__)

@app.route('/submittodoitem', methods=['POST'])
def submit_todo_item():
 

    item_name = request.form.get('itemName')
    item_description = request.form.get('itemDescription')
    todo_data = {
        "itemName": item_name,
        "itemDescription": item_description
    }

    collection.insert_one(todo_data)
    return "todo item saved succesfully!"

@app.route('/view')
def view():
    
    data = collection.find()

    data = list(data)
    for item in data:

        print(item)
        del item['_id']
        
    data = {
        'data' : data
    }
         
    return jsonify(data)

   
if __name__=='__main__':

    app.run(debug=True, port=2000,host='0.0.0.0')
