from app import app, db

def migrate():
    with app.app_context():
        db.session.execute("""
        
        CREATE TABLE roles(
            id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
            role VARCHAR(255) NOT NULL
        );
                        
        CREATE TABLE users(  
            id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
            email VARCHAR(255) NOT NULL UNIQUE,
            fullname VARCHAR(255) NOT NULL,
            password VARCHAR(255) NOT NULL,
            contact INT NOT NULL,
            car_plate VARCHAR(10) NOT NULL UNIQUE,
            role_id INT NOT NULL,
            created_at DATETIME,
            CONSTRAINT fk_user_roles FOREIGN KEY (role_id) REFERENCES roles (id)
        );

        CREATE TABLE vehicles(  
            id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
            brand VARCHAR(255) NOT NULL,
            model VARCHAR(255) NOT NULL,
            type VARCHAR(255) NOT NULL,
            user_id int NOT NULL,
            created_at DATETIME,
            CONSTRAINT fk_users_vehicles FOREIGN KEY (user_id) REFERENCES users(id)
        );

        CREATE TABLE logs(
            id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
            type VARCHAR(255) NOT NULL,
            date_time DATETIME NOT NULL,
            vehicle_id int NOT NULL,
            CONSTRAINT fk_logs_vehicles FOREIGN KEY (vehicle_id) REFERENCES vehicles(id)
        );


        """)