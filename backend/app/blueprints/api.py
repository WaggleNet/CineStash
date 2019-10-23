from flask import Blueprint, request, redirect, session, current_app, jsonify
from bson import ObjectId

from ..services.mongo import project_db

blueprint = Blueprint('api', __name__, url_prefix='/api')


@blueprint.route('/projects/', methods=['GET'])
def list_projects():
    db = project_db()
    projects = db.find(projection={'scenes': False})
    return jsonify(result=projects)


@blueprint.route('/projects/', methods=['POST'])
def create_project():
    db = project_db()
    data = request.json
    db.insert_one(data)
    return jsonify(result='ok')


@blueprint.route('/projects/<_id>', methods=['GET'])
def get_project(_id):
    db = project_db()
    project = db.find_one({'_id': ObjectId(_id)})
    return jsonify(result=project)


@blueprint.route('/projects/<_id>', methods=['POST'])
def set_project(_id):
    data = request.json
    db = project_db()
    db.update_one({'_id': ObjectId(_id)}, {'$set': data})
    return jsonify(result='ok')


@blueprint.route('/projects/<_id>', methods=['DELETE'])
def delect_project(_id):
    db = project_db()
    db.delete_one({'_id': ObjectId(_id)})
    return jsonify(result='ok')
