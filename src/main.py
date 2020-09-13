from datetime import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from src.migrations import upgrade
from src.queries import create_delivery, create_address, get_user_by_email, \
    get_all_deliveries, create_user
from src.settings import DB_URI

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
db = SQLAlchemy(app)
upgrade()


@app.route('/')
def hello_world():
    user = {
        'name': 'John Snow',
        'password': 'johnspassword',
        'email': 'john_snow@gmail.com'
    }

    # create_user(user)
    user = get_user_by_email(user['email'])

    delivery_address = {
        'cep': '890672223',
        'road': 'Rua da kiki',
        'state': 'Da Bruxa',
        'city': 'xanana',
        'complement': 'Aos fundos',
        'user_id': user['id']
    }

    pick_up_adrdess = {
        'cep': '890672223',
        'road': 'Rua da kiki',
        'state': 'Da Bruxa',
        'city': 'xanana',
        'complement': 'Aos fundos',
        'user_id': user['id']
    }
    # create_address(pick_up_adrdess)
    # create_address(delivery_address)

    delivery = {
        'delivery_address_id': 'fd266b01-ef24-428d-9115-73778558ffa5',
        'pick_up_address_id': '0cee33d2-d98b-4116-be3b-6a6342a6185f',
        'delivery_date': datetime.now(),
        'pick_up_date': datetime.now(),
        'status': 'in_queue',
        'price': 2.56,
        'package_weight': 2.567,
        'user_id': user['id']

    }

    create_delivery(delivery)

    deliveries = get_all_deliveries()

    return 'Hello, World!'


if __name__ == "__main__":
    app.run()
