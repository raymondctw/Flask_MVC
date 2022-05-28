from flask import Blueprint, Flask, request, render_template, jsonify
from app import db
from app.model import User
admin_blueprint = Blueprint('admin_blueprint', __name__, template_folder='templates/admin')

@admin_blueprint.route('/')
@admin_blueprint.route('/Dashboard')
def Dashboard():
    return 'admin/Dashboard'

@admin_blueprint.route('/addUser')
def addUser():
    username = request.values.get('username')
    password = request.values.get('password')

    new_user = User.User(username, password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'status': 'success', 'message': f'create user ({username}, {password}) successfully'})


@admin_blueprint.route('/getUser')
def getUser():
    query_results = User.User.query.all()


    return jsonify({'data': [{'username': user.username, 'password': user.password} for user in query_results]})