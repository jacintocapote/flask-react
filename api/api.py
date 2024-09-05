from flask import Flask
from flask_migrate import Migrate
from app.models import db
from app.controllers.user_controller import user_blueprint
from app.controllers.bank_account_controller import account_blueprint
from app.controllers.currency_controller import currency_blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    migrate = Migrate(app, db)

    app.register_blueprint(user_blueprint, url_prefix='/api')
    app.register_blueprint(account_blueprint, url_prefix='/api')
    app.register_blueprint(currency_blueprint, url_prefix='/api')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)