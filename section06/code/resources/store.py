from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store: 
            return store.json()
        return {'message': 'store not found.'}, 404

    def post(self, name):
        store = StoreModel.find_by_name(name)

        if store:
            return {'message': 'store already exists'}, 400
        
        store = StoreModel(name)
        
        try:
            store.save_to_db()
        except:
            return {'message': 'An error has occured' }, 500
        
        return {'message': 'Saved Store' }, 201
        
    
    def delete(self, name):
        if StoreModel.find_by_name(name):
            StoreModel.delete_from_db(name)
            return {'message': 'Removed Store'},200

        return {'message': 'Store not found'}, 404

class StoreList(Resource):
    def get(self):
        return {'stores': [store.json() for store in StoreModel.query.all()]}