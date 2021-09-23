from flask import Blueprint, render_template, request


algorithm_bp = Blueprint('algorithm', __name__,
                         url_prefix='/algorithm',
                         template_folder='templates',
                         static_folder='static',
                         static_url_path='assets')

