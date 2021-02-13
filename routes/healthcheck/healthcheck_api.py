import datetime
import json
import logging

from flask import Blueprint
from common.constants import *

healthcheck_api_resource = Blueprint("healthcheck_api", __name__)


@healthcheck_api_resource.route("/healthcheck", methods=['GET'])
def healthcheck():
    res = {
        "version": VERSION,
        "timestamp": f"{datetime.datetime.now().isoformat()[0:19]}Z"
    }
    logging.info(f"called healthcheck {json.dumps(res)}")
    return res

