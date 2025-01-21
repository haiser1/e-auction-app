from config import app, db
from flask_cors import CORS
from models import item, transaction, user, auction, bid
import logging
from sqlalchemy.exc import SQLAlchemyError
from routes.auth_route import auth_route
from routes.user_route import user_route
from routes.item_route import item_route
from flask_swagger_ui import get_swaggerui_blueprint

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

CORS(app)

swager_url = '/api/docs'
api_url = '/static/api_docs.yml'
swager_ui_blueprint = get_swaggerui_blueprint(
    swager_url,
    api_url,
    config={
        'app_name': 'Auction API Documentation'
    }
)

app.register_blueprint(swager_ui_blueprint, url_prefix=swager_url)

app.register_blueprint(auth_route)
app.register_blueprint(user_route)
app.register_blueprint(item_route)

if __name__ == '__main__':
    try:
        print("Connecting to database...")
        
        with db.engine.connect() as connection:
            print("Database connected successfully!")

        with app.app_context():
            db.create_all()
            print("Tables created (if not exist).")

    except SQLAlchemyError as e:
        print(f"SQLAlchemy Error: {e}")
    except Exception as ex:
        print(f"Unexpected error: {ex}")

    app.run(debug=True)
