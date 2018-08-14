from flask import Flask, Blueprint
from flask_restplus import Namespace, fields, Resource
from stellar_base.address import Address

api = Namespace('wallet', description='Wallet operations')

@api.route('/<string:address>')
class Address(Resource):
    def get(self, address):
        address = Address(address=address, network='public')
        address.get()  # get the updated information
        return {
            'balances': address.balances
        }


@api.route('/<string:address>/payments')
class Payments(Resource):
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