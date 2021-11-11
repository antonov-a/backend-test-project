#!/usr/bin/env python3

import os
import random

from src.modules import alchemy


def db_init():
    rnd = random.random()
    fp = f"/tmp/alchemy_test_{rnd}.sqlite"
    sql = alchemy.ProductsDB(fp)
    return sql, fp


def test_init():
    _, fp = db_init()

    assert os.path.exists(fp)
    os.remove(fp)


def test_add():
    sql, fp = db_init()

    product = alchemy.Product()
    product.name = "Lavender heart"
    product.price = "9.25"
    sql.add_products([product])

    q = sql.query_all_products()
    assert len(q) == 1
    assert q[0].name == "Lavender heart"
    os.remove(fp)


def test_add_several():
    sql, fp = db_init()

    heart = alchemy.Product()
    heart.name = "Lavender heart"
    heart.price = "9.25"

    cufflinks = alchemy.Product()
    cufflinks.name = "Personalised cufflinks"
    cufflinks.price = "45.00"

    kids_t = alchemy.Product()
    kids_t.name = "Kids T-shirt"
    kids_t.price = "19.95"

    sql.add_products([heart, cufflinks, kids_t])

    q = sql.query_all_products()
    assert len(q) == 3
    assert q[0].name == "Lavender heart"
    assert q[1].price == "45.00"
    assert q[2].name == "Kids T-shirt"
    os.remove(fp)


def test_query_id():
    sql, fp = db_init()

    product = alchemy.Product()
    product.name = "Lavender heart"
    product.price = "9.25"
    sql.add_products([product])

    q = sql.query_by_id(1)
    assert q.name == "Lavender heart"
    os.remove(fp)


def test_update_id():
    sql, fp = db_init()

    product = alchemy.Product()
    product.name = "Lavender heart"
    product.price = "9.25"
    sql.add_products([product])

    sql.update_by_id(1, name = "Something else")

    q = sql.query_by_id(1)
    assert q.name == "Something else"
    os.remove(fp)


def test_delete_id():
    sql, fp = db_init()

    product = alchemy.Product()
    product.name = "Lavender heart"
    product.price = "9.25"
    sql.add_products([product])

    q = sql.query_all_products()
    assert len(q) == 1

    sql.delete_by_id(1)
    q = sql.query_all_products()
    assert len(q) == 0

    os.remove(fp)
