#!/usr/bin/env python3

from modules import alchemy

productsDB = alchemy.ProductsDB()


def get_products():
    return [x.dump() for x in productsDB.query_all_products()]


def post_product(body):
    product = alchemy.Product()
    product.price = str(body["price"])
    product.name = body["name"]
    productsDB.add_products([product])
    return product.dump()


def get_product(id):
    q = productsDB.query_by_id(id)
    if q:
        return q.dump()
    else:
        return "Product not found", 404


def put_product(id, body):
    if productsDB.query_by_id(id):
        r = productsDB.update_by_id(
            id,
            name = body.get("name"),
            price = body.get("price")
        )
        return r.dump()
    else:
        return "Product not found", 404


def delete_product(id):
    if productsDB.query_by_id(id):
        productsDB.delete_by_id(id)
        return "OK", 200
    else:
        return "Product not found", 404