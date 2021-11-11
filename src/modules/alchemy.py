import datetime
import json

from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()


class Product(Base):
    __tablename__ = "products"
    id = Column("id", Integer, primary_key = True, autoincrement = True)
    name = Column("name", String)
    price = Column("price", String) #TODO: Suggest swapping for float

    def __str__(self):
        return f"Product({self.id} - {self.name} - {self.price}£)"

    def dump(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price
        }


class ProductsDB:

    def __init__(self, location = None):
        """
        initialization of database connection

        :param location: location of the database, defaults to current directory
        """
        if not location:
            location = "products.sqlite"
        self.engine = create_engine(f"sqlite:///{location}")
        Base.metadata.create_all(bind = self.engine)
        Session = sessionmaker(bind = self.engine)
        self.session = Session()


    def query_all_products(self):
        """
        query all products in the database

        :return: list of Product objects
        """
        return self.session.query(Product).all()


    def add_products(self, products):
        """
        this method would add every Product in iterable to database

        :param product: list of Product objects
        :return: None
        """
        for product in products:
            self.session.add(product)
        self.session.commit()


    def _query_by_id(self, product_id):
        """
        run Query and retrieve matching product id

        :param product_id: id of the product in the database
        :return: Query object
        """
        return self.session.query(Product).filter(Product.id == product_id)


    def query_by_id(self, product_id):
        """
        retrieve Product object with matching id

        :param product_id: id of the product in the database
        :return: Product object
        """
        return self._query_by_id(product_id).first()


    def update_by_id(self, product_id, name = None, price = None):
        """
        update Product with matching id

        :param product_id: id of the product in the database
        :param name: new product name
        :param price: new product price
        :return: None
        """
        product = self._query_by_id(product_id).first()
        if price:
            product.price = price
        if name:
            product.name = name
        self.add_products([product])
        return product


    def delete_by_id(self, product_id):
        """
        delete Product from database

        :param product_id: id of the product in the database
        :return: None
        """
        return self._query_by_id(product_id).delete()
