import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

from models.item import ItemModel


class Items(Resource):
    @jwt_required()
    def get(self):
        connection  = sqlite3.connect('data.db')
        cursor      = connection.cursor()

        query       = "SELECT * FROM items"
        result      = cursor.execute(query)

        items = []

        for row in result:
            items.append({'name': row[0], 'price': row[1]})

        connection.close()

        return {'items': items}



class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', 
        type = float,
        required = True,
        help = "This field cant be blank"    
    )

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)

        if item:
            return item.json()

        return { 'message': 'Item not found'}, 404


    def post(self, name):

        if ItemModel.find_by_name(name):
            return {'message': 'an item with the same name already exists'}, 400 
        
        data = Item.parser.parse_args()
        item = ItemModel(name, data['price'])

        try:
            item.insert()
        except:
            return {'message': 'An error occurred inserting item.'}, 500 #internal server error

        return item.json(), 201

        

    def put(self, name):
        data = Item.parser.parse_args()

        item = ItemModel.find_by_name(name)
        updated_item = ItemModel(name, data['price'])

        if item is None:
            try:
                updated_item.insert()
            except:
                return {'message': 'An error occurred inserting item.'}, 500 #internal server error
        else:
            try:
                updated_item.update()
            except:
                return {'message': 'An error occurred updating item.'}, 500 #internal server error

        return updated_item.json(), 200
    
    def delete(self, name):
        
        if not ItemModel.find_by_name(name):
            return {'message': 'could not find an item with the provided name'}

        connection  = sqlite3.connect('data.db')
        cursor      = connection.cursor()

        query       = "DELETE FROM items WHERE name=?"

        cursor.execute(query, (name,))

        connection.commit()
        connection.close()

        return {'message': 'item Deleted'}