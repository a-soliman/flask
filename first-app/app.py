from flask import Flask

app = Flask(__name__)

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
      pass

# POST
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
      pass

# GET /store/<string: name>
@app.route('/store/<string:name>/item', methods=['GET'])
def get_items_in_store(name):
      pass


app.run(port = 5000)