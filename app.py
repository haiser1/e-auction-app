from config import app, db
from flask_cors import CORS
from models import item, user, auction, bid, winner
from sqlalchemy.exc import SQLAlchemyError
from routes.auth_route import auth_route
from routes.user_route import user_route
from routes.item_route import item_route
from routes.auction_route import auction_route
from routes.bid_route import bid_route
from routes.winner_route import winner_route
from flask_swagger_ui import get_swaggerui_blueprint
from bcrypt import hashpw, gensalt

swagger_url = '/api/docs'
api_url = '/static/api_docs.yml'
swagger_ui_blueprint = get_swaggerui_blueprint(
    swagger_url,
    api_url,
    config={
        'app_name': 'Auction API Documentation'
    }
)

app.register_blueprint(swagger_ui_blueprint, url_prefix=swagger_url)
password_hash = hashpw('password'.encode('utf-8'), gensalt())

app.register_blueprint(auth_route)
app.register_blueprint(user_route)
app.register_blueprint(item_route)
app.register_blueprint(auction_route)
app.register_blueprint(bid_route)
app.register_blueprint(winner_route)

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

    app.run(debug=True, port=5001)
