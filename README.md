# ESP-32 Parking positions booking system

## Run app

Requirements:
- Python
- PIP (Python package manager)

Install all dependencies.
```sh
pip install -r requirements.txt
```

Update database *.env* file configuration with your own config:
Ex.:
```sh
DB_CONNECTION=mysql+mysqldb
DB_HOST=localhost
DB_PORT=3306
DB_USER=my_user
DB_PASSWORD=my_user_password
DB_NAME=my_database_name
```

Run application.
```sh
flask run
```

And the app will be available on <http://localhost:5000/>.
