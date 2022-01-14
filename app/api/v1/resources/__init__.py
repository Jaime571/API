from flask_restful import Resource, reqparse
import requests



url = 'http://192.168.191.63:8000/middleware/tienda/articulos'#URL que se v a autilizar como variable para poder enviar y recibir información del middleware
urlVerificacion = 'http://192.168.191.77:5000/authOperation'

#region RequestParserPost
item_post_args = reqparse.RequestParser()
item_post_args.add_argument('idArticulo', type=int, help="id of the article", required=True)
item_post_args.add_argument('idCategoriaDeArticulo', type=int, help="id of the category", required=True)
item_post_args.add_argument('Nombre', type=str, help="name of the article", required=True)
item_post_args.add_argument('Marca', type=str, help="brand of the article", required=True)
item_post_args.add_argument('PrecioVenta', type=int, help="price of the article", required=True)
item_post_args.add_argument('Existencia', type=int, help="existence of the article", required=True)
item_post_args.add_argument('Descripcion', type=str, help="desc of the article", required=True)
item_post_args.add_argument('IdUsuario', type=int, help="desc of the article", required=True)
#endregion

#region RequestParserPatch
item_patch_args = reqparse.RequestParser()
item_patch_args.add_argument('idArticulo', type=int, help="id of the article", required=False)
item_patch_args.add_argument('idCategoriaDeArticulo', type=int, help="id of the category", required=False)
item_patch_args.add_argument('Nombre', type=str, help="name of the article", required=False)
item_patch_args.add_argument('Marca', type=str, help="brand of the article", required=False)
item_patch_args.add_argument('PrecioVenta', type=int, help="price of the article", required=False)
item_patch_args.add_argument('Existencia', type=int, help="existence of the article", required=False)
item_patch_args.add_argument('Descripcion', type=str, help="desc of the article", required=False)
item_patch_args.add_argument('IdUsuario', type=int, help="desc of the article", required=False)
#endregion

class ListItems(Resource):#Obtiene y manda todos los articulos disponibles
    def get(self):
        response = requests.get(url)
        return response.json()

class SearchItems(Resource):
    def get(self, id_items):#Obtiene y muestra el item buscado
        response = requests.get(f'{url}/{id_items}')#En esta línea mando el parametro que recibí al middleware esperando una respuesta
        return response.json()#Retorno la respuesta que haya recibido del middleware en formato JSON

class AddItem(Resource):#Revisada con el middle
    def post(self, id_usuario):#Manda la información de un nuevo item
        a = requests.get(f'{urlVerificacion}/{id_usuario}')
        a = a.json()
        
        if(a['idtipousuario'] == '3'):
            args = item_post_args.parse_args()
            items = {"IdArticulo": args["idArticulo"],
                    "IdCategoriadearticulo": args["idCategoriaDeArticulo"],
                    "Nombre": args["Nombre"],
                    "Marca": args["Marca"],
                    "PrecioVenta": args["PrecioVenta"],
                    "Existencia": args["Existencia"],
                    "Descripcion": args["Descripcion"],
                    "IdAlmacenista": args["IdUsuario"]}
            response = requests.post(url + "/", data = items)
            return response.json()#jsonify({response.status_code, 'El articulo fue agregado de manera correcta'})
        jsonResult = {"mensaje":"No es"}
        return jsonResult

class DeleteItem(Resource):
    def delete(self,id_items, id_usuario):#Manda la información de un nuevo item
        a = requests.get(f'{urlVerificacion}/{id_usuario}')
        a = a.json()
        
        if(a['idtipousuario'] == '3'):
            response = requests.delete(f'{url}/{id_items}/')
            return response.json()
        jsonResult = {"mensaje":"No es"}
        return jsonResult

class EditItem(Resource):
    def patch(self, id_items, id_usuario):#Manda la información de un nuevo item
        a = requests.get(f'{urlVerificacion}/{id_usuario}')
        a = a.json()
        if(a['idtipousuario'] == '3'):
            args = item_patch_args.parse_args()
            items = {"IdArticulo": args["idArticulo"],
                    "IdCategoriadearticulo": args["idCategoriaDeArticulo"],
                    "Nombre": args["Nombre"],
                    "Marca": args["Marca"],
                    "PrecioVenta": args["PrecioVenta"],
                    "Existencia": args["Existencia"],
                    "Descripcion": args["Descripcion"],
                    "IdAlmacenista": args["IdUsuario"]}
            response = requests.patch(f'{url}/{id_items}/', items)
            return response.json()
        jsonResult = {"mensaje":"No es"}
        return jsonResult