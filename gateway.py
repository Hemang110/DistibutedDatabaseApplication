import requests
from flask import Flask, request, jsonify

#create flask app
app = Flask(__name__)

# creating helper function to check request body content-type
def check_content_type(incoming_request):
    status=False
    content_type = incoming_request.headers.get('Content-Type')
    if content_type == 'application/json':
        status = True
    
    return status

def make_post_request(port,service,payload):
    url = 'http://localhost:port/service'.replace('service',service).replace('port',port)
    return requests.post(url=url,json=payload)

@app.route('/db-app',methods = ['GET','POST'])
def handle_app_requests():

    if request.method == 'GET':
        return jsonify({'supported functions': 'get data', 'supported DB': 'MySQL, MongoDB'})
    
    if request.method=='POST':
        if check_content_type(request):
            request_body = request.json
            if 'type' in request_body.keys():
                if request_body['type'].lower()=='sql':
                    response = make_post_request('9001','get-data',request_body)
                    return response.json()
                
                if request_body['type'].lower()=='mongodb':
                    response= make_post_request('2002','get-data' ,request_body)
                    return response.json()
        
        return jsonify({'error': 'Content-Type not supported!'})
    

if __name__ == '__main__':
    app.run(host='localhost',port=9000,debug=True)
    
