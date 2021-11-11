#!/usr/bin/env python3

import requests


if __name__ == "__main__":
    products = [
        {
            "name": "Lavender heart",
            "price": "9.25"
        },
        {
            "name": "Personalised cufflinks",
            "price": "45.00"
        },
        {
            "name": "Kids T-shirt",
            "price": "19.95"
        },        
    ]
    for product in products:
        r = requests.post("http://127.0.0.1:5000/v1/product", json = product)
        print(r)
