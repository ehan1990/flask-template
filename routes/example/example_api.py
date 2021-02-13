from flask import Blueprint, jsonify, request

from libs.datastore import DataStore

example_api_resource = Blueprint("example_api", __name__)


@example_api_resource.route("/example", methods=['GET'])
def list_datastore_api():
    resp = jsonify(DataStore.list_all())
    return resp


@example_api_resource.route("/example", methods=['POST'])
def add_datastore_api():
    data = request.get_json(force=True)
    DataStore.insert(data["val"])
    resp = jsonify(success=True)
    return resp


@example_api_resource.route("/example/not-found", methods=['GET'])
def not_found_api():
    resp = jsonify(success=False)
    resp.status_code = 404
    return resp


@example_api_resource.route("/example/<string:object_id>", methods=['GET'])
def params_api(object_id):
    page = request.args.get("page")
    resp = {
        "object_id": object_id,
        "page": page
    }
    return jsonify(resp)
