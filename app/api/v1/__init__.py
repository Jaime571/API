from flask_restful import Api
from flask import make_response, jsonify, Blueprint


blu_api = Blueprint('blu_api', __name__)#Se completa la URL del endpoint
api = Api(blu_api)

from app.api.v1.resources import AddItem, DeleteItem, EditItem, SearchItems, ListItems
from app.api.v1.resources.cart import ShowCart, AddItemToCart, DeleteItemFromCart

#Respuesta personalizada 
@api.representation('application/json')
def out_json(data, code, headers=None):
    resp = make_response(
        jsonify(dict(status='ok',code = code, data = data))
    )
    resp.headers.extend(headers or {})
    return resp

api.add_resource(ListItems, '/api/v1/items/')
api.add_resource(SearchItems, '/api/v1/items/search/<int:id_items>')
api.add_resource(AddItem, '/api/v1/items/add/<int:id_usuario>')
api.add_resource(EditItem, '/api/v1/items/edit/<int:id_items>/<int:id_usuario>')
api.add_resource(DeleteItem, '/api/v1/items/delete/<int:id_usuario>/<int:id_items>')
api.add_resource(ShowCart, '/api/v1/cart/<int:id_user>')
api.add_resource(AddItemToCart, '/api/v1/cart/add/')
api.add_resource(DeleteItemFromCart, '/api/v1/cart/delete/')