from flask import Blueprint, request, redirect, session, current_app, jsonify


blueprint = Blueprint('api', __name__, url_prefix='/api')
