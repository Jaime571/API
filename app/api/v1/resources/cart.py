from flask_cors import cross_origin
from flask_restful import Resource, reqparse
import requests, json


url = 'http://192.168.191.63:8000/middleware/tienda/carritos/'#URL que se v a autilizar como variable para poder enviar y recibir información del middleware

#region RequestParser
item_post_args = reqparse.RequestParser()
item_post_args.add_argument('IdCarrito', type=int, help="id of the cart", required=True)
item_post_args.add_argument('IdUsuario', type=int, help="id of the user", required=True)
item_post_args.add_argument('IdArticulo', type=int, help="name of the article", required=True)
item_post_args.add_argument('Cantidad', type=int, help="brand of the article", required=True)
#endregion

class ShowCart(Resource):
    
    def get(self, id_usuario):#Obtiene y muestra el item buscado
        response = requests.get(f'{url}/{id_usuario}')#En esta línea mando el parametro que recibí al middleware esperando una respuesta
        return response.json()#Retorno la respuesta que haya recibido del middleware en formato JSON

class AddItemToCart(Resource):
    
    def post(self):#Manda la información de un nuevo item
        args = item_post_args.parse_args()
        item = {"idcarrito": args["IdCarrito"],
                "idusuario": args["IdUsuario"],
                "idarticulo": args["IdArticulo"],
                "cantidad": args["Cantidad"]}
        response = requests.post(url, data= json.dumps(item))
        return response.json()

class DeleteItemFromCart(Resource):
    
    def delete(self, id_items):#Manda la información de un nuevo item
        response = requests.delete(f'{url}/{id_items}')
        return response.json()