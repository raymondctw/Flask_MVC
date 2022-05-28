from flask import Blueprint, Flask, request, render_template

main_blueprint = Blueprint('main_blueprint', __name__)

@main_blueprint.route('/')
@main_blueprint.route('/Dashboard')
def Dashboard():
    return render_template('home.html')






