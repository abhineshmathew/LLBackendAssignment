from flask import blueprints

bp = blueprints.Blueprint(name='orders', import_name=__name__, url_prefix='/')

from app.main import routes