from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

items = []

class Item(Resource):
    def get(self, name):
        for item in items:
            if item['name'] == name:
                return {'item': item}
        return {'message': 'item was not found'}
    
    def post(self, name):
        item = {'name': name, 'price': 12.00}
        items.append(item)
        return {'message': 'created item', 'item': item }
    
    def delete(self, name):
        for i in range(len(items)):
            if items[i]['name'] == name:
                items.pop(i)
                return {'message': 'item deleted'}
        return {'message': 'item was not found.'}

api.add_resource(Item, '/item/<string:name>')
app.run(port=5000)