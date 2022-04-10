from flask import Flask,jsonify, request

app = Flask(__name__)

data = [
    {
        'id': 1,
        'Name': u'xyz',
        'Contact': u'1234567890', 
        'done': False
    },
    {
        'id': 2,
        'Name': u'zyx',
        'Contact': u'0987654321', 
        'done': False
    }
]

@app.route("/")

def hello():
    return "Hello World"

@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Provide the correct data"
        },400)

    contact = {
        'id': tasks[-1]['id'] + 1,
        'Name': request.json['Name'],
        'Contact': request.json.get('Contact', ""),
        'done': False
    }
    data.append(contact)
    return jsonify({
        "status":"success",
        "message": "Contact has been added"
    })
    

@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : data
    }) 

if (__name__ == "__main__"):
    app.run(debug=True)