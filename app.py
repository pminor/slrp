from api import create_app, db
from flask_migrate import Migrate 

app = create_app()

migrate = Migrate(app, db) 

if __name__ == '__main__':
    app.run(port=5001, host='0.0.0.0')