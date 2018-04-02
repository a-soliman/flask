from flask import Flask, jsonify

app = Flask(__name__)

stores = [
    {
    'name': 'My wonderfull store',
    'items': [
            {
            'name': 'mug',
            'price': 7.55
            },
            {
            'name': 'pen',
            'price': 0.79
            }
        ]
    },
    {
    'name': 'Another Store',
    'items': [
        {
        'name': 'laptop',
        'price': 499.99
        }
    ]
    }
]
# POST /store data: {name:}
@app.route('/store', methods=['POST'])
def create_store():
    pass


# GET /store/<string: name>
@app.route('/store/<string:name>', methods=['GET'])
def get_item_in_store(name):
    pass

# GET/store
@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})

# POST
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    pass

# GET /store/<string: name>
@app.route('/store/<string:name>/item', methods=['GET'])
def get_items_in_store(name):
    pass


app.run(port = 5000)