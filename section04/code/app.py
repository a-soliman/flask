from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

items = []

class Items(Resource):
    def get(self):
        return {'items': items}, 200



class Item(Resource):
    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'item': item}, 200 if item else 404

    def post(self, name):
        # ensure names are unique
        if next(filter(lambda x: x['name'] == name, items), None) is not None:
            return { 'message': 'An item with the provided name already exists'}, 400

        data = request.get_json()
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return {'message': 'created item', 'item': item }, 201

    def put(self, name):
        data = request.get_json()
        
        for item in items:
            if item['name'] == name:
                item['price'] = data['price']
                return {'message': 'updated item', 'item': item}, 201
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return {'message': 'created item', 'item': item}, 201
    
    def delete(self, name):
        for i in range(len(items)):
            if items[i]['name'] == name:
                items.pop(i)
                return {'message': 'item deleted'}
        return {'message': 'item was not found.'}, 404

api.add_resource(Items, '/items')
api.add_resource(Item, '/item/<string:name>')

app.run(port=5000, debug=True)