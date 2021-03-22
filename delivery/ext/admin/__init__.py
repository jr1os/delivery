from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from delivery.ext.db import db
from delivery.ext.db.models import Category

admin = Admin()

def init_app(app):
    admin.name = app.config.get("ADMIN_NAME", "CodeFoods")
    admin.template_mode = app.config.get("ADMIN_TEPLATE_MODE", "bootstrap4")
    admin.init_app(app)

    # Proteger com senha

    admin.add_view(ModelView(Category, db.session))


