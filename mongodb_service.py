import pymongo
from flask import Flask,jsonify,request

app = Flask(__name__)

def validate_request(required_keys,actual_keys):
    status=True
    for key in required_keys:
        if key not in actual_keys:
            status = False
    
    return status

@app.route('/get-data',methods = ['GET','POST'])
def handle_mongo_requests():
    request_body = request.json
    if validate_request(['connection-string','db-name','collection'],request_body.keys()):
        client = pymongo.MongoClient(str(request_body['connection-string']))
        mydb = client[request_body['db-name']]
        collection = mydb[request_body['collection']]
        return jsonify({'data':str(list(collection.find()))})
    return jsonify({'Error':'Required Keys not found'})

if __name__ == "__main__":
    app.run(host='localhost',port=2002,debug=True)