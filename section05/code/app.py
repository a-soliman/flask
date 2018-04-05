from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required

from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'ahmed'
api = Api(app)

jwt = JWT(app, authenticate, identity) #/auth

items = []

class Items(Resource):
    @jwt_required()
    def get(self):
        return {'items': items}, 200



class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', 
        type = float,
        required = True,
        help = "This field cant be blank"    
    )

    @jwt_required()
    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'item': item}, 200 if item else 404

    def post(self, name):
        # ensure names are unique
        if next(filter(lambda x: x['name'] == name, items), None) is not None:
            return { 'message': 'An item with the provided name already exists'}, 400

        data = Item.parser.parse_args()
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return {'message': 'created item', 'item': item }, 201

    def put(self, name):
        

        data = Item.parser.parse_args()

        item =  next(filter(lambda x: x['name'] == name, items), None)
        if item:
            item['price'] = data['price']
            return {'message': 'updated item', 'item': item}, 201
        else:
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