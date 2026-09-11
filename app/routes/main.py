from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return render_template('home.html')

@main_bp.route('/sobre')
def sobre():
    return "Pagina sobre Pela Vidda em construção."

