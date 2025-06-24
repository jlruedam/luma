# Luma
from config import Config
from models import db, User, Tour
from auth.routes import auth_bp
from sales.routes import sales_bp
from agencies.routes import agencies_bp
from tours.routes import tours_bp
from clients.routes import clients_bp
from vendors.routes import vendors_bp
from payments.routes import payments_bp


# Flask
from flask import Flask
from flask import render_template
from flask_migrate import Migrate
from flask_login import LoginManager, login_required

from werkzeug.security import generate_password_hash

# Instance de app Flask
app = Flask(__name__)
app.config.from_object(Config)

# Login configuration
login_manager = LoginManager()
login_manager.init_app(app)
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

login_manager.login_view = 'auth.login'

# Init database
db.init_app(app)
migrate = Migrate(app, db)

# Add routes with blueprints
app.register_blueprint(sales_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(agencies_bp)
app.register_blueprint(tours_bp)
app.register_blueprint(clients_bp)
app.register_blueprint(vendors_bp)
app.register_blueprint(payments_bp)


# Home
@app.route("/")
def landpage():
    tours = Tour.query.all()
    return render_template("landpage.html", tours = tours)


@app.route("/home")
@login_required
def home():
    return render_template("index.html")

with app.app_context():
    db.create_all()

    # Crear usuario administrador si no existe
    if not User.query.filter_by(username="admin").first():
        admin = User(
            username="admin",
            password=generate_password_hash("admin123"),
            is_admin=True  # Asegúrate de tener este campo en el modelo
        )
        db.session.add(admin)
        db.session.commit()
        print("✅ Usuario administrador creado.")
    else:
        print("ℹ️ Usuario administrador ya existe.")



if __name__ == "__main__":
    app.run(debug=True)
