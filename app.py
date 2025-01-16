from config import app, db
from flask_cors import CORS
from models import item, transaction, users, auction, bid
import logging
from sqlalchemy.exc import SQLAlchemyError

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

CORS(app)

if __name__ == '__main__':
    try:
        print("Connecting to database...")
        print(app.config['SQLALCHEMY_DATABASE_URI'])
        
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
