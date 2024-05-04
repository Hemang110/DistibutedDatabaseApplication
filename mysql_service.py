import mysql.connector as conn
from flask import Flask, request,jsonify

app= Flask(__name__)

@app.route('/get-data',methods = ['GET','POST'])
def handle_sql_requests():
    request_body = request.json
    if 'username' in request_body.keys() and 'password' in request_body.keys():
        mydb = conn.connect(host = 'localhost',user = str(request_body['username']), passwd =str(request_body['password']))
        cursor = mydb.cursor()

        if 'query' in request_body.keys():
            cursor.execute(str(request_body['query']))
            return jsonify({'data':str(cursor.fetchall())})
        
    return jsonify({"Error": "Required key not found"})

if __name__ == '__main__':
    app.run(host='localhost',port=9001,debug=True)