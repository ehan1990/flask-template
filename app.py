import logging
import os

from flask import Flask

from common.constants import *
from libs.datastore import DataStore
from routes.healthcheck.healthcheck_api import healthcheck_api_resource
from routes.example.example_api import example_api_resource

app = Flask(__name__)
app.register_blueprint(healthcheck_api_resource)
app.register_blueprint(example_api_resource)


def configure_logger():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(filename)s:%(lineno)d %(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


if __name__ == '__main__':
    configure_logger()
    PORT = int(os.environ.get("PORT", DEFAULT_PORT))
    DataStore.init()

    logging.info(f"running app version {VERSION}, port={PORT}")
    app.run(host="0.0.0.0", debug=True, port=PORT)
