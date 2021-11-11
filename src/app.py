#!/usr/bin/env python3

import logging

import connexion

if __name__ == "__main__":
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    console = logging.StreamHandler()
    logger.addHandler(console)
    formatter = logging.Formatter("%(asctime)s;%(levelname)s;%(message)s")
    console.setFormatter(formatter)

    logging.debug("Process started")

    app = connexion.FlaskApp(__name__, port=5000, specification_dir="modules/openapi/")
    app.add_api("server.yaml", strict_validation=True)
    app.run()
