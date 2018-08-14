from flask_restplus import Namespace, Resource
from stellar_base.address import Address

api = Namespace('wallet', description='Wallet operations')

@api.route('/<string:publickey>')
class WalletAddress(Resource):
    def get(self, publickey):
        address = Address(address=publickey, network='public')
        address.get()  # get the updated information
        return {
            'balances': address.balances
        }


@api.route('/<string:address>/payments')
class WalletPayments(Resource):
    def get(self, id):
        return {id: id}


# Schema validation example:

# @api.route('/')
# class CatList(Resource):
#     @api.doc('list_cats')
#     @api.marshal_list_with(cat)
#     def get(self):
#         '''List all cats'''
#         return CATS
#
# @api.route('/<id>')
# @api.param('id', 'The cat identifier')
# @api.response(404, 'Cat not found')
# class Cat(Resource):
#     @api.doc('get_cat')
#     @api.marshal_with(cat)
#     def get(self, id):
#         '''Fetch a cat given its identifier'''
#         for cat in CATS:
#             if cat['id'] == id:
#                 return cat
#         api.abort(404)